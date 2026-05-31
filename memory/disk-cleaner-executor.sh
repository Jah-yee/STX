#!/bin/bash
#==============================================================================
# Disk Cleaner Executor - 三轮磁盘清理脚本
# 
# 用法:
#   ./disk-cleaner-executor.sh [OPTIONS]
#   
#   Options:
#     --dry-run        仅扫描，不删除
#     --auto-confirm   自动确认所有轮次（跳过交互）
#     --round N        仅运行第 N 轮 (1|2|3)
#     --scan-root DIR  添加扫描根目录（可多次指定）
#     --help           显示帮助
#
# 环境变量:
#   DRY_RUN=1          干运行模式
#   AUTO_CONFIRM=1     自动确认
#   PATTERNS_FILE      safe-patterns.md 路径
#   FRAMEWORK_FILE     framework.md 路径
#   LOG_DIR            日志目录
#
# 输出:
#   ~/.openclaw/logs/disk-cleaner/round{N}-{scan|report}-*.{log|json}
#   ~/.openclaw/logs/disk-cleaner/summary-*.json
#==============================================================================

set -euo pipefail

#------------------------------
# 配置
#------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_PATTERNS_FILE="$SCRIPT_DIR/safe-patterns.md"
DEFAULT_FRAMEWORK_FILE="$SCRIPT_DIR/framework.md"
DEFAULT_LOG_DIR="$HOME/.openclaw/logs/disk-cleaner"

PATTERNS_FILE="${PATTERNS_FILE:-$DEFAULT_PATTERNS_FILE}"
FRAMEWORK_FILE="${FRAMEWORK_FILE:-$DEFAULT_FRAMEWORK_FILE}"
LOG_DIR="${LOG_DIR:-$DEFAULT_LOG_DIR}"

# 默认扫描根目录
declare -a SCAN_ROOTS=(
    "$HOME/.openclaw"
    "$HOME/.cache"
    "$HOME/tmp"
    "/tmp/openclaw-*"
    "$HOME/Downloads"
)

# 全局状态
DRY_RUN="${DRY_RUN:-0}"
AUTO_CONFIRM="${AUTO_CONFIRM:-0}"
RUN_ROUND="${RUN_ROUND:-0}"   # 0 = 全部轮次

# JSON 报告数据（每轮）
declare -A ROUND_TIMESTAMP
declare -A ROUND_SCANNED_PATHS
declare -A ROUND_CANDIDATES_FOUND
declare -A ROUND_CANDIDATES_SIZE_MB
declare -A ROUND_DELETED_COUNT
declare -A ROUND_DELETED_SIZE_MB
declare -A ROUND_ERRORS
declare -A ROUND_RECOMMENDATIONS

# 全局错误累积
GLOBAL_ERRORS=()

#------------------------------
# 工具函数
#------------------------------

log() {
    local level="$1"; shift
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [$level] $*" | tee -a "$CURRENT_LOG"
}

info()  { log "INFO" "$@"; }
warn()  { log "WARN" "$@"; }
error() { log "ERROR" "$@"; }

# 生成时间戳文件名片段
ts() { date '+%Y%m%d-%H%M%S'; }

# 统计目录大小（MB，整数）
dir_size_mb() {
    local path="$1"
    if [[ -d "$path" ]]; then
        du -sm "$path" 2>/dev/null | awk '{print $1}' || echo "0"
    elif [[ -f "$path" ]]; then
        stat -c%s "$path" 2>/dev/null | awk '{printf "%.0f", $1/1024/1024}' || echo "0"
    else
        echo "0"
    fi
}

# 统计文件大小（MB，整数，向下取整）
file_size_mb() {
    local path="$1"
    stat -c%s "$path" 2>/dev/null | awk '{printf "%.0f", $1/1024/1024}' || echo "0"
}

# 人类可读大小
human_size() {
    local bytes="$1"
    if (( bytes >= 1073741824 )); then
        echo "$(awk "BEGIN {printf \"%.1f\", $bytes/1073741824}")G"
    elif (( bytes >= 1048576 )); then
        echo "$(awk "BEGIN {printf \"%.1f\", $bytes/1048576}")M"
    elif (( bytes >= 1024 )); then
        echo "$(awk "BEGIN {printf \"%.1f\", $bytes/1024}")K"
    else
        echo "${bytes}B"
    fi
}

