# 多模型并行执行配置

> 最后更新: 2026-04-15

---

## 🎯 目的

最大化 token 消耗，并行执行多个子代理，提高任务质量

---

## ⚙️ 已配置参数

| 参数 | 之前 | 现在 | 说明 |
|------|------|------|------|
| maxConcurrent | 4 | 20 | 主会话并发 |
| subagents.maxConcurrent | 8 | 30 | 子代理并发 |
| compaction.mode | safeguard | **never** | 禁用压缩，保留完整上下文 |

---

## 🚀 子代理并行策略

### 模式1: 多模型并行 (5个同时)
```python
# 5个不同模型同时处理同一任务
agents = [
    {"id": "minimax-m2.1", "task": "分析..."},
    {"id": "elephant-alpha", "task": "分析..."},
    {"id": "kimi-k2.5", "task": "分析..."},
    {"id": "gemma-4-26b", "task": "分析..."},
    {"id": "gpt-oss", "task": "分析..."}
]
# 并行spawn所有
```

### 模式2: Chain式审查 (3轮)
```
Round 1: 3个模型并行写
    ↓
Round 2: 3个模型并行审查
    ↓
Round 3: 1个模型汇总
```

### 模式3: 多角度分析 (4个专家)
```
4个专家同时分析:
- Business专家
- Tech专家
- Policy专家
- Ethics专家
```

---

## 📋 使用示例

### 并行生成 (5个模型)
```python
# 不要一个一个spawn，要一次spawn 5个！
for model in ["MiniMax", "Elephant", "Kimi", "Gemma4", "GPT-OSS"]:
    spawn(subagent, model=model, task=...)
```

### Chain审查 (3轮)
```
Round 1: [A, B, C] → 产出
Round 2: [D, E, F] → 审查
Round 3: [G] → 汇总
```

---

## ⚡ 加速执行

1. **不要串行** - 要并行
2. **不要一个模型** - 要多个模型
3. **不要单次** - 要多轮审查
4. **不要保留** - 要完整上下文 (compaction=never)

---

## 🎯 任务建议

| 任务类型 | 子代理数 | 说明 |
|----------|----------|------|
| 代码 | 3个 | 写+审查+测试 |
| 调研 | 5个 | 5个模型并行 |
| 分析 | 4个 | 4专家并行 |
| 审核 | 2个 | 双模型验证 |

---

*Config by 太子 | 2026-04-15*