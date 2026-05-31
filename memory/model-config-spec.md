# 模型配置规范

> 最后更新: 2026-04-15

---

## 📋 Fallback 优先级 (12个)

| # | 模型 | 类型 | 价格 | 状态 |
|---|------|------|------|------|
| 1 | minimax-portal/MiniMax-M2.1 | 主用 | $0 | ✅ OAuth |
| 2 | openrouter/elephant-alpha | 推理 | $0 | ✅ 最强 |
| 3 | nvidia-kimi/moonshotai/kimi-k2.5 | 推理 | $0 | ✅ |
| 4 | openrouter/z-ai-glm-4.5-air:free | 备用 | $0 | ✅ |
| 5 | openrouter/google-gemma-3-4b-it:free | 轻量 | $0 | ✅ |
| 6 | openrouter/xiaomi-mimo-v2-pro | 付费 | $0.10 | ✅ |
| 7 | openrouter/stepfun-step-3.5-flash | 付费 | $0.10 | ✅ |
| 8 | openrouter/openai-gpt-4o-mini | 备用 | $0.15 | ✅ |
| 9 | openrouter/openai-gpt-oss-20b:free | 免费 | $0 | ✅ |
| 10 | openrouter/openai-gpt-oss-120b:free | 免费 | $0 | ✅ |
| 11 | openrouter/nvidia-nemotron-3-nano-30b-a3b:free | 免费 | $0 | ✅ |
| 12 | openrouter/nvidia-nemotron-nano-9b-v2:free | 免费 | $0 | ✅ |

---

## 🔄 自动 Fallback 机制

当主模型失败时，自动尝试下一个：
- Rate limit (429) → 跳过下一个
- No credit → 跳过下一个
- Timeout → 跳过下一个
- 其他错误 → 跳过下一个

---

## 🎯 使用场景

| 任务 | 推荐模型 | 原因 |
|------|----------|------|
| 深度思考 | MiniMax-M2.1 | 思考模式 |
| 推理 | Elephant Alpha | 最强 |
| 代码 | Elephant Alpha | 上下文长 |
| 轻量任务 | Gemma 3 4B | 免费快速 |
| 备用保底 | GPT-4o Mini + OSS | 免费 |

---

## ⚙️ 配置位置

`~/.openclaw/openclaw.json`

```json
{
  "agents": {
    "defaults": {
      "model": {
        "primary": "minimax-portal/MiniMax-M2.1",
        "fallbacks": [...] // 12个模型
      }
    }
  }
}
```

---

*Config by 太子 | 2026-04-15*