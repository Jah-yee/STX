# PR 扫描报告 · repos-1.md
> 扫描时间: 2026-04-24 (过去7天: 2026-04-17 ~ 2026-04-24)
> 仓库: psf/requests & beetbox/beets

---

## 📋 搜索结果总览

| # | 搜索条件 | 结果数 |
|---|---------|--------|
| 1 | psf/requests · bug · created:>2026-04-17 | **0** |
| 2 | psf/requests · good first issue · created:>2026-04-17 | **0** |
| 3 | beetbox/beets · bug · created:>2026-04-17 | **0** |
| 4 | beetbox/beets · good first issue · created:>2026-04-17 | **0** |
| 5 | beetbox/beets · docs+typo · created:>2026-04-17 | **0** |

---

## 📖 过去7天新增 Issue（非标签过滤，仅供参考）

### psf/requests · 0个新 issue

---

### beetbox/beets · 3个新 issue

#### 1. #6577 · `original_date` ignored on import
- **置信度**: ⭐⭐
- **GH链接**: https://github.com/beetbox/beets/issues/6577
- **修复内容**: 用户配置了 `original_date: yes`，但导入时 `year` 字段存的是唱片压制年份(1988)而非原始发行年份(1979)，`original_date` 配置被忽略
- **为什么能做**: 问题清晰（`original_date` 配置未生效），可通过检查 import pipeline 中 year/original_date 的赋值逻辑修复；复现路径明确（导入特定 Michael Jackson 专辑）
- **最小改法**: 在 `beets/library.py` 或 `beets/importer.py` 中，确保 `original_date: yes` 时优先从 MusicBrainz 的 `original_date` 而非 `date` 字段赋值 `year`
- **标签**: 无标签（非 bug 标）
- **创建时间**: 2026-04-23

#### 2. #6560 · `ReadError` reason not printed
- **置信度**: ⭐⭐⭐
- **GH链接**: https://github.com/beetbox/beets/issues/6560
- **修复内容**: 当文件读取失败时，日志只打印 `error reading <super: <class 'ReadError'>, <ReadError object>>`，没有显示具体原因（通常是权限问题、文件损坏等）
- **为什么能做**: 错误日志格式问题，改 1 行代码即可；且有 maintainer (snejus) 积极参与讨论，问题定位清晰
- **最小改法**: 在 `beets/util.py` 或 `beets/ui/__init__.py` 中，将 `ReadError` 的日志输出从 `str(error)` 改为 `str(error.args[0])` 或类似方式暴露真实原因
- **标签**: 无标签（非 bug 标）
- **创建时间**: 2026-04-21

#### 3. #6553 · Beets logging overhaul
- **置信度**: ⭐⭐
- **GH链接**: https://github.com/beetbox/beets/issues/6553
- **修复内容**: 提议重构 beets 日志系统为 config-driven（用 `logging.config.dictConfig`），同时列出 5 个前置小任务可单独提 PR：
  - (1) `capture_log` → pytest `caplog` (纯测试清理)
  - (2) `PluginLogFilter` → proper `Formatter` (日志格式化)
  - (3) 移除 import 时的日志 side-effects
  - (4) 统一 `-v` verbose 标志优先级
  - (5) dictConfig 本身
- **为什么能做**: maintainer (snejus) 明确表示愿意接受拆分 PR，前两个子任务（capture_log 和 PluginLogFilter）是纯测试/日志清理，非常适合新人
- **最小改法**: 
  - 子任务(1): 测试文件里把 `capture_log` 替换为 pytest 内置 `caplog`
  - 子任务(2): `beets/plugins.py` 中的 `PluginLogFilter` 改为标准 `logging.Formatter`
- **标签**: 无标签（feature/discussion）
- **创建时间**: 2026-04-19

---

## 🔎 额外发现（非严格标签匹配，但有价值）

### beetbox/beets · "good first issue" 标签（近期最活跃）

#### #6439 · Lyrics: force / use a specific URL for lyrics
- **置信度**: ⭐⭐⭐⭐
- **GH链接**: https://github.com/beetbox/beets/issues/6439
- **修复内容**: 让 lyrics 插件支持强制使用指定 lrclib URL/ID，而非按 duration 匹配
- **为什么能做**: 有新贡献者 (ariasfifer) 已在评论区表示想接手，maintainer (snejus) 明确回复 "This is indeed a good first issue, please go ahead!"；功能边界清晰
- **最小改法**: 在 `beetsplug/lyrics.py` 中新增 `source` 配置项（或 `--lyrics-source` CLI 标志），传给 lrclib API 时用指定 ID 覆盖默认搜索逻辑
- **标签**: `good first issue`, `lyrics`
- **创建时间**: 2026-03-13（略早于目标窗口，但标签已确认）

---

## 📝 说明

- 严格按 `created:>2026-04-17` 日期过滤，过去7天内 psf/requests 和 beetbox/beets 均无带 `bug` / `good first issue` / `docs`+`typo` 标签的新 issue
- 但 beetbox/beets 有3个未标签的新 issue，其中 #6560 和 #6553(子任务) 适合做 PR
- #6439 虽创建于3月，但 maintainer 已明确标记为 good first issue，适合跟进
