# 📋 任务健康报告 - 2026-04-05

## 概览
| 指标 | 数量 | 占比 |
|------|------|------|
| 总任务 | 47 | 100% |
| 正常 | 6 | 12.8% |
| 错误 | 9 | 19.1% |
| 跳过(禁用) | 32 | 68.1% |

## 失败任务分析

### 模型超时问题 (7个)
| 任务名 | 连续失败 | 错误详情 |
|--------|---------|---------|
| 守护装置 - 知识归档 | 1 | timeout |
| 🛡️ 自我进化与验证 - 6小时 | 2 | timeout |
| 守护装置 - 每日健康检查 | 1 | timeout |
| 凌晨PR攻关 - 并发多项目 | 1 | timeout |
| 晚间探索 - 做项目+部署 | 2 | timeout |
| 品牌内容生产 - 每日推文 | 1 | timeout |
| 品牌内容生产 - 深度长文 | 2 | timeout |

**错误原因**: `FallbackSummaryError: All models failed (2): minimax-portal/MiniMax-M2.1: LLM request timed out`

### Moltbook API问题 (2个)
| 任务名 | 连续失败 | 错误详情 |
|--------|---------|---------|
| Moltbook - 短暴论版 | 4 | AxiosError: Request failed with status code 400 |
| Moltbook - 英文长文版 | 6 | AxiosError: Request failed with status code 400 |

**可能原因**: 
- API token失效
- 请求格式问题
- 账号被限制

## 正常任务 (6个)
1. 守护装置 - 任务健康监控 ✅
2. GitHub Trending 扫描 ✅
3. 早晚安问候 ✅
4. 每日启发分享 ✅
5. 午间探索 - 找PR权威项目 ✅
6. 守护装置 - 能力验证 ✅

## 待处理事项

### 需要人工介入
- [ ] 检查 Moltbook API token 是否有效
- [ ] 考虑切换到更快的模型或增加超时配置

### 自动恢复
- [ ] 超时任务会在下次模型恢复后自动执行

## 基准指标
- 任务成功率: 12.8% (目标 > 85%) ⚠️
- 失败检测时间: < 6h ✅
- 恢复成功率: N/A

---
Generated: 2026-04-05 18:03 UTC