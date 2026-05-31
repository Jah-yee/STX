# 全量系统检测与优化报告

## 一、系统现状（Discover）

### 1.1 Cron Jobs（24个）

| # | 任务名 | 频次 | 状态 | 问题 |
|---|----------|------|------|------|
| 1 | Moltbook高频运营 | 15min | idle | 待执行 |
| 2 | PR攻关 | 15min | idle | 待执行 |
| 3 | 凌晨PR攻关 | 2,4点 | ok | |
| 4 | PR午间探索 | 14点 | ok | |
| 5 | 2小时项目交付 | 22点 | ok | |
| 6 | 每日自省 | 22点 | ok | |
| 7 | 知识归档 | 23点 | ok | |
| 8 | 任务健康监控 | 6h | ok | |
| 9 | 自我进化验证 | 6h | ok | |
| 10 | 每日健康检查 | 1点 | ok | |
| 11 | GitHub Trending | 6h | ok | |
| 12 | 晨间探索 | 3点 | error | 超时 |
| 13 | Daily探索 | 9点 | error | 超时 |
| 14 | Todo检查 | 21点 | error | 超时 |
| 15 | 潜在创业者 | 10点 | error | 超时 |
| 16-24 | 其他 | various | ok | |

### 1.2 Skills（71个）

**已验证可用（18个）**：
- lark-calendar, lark-contact, lark-doc, lark-drive
- lark-im, lark-minutes, lark-sheets, weather, github
- lark-base, lark-event, lark-mail, lark-openapi-explorer
- lark-shared, lark-skill-maker, lark-task, lark-vc, pua

**未触发（53个）**：
- 其他system skills

### 1.3 Extensions

| 名称 | 状态 |
|------|------|
| lossless-claw | ✅ 已加载 |

### 1.4 MCP服务器

| 服务器 | 状态 |
|--------|------|
| filesystem | ✅ 已配置 |
| github | ✅ 已配置 |
| MiniMax (web_search) | ❌ 未配置 |

---

## 二、问题定义（Define）

### 2.1 高优先级问题

| # | 问题 | 影响 |
|---|------|------|
| 1 | 4个探索任务超时 | 无法产出 |
| 2 | MiniMax MCP缺失 | web_search不可用 |
| 3 | 任务间无上下文串联 | 效率低 |

### 2.2 可优化空间

| # | 优化点 | 预期提升 |
|---|----------|----------|
| 1 | 重用成功任务prompt | 成功率 |
| 2 | 增加任务串联 | 上下文复用 |
| 3 | 精简error任务 | 资源利用率 |

---

## 三、方案设计（Think）

### 3.1 超时任务优化

**问题源**：探索类任务timeout太短 + 模型调用超时

**方案**：
- 保留深度任务（凌晨2/4点）
- 删除高频探索任务（使用已有Trending扫描替代）
- 调整超时配置

### 3.2 任务串联工作流

**设计**：建立任务间上下文传递
- Moltbook → PR → Trending
- 结果相互引用

### 3.3 Skills整合

**策略**：
- 将高频Skills绑定到cron任务
- 自动化调用链

---

## 四、执行计划（Execute）

### 4.1 里程碑

| 阶段 | 任务 | 目标 |
|------|------|------|
| M1 | 关闭4个error任务 | 简化系统 |
| M2 | 配置MiniMax MCP | 恢复搜索 |
| M3 | 建立任务串联 | 上下文复用 |
| M4 | 验证产出 | 确认运行 |

### 4.2 具体行动

```
[ ] 关闭超时任务（晨间/Daily/Todo/潜在创业者）
[ ] 检查MiniMax MCP配置
[ ] 创建任务串联workflow
[ ] 验证Moltbook+PR任务执行
[ ] 更新memory
```

---

## 五、交付（Deliver）

状态：执行中

预期产出：
- 系统简化（20个有效任务）
- 搜索能力恢复
- 任务上下文串联

