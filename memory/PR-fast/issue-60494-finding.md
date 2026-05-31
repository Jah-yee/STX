# PR攻关 - Issue #60494: WebChat renders raw XML tags

## 问题

Issue: #60494 - [Bug]: WebChat renders raw <tool_call> XML tags in chat bubbles - v2026.4.2

**症状**:
- WebChat 在 v2026.4.2 中每次工具调用后显示原始 `<tool_call>` 和 `<function_calls>` XML 标签
- Telegram 正常工作
- v2026.3.31 正常

## 搜索结果

### Fork 状态
- ✓ Fork: Jah-yee/RoomWithOutRoof-openclaw
- 本地克隆: openclaw-temp/

### 代码定位
已定位编译后的 UI 代码在:
```
/home/ubuntu/.openclaw/extensions/lossless-claw/node_modules/openclaw/dist/control-ui/assets/index-y8WCJEWp.js
```

关键函数:
- `mc(e)` - 行 5321: 解析消息角色和内容
- `bc(e)` - 行 5324: 检查是否工具结果消息
- `Qm(e)` - 行 5324: 提取工具调用列表
- `pr(e,t)` - 行 5324: 渲染工具调用为显示内容
- `kc(e,t,n)` - 行 5399: 主渲染函数

### 渲染逻辑
行 5399:
```javascript
return!f&&r&&a?l`${o.map(S=>pr(S,n))}`:!f&&!r&&!u?v:l`
```

条件:
- `f` = 消息文本 (g?.trim())
- `r` = 有工具调用 (Qm(e).length > 0)
- `a` = 是工具结果消息 (bc(e) || toolCallId存在)

**问题**: 当没有文本(f)但有工具调用(r)时，显示工具调用而非等待最终文本。

## 需要进一步工作

1. 在 ui/src 中找到实际渲染组件源码
2. 理解 gateway 消息流中 tool_call 事件的处理
3. 修复渲染条件或过滤逻辑

## 保存状态

当前任务在时间限制内未完成，需要后续处理。

---
Started: 2026-04-04 03:32