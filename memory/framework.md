# Disk Cleaner Framework

## 执行策略总览

```
Round 1: 安全清理 → 低风险 Pattern，直接扫描删除
Round 2: 大文件扫描 → >100MB 文件，>30天未访问大文件
Round 3: 深度分析 → 重复文件、孤立大目录
```

## 每轮必须步骤

### 1. 扫描发现 (Scan)
- 使用 `find` 列出候选文件/目录
- 限定扫描根目录（避免扫描 /sys, /proc 等系统目录）
- 使用 `-type f` 或 `-type d` 限定类型
- 记录原始候选列表

### 2. 评估分析 (Evaluate)
- `du -sh` 统计每个候选的大小
- `stat` 获取元数据（访问时间、修改时间）
- `file` 识别文件类型
- 生成评估报告

### 3. 生成报告 (Report)
- JSON 格式输出
- 包含：发现数量、总大小、风险等级、建议
- 保存到 `~/.openclaw/logs/disk-cleaner/`

### 4. 执行删除 (Execute)
- 仅删除用户确认的项目
- 使用 `rm -rf` 删除目录
- 使用 `rm -f` 删除文件
- 记录已删除清单

### 5. 结果验证 (Verify)
- 确认文件已不存在
- 统计实际释放空间
- 更新最终报告

## 扫描根目录配置

```bash
SCAN_ROOTS=(
    "$HOME/.openclaw"
    "$HOME/.cache"
    "$HOME/tmp"
    "/tmp"
    "$HOME/Downloads"
)
```

## 日志目录结构

```
~/.openclaw/logs/disk-cleaner/
├── round1-scan-YYYYMMDD-HHMMSS.log
├── round1-report-YYYYMMDD-HHMMSS.json
├── round2-scan-YYYYMMDD-HHMMSS.log
├── round2-report-YYYYMMDD-HHMMSS.json
├── round3-scan-YYYYMMDD-HHMMSS.log
├── round3-report-YYYYMMDD-HHMMSS.json
└── summary-YYYYMMDD-HHMMSS.json
```

## 确认机制

- 交互模式：每轮清理前显示待删列表，等待用户输入 y/n
- 静默模式：`AUTO_CONFIRM=1` 环境变量跳过确认
- 干运行模式：`DRY_RUN=1` 仅扫描不删除

## 并发与性能

- 大目录扫描使用 `find` 单线程避免 IO 过载
- 日志写入使用追加模式
- JSON 报告每轮独立文件
