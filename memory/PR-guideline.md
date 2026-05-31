# PR 提交规范

> 最后更新: 2026-04-25

---

## 🚫 禁止提交PR的目标（阶段性）

> 生效日期: 2026-04-25

以下组织及旗下所有仓库**暂不接受PR提交**：

| 组织 | 代表仓库 | 原因 |
|------|----------|------|
| **Python** | CPython, PyTorch, pandas, numpy 等 | 阶段性能量聚焦调整 |

**说明**：这是阶段性策略调整，非永久禁止。恢复时间待定。

---

## 📋 PR署名规范

| 项 | 要求 |
|------|------|
| **Author** | 只用 RoomWithOutRoof |
| **Co-authors** | 不显示 |
| **显示方式** | 不要出现 "OpenClaw AI and others" |

---

## 🎯 执行时注意

### 1. 不要用fork方式
- 尽量在主repo创建分支提交
- 或者用 `--base` 参数

### 2. 确保commit author正确
```bash
git config user.name "RoomWithOutRoof"
git config user.email "roomwithoutroof@outlook.com"
```

### 3. GH账号
- Login: Jah-yee
- Profile name: RoomWithOutRoof

---

## ⚠️ 禁止出现

- ❌ OpenClaw AI
- ❌ "and others added N commits"
- ❌ co-author 显示

---

## 📊 PR 数量管控策略

> 生效日期: 2026-04-26

### 硬性 Gate（提 PR 前必须检查）

**Gate-1: 查重**
提 PR 前扫描 PRs.md 中该 repo 是否已有 OPEN PR：
- 有 → 评估：新的 fix 是否"同一 issue 的更好方案"？
  - 是 → push 到已有 PR 的分支，comment 说明是改进版本
  - 否 → **禁止新提 PR**，记录到候选队列
- 无 → 正常提 PR

**Gate-2: 数量上限**
每个 repo 同时最多 **2个 OPEN PR**：
- 已有2个 OPEN → 禁止提新的，等现有 PR 被 merge 或关闭

**Gate-3: 一个 fix 一个 commit**
- 一个 PR = 一个 fix = 一个 commit
- 不要分多个 commit 堆在一个 PR 里
- 如果需要改，用 rebase squash 合并后再 push

---

### 主动清理规则（每次「搜」步骤开始时执行）

**清理-1: 去重**
扫描 PRs.md，同一 repo 有 2+ 个 OPEN PR：
→ 保留**最新/最完整**的那个，关闭其他的，附原因

**清理-2: 僵尸检测**
- OPEN PR 超过 **14天无 review** → 发 ping comment
- OPEN PR 超过 **21天无 review** → 标记为"可能关闭"，在 PR body 加 note

**清理-3: In Progress 降级**
In Progress 条目超过 **7天** 未提 PR → 降级到"候选队列"，注明"待提"

**清理-4: 关闭重复/竞争 PR**
同一 repo 有多个 PR 修复同一 issue：
→ 保留最完整的，关闭其他的，避免 reviewer 困惑

---

### 实施检查清单

每次提 PR 前必须确认：
- [ ] 该 repo 在 PRs.md 中无 OPEN PR（Gate-1）
- [ ] 该 repo OPEN PR 数量 < 2（Gate-2）
- [ ] 本 PR 只有 1个 commit（Gate-3）
- [ ] 扫描是否有其他 PR 修复同一 issue（清理-4）

---

*最后更新: 2026-04-26*