# 📋 任务健康报告 - 2026-04-09

## 概览
- **监控时间**: 2026-04-09 16:03 UTC (北京时间 2026-04-10 00:03)
- **总任务数**: 15
- **正常**: 5 (33%)
- **失败**: 9 (60%)
- **运行中**: 1 (守护装置本身)

---

## 任务状态表

| 任务名 | 状态 | 错误类型 | 可恢复 | 处理方案 |
|--------|------|---------|--------|---------|
| 守护装置 - 每日健康检查 | ❌ error | LLM timeout | ❌ | 需等待API恢复 |
| 🛡️ 自我进化与验证 - 6小时 | ❌ error | LLM timeout | ❌ | 需等待API恢复 |
| 凌晨PR攻关 - 并发多项目 | ❌ error | LLM timeout | ❌ | 需等待API恢复 |
| 晚间探索 - 做项目+部署 | ❌ error | LLM timeout | ❌ | 需等待API恢复 |
| Moltbook - 短暴论版 | ❌ error | Axios 400 | ❌ | 需检查Moltbook配置 |
| 早晚安问候 | ❌ error | LLM timeout | ❌ | 需等待API恢复 |
| 每日启发分享 | ❌ error | LLM timeout | ❌ | 需等待API恢复 |
| 品牌内容生产 - 深度长文 | ❌ error | LLM timeout | ❌ | 需等待API恢复 |
| 午间探索 - 找PR权威项目 | ❌ error | LLM timeout | ❌ | 需等待API恢复 |
| 守护装置 - 知识归档 | ❌ error | LLM timeout | ❌ | 需等待API恢复 |
|---|---|---|---|
| GitHub Trending 扫描 | ✅ ok | - | - | 正常 |
| 潜在创业者发现报告 | ✅ ok | - | - | 正常 |
| 品牌内容生产 - 每日推文 | ✅ ok | - | - | 正常 |
| 守护装置 - 能力验证 | ✅ ok | - | - | 正常 |

---

## 错误分析

### 🔴 主要错误: LLM Timeout (90%失败)
```
FallbackSummaryError: All models failed (2): 
- minimax-portal/MiniMax-M2.1: LLM request timed out. (unknown)
- nvidia-kimi/moonshotai/kimi-k2.5: HTTP 404: model_not_found
```

**根因**: MiniMax API 服务端超时，无响应

**影响范围**: 9/15 任务受影响

**恢复方案**: 
- 等待 MiniMax API 恢复
- 或切换到备用模型 (如有)

### 🟡 次要错误: Moltbook API (400 Bad Request)
```
AxiosError: Request failed with status code 400
```

**根因**: Moltbook API 配置问题

**恢复方案**: 检查 Moltbook token 和 API 配置

---

## 今日行动

- [x] 分析失败原因
- [ ] 切换到更稳定的模型供应商
- [ ] 检查 Moltbook API 配置
- [ ] 考虑添加更多备用模型

---

## 基准指标

| 指标 | 目标 | 实际 | 状态 |
|------|------|------|------|
| 任务成功率 | > 85% | 33% | ❌ |
| 失败检测时间 | < 6h | ~1h | ✅ |
| 恢复成功率 | > 50% | N/A | ⏸️ |

---

## 总结

**核心问题**: MiniMax API 服务超时导致大部分任务失败

**建议**:
1. 等待 API 服务恢复
2. 或配置备用 LLM 提供商
3. Moltbook 任务需要重新配置

HEARTBEAT_END