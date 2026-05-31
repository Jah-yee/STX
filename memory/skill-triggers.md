# 技能触发规则 - 分布式嵌入

## 分布式触发矩阵

### SOUL.md嵌入
- 三省六部触发
- 技能调用判断
- 用户纠正响应

### HEARTBEAT.md嵌入
- 周期性自检（每6小时）
- 上下文大小检查（>5000tokens）
- 技能效率评估

### AGENTS.md嵌入
- PR创建时触发：qa-team + pr-review-assistant
- 任务分配逻辑

## 触发条件完整矩阵

| 技能 | 触发条件 | 文件位置 |
|------|----------|----------|
| self-improving | 用户纠正/失败2次 | ~/.self-improving/ |
| qa-team | PR创建时 | AGENTS.md |
| context-management | >5000tokens | HEARTBEAT.md |
| pr-review-assistant | PR创建时 | AGENTS.md |

## 嵌入验证

每6小时检查：
1. HEARTBEAT.md → 自检技能
2. SOUL.md → 用户纠正
3. AGENTS.md → PR流程
