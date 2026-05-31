# anomalyco/opencode#4930 - Retain model/agent selection when switching sessions

## Issue 信息
- **编号**: #4930
- **标题**: Feature Request: Retain current model and agent selection when switching sessions
- **标签**: good first issue
- **用户**: JosXa

## 分析摘要
在 `packages/opencode/src/session/prompt.ts` 中，model选择通过以下逻辑解析：
```typescript
const model = input.model ?? agent.model ?? (await lastModel(input.sessionID))
```

## 提议方案
1. 存储全局活跃的 model/agent 选择
2. 切换session时，优先使用全局选择，否则回退到session存储值

## 评论状态
✅ 已发送分析评论: https://github.com/anomalyco/opencode/issues/4930#issuecomment-4186886192

## 待后续
- 等维护者回复确认方案
- 或直接实现PR