# OpenRouter 配置

> 时间：2026-04-15

## API 密钥 (已配置)

- **密钥**: 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
- **状态**: 待验证

---

## API 配置

### 端点
```
https://openrouter.ai/api/v1/chat/completions
```

### 请求格式 (Python)
```python
import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "openai/gpt-4o-mini",  # 或使用free模型
        "messages": [
            {"role": "user", "content": "Hello"}
        ]
    })
)
```

---

## 免费模型

使用 `:free` 后缀访问免费模型：
```json
{"model": "meta-llama/llama-3.2-3b-instruct:free"}
```

### 免费模型列表
- meta-llama/llama-3.2-3b-instruct:free
- google/gemma-2-2b-instruct:free
- etc.

---

## 模型命名规范

格式: `provider/model-name:variant`

示例:
| 模型 | 标识 |
|------|------|
| GPT-4o | openai/gpt-4o |
| Claude | anthropic/claude-3.5-sonnet |
| Gemini | google/gemma-2-5b-pro |
| 免费版 | model:free |

---

*记录时间: 2026-04-15*