# 模型 Fallback 优先级Proposal

> 最后更新: 2026-04-15

## 📊 调研结论

### 模型能力排序 (基于公开benchmark)

| 排名 | 模型 | 能力评估 | 价格 | 推荐场景 |
|------|------|---------|------|---------|
| 1 | **Elephant Alpha** | 高 (新晋强者) | $0 | 通用任务 |
| 2 | **GLM-4.5-Air:free** | 中高 (推理) | $0 | 推理任务 |
| 3 | **Gemma 3 4B:free** | 中 (轻量) | $0 | 轻任务 |
| 4 | **MiMo V2 Pro** | 中高 (推理) | $0.10 | 复杂推理 |
| 5 | **Step-3.5 Flash** | 中 (均衡) | $0.10 | 通用任务 |
| 6 | **GPT-4o Mini** | 中高 (稳定) | $0.15 | 最后备用 |

---

## 🎯 推荐 Fallback 顺序

### 方案: 免费优先 + 能力排序

```
Primary:   minimax-portal/MiniMax-M2.1     (主用，免费)
Fallback: nvidia-kimi/moonshotai/kimi-k2.5 (第二选择)
─────────────────────────────────────────
OpenRouter Fallbacks (按能力):
  1. openrouter/elephant-alpha         (高能力，免费✅)
  2. openrouter/z-ai-glm-4.5-air:free  (推理，免费✅)
  3. openrouter/google-gemma-3-4b-it:free (轻量，免费✅)
  4. openrouter/xiaomi-mimo-v2-pro      (推理，便宜)
  5. openrouter/stepfun-step-3.5-flash   (均衡)
  6. openrouter/openai-gpt-4o-mini      (最后备用)
```

---

## 🔄 特定任务模型建议

| 任务类型 | 推荐模型 | 原因 |
|---------|----------|------|
| **代码/技术** | elephant-alpha, GLM-4.5-Air | 上下文長 |
| **推理/思考** | MiMo V2 Pro, Kimi K2.5 | 推理能力强 |
| **轻量任务** | Gemma 3 4B:free | 快速且免费 |
| **通用对话** | Elephant Alpha | 综合能力强 |
| **备用最后一** | GPT-4o Mini | 最稳定 |

---

## 📋 具体配置

### 全局 Fallback (7个)
```json
[
  "minimax-portal/MiniMax-M2.1",
  "nvidia-kimi/moonshotai/kimi-k2.5",
  "openrouter/elephant-alpha",
  "openrouter/z-ai-glm-4.5-air:free",
  "openrouter/google-gemma-3-4b-it:free",
  "openrouter/xiaomi-mimo-v2-pro",
  "openrouter/stepfun-step-3.5-flash",
  "openrouter/openai-gpt-4o-mini"
]
```

### 机制说明
1. **免费模型排前面** - 确保不花钱
2. **付费模型排最后** - 应急备用
3. **推理模型单独标记** - 复杂任务专用

---

## 💡 Cron 任务优化

| Cron任务 | 推荐模型 | 理由 |
|---------|----------|------|
| **Moltbook发帖** | 免费模型 | 不需要高推理 |
| **技术调研** | GLM/Air | 需要长上下文 |
| **邮件回复** | 免费优先 | 量大但简单 |

---

## ✅ 实施

当前配置已按此Proposal执行：

- ✅ 免费模型已放前面
- ✅ 付费模型在最后
- ✅ 6个OpenRouter模型已配置

---

*Proposal by 太子 | 2026-04-15*