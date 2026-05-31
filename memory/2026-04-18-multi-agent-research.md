# Research: Multi-Agent Orchestration Patterns

**Date:** 2026-04-18  
**Focus:** Subagent coordination, spawning strategies, result aggregation

---

## 技术选型

### 现有架构分析

**当前系统组件：**
- **OpenClaw runtime** — 主控制器，支持 `sessions_spawn` 和 `subagents`
- **MCP tools (mcporter)** — 3/5 servers online，支持 exa, twitter 等
- **飞书集成** — channel-based communication
- **Cron 驱动** — 定时任务驱动日常探索

**当前 Subagent 使用模式：**
| 模式 | 用途 | 状态 |
|------|------|------|
| `runtime: "subagent"` | 并行任务执行 | ✅ 主力 |
| `runtime: "acp"` | ACP harness (Codex等) | ✅ 可用 |
| `thread: true` | 持久线程会话 | ✅ 配置 |

---

### Option A: 树形编排者模式 (推荐)

```
主 Agent
├── 子代理 A (并行) → 结果
├── 子代理 B (并行) → 结果
└── 子代理 C (顺序依赖)
```

**优点：**
- 天然适配并行任务（AGENTS.md 明确要求 spawn 多个）
- 结果 push-based，无需轮询
- 支持任务链（编排者拆解 → 分发 → 汇总）
- 最多 50 个并发子代理

**缺点：**
- 汇总逻辑需要主 agent 处理
- 子代理崩溃需要重试机制

**适用场景：** 搜索类任务、生成+审查循环

---

### Option B: 链式依赖模式

```
任务A → 结果 → 任务B → 结果 → 任务C
```

**优点：** 依赖清晰，易调试
**缺点：** 阻塞性强，无法并行
**适用场景：** 有严格先后顺序的工作流

---

### Option C: 意图路由模式

根据任务复杂度自动选择：
- 简单查询 → 直接回答
- 中等复杂度 → spawn 1-2 个子代理
- 高复杂度 → 编排者模式 + 多子代理

**优点：** 资源高效利用
**缺点：** 需要准确判断任务复杂度

---

## 实现建议

### 推荐方案：Option A (树形编排者) + Option C (意图路由)

**核心逻辑：**
```
判断任务复杂度
├── 简单 (< 5分钟) → 直接回答
├── 中等 (多步骤) → spawn 2-3 个并行子代理
└── 复杂 (需要调研) → 编排者拆解 → 50 并发上限分发
```

### 关键参数

| 参数 | 值 | 说明 |
|------|------|------|
| `runTimeoutSeconds` | 300-600 | 子代理超时 |
| `mode` | `run` (一次性) 或 `session` (持久) | 根据场景选择 |
| `cleanup` | `delete` (默认) | 避免 session 堆积 |
| `maxItems` | 50 | 子代理并发上限 |

### 结果聚合策略

1. **Push-based 完成通知** — 子代理完成后自动 announce
2. **sessions_history** — 按需读取历史，不主动轮询
3. **lcm_expand_query** — 压缩内容按需扩展

---

## 已知问题与陷阱

### ❌ 陷阱 1: 轮询子代理状态
```python
# 错误示例
while True:
    status = subagents_list()
    if all_done(status):
        break
    sleep(1)  # 不要这样做！
```

**正确做法：** 等待 push-based 完成通知

### ❌ 陷阱 2: 共享 context 污染
子代理共享 workspace 目录，可能产生文件冲突

**缓解：** 使用独立 `cwd` 或 `/tmp/` 临时文件

### ❌ 陷阱 3: 超时设置不当
- 太短：复杂任务被强制终止
- 太长：资源占用过高

**建议：** 搜索类 300s，研究类 600s

### ❌ 陷阱 4: 子代理结果丢失
没有收集所有子代理的返回就结束

**正确做法：**
```python
# 追踪所有 expected sessionKeys
expected = ["sessionA", "sessionB", "sessionC"]
# 等所有完成事件到达后再返回最终结果
```

---

## 集成点

### 与现有系统对接

| 组件 | 集成方式 |
|------|---------|
| **飞书** | `message` 工具，channel 通信 |
| **记忆系统** | `memory/` 目录，YYYY-MM-DD.md 格式 |
| **Cron** | `openclaw cron` 调度 |
| **MCP** | `mcporter call` 调用外部工具 |

### 与 AGENTS.md 的对应关系

| AGENTS.md 要求 | 实现方式 |
|----------------|---------|
| spawn 子代理 | `sessions_spawn runtime="subagent"` |
| 50 并发 | `maxItems: 50` |
| 推送完成 | 子代理自动 announce |
| 编排者模式 | 主 agent 拆解 → 分发 → 汇总 |

---

## 风险与注意事项

1. **子代理崩溃** — 需要重试逻辑，建议 `runTimeoutSeconds` 内嵌保护
2. **并发过多** — 50 上限，复杂任务分批
3. **结果丢失** — 追踪 expected sessions，确保全部到达
4. **Session 堆积** — 使用 `cleanup: "delete"` 或定期清理
5. **模型 fallback** — 当前用 `minimax-portal/MiniMax-M2.7`，有 12 个备用模型

---

## 下一步

1. **实现意图路由** — 自动判断任务复杂度选择执行模式
2. **增强错误处理** — 子代理崩溃时自动重试
3. **优化结果聚合** — 统一汇总格式，减少主 agent 处理负担
4. **监控优化** — 追踪子代理成功率，持续改进

---

## 参考资料

- OpenClaw sessions_spawn 文档
- AGENTS.md 多子代理强制检查要求
- SOUL.md 三省六部协作模式