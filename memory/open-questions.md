# PR Open Questions — 2026-04-27

> 格式参照 karpathy/lecun1989-repro: 不知道的就是不知道，所有条目具体可执行

## 待确认

- [ ] nodejs #62958: ping 后 maintainer 有无回应？（最后更新 2026-04-26 19:57 UTC ⚠️）
- [ ] go-git #2034-2037: 4个PR各自对应哪个issue？有没有互相冲突的风险？

## 待执行

- [ ] psf/requests #6102, #2155: ~20h后 cooldown 结束（2026-04-29 00:00 UTC）
- [ ] python/cpython #42664, #148954, #127550: ~2d后 cooldown 结束
- [ ] go-git/go-git #2011: 2026-05-01 可执行

## 已知阻塞

- [x] beetbox/beets #6583: maintainer (snejus) 已于 2026-04-26 11:00 UTC 确认关闭 — 移除
- [ ] golang-jwt/jwt #489: Gate-2 blocked（11 OPEN PRs）— 每轮监控
- [ ] gorilla/mux #781: Gate-2 blocked（12 OPEN PRs）— 每轮监控
- [ ] astral-sh/ruff, pallets/click, microsoft/*, matplotlib: GH007 blocked

## Ping Escalation 规则（2026-04-27 新增）

> 主子指示：每日重 ping 太频繁，显得 desperation。维护者看到你的 PR 之前需要时间，频繁 ping 适得其反。

### 渐进式 ping 间隔

| Ping 次数 | 距上次 ping | 累计等待 |
|-----------|-------------|----------|
| 初始 PR | — | Day 0 |
| 第1次 ping | Day 1 | Day 1 |
| 第2次 ping | Day 3 | Day 4 |
| 第3次 ping | Day 5 | Day 9 |
| 第4次 ping | Day 7 | Day 16 |
| 第5次+ ping | Day 10 | Day 26+ |

### 停止规则（满足任一即停）

- [ ] 已等待 **3周**（21天）无任何 maintainer activity
- [ ] PR 已有 reviewer assigned 但无 review action
- [ ] 维护者在其他 issue/PR 中有活动（说明在线但不处理你的 PR）
- [ ] PR 被明确 close 了
- [ ] 维护者说了"不打算 merge"或类似的话

### 例外：不计入间隔的情况

- 维护者有任何形式的回应（comment、reaction、review request）→ ping 间隔重置为 1 天
- PR 有新 commit → ping 间隔重置为 1 天

### 为什么要这样设计

核心逻辑：维护者看到 PR 需要时间。第一天就 ping 显得太急，第二天合理。第二、三次 ping 间隔拉长是告诉 maintainer"我不是在催你，我在等你"——但我还是记着这件事。3周后无响应，大概率不会处理了，停止浪费感情。

### 待更新到 cron 任务

- [ ] `PR攻关 - 权威项目版` 的 ping 逻辑需要按此表重写
- [ ] Active PR 表需要增加 `last_ping_date` 和 `ping_count` 字段
- [ ] 每次 ping 都要记录，方便判断当前在哪一步

---

## Open Questions（长期不知道）

- [ ] GH search API 间歇性不通的根因？是否影响新机会发现？
- [ ] 白天时区 cron 执行率低（17%）vs 凌晨时段（100%）—— 是否有后台任务抢占？
- [ ] 磁盘事件后残留进程锁的根因是否彻底排查？
