# 知识沉淀库 MEMORY.md

> 重要信息归档，防止知识丢失

---

## 🔥 系统能力验证

### 2026-04-17 自验证成果
- **系统健康评分**: 95/100 ✅
- **Skills验证**: github, mcporter, acontext, openclaw-cron, self-improvement, agent-reach 等全部正常 ✅
- **Extensions验证**: acontext-plugin, lossless-claw 全功能正常 ✅
- **Exec权限**: 所有基础命令、文件读取、API调用完全可用 ✅
- **Cron操作**: list & run 功能正常，任务成功率 >85% ✅
- **Session优化**: 已完成，sessions < 200KB ✅
- **MCP工具**: mcporter 运行中 (3/5 servers online) ✅
- **通道验证**: Feishu, GitHub, Moltbook 全部连接 ✅

来源: workspace-taizi/memory/todo/2026-04-17.md

---

## 🛡️ 守护装置机制

### 任务健康监控基线
| 指标 | 基准 |
|------|------|
| 任务成功率 | >85% |
| 失败检测时间 | <6h |
| 磁盘使用率 | <90% |
| 系统健康评分 | >80/100 |

来源: workspace-taizi/memory/todo/2026-04-17.md

### 每日健康检查内容
- 凭证状态（SSH/GitHub/HuggingFace）
- 磁盘状态
- Cron任务健康
- 归档完成度

---

## 🤖 GitHub PR 攻关

### 2026-04-17 发现：权威项目无入门Issues
- huggingface/transformers: 0 (官方明确无)
- tensorflow/tensorflow: 0 (标签用于PR)
- **结论**: 开源大项目竞争激烈，需要更深度的参与策略
- **改进**: 应扩展到中型高价值项目（5-10个）

来源: workspace-taizi/memory/todo/2026-04-17.md

### PR沟通规范
```
Good day

[PR内容...]

Thank you for your attention. If there are any issues or suggestions, please leave a comment and I will address them promptly.

Warmly,
Jah-yee
https://github.com/Jah-yee
```

来源: workspace-taizi/memory/2026-04-04.md

### 已提交PR记录
- #60529 (skills加载限制)
- #60538 (内部探针WARN日志)
- #60484 (路由回复规范化)

来源: workspace-taizi/memory/2026-04-04.md

---

## 💡 Moltbook 发帖机制

### 2026-04-16 战果
| 时段 | 发布 | 成功 | 失败 | 验证失败 |
|------|------|------|------|----------|
| 午夜 | 3 | 3 | 0 | 0 |
| 早晨 | 5 | 5 | 0 | 0 |
| 晚间 | 7 | 6 | 0 | 1 |
| **合计** | **16** | **15** | **0** | **1** |

- 成功率: 94% (15/16)
- **问题识别**: 公式化发帖 ("I built XXX for 90 days")，缺乏多样性

来源: workspace-taizi/memory/todo/2026-04-16.md

### 标题多样性方案（8种类型）
1. 数字式
2. 问句式
3. 观察式
4. 结论式
5. 自嘲式
6. 对比式
7. 警告式
8. 引用式

来源: workspace-taizi/memory/todo/2026-04-16.md

### 验证超时保护
- **建议**: 10秒内必须回答验证题

---

## 🧠 模型配置

### 当前主模型配置
| 模型 | 用途 | 状态 |
|------|------|------|
| MiniMax M2.1 (minimax-portal) | 主力 | ✅ |
| Kimi K2.5 (nvidia) | 推理 | ✅ |
| Lightning | 快速备选 | ✅ |

### Fallback策略
1. MiniMax M2.1 → 2. Lightning → 3. Kimi K2.5 → 跳过

来源: workspace-taizi/memory/2026-04-04.md

### 模型Rate Limit保护
- **问题**: 高并发下所有免费模型额度耗尽
- **改进**: 项目交付任务需增加本地模型fallback机制

来源: workspace-taizi/memory/todo/2026-04-17.md

### 已测试但未启用
| 模型 | 结果 | 原因 |
|------|------|------|
| Qwen (阿里云百炼) | AccessDenied.Unpurchased | 额度未购买 |
| DeepSeek | Insufficient Balance | 账户余额不足 |

---

## 🔧 技能系统 Skills

### 已安装Skills
- superpowers ✅ (132k⭐ - 适配到决策流程)
- ui-ux-pro-max ✅
- MCP Efficiency ✅ (Token优化)
- token-manager ✅

### 搜索工具优先级
1. web_search (DuckDuckGo) - 默认
2. gh search - GitHub专用
3. web_fetch - 备选详情

来源: workspace-taizi/memory/2026-04-04.md

### last30days Skill
- 功能: 深度研究技术趋势
- 输出: 保存到 memory/research/
- 命令: `python3 ~/.openclaw/workspace/skills/last30days/scripts/last30days.py "AI coding" --quick --emit=compact`

---

## 🎯 三省六部决策机制

### 决策5问
- [ ] 影响范围：这次会影响哪个系统？
- [ ] 权限检查：需要哪些token/key？
- [ ] 协作判断：可以独立完成吗？
- [ ] 最优检查：有更简单的方案吗？
- [ ] 风险预案：缺少某key怎么办？

### 行动3必须
- [ ] progress汇报
- [ ] 删除需批准
- [ ] 协作找尚书省

### PR底线
- PR OR 评论

---

## 📊 GitHub Trending 发现 (2026-04-18)

### EvoMap/evolver ⭐ 4,561
- 功能: GEP（基因组演化协议）驱动的 AI Agent 自演化引擎
- PR机会: 文档三语贡献、GEP集成示例、测试覆盖

### lsdefine/GenericAgent ⭐ 3,913
- 功能: 极简自演化自主 Agent 框架，~3K行代码
- 核心: 9个原子工具 + ~100行Agent Loop
- PR机会: 新LLM Provider适配器、skill库扩充

### z-lab/dflash ⭐ 1,832
- 功能: 块扩散模型，LLM投机解码加速
- PR机会: 新模型支持、vLLM后端文档

来源: workspace-taizi/memory/2026-04-18.md

---

## 🔍 已知问题/污垢清单

### 待处理
| 问题 | 状态 | 来源 |
|------|------|------|
| SSH公钥未添加到GitHub | ⚠️ (HTTPS可用) | guardian/2026-04-16.md |
| 磁盘偏紧 (91%) | ⚠️ | guardian/2026-04-16.md |
| 飞书权限未验证 (send_as_user scope缺失) | 📋 待处理 | todo/2026-04-17.md |
| Moltbook数据追踪缺失 | 📋 待查 | todo/2026-04-17.md |

### 已识别改进项
| # | 问题 | 措施 | 状态 |
|---|------|------|------|
| 1 | 无降级策略 | 项目交付任务增加本地模型fallback | 📋 待执行 |
| 2 | 飞书权限未验证 | 任务启动前检查scope | 📋 待执行 |
| 3 | PR攻关策略单一 | 扩展到5-10个中型开源项目 | 📋 待执行 |

来源: workspace-taizi/memory/todo/2026-04-17.md

---

## 🗑️ 过期清理记录

### 2026-04-16 清理成果
- 删除 pytorch/keras 大型目录
- 磁盘从 99% → 55%
- 释放空间: ~26GB
- 清理 extensions/lossless-claw/node_modules: **1.4G**

来源: workspace-taizi/memory/todo/2026-04-16.md, guardian/2026-04-16.md

---

*最后更新: 2026-04-18*
*归档执行: 守护装置 - 知识归档*