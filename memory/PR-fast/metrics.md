# PR攻关 指标追踪

**创建时间：** 2026-05-01 09:49 CST
**用途：** 每次cron记录正向指标，长期追踪

---

## 📊 指标定义

| 指标 | 说明 | 目标 |
|------|------|------|
| scan_count | 扫描的仓库数量 | ≥15 |
| gate1_pass | 通过Gate-1的候选数 | ≥5 |
| contributing_read | 读完CONTRIBUTING.md的数量 | ≥3 |
| issues_found | 找到的可用issues数 | ≥10 |
| gate2_pass | 通过Gate-2的候选数 | ≥2 |
| draft_created | 写了fix草案的数量 | ≥1 |
| gate3_pass | 通过Gate-3的候选数 | ≥1 |
| pr_created | 成功创建的PR数 | ≥1 |
| execution_time_ms | 本轮总执行时间（ms） | <180000 |

---

## 📈 趋势记录

### 2026-05-01

| Run | scan | gate1 | cont_read | issues | gate2 | draft | gate3 | pr | time_ms | 备注 |
|-----|-------|-------|-----------|--------|-------|-------|-------|-----|---------|------|
| 90th | ? | ? | ? | ? | ? | ? | ? | 0 | ? | 扫描轮次 |
| 91th | ? | ? | ? | ? | ? | ? | ? | 0 | ? | 无新机会 |
| 92th | ? | ? | ? | ? | ? | ? | ? | ? | ? | **v3第一轮** |

---

## 🎯 目标解读

### 为什么需要这些指标？

| 指标 | 解决的问题 |
|------|-----------|
| scan_count | 广度够不够？之前每轮只扫3-5个 |
| gate1_pass | 有多少仓库可进入下一轮？ |
| contributing_read | 真的去读规则了吗？ |
| issues_found | 机会发现能力 |
| gate2_pass | 评估通过率 |
| draft_created | 真正开始写方案了吗？ |
| pr_created | 最终产出 |

### 健康标准

```
扫描量 ≥ 15/轮  ✅
Gate-1通过 ≥ 5/轮  ✅
CONTRIBUTING读完 ≥ 3/轮  ✅
Issues找到 ≥ 10/轮  ✅
最终PR ≥ 1/2轮  ✅
```

---

## 📉 异常告警

| 指标 | 告警线 | 原因 |
|------|--------|------|
| scan_count | < 10 | 扫描不够广 |
| gate1_pass | < 3 | 过滤太严或blocklist太多 |
| pr_created | 连续3轮 = 0 | 产出有问题 |

---

**下次更新：** 2026-05-01 下一轮cron
