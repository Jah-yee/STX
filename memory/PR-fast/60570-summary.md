# PR-fast 攻关记录

## Issue #60570: Bug: `tools.exec.host=auto` blocks agent-requested `host=node`

### 状态
- **阶段**: ✅ 已完成
- **PR**: https://github.com/openclaw/openclaw/pull/60573
- **启动时间**: 2026-04-04 06:39 UTC
- **完成时间**: 2026-04-04 06:44 UTC

### 问题摘要
当 `tools.exec.host` 设置为 `"auto"` 时，代理无法动态请求 `host=node` 在连接的节点上执行命令。请求在到达节点之前就被网关级别拒绝了。

### 根因
`model-runtime` 中的 `isRequestedExecTargetAllowed` 函数使用严格相等检查，没有对 `auto` 做特殊处理。

### 修复方案
修改 `isRequestedExecTargetAllowed` 函数，当 `configuredTarget === "auto"` 时返回 `true`。

### 期望 PR
- **来源仓库**: openclaw/openclaw
- **目标分支**: main → Jah-yee:fix/issue-60570