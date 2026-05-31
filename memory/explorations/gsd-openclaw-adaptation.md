# GSD → OpenClaw 适配计划

## 背景
- GSD (get-shit-done-cc) 是个 AI 编程增强框架，原为 Claude Code 设计
- 核心价值：70+ 工作流模板 + 上下文工程 + 状态管理
- 目标：适配到 OpenClaw runtime，发挥 OpenClaw 特性

## 适配策略
不硬套 Claude Code 模板，而是**围绕 OpenClaw 重新设计**

## GSD 核心模块

### 1. Workflows (70+ 工作流)
位置：`/usr/lib/node_modules/get-shit-done-cc/get-shit-done/workflows/`

核心文件：
- `do.md` — 意图路由分发器
- `autonomous.md` — 自主执行
- `execute-phase.md` — 阶段执行
- `plan-phase.md` — 规划阶段
- `verify-work.md` — 验证工作
- `research-phase.md` — 研究阶段
- `discuss-phase.md` — 讨论愿景
- 等 70+ 个

### 2. References (参考文档)
位置：`/usr/lib/node_modules/get-shit-done-cc/get-shit-done/references/`

核心文件：
- `checkpoints.md` — 检查点
- `verification-patterns.md` — 验证模式
- `user-profiling.md` — 用户画像
- `model-profiles.md` — 模型配置
- `gates.md` — 门控
- 等 34 个

### 3. Contexts (上下文模板)
- `dev.md`
- `research.md`
- `review.md`

## OpenClaw 映射

| GSD | OpenClaw 实现 |
|------|-------------|
| 工作流 | `~/.openclaw/skills/` skill |
| 参考文档 | 放入 skill 的 `references/` 或 `scripts/` |
| 意图路由 | skill description + 触发关键词 |
| 状态管理 | workspace 项目文件 + MEMORY.md |
| 子代理编排 | `sessions_spawn` runtime=subagent |
| 命令路由 | cron job 或 message handler |

## 适配优先级

### P0 - 核心要适配什么
1. **意图路由** → 把 `do.md` 的路由逻辑改成 OpenClaw skill 触发
2. **状态管理** → 用 OpenClaw workspace 文件结构
3. **工作流模板** → 选择最常用的 10 个转为 skill

### P1 - 可选适配
- 验证模式 → OpenClaw 的 skill 验证
- 上下文工程 → 用 OpenClaw 的 context 文件

## 进展
- [x] 分析 GSD 代码结构
- [x] 设计适配方案
- [x] 选择优先适配的工作流
- [x] 开始写第一个 OpenClaw skill

## 已完成 Skills

### 1. gsd-router (意图路由)
- 位置: `~/.openclaw/skills/gsd-router/SKILL.md`
- 功能: 分析用户输入，路由到合适的 OpenClaw skill
- 基于: GSD do.md

### 2. gsd-quick (快速任务)
- 位置: `~/.openclaw/skills/gsd-quick/SKILL.md`
- 功能: 执行小而独立的快速任务
- 基于: GSD quick.md

### 3. gsd-research (研究)
- 位置: `~/.openclaw/skills/gsd-research/SKILL.md`
- 功能: 调研技术方案、库选项、常见陷阱
- 基于: GSD research-phase.md

### 4. gsd-debug (调试)
- 位置: `~/.openclaw/skills/gsd-debug/SKILL.md`
- 功能: 系统性调查错误、崩溃、故障
- 基于: GSD diagnose-issues.md

## 后续计划
- [ ] gsd-new-project (新建项目)
- [ ] gsd-map-codebase (分析代码库)
- [ ] gsd-add-phase (添加阶段)
- [ ] gsd-add-todo (添加待办)
- [ ] gsd-add-tests (添加测试)
- [ ] gsd-progress (进度查看)
- [ ] gsd-resume (恢复工作)
- [ ] gsd-complete-milestone (完成里程碑)

## 日期
2026-04-13