# 安全可删除文件 Patterns 列表

> 本文档用于磁盘清理场景，列出可以安全删除的文件类型、路径和条件。

---

## 1. 缓存文件

### 1.1 Python 编译缓存

| Pattern/路径 | 风险等级 | 删除条件 | 需要人工确认 |
|---|---|---|---|
| `**/*.pyc` | LOW | 无条件可删 | 否 |
| `**/__pycache__/` | LOW | 无条件可删 | 否 |
| `**/*.pyo` | LOW | 无条件可删 | 否 |

**find 命令示例：**
```bash
# 删除所有 __pycache__ 目录
find /path/to/scan -type d -name '__pycache__' -exec rm -rf {} +

# 删除所有 .pyc 文件
find /path/to/scan -type f -name '*.pyc' -delete

# 删除所有 .pyo 文件
find /path/to/scan -type f -name '*.pyo' -delete
```

### 1.2 Java 编译缓存

| Pattern/路径 | 风险等级 | 删除条件 | 需要人工确认 |
|---|---|---|---|
| `**/*.class` | LOW | 无条件可删（构建目录内） | 是（确认在构建目录内） |

**find 命令示例：**
```bash
# 删除 target/ 下的 .class 文件（仅在确认不需要保留编译结果时）
find /path/to/scan -type d -name 'target' -exec find {} -type f -name '*.class' -delete \;
```

### 1.3 Node.js / 前端构建缓存

| Pattern/路径 | 风险等级 | 删除条件 | 需要人工确认 |
|---|---|---|---|
| `**/node_modules/.cache/` | LOW | 无条件可删 | 否 |
| `**/*.tsbuildinfo` | LOW | 无条件可删 | 否 |
| `**/.npm/_cacache/` | MEDIUM | 谨慎，确认不在生产环境 | 是 |

**find 命令示例：**
```bash
# 删除 node_modules/.cache
find /path/to/scan -type d -path '*/node_modules/.cache' -exec rm -rf {} +

# 删除 .tsbuildinfo 文件
find /path/to/scan -type f -name '*.tsbuildinfo' -delete
```

### 1.4 日志文件

| Pattern/路径 | 风险等级 | 删除条件 | 需要人工确认 |
|---|---|---|---|
| `**/*.log` | MEDIUM | 超过 30 天未修改，且非实时业务日志 | 是 |
| `**/*.tmp` | LOW | 超过 7 天未访问 | 否 |
| `**/*.temp` | LOW | 超过 7 天未访问 | 否 |

**find 命令示例：**
```bash
# 删除 30 天前的 .log 文件
find /path/to/scan -type f -name '*.log' -atime +30 -delete

# 删除 7 天前的临时文件
find /path/to/scan -type f \( -name '*.tmp' -o -name '*.temp' \) -atime +7 -delete

# ⚠️ 安全做法：先列出不删除，观察确认后再删
find /path/to/scan -type f -name '*.log' -atime +30 -print
```

---

## 2. 构建产物（可重建）

> 这些目录/文件都是构建输出，可以从源代码重新生成，删除风险低。

| Pattern/路径 | 风险等级 | 删除条件 | 需要人工确认 |
|---|---|---|---|
| `**/dist/` | MEDIUM | 确认是构建产物而非源码 | 是 |
| `**/build/` | MEDIUM | 确认是构建产物而非源码 | 是 |
| `**/out/` | MEDIUM | 确认是构建产物而非源码 | 是 |
| `**/target/` (Rust/Cargo) | LOW | 无条件可删 | 否 |
| `**/*.o` (非系统目录) | LOW | 在项目目录内 | 否 |
| `**/*.a` (非系统目录) | LOW | 在项目目录内 | 否 |
| `**/*.so` (非系统目录) | MEDIUM | 在项目目录内，非系统库 | 是 |
| `**/.next/` | LOW | 无条件可删 | 否 |
| `**/.nuxt/` | LOW | 无条件可删 | 否 |
| `**/.cache/` (项目内) | LOW | 无条件可删 | 否 |
| `**/coverage/` | LOW | 无条件可删（测试覆盖率报告） | 否 |

**find 命令示例：**
```bash
# 删除 Rust target 目录
find /path/to/scan -type d -name 'target' -exec rm -rf {} +

# 删除所有 dist/ 和 build/ 目录（先预览）
find /path/to/scan -type d \( -name 'dist' -o -name 'build' -o -name 'out' \) -print

# 确认后删除
find /path/to/scan -type d \( -name 'dist' -o -name 'build' -o -name 'out' \) -exec rm -rf {} +

# 删除 .next .nuxt .cache 目录
find /path/to/scan -type d \( -name '.next' -o -name '.nuxt' -o -name '.cache' \) -exec rm -rf {} +

# 删除 coverage 目录
find /path/to/scan -type d -name 'coverage' -exec rm -rf {} +
```

---

## 3. 开发环境临时文件