# 初始化日志目录
init_log_dir() {
    mkdir -p "$LOG_DIR"
    CURRENT_LOG="$LOG_DIR/disk-cleaner-$(ts).log"
    info "日志目录: $LOG_DIR"
    info "主日志文件: $CURRENT_LOG"
}

# 生成 JSON 报告片段
json_report() {
    local round="$1"
    local scanned_paths_json
    scanned_paths_json=$(printf '%s\n' "${ROUND_SCANNED_PATHS[$round]:-[]}" | jq -R . | jq -s .)
    local errors_json
    errors_json=$(printf '%s\n' "${ROUND_ERRORS[$round]:-}" | jq -R . | jq -s .)
    local recs_json
    recs_json=$(printf '%s\n' "${ROUND_RECOMMENDATIONS[$round]:-}" | jq -R . | jq -s .)

    cat <<EOF
{
  "timestamp": "${ROUND_TIMESTAMP[$round]:-not-run}",
  "round": $round,
  "scanned_paths": $scanned_paths_json,
  "candidates_found": ${ROUND_CANDIDATES_FOUND[$round]:-0},
  "candidates_size_mb": ${ROUND_CANDIDATES_SIZE_MB[$round]:-0},
  "deleted_count": ${ROUND_DELETED_COUNT[$round]:-0},
  "deleted_size_mb": ${ROUND_DELETED_SIZE_MB[$round]:-0},
  "errors": $errors_json,
  "recommendations": $recs_json
}
EOF
}

# 保存 JSON 报告
save_report() {
    local round="$1"
    local report_file="$LOG_DIR/round${round}-report-$(ts).json"
    json_report "$round" > "$report_file"
    info "报告已保存: $report_file"
}

# 打印分隔线
divider() {
    echo ""
    echo "============================================"
    echo "$*"
    echo "============================================"
}

