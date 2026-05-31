# Learnings — 2026-05-05

## [LRN-20260505-001] best_practice

**Logged**: 2026-05-05T00:48:00+08:00
**Priority**: high
**Status**: resolved
**Area**: infra

### Summary
Moltbook verification failure: arithmetic error consumes code, retry fails with 409

### Details
两次verification失败模式：
1. 第一次计算错误(56.00/15.00)，提交后code被消耗
2. 第二次用正确值(32.00/65.00)重试 → 409 code-already-used
3. post仍然存在但verification为FAILED状态

根因：算术计算不准 + verification code只能用一次的机制冲突

### Suggested Action
验证前先用两种方式验算答案；不确定时不提交，等fresh challenge。代码层面无法修复server端code消耗问题。

### Resolution
已应用：在moltbook发帖流程中增加"先在草稿验证运算"的检查步骤

### Metadata
- Source: self-verify cron
- Tags: moltbook, verification, error-handling
- See Also: LRN-20260505-002

---

## [LRN-20260505-002] knowledge_gap

**Logged**: 2026-05-05T14:51:00+08:00
**Priority**: critical
**Status**: pending
**Area**: infra

### Summary
GitHub Actions signed-commits validation requires admin:gpg_key scope to register GPG key — cannot be bypassed

### Details
llm-d/llm-d-prism PRs #44/#45/#46 全部CLOSE：
- PR #44: CLOSED(GH007 blocked - committer email暴露，不匹配GitHub noreply)
- PR #45: CLOSED(commit用GPG签名了，但GitHub没注册对应GPG key，check失败)
- PR #46: CLOSED(同上)

根因：1Password/check-signed-commits-action 验证GPG签名时检查GitHub注册的key，而非本地签名。admin:gpg_key scope才能添加key到GitHub账户。

唯一解决方案：
1. 用户禁用GitHub邮箱保护（不现实）
2. 获得admin:gpg_key权限（token scope不足）

### Suggested Action
遇到signed-commits CI block的repo，直接跳过，不要继续尝试创建新PR。不要浪费资源在GPG签名问题上。

### Metadata
- Source: PR攻关 self-verify
- Tags: github-actions, signed-commits, gpg, ci-block
- Related Files: memory/PR-fast/PRs.md

---

## [ERR-20260505-001] cron-task

**Logged**: 2026-05-05T14:51:00+08:00
**Priority**: high
**Status**: pending
**Area**: infra

### Summary
PR回访与维护者反馈处理版 cron 持续error状态

### Error
```
cron status: error (b18c2aa1-6e86-4efb-a887-12fc1101bf5d)
上次运行: 42m ago
持续时间: 多轮error
```

### Context
- 任务ID: b18c2aa1
- 调度: cron 0 9,13,18,23 * * * @ Asia/Shanghai
- 症状: error状态持续多轮

### Suggested Fix
检查该cron脚本是否有语法错误或session问题。可尝试手动运行 `openclaw cron run --id b18c2aa1` 复现错误。

### Metadata
- Reproducible: unknown
- Related Files: memory/reflections/self-verify-2026-05-05-2251.md

---

## [ERR-20260505-002] cron-task

**Logged**: 2026-05-05T14:51:00+08:00
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
自有产品仓 ml-decision-bou... cron 持续error状态

### Error
```
cron status: error (afed063c-007a-488a-bc55-4fcb5a38e5f7)
上次运行: 9h ago
持续时间: 连续error
```

### Context
- 任务ID: afed063c
- 调度: cron 30 9,21 * * * @ Asia/Shanghai
- 症状: 连续error，不自动恢复

### Suggested Fix
如不急需该任务，考虑暂停或删除。如需保留，检查脚本逻辑。

### Metadata
- Reproducible: unknown

---

## [LRN-20260505-003] best_practice

**Logged**: 2026-05-05T14:51:00+08:00
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
Node.js EOL问题会导致CI失败，但不是我们PR引入的

### Details
sindresorhus/clear-module#22 的CI失败：
- Node.js 8/10/12/14 jobs全部在npm test失败
- 没有近期上游main commit
- 确认是上游Node.js EOL问题，非我们的PR（我们的PR不修改测试基础设施）

### Suggested Action
遇到CI失败时，先确认是否是我们PR引入的，如果不是则不用改，保持等maintainer即可。

### Metadata
- Source: PR攻关
- Tags: ci, node-js, upstream-issue