| Pattern/路径 | 风险等级 | 删除条件 | 需要人工确认 |
|---|---|---|---|
| `**/.venv/` | MEDIUM | 确认虚拟环境可重建 | 是 |
| `**/venv/` | MEDIUM | 确认虚拟环境可重建 | 是 |
| `**/env/` | MEDIUM | 确认虚拟环境可重建 | 是 |
| `**/*.egg-info/` | LOW | 无条件可删 | 否 |
| `**/.pytest_cache/` | LOW | 无条件可删 | 否 |
| `**/__pycache__/` | LOW | 见 1.1 节 | 否 |
| `**/.idea/workspace.xml` | MEDIUM | 仅 workspace.xml，其他 Idea 文件勿删 | 是 |

**find 命令示例：**
```bash
# 删除虚拟环境（⚠️ 强烈建议人工确认）
find /path/to/scan -type d \( -name '.venv' -o -name 'venv' -o -name 'env' \) -exec rm -rf {} +

# 删除 .egg-info
find /path/to/scan -type d -name '*.egg-info' -exec rm -rf {} +

# 删除 .pytest_cache
find /path/to/scan -type d -name '.pytest_cache' -exec rm -rf {} +

# 删除 Idea workspace.xml（保留其他 .idea 文件）
find /path/to/scan -type f -name 'workspace.xml' -path '*/.idea/*' -delete
```

---

## 4. 下载/解压残留

| Pattern/路径 | 风险等级 | 删除条件 | 需要人工确认 |
|---|---|---|---|
| `~/Downloads/*.tar.gz` | MEDIUM | 超过 30 天未访问 | 是 |
| `~/Downloads/*.zip` | MEDIUM | 超过 30 天未访问 | 是 |
| `~/Downloads/*.tgz` | MEDIUM | 超过 30 天未访问 | 是 |
| 重复的压缩包 | MEDIUM | 与同名目录内容重复 | 是 |

**find 命令示例：**
```bash
# 删除下载目录中 30 天未访问的压缩包
find ~/Downloads -type f \( -name '*.tar.gz' -o -name '*.zip' -o -name '*.tgz' -o -name '*.bz2' \) -atime +30 -delete

# 先预览
find ~/Downloads -type f \( -name '*.tar.gz' -o -name '*.zip' -o -name '*.tgz' -o -name '*.bz2' \) -atime +30 -print
```

---

## 5. 旧镜像/容器残渣

| Pattern/路径 | 风险等级 | 删除条件 | 需要人工确认 |
|---|---|---|---|
| dangling Docker 镜像 | MEDIUM | 无标签、未使用的镜像 | 是 |
| Docker 构建缓存 | MEDIUM | 确认无正在使用的构建缓存 | 是 |
| 停止的容器残渣 | LOW | 确认容器已停止且不再需要 | 是 |

**命令示例：**
```bash
# ⚠️ 以下命令需要 Docker 权限，建议非 root 用户使用 docker 命令
# 列出 dangling（无标签）镜像
docker images -f "dangling=true"

# 删除 dangling 镜像
docker image prune -f

# 删除所有未使用的镜像（谨慎）
docker image prune -a -f

# 删除停止的容器
docker container prune -f

# 完全清理（谨慎）
docker system prune -a -f
```

---

## 6. 大文件识别阈值

> 大文件往往占用最多磁盘空间，以下是识别标准：

| 阈值条件 | 风险等级 | 删除条件 | 需要人工确认 |
|---|---|---|---|
| 单文件 > 100MB 且 60 天未访问 | MEDIUM | 确认非活跃使用文件 | 是 |
| 单文件 > 500MB 且 180 天未访问 | HIGH | 确认非活跃使用文件 | 是 |
| 单文件 > 1GB 且 1 年未访问 | HIGH | 极度谨慎 | 是 |

**find 命令示例：**
```bash
# 找出 > 100MB 且 60 天未访问的文件（先预览）
find /path/to/scan -type f -size +100M -atime +60 -print

# 找出 > 500MB 且 180 天未访问的文件
find /path/to/scan -type f -size +500M -atime +180 -print

# 找出 > 1GB 的文件（无论访问时间）
find /path/to/scan -type f -size +1G -print

# 结合人类可读输出
find /path/to/scan -type f -size +100M -atime +60 -exec ls -lh {} \;
```

---

## 7. 危险排除清单（绝对不删）

> 以下路径和文件 **绝对不可删除**，否则系统或数据将遭受不可逆损坏：