#------------------------------
# Round 1: 安全清理（已知 pattern）
#------------------------------
run_round1() {
    local round=1
    divider "ROUND $round: 安全清理（已知 Pattern）"
    
    ROUND_TIMESTAMP[$round]=$(date -Iseconds)
    local candidates=()
    local total_size=0
    local errors=()

    info "读取 Pattern 文件: $PATTERNS_FILE"

    # --- 扫描 __pycache__ ---
    for root in "${SCAN_ROOTS[@]}"; do
        [[ -d "$root" ]] || [[ -e "$root" ]] || continue
        info "扫描: $root"
        while IFS= read -r -d '' item; do
            local size
            size=$(dir_size_mb "$item")
            candidates+=("$item|$size")
            total_size=$((total_size+size))
            ROUND_CANDIDATES_FOUND[$round]=$((${ROUND_CANDIDATES_FOUND[$round]:-0}+1))
        done < <(find "$root" -name '__pycache__' -type d -print0 2>/dev/null)
    done

    # --- 扫描 *.pyc ---
    for root in "${SCAN_ROOTS[@]}"; do
        [[ -d "$root" ]] || [[ -e "$root" ]] || continue
        while IFS= read -r -d '' item; do
            local size
            size=$(file_size_mb "$item")
            candidates+=("$item|$size")
            total_size=$((total_size+size))
            ROUND_CANDIDATES_FOUND[$round]=$((${ROUND_CANDIDATES_FOUND[$round]:-0}+1))
        done < <(find "$root" -name '*.pyc' -type f -print0 2>/dev/null)
    done

    # --- 扫描 .pytest_cache ---
    for root in "${SCAN_ROOTS[@]}"; do
        [[ -d "$root" ]] || continue
        while IFS= read -r -d '' item; do
            local size
            size=$(dir_size_mb "$item")
            candidates+=("$item|$size")
            total_size=$((total_size+size))
            ROUND_CANDIDATES_FOUND[$round]=$((${ROUND_CANDIDATES_FOUND[$round]:-0}+1))
        done < <(find "$root" -name '.pytest_cache' -type d -print0 2>/dev/null)
    done

    # --- 扫描 .cache 目录 ---
    for root in "${SCAN_ROOTS[@]}"; do
        [[ -d "$root" ]] || continue
        while IFS= read -r -d '' item; do
            local size
            size=$(dir_size_mb "$item")
            candidates+=("$item|$size")
            total_size=$((total_size+size))
            ROUND_CANDIDATES_FOUND[$round]=$((${ROUND_CANDIDATES_FOUND[$round]:-0}+1))
        done < <(find "$root" -name '.cache' -type d -print0 2>/dev/null)
    done

    # --- 扫描 *.log 文件（通用） ---
    for root in "${SCAN_ROOTS[@]}"; do
        [[ -d "$root" ]] || continue
        while IFS= read -r -d '' item; do
            local size
            size=$(file_size_mb "$item")
            # 仅记录，不自动删除（需要确认）
            candidates+=("$item|$size")
            total_size=$((total_size+size))
            ROUND_CANDIDATES_FOUND[$round]=$((${ROUND_CANDIDATES_FOUND[$round]:-0}+1))
        done < <(find "$root" -name '*.log' -type f -print0 2>/dev/null)
    done

    # --- 扫描 *.tmp, *.temp ---
    for root in "${SCAN_ROOTS[@]}"; do
        [[ -d "$root" ]] || continue
        while IFS= read -r -d '' item; do
            local size
            size=$(file_size_mb "$item")
            candidates+=("$item|$size")
            total_size=$((total_size+size))
            ROUND_CANDIDATES_FOUND[$round]=$((${ROUND_CANDIDATES_FOUND[$round]:-0}+1))
        done < <(find "$root" \( -name '*.tmp' -o -name '*.temp' \) -type f -print0 2>/dev/null)
    done

    # --- 扫描 Vim swap 文件 ---
    for root in "${SCAN_ROOTS[@]}"; do
        [[ -d "$root" ]] || continue
        while IFS= read -r -d '' item; do
            local size
            size=$(file_size_mb "$item")
            candidates+=("$item|$size")
            total_size=$((total_size+size))
            ROUND_CANDIDATES_FOUND[$round]=$((${ROUND_CANDIDATES_FOUND[$round]:-0}+1))
        done < <(find "$root" \( -name '*.swp' -o -name '*.swo' -o -name '*~' \) -type f -print0 2>/dev/null)
    done

    # --- 扫描 node_modules/.cache ---
    for root in "${SCAN_ROOTS[@]}"; do
        [[ -d "$root" ]] || continue
        while IFS= read -r -d '' item; do
            local size
            size=$(dir_size_mb "$item")
            candidates+=("$item|$size")
            total_size=$((total_size+size))
            ROUND_CANDIDATES_FOUND[$round]=$((${ROUND_CANDIDATES_FOUND[$round]:-0}+1))
        done < <(find "$root" -path '*/node_modules/.cache' -type d -print0 2>/dev/null)
    done

    # 汇总
    ROUND_CANDIDATES_SIZE_MB[$round]=$total_size
    ROUND_SCANNED_PATHS[$round]="[$(IFS=','; echo "${SCAN_ROOTS[*]}")]"

    info "发现 ${ROUND_CANDIDATES_FOUND[$round]:-0} 个候选，总计约 ${total_size}MB"
    : "${ROUND_CANDIDATES_FOUND[$round]:=0}" "${ROUND_DELETED_COUNT[$round]:=0}" "${ROUND_DELETED_SIZE_MB[$round]:=0}"

    # --- 显示候选列表 ---
    if [[ ${#candidates[@]} -eq 0 ]]; then
        info "Round 1: 没有发现需要清理的候选"
        ROUND_RECOMMENDATIONS[$round]="无候选"
        save_report "$round"
        return 0
    fi

    echo ""
    echo "【Round 1 候选清单】共 ${#candidates[@]} 项，约 ${total_size}MB"
    echo "--------------------------------------------"
    for c in "${candidates[@]}"; do
        local path="${c%%|*}"
        local size="${c##*|}"
        echo "  [${size}MB] $path"
    done
    echo "--------------------------------------------"

    # --- 确认删除 ---
    if [[ "$DRY_RUN" == "1" ]]; then
        info "DRY_RUN 模式: 跳过删除"
    elif [[ "$AUTO_CONFIRM" == "1" ]]; then
        info "AUTO_CONFIRM: 自动确认删除"
    else
        echo -n "确认删除以上 ${#candidates[@]} 项? (y/N): "
        local reply
        read -r reply
        if [[ "$reply" != "y" && "$reply" != "Y" ]]; then
            info "用户取消 Round 1"
            ROUND_RECOMMENDATIONS[$round]="用户取消"
            save_report "$round"
            return 0
        fi
    fi

    # --- 执行删除 ---
    local deleted_count=0
    local deleted_size=0
    for c in "${candidates[@]}"; do
        local path="${c%%|*}"
        local size="${c##*|}"
        
        if [[ -e "$path" ]]; then
            if [[ "$DRY_RUN" != "1" ]]; then
                rm -rf "$path" 2>/dev/null
            fi
            
            if [[ "$?" == "0" ]] || [[ "$DRY_RUN" == "1" && -e "$path" ]]; then
                deleted_count=$((deleted_count+1))
                deleted_size=$((deleted_size+size))
                info "删除: $path (${size}MB)"
            else
                errors+=("删除失败: $path")
                GLOBAL_ERRORS+=("Round1: $path")
            fi
        fi
    done

    # --- 验证 ---
    local verified=0
    local verified_size=0
    for c in "${candidates[@]}"; do
        local path="${c%%|*}"
        local size="${c##*|}"
        if [[ ! -e "$path" ]]; then
            verified=$((verified+1))
            ((verified_size += size))
        fi
    done

    ROUND_DELETED_COUNT[$round]=$deleted_count
    ROUND_DELETED_SIZE_MB[$round]=$deleted_size
    ROUND_ERRORS[$round]="${errors[*]:-}"
    ROUND_RECOMMENDATIONS[$round]="安全清理完成，删除 $deleted_count 项，释放约 $deleted_size MB"

    info "Round 1 完成: 删除 $deleted_count 项，验证 $verified 项仍存在"

    # --- 干运行模式补充计数 ---
    if [[ "$DRY_RUN" == "1" ]]; then
        ROUND_DELETED_COUNT[$round]=0
        ROUND_DELETED_SIZE_MB[$round]=0
        ROUND_RECOMMENDATIONS[$round]="DRY_RUN: 需删除 ${#candidates[@]} 项，约 ${total_size}MB"
    fi

    save_report "$round"
}

#------------------------------
# Round 2: 大文件扫描
#------------------------------
run_round2() {
    local round=2
    divider "ROUND $round: 大文件扫描 (>100MB, >30天未访问)"

    ROUND_TIMESTAMP[$round]=$(date -Iseconds)
    local candidates=()
    local total_size=0
    local errors=()

    ROUND_CANDIDATES_FOUND[$round]=0

    info "扫描 > 100MB 的文件..."

    # --- 扫描 > 100MB 的文件 ---
    for root in "${SCAN_ROOTS[@]}"; do
        [[ -d "$root" ]] || continue
        info "大文件扫描: $root"
        while IFS= read -r -d '' item; do
            local size_bytes
            size_bytes=$(stat -c%s "$item" 2>/dev/null) || continue
            local size_mb=$((size_bytes / 1024 / 1024))
            
            candidates+=("$item|$size_mb")
            total_size=$((total_size+size_mb))
            ROUND_CANDIDATES_FOUND[$round]=$((${ROUND_CANDIDATES_FOUND[$round]:-0}+1))
            info "  大文件: $item (${size_mb}MB)"
        done < <(find "$root" -type f -size +100M -print0 2>/dev/null)
    done

    info "扫描 > 30天未访问的大文件 (>10MB 且 >30天)..."

    # --- 扫描 > 30天未访问的大文件 ---
    for root in "${SCAN_ROOTS[@]}"; do
        [[ -d "$root" ]] || continue
        while IFS= read -r -d '' item; do
            # 跳过已经是候选的（避免重复）
            local already=0
            for c in "${candidates[@]}"; do
                [[ "${c%%|*}" == "$item" ]] && already=1 && break
            done
            [[ "$already" == "1" ]] && continue

            local size_bytes
            size_bytes=$(stat -c%s "$item" 2>/dev/null) || continue
            local size_mb=$((size_bytes / 1024 / 1024))
            
            candidates+=("$item|$size_mb")
            total_size=$((total_size+size_mb))
            ROUND_CANDIDATES_FOUND[$round]=$((${ROUND_CANDIDATES_FOUND[$round]:-0}+1))
            info "  旧文件: $item (${size_mb}MB, atime > 30天)"
        done < <(find "$root" -type f -atime +30 -size +10M -print0 2>/dev/null)
    done

    ROUND_CANDIDATES_SIZE_MB[$round]=$total_size
    ROUND_SCANNED_PATHS[$round]="[$(IFS=','; echo "${SCAN_ROOTS[*]}")]"
    ROUND_DELETED_COUNT[$round]=0
    ROUND_DELETED_SIZE_MB[$round]=0

    info "发现 ${ROUND_CANDIDATES_FOUND[$round]:-0} 个候选，总计约 ${total_size}MB"

    if [[ ${#candidates[@]} -eq 0 ]]; then
        info "Round 2: 没有发现大文件候选"
        ROUND_RECOMMENDATIONS[$round]="无候选"
        save_report "$round"
        return 0
    fi

    # --- 显示候选 + 元数据 ---
    echo ""
    echo "【Round 2 候选清单】共 ${#candidates[@]} 项，约 ${total_size}MB"
    echo "--------------------------------------------"
    for c in "${candidates[@]}"; do
        local path="${c%%|*}"
        local size="${c##*|}"
        local atime
        atime=$(stat -c "%y" "$path" 2>/dev/null | cut -d' ' -f1 || echo "unknown")
        local ftype
        ftype=$(file -b "$path" 2>/dev/null | cut -d',' -f1 || echo "unknown")
        echo "  [${size}MB] [$atime] [$ftype]"
        echo "    $path"
    done
    echo "--------------------------------------------"
    echo ""
    echo "⚠️  大文件删除风险较高，请仔细确认！"

    # --- 确认删除 ---
    if [[ "$DRY_RUN" == "1" ]]; then
        info "DRY_RUN 模式: 跳过删除"
    elif [[ "$AUTO_CONFIRM" == "1" ]]; then
        warn "AUTO_CONFIRM: 跳过确认 (大文件高风险!)"
    else
        echo -n "确认删除以上 ${#candidates[@]} 项? 输入 'yes-delete' 确认: "
        local reply
        read -r reply
        if [[ "$reply" != "yes-delete" ]]; then
            info "用户取消 Round 2"
            ROUND_RECOMMENDATIONS[$round]="用户取消"
            save_report "$round"
            return 0
        fi
    fi

    # --- 执行删除 ---
    local deleted_count=0
    local deleted_size=0
    for c in "${candidates[@]}"; do
        local path="${c%%|*}"
        local size="${c##*|}"
        
        if [[ -e "$path" ]]; then
            if [[ "$DRY_RUN" != "1" ]]; then
                rm -f "$path" 2>/dev/null
            fi
            
            if [[ "$?" == "0" ]] || [[ "$DRY_RUN" == "1" && -e "$path" ]]; then
                deleted_count=$((deleted_count+1))
                deleted_size=$((deleted_size+size))
                info "删除: $path (${size}MB)"
            else
                errors+=("删除失败: $path")
                GLOBAL_ERRORS+=("Round2: $path")
            fi
        fi
    done

    ROUND_DELETED_COUNT[$round]=$deleted_count
    ROUND_DELETED_SIZE_MB[$round]=$deleted_size
    ROUND_ERRORS[$round]="${errors[*]:-}"
    ROUND_RECOMMENDATIONS[$round]="大文件清理完成，删除 $deleted_count 项，释放约 $deleted_size MB"

    info "Round 2 完成: 删除 $deleted_count 项"

    if [[ "$DRY_RUN" == "1" ]]; then
        ROUND_DELETED_COUNT[$round]=0
        ROUND_DELETED_SIZE_MB[$round]=0
        ROUND_RECOMMENDATIONS[$round]="DRY_RUN: 需删除 ${#candidates[@]} 项，约 ${total_size}MB"
    fi

    save_report "$round"
}

#------------------------------
# Round 3: 深度分析
#------------------------------
run_round3() {
    local round=3
    divider "ROUND $round: 深度分析（重复文件 + 孤立大目录）"

    ROUND_TIMESTAMP[$round]=$(date -Iseconds)
    local candidates=()
    local total_size=0
    local errors=()

    ROUND_CANDIDATES_FOUND[$round]=0

    info "=== 阶段 A: 扫描重复文件 ==="

    # 深度分析较慢，先按大小分组找候选
    # 找 > 5MB 的文件，按大小分组
    declare -A size_groups
    local tmp_size_map="$LOG_DIR/size-map-$(ts).tmp"
    > "$tmp_size_map"

    for root in "${SCAN_ROOTS[@]}"; do
        [[ -d "$root" ]] || continue
        info "深度扫描: $root"
        while IFS= read -r -d '' item; do
            local size_bytes
            size_bytes=$(stat -c%s "$item" 2>/dev/null) || continue
            local size_mb=$((size_bytes / 1024 / 1024))
            # 仅关注 > 5MB 的文件
            ((size_mb < 5)) && continue
            echo "$size_bytes|$item" >> "$tmp_size_map"
        done < <(find "$root" -type f -size +5M -print0 2>/dev/null)
    done

    # 按大小排序，找相同大小的文件（重复文件候选）
    info "分析相同大小的文件（重复候选）..."
    local prev_size=""
    local same_size_group=()

    while IFS='|' read -r size_bytes path; do
        [[ -z "$size_bytes" ]] && continue
        if [[ "$size_bytes" == "$prev_size" ]]; then
            same_size_group+=("$path")
        else
            # 处理上一组
            if [[ ${#same_size_group[@]} -gt 1 ]]; then
                info "发现 ${#same_size_group[@]} 个相同大小 ($((prev_size/1024/1024))MB) 文件"
                for p in "${same_size_group[@]}"; do
                    [[ -f "$p" ]] || continue
                    local size_mb=$((size_bytes / 1024 / 1024))
                    candidates+=("$p|$size_mb|duplicate")
                    total_size=$((total_size+size_mb))
                    ROUND_CANDIDATES_FOUND[$round]=$((${ROUND_CANDIDATES_FOUND[$round]:-0}+1))
                done
            fi
            same_size_group=("$path")
            prev_size="$size_bytes"
        fi
    done < <(sort -t'|' -k1 -n "$tmp_size_map" 2>/dev/null)

    # 处理最后一组
    if [[ ${#same_size_group[@]} -gt 1 ]]; then
        for p in "${same_size_group[@]}"; do
            [[ -f "$p" ]] || continue
            local size_mb=$((prev_size / 1024 / 1024))
            candidates+=("$p|$size_mb|duplicate")
            total_size=$((total_size+size_mb))
            ROUND_CANDIDATES_FOUND[$round]=$((${ROUND_CANDIDATES_FOUND[$round]:-0}+1))
        done
    fi

    rm -f "$tmp_size_map"

    info "=== 阶段 B: 扫描孤立大目录 (>50MB 且 < 30天无子目录变更) ==="

    # 找 > 50MB 的目录，且很久没有被修改
    for root in "${SCAN_ROOTS[@]}"; do
        [[ -d "$root" ]] || continue
        while IFS= read -r -d '' item; do
            # 检查是否有最近变更的子目录
            local recent_change
            recent_change=$(find "$item" -maxdepth 2 -type d -atime -30 2>/dev/null | wc -l)
            ((recent_change > 1)) && continue  # 有近期变更，跳过

            local size
            size=$(dir_size_mb "$item")
            ((size < 50)) && continue

            candidates+=("$item|$size|orphaned_dir")
            total_size=$((total_size+size))
            ROUND_CANDIDATES_FOUND[$round]=$((${ROUND_CANDIDATES_FOUND[$round]:-0}+1))
            info "  孤立大目录: $item (${size}MB)"
        done < <(find "$root" -type d -size +50M -print0 2>/dev/null)
    done

    ROUND_CANDIDATES_SIZE_MB[$round]=$total_size
    ROUND_SCANNED_PATHS[$round]="[$(IFS=','; echo "${SCAN_ROOTS[*]}")]"
    ROUND_DELETED_COUNT[$round]=0
    ROUND_DELETED_SIZE_MB[$round]=0

    info "发现 ${ROUND_CANDIDATES_FOUND[$round]:-0} 个深度分析候选，总计约 ${total_size}MB"

    if [[ ${#candidates[@]} -eq 0 ]]; then
        info "Round 3: 没有发现深度分析候选"
        ROUND_RECOMMENDATIONS[$round]="无候选"
        save_report "$round"
        return 0
    fi

    # --- 显示候选 ---
    echo ""
    echo "【Round 3 候选清单】共 ${#candidates[@]} 项，约 ${total_size}MB"
    echo "--------------------------------------------"
    local dup_count=0 dir_count=0
    for c in "${candidates[@]}"; do
        local path="${c%%|*}"
        local rest="${c#*|}"
        local size="${rest%%|*}"
        local type="${rest##*|}"
        
        echo -n "  [${size}MB] [$type] $path"
        if [[ "$type" == "duplicate" ]]; then
            dup_count=$((dup_count+1))
            echo " (⚠️ 重复文件，建议保留一份)"
        else
            dir_count=$((dir_count+1))
            echo " (⚠️ 孤立大目录)"
        fi
    done
    echo "--------------------------------------------"
    echo "  重复文件: $dup_count 项 | 孤立目录: $dir_count 项"
    echo "--------------------------------------------"
    echo ""
    echo "⚠️  深度分析风险最高，请务必确认！"

    # --- 确认 ---
    if [[ "$DRY_RUN" == "1" ]]; then
        info "DRY_RUN 模式: 跳过删除"
    elif [[ "$AUTO_CONFIRM" == "1" ]]; then
        warn "AUTO_CONFIRM: 跳过确认 (深度分析极高风险!)"
    else
        echo -n "确认删除以上 ${#candidates[@]} 项? 输入 'yes-delete-deep' 确认: "
        local reply
        read -r reply
        if [[ "$reply" != "yes-delete-deep" ]]; then
            info "用户取消 Round 3"
            ROUND_RECOMMENDATIONS[$round]="用户取消"
            save_report "$round"
            return 0
        fi
    fi

    # --- 执行删除 ---
    local deleted_count=0
    local deleted_size=0
    for c in "${candidates[@]}"; do
        local path="${c%%|*}"
        local rest="${c#*|}"
        local size="${rest%%|*}"
        local type="${rest##*|}"
        
        if [[ -e "$path" ]]; then
            if [[ "$DRY_RUN" != "1" ]]; then
                if [[ "$type" == "orphaned_dir" ]]; then
                    rm -rf "$path" 2>/dev/null
                else
                    rm -f "$path" 2>/dev/null
                fi
            fi
            
            if [[ "$?" == "0" ]] || [[ "$DRY_RUN" == "1" && -e "$path" ]]; then
                deleted_count=$((deleted_count+1))
                deleted_size=$((deleted_size+size))
                info "删除 [$type]: $path (${size}MB)"
            else
                errors+=("删除失败 [$type]: $path")
                GLOBAL_ERRORS+=("Round3: $path")
            fi
        fi
    done

    ROUND_DELETED_COUNT[$round]=$deleted_count
    ROUND_DELETED_SIZE_MB[$round]=$deleted_size
    ROUND_ERRORS[$round]="${errors[*]:-}"
    ROUND_RECOMMENDATIONS[$round]="深度清理完成，删除 $deleted_count 项，释放约 $deleted_size MB"

    info "Round 3 完成: 删除 $deleted_count 项"

    if [[ "$DRY_RUN" == "1" ]]; then
        ROUND_DELETED_COUNT[$round]=0
        ROUND_DELETED_SIZE_MB[$round]=0
        ROUND_RECOMMENDATIONS[$round]="DRY_RUN: 需删除 ${#candidates[@]} 项，约 ${total_size}MB"
    fi

    save_report "$round"
}

#------------------------------
# 生成最终汇总报告
#------------------------------
generate_summary() {
    divider "磁盘清理汇总报告"

    local total_deleted_count=0
    local total_deleted_size=0
    local total_candidates=0

    for r in 1 2 3; do
        [[ "${ROUND_DELETED_COUNT[$r]:-0}" == "0" && "${ROUND_CANDIDATES_FOUND[$r]:-0}" == "0" ]] && continue
        total_deleted_count=$((total_deleted_count + ${ROUND_DELETED_COUNT[$r]:-0}))
        total_deleted_size=$((total_deleted_size + ${ROUND_DELETED_SIZE_MB[$r]:-0}))
        total_candidates=$((total_candidates + ${ROUND_CANDIDATES_FOUND[$r]:-0}))
        echo "  Round $r: 删除 ${ROUND_DELETED_COUNT[$r]:-0} 项, 释放 ${ROUND_DELETED_SIZE_MB[$r]:-0} MB"
    done

    echo ""
    echo "  📊 总计: 发现 $total_candidates 候选，删除 $total_deleted_count 项，释放约 $total_deleted_size MB"
    
    if [[ ${#GLOBAL_ERRORS[@]} -gt 0 ]]; then
        echo ""
        echo "  ⚠️  错误 (${#GLOBAL_ERRORS[@]}):"
        for e in "${GLOBAL_ERRORS[@]}"; do
            echo "    - $e"
        done
    fi

    # 保存汇总 JSON
    local summary_file="$LOG_DIR/summary-$(ts).json"
    local errors_json="[$(IFS=','; echo "${GLOBAL_ERRORS[*]+${GLOBAL_ERRORS[*]}}")]"
    [[ ${#GLOBAL_ERRORS[@]} -eq 0 ]] && errors_json="[]"

    cat <<EOF > "$summary_file"
{
  "timestamp": "$(date -Iseconds)",
  "summary": {
    "total_candidates": $total_candidates,
    "total_deleted_count": $total_deleted_count,
    "total_deleted_size_mb": $total_deleted_size,
    "errors": $errors_json
  },
  "rounds": {
    "1": $(json_report 1),
    "2": $(json_report 2),
    "3": $(json_report 3)
  }
}
EOF

    info "汇总报告: $summary_file"
}

#------------------------------
# 帮助信息
#------------------------------
usage() {
    cat <<EOF
Disk Cleaner Executor - 三轮磁盘清理脚本

用法: $0 [OPTIONS]

Options:
  --dry-run           仅扫描，不删除
  --auto-confirm      自动确认所有轮次（跳过交互）
  --round N           仅运行第 N 轮 (1|2|3)
  --scan-root DIR     添加扫描根目录（可多次指定）
  --help              显示此帮助

环境变量:
  DRY_RUN=1           干运行模式
  AUTO_CONFIRM=1      自动确认
  PATTERNS_FILE       safe-patterns.md 路径
  FRAMEWORK_FILE      framework.md 路径
  LOG_DIR             日志目录

示例:
  $0 --dry-run                        # 干运行，查看会清理什么
  $0 --auto-confirm                   # 自动确认执行
  $0 --round 1                        # 仅运行 Round 1
  DRY_RUN=1 $0                        # 干运行（环境变量方式）

Round 说明:
  Round 1 - 安全清理: 删除 __pycache__, *.pyc, node_modules 等已知安全 pattern
  Round 2 - 大文件扫描: 找出 > 100MB 和 > 30天未访问的大文件
  Round 3 - 深度分析: 扫描重复文件、孤立大目录

EOF
}

#------------------------------
# 解析参数
#------------------------------
parse_args() {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --dry-run)
                DRY_RUN=1
                shift
                ;;
            --auto-confirm)
                AUTO_CONFIRM=1
                shift
                ;;
            --round)
                RUN_ROUND="$2"
                shift 2
                ;;
            --scan-root)
                SCAN_ROOTS+=("$2")
                shift 2
                ;;
            --help|-h)
                usage
                exit 0
                ;;
            *)
                echo "未知参数: $1"
                usage
                exit 1
                ;;
        esac
    done
}

#------------------------------
# 主流程
#------------------------------
main() {
    echo "磁盘清理脚本启动 | $(date)"
    echo "DRY_RUN=$DRY_RUN | AUTO_CONFIRM=$AUTO_CONFIRM | RUN_ROUND=$RUN_ROUND"
    echo "扫描根目录: ${SCAN_ROOTS[*]}"
    
    init_log_dir

    # 检查依赖
    for cmd in jq find du stat sort; do
        if ! command -v "$cmd" &>/dev/null; then
            warn "命令 '$cmd' 未安装，部分功能可能受影响"
        fi
    done

    # 检查参考文件
    if [[ ! -f "$PATTERNS_FILE" ]]; then
        warn "Pattern 文件不存在: $PATTERNS_FILE，将使用内置 pattern"
    fi
    if [[ ! -f "$FRAMEWORK_FILE" ]]; then
        warn "Framework 文件不存在: $FRAMEWORK_FILE，将使用内置策略"
    fi

    # 运行轮次
    if [[ "$RUN_ROUND" == "0" ]]; then
        run_round1
        run_round2
        run_round3
    else
        case "$RUN_ROUND" in
            1) run_round1 ;;
            2) run_round2 ;;
            3) run_round3 ;;
            *) echo "无效轮次: $RUN_ROUND (仅支持 1|2|3)"; exit 1 ;;
        esac
    fi

    generate_summary

    echo ""
    info "磁盘清理完成!"
    [[ "$DRY_RUN" == "1" ]] && info "DRY_RUN 模式: 未实际删除任何文件"
}

parse_args "$@"
main
