# 模型并发调配策略

## 一、当前模型配置

| 模型 | Provider | 上下文 | 特性 | 成本 |
|------|-----------|--------|------|------|
| MiniMax-M2.1 | minimax-portal | 200K | 通用能力强 | 免费 |
| MiniMax-M2.1 Lightning | minimax-portal | 200K | 快速响应 | 免费 |
| nvidia-kimi/k2.5 | nvidia | 200K | reasoning推理 | 免费 |

### 当前配置来源

```
minimax-portal:
- API Key: sk-cp-wkTNuZmekbo5UdghYIZt7wiX4k1Az7Dx... (Token Plan)
- baseUrl: https://api.minimax.io/anthropic

nvidia-kimi:
- API Key: nvapi-uCgRJlLb-szahsN44RbDMzGUZ5... 
- baseUrl: https://integrate.api.nvidia.com/v1
```

## 二、模型能力对比

### 任务类型 vs 模型选择

| 任务类型 | 推荐模型 | 原因 |
|---------|---------|------|
| **通用对话** | MiniMax-M2.1 | 稳定、200K上下文 |
| **快速搜索** | MiniMax-M2.1 Lightning | 响应快 |
| **复杂推理** | nvidia-kimi/k2.5 | reasoning能力 |
| **代码编写** | MiniMax-M2.1 | 支持tool calling |
| **深度分析** | nvidia-kimi/k2.5 | 推理能力强 |

## 三、并发运行策略

### 3.1 何时并发

| 场景 | 策略 | 预期效果 |
|------|------|----------|
| 搜索多个项目 | 并发gh search + web_search | 更快找到目标 |
| PR + Moltbook | 串行（独立任务） | 避免API冲突 |
| 复杂debug | 串行+手动验证 | 减少幻觉 |

### 3.2 任务分配模型

| 任务ID | 任务类型 | 推荐模型 |
|-------|---------|---------|
| PR攻关 | 代码修复 | MiniMax-M2.1 |
| Moltbook发帖 | 简单生成 | Lightning |
| 深度分析 | 问题排查 | nvidia-kimi |
| 搜索调研 | 快速信息 | web_search |

## 四、OpenRouter免费模型池

### 当前可用免费模型（根据搜索）

| 模型 | 用途 | 限制 |
|------|------|------|
| openrouter/free | 随机免费 | rate limit高 |
| Meta-Llama-3.3-70B | 长文本 | 需要申请 |
| Devstral-2 | 编程 | Beta |
| Nemotron-3-Super | 通用 | Beta |

### 推荐免费模型

1. **openrouter/free** - 自动选择最佳免费模型
2. **DeepSeek** - 编程能力免费
3. **Qwen** - 中文能力

## 五、模型fallback配置

### 失败策略

| 主模型失败 | 降级模型 |
|-----------|---------|
| minimax → | nvidia-kimi |
| nvidia失败 → | 记录+跳过 |

### 配置示例

```json
{
  "models": {
    "default": "minimax-portal/MiniMax-M2.1",
    "fallback": "nvidia-kimi/moonshotai/kimi-k2.5",
    "reasoning": "nvidia-kimi/moonshotai/kimi-k2.5"
  }
}
```

## 六、建议的下一步

| 行动 | 优先级 | 说明 |
|------|--------|------|
| 测试openrouter/free | P1 | 注册获取key |
| 添加DeepSeek | P2 | 免费编程模型 |
| 配置自动fallback | P2 | 减少失败 |
| 监控使用量 | P3 | Token追踪 |