| 路径/Pattern | 风险等级 | 说明 |
|---|---|---|
| `/etc/` | 🔴 极高 | 系统配置目录，删后系统崩溃 |
| `/usr/` | 🔴 极高 | 系统程序和库，删后系统无法运行 |
| `/bin/` | 🔴 极高 | 核心可执行文件 |
| `/sbin/` | 🔴 极高 | 核心系统可执行文件 |
| `/lib*/` | 🔴 极高 | 核心系统库（/lib, /lib64 等） |
| `/var/lib/` 下的系统数据库 | 🔴 极高 | 如 pacman、dpkg 数据库等 |
| `/var/log/` 下的活跃日志 | 🔴 极高 | 当前正在写入的日志 |
| `~/.ssh/` | 🔴 极高 | SSH 密钥和配置，删除后无法远程登录 |
| `~/.gnupg/` | 🔴 极高 | GPG 密钥，删除后加密数据永久丢失 |
| 用户家目录的 Documents/ | 🔴 极高 | 用户文档 |
| 用户家目录的 Desktop/ | 🔴 极高 | 桌面文件 |
| `/boot/` | 🔴 极高 | 内核和启动文件 |
| `/proc/` | 🔴 极高 | 虚拟文件系统 |
| `/sys/` | 🔴 极高 | 系统内核接口 |
| `/dev/` | 🔴 极高 | 设备文件 |

### 排除命令示例

```bash
# 安全扫描：在排除危险目录后执行清理
# 例如：清理 __pycache__ 但排除系统目录
find /path/to/scan \
  -type d -name '__pycache__' \
  ! -path '*/etc/*' \
  ! -path '*/usr/*' \
  ! -path '*/.local/share/Trash/*' \
  -exec rm -rf {} +

# 排除示例（通用安全 find 模板）
find /path/to/scan -type f -name '*.pyc' \
  ! -path '/etc/*' \
  ! -path '/usr/*' \
  ! -path '/var/*' \
  -delete
```

---

## 8. 综合清理脚本模板

```bash
#!/bin/bash
# disk-cleaner-safe.sh — 安全清理模板（请根据实际情况修改路径）

SCAN_ROOT="${1:-.}"   # 默认当前目录，可传参指定

echo "=== 安全清理预览模式（不实际删除）==="
echo "扫描根目录: $SCAN_ROOT"
echo ""

# 1. Python 缓存
echo "[1/7] Python 缓存..."
find "$SCAN_ROOT" -type d -name '__pycache__' -print 2>/dev/null
find "$SCAN_ROOT" -type f -name '*.pyc' -print 2>/dev/null

# 2. Node 缓存
echo "[2/7] Node 缓存..."
find "$SCAN_ROOT" -type d -path '*/node_modules/.cache' -print 2>/dev/null

# 3. 构建产物
echo "[3/7] 构建产物..."
find "$SCAN_ROOT" -type d \( -name 'target' -o -name '.next' -o -name '.nuxt' \) -print 2>/dev/null

# 4. 虚拟环境
echo "[4/7] 虚拟环境（建议手动确认）..."
find "$SCAN_ROOT" -type d \( -name '.venv' -o -name 'venv' \) -print 2>/dev/null

# 5. 日志
echo "[5/7] 30天前日志..."
find "$SCAN_ROOT" -type f -name '*.log' -atime +30 -print 2>/dev/null

# 6. 大文件
echo "[6/7] 大文件 (>100MB, 60天未访问)..."
find "$SCAN_ROOT" -type f -size +100M -atime +60 -print 2>/dev/null

# 7. 危险排除检查
echo "[7/7] 危险路径检查..."
find "$SCAN_ROOT" -type d \( -name 'etc' -o -name 'usr' -o -name 'bin' -o -name 'sbin' -o -name 'lib' \) -print 2>/dev/null

echo ""
echo "=== 预览结束 ==="
echo "如确认无误，删除 --dry-run 参数并确保 SCAN_ROOT 正确。"
```

---

## 9. 各语言/框架速查表

| 技术栈 | 可删目录/文件 | 风险 |
|---|---|---|
| Python | `__pycache__/`, `*.pyc`, `*.pyo`, `.pytest_cache/`, `*.egg-info/` | LOW |
| Java | `target/`, `*.class` | LOW |
| Node.js | `node_modules/`, `.npm/`, `.cache/`, `*.tsbuildinfo` | LOW（仅 .cache） |
| Rust | `target/` | LOW |
| Go | `vendor/`（如用 mod）| MEDIUM |
| .NET | `bin/`, `obj/` | LOW |
| Ruby | `.bundle/`, `vendor/cache/` | MEDIUM |
| PHP | `vendor/`, `.phpunit.cache/` | MEDIUM |
| Flutter | `.dart_tool/`, `build/` | LOW |
| Android | `build/`, `.gradle/` | MEDIUM |

---

## 10. 风险等级说明

| 等级 | 含义 | 建议 |
|---|---|---|
| 🔴 极高 | 删后系统/数据永久损坏 | 绝对禁止 |
| HIGH | 删除后功能严重受损 | 必须人工确认 |
| MEDIUM | 删除后需重建，但可恢复 | 建议预览后操作 |
| LOW | 删除后自动重建或无实质影响 | 可放心清理 |

---

*文档版本：2026-04-16*
*适用场景：个人开发机、CI/CD 服务器、Web 服务器磁盘清理*
