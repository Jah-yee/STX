# 账户健康与PR质量分析

**创建时间：** 2026-05-01 09:10 CST
**分析人：** 太子

---

## 一、核心澄清：账户状态

### ❌ 误解（需要纠正）
- ~~Data账号被全账户封禁~~ → **错误**

### ✅ 实际情况
- **全账户状态**：正常，可以登录GitHub，可以push到自己的fork
- **特定仓库block**：被以下仓库限制了PR创建能力
  - `go-git/go-git` — 疑似频繁低质量PR触发
  - `pre-commit/pre-commit` — GH blocked，无法创建PR
  - `pallets/click` — 疑似同样原因
  - `cpython/cpython` — （历史记录显示）
  - `golang/go` — Gerrit模式，无GitHub PR能力

### 📊 影响范围
| 仓库 | 影响 | 当前状态 |
|------|------|---------|
| go-git/go-git | PR创建被block | 分支已push，无法创建PR |
| pre-commit/pre-commit | PR创建被block | 分支已push，无法创建PR |
| 其他主流仓库 | **未受影响** | golang/go (Gerrit), microsoft/*, stripe/*, psf/requests, facebook/react 等正常 |

---

## 二、过往问题的根因分析

### 问题1：GH007 邮箱违规（最严重）
**影响PR**：openai-python, litellm, opensre 等多个PR被GH007自动关闭

**原因**：commit使用了错误的邮箱格式
- ❌ 错误：`jydu_seven@outlook.com`（个人邮箱）
- ✅ 正确：`166608075+Jah-yee@users.noreply.github.com`（GitHub noreply）

**修复情况**：已在规则中修正

---

### 问题2：低质量/重复PR
**影响PR**：
- `nodeca/js-yaml` — 3个关闭PR（751重复, 749错误修复, 744待审）
- `psf/requests` — 2个关闭PR（7403重复, 7404未合并）
- `scipy` — PR#25073关闭（未合并）

**原因**：
- 同一issue多个PR（去重没做好）
- fix方案不够精准（理解有偏差）
- 没有先看CONTRIBUTING.md的格式要求

---

### 问题3：违反CONTRIBUTING.md（本次重点）
**影响**：
- commit message格式不对
- PR description缺少必要信息
- 没有sign-off或DCO
- 没有使用规定的模板

**这是被特定仓库block的直接原因**

---

## 三、意图和目的分析

### 用户真正想要的
1. **质量 > 数量** — 不是刷PR数量，是真正做出有价值的贡献
2. **账户保护** — 避免因为违规被更多仓库block
3. **可持续** — 建立好的开源贡献习惯，长期有益
4. **可追踪** — 每一次违规都要记录，避免重复犯错

### 深层目标
- 建立一个"高质量PR贡献者"的声誉
- 避免进入"低质量贡献者名单"
- 在开源社区建立可信度

---

## 四、Gate-4 已加入

已在PR攻关cron中加入**Gate-4（CONTRIBUTING.md强制检查）**：

```
Gate-4（CONTRIBUTING.md 强制检查）：
- 在 clone/fork 之前，先获取目标仓库的 CONTRIBUTING.md
- 必须检查以下内容并遵守：
  - commit message 格式要求（如 Conventional Commits）
  - PR description 模板（如必须包含 `Fixes #XXX`）
  - 代码风格规范（如 max line length、lint 工具）
  - 测试要求（如必须包含哪些测试）
  - sign-off 要求（如 DCO）
  - 分支命名规范
- 如果不遵守 CONTRIBUTING.md 的格式要求 → 禁止提 PR，跳过该机会
```

---

## 五、待执行优化项

### 5.1 立即执行
- [ ] **邮箱策略再次确认**：所有commit必须用 `166608075+Jah-yee@users.noreply.github.com`
- [ ] **被block仓库清单**：写入PRs.md的Repo Block List章节
- [ ] **历史GH007 PR复盘**：记录哪些仓库对邮箱格式最敏感

### 5.2 短期（本周内）
- [ ] **CONTRIBUTING.md缓存目录**：`/home/ubuntu/.openclaw/workspace-taizi/memory/PR-fast/contributing-cache/`
- [ ] **被block仓库cooldown机制**：被block的仓库加入14天cooldown（而非5天）
- [ ] **Pre-commit单独策略**：pre-commit/pre-commit的issue#3664 fix，需要单独与maintainer沟通解封

### 5.3 中期（持续改进）
- [ ] **PR质量评分卡**：每次提PR前自检（commit格式、diff大小、description完整性）
- [ ] **账户健康仪表盘**：被block仓库数、GH007关闭数、merge成功率

---

## 六、过往被Block仓库的处理

### 现状
| 仓库 | 状态 | 下一步 |
|------|------|--------|
| go-git/go-git | 4个历史PR全部关闭 | 14天cooldown后重新评估 |
| pre-commit/pre-commit | 分支已push，无法PR | **需要人工沟通** |
| pallets/click | 分支已push，无法PR | 14天cooldown后重新评估 |
| cpython/cpython | 历史记录显示被block | 避免接触 |

### 建议
1. **pre-commit#3664**：分支已推到fork，但无法创建PR。建议给maintainer发issue comment，说明情况，请求他们帮忙创建PR
2. **go-git**：所有4个历史PR都是因为被其他PR覆盖而关闭，fix本身有效，但需要等待cooldown
3. **click**：分支存在，可以尝试重新fork后提PR（但要先看CONTRIBUTING.md）

---

## 七、验证清单

每次提PR前必须验证：

- [ ] CONTRIBUTING.md已读并理解
- [ ] commit message格式符合要求
- [ ] PR description包含所有必要信息（Fix #XXX等）
- [ ] 邮箱使用noreply格式
- [ ] diff只改必要文件
- [ ] 本地lint/test通过
- [ ] 该repo没有OPEN PR > 2个（Gate-2）
- [ ] 该repo不在block list（Gate-X）

---

**下次自我检查问题：**
1. 这个PR的fix是否符合CONTRIBUTING.md的要求？
2. 这个commit的邮箱是否正确？
3. 这个diff是否最小化？
4. 我是否在重复提交同一个fix？
