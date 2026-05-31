# Safe Patterns for Disk Cleaning

## 目录清理 Pattern（风险低，可直接删除）

| Pattern | 说明 | 风险 |
|---------|------|------|
| `__pycache__` | Python 字节码缓存 | 低 |
| `*.pyc` | Python 编译文件 | 低 |
| `*.pyo` | Python 优化编译文件 | 低 |
| `.pytest_cache` | pytest 缓存 | 低 |
| `.mypy_cache` | mypy 缓存 | 低 |
| `node_modules/.cache` | Node 缓存 | 低 |
| `.npm` | npm 缓存 | 低 |
| `.yarn` | yarn 缓存 | 低 |
| `.pnpm-store` | pnpm 缓存 | 低 |
| `.next/cache` | Next.js 缓存 | 低 |
| `.nuxt/cache` | Nuxt 缓存 | 低 |
| `.vite/cache` | Vite 缓存 | 低 |
| `.snowsql/logs` | SnowSQL 日志 | 低 |
| `.cache` | 通用缓存目录 | 低 |
| `*.log` | 日志文件（需确认非活跃） | 中 |
| `.DS_Store` | macOS 元数据 | 低 |
| `Thumbs.db` | Windows 缩略图 | 低 |
| `*.tmp` | 临时文件 | 中 |
| `*.temp` | 临时文件 | 中 |
| `.swp` | Vim swap 文件 | 低 |
| `*.swo` | Vim swap 文件 | 低 |
| `~` | Emacs 自动保存 | 低 |

## 需要评估后删除 Pattern（风险中）

| Pattern | 说明 | 需确认 |
|---------|------|--------|
| `*.bak` | 备份文件 | 是否在用 |
| `*~
```bash
        backup-* | 手动备份目录 | 是否在用 |
| `old` | old 目录 | 是否废弃 |
| `archive` | archive 目录 | 是否废弃 |
| `dist` | 构建产物 | 可从源码重新构建 |
| `build` | 构建产物 | 可从源码重新构建 |
| `.next` | Next.js 构建（不是 cache） | 可重建 |
| `.output` | Nuxt 构建产物 | 可重建 |

## 大文件 Pattern（> 100MB 需要评估）

- `*.iso` - 系统镜像
- `*.dmg` - macOS 安装包
- `*.tar.gz` - 压缩包（需确认是否必需）
- `*.zip` > 100MB - 大 zip 文件
- `*.mp4` > 100MB - 视频文件
- `*.mov` > 100MB - 视频文件
- `*.avi` > 100MB - 视频文件
- `*.mkv` > 100MB - 视频文件
