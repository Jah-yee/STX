# PR攻关 可研 Candidate 名单

**创建时间：** 2026-05-01 09:18 CST
**更新时间：** 2026-05-01 09:26 CST
**维护人：** 太子
**用途：** 分步验证 + 执行

---

## 📋 分步验证流程（Gate）

```
Gate-1: 仓库不在blocklist
Gate-2: OPEN PR < 3
Gate-3: 不在Gerrit模式
Gate-4: CONTRIBUTING.md 已读并遵守 ← 【本次强化重点】
Gate-5: issue 质量可fix
```

---

## ⚠️ Scope Guide（核心原则）

> **大仓库的小修复 ✅ 在scope里！star多issue多反而是好机会**

### 好目标
| 修复类型 | 大仓库？ | 在scope？ |
|---------|---------|----------|
| typo / 拼写错误 | ✅ 任何规模 | ✅ ✅ |
| outdated docs / 文档过时 | ✅ 任何规模 | ✅ ✅ |
| small syntax error | ✅ 任何规模 | ✅ ✅ |
| simple doc fix | ✅ 任何规模 | ✅ ✅ |
| 中等仓库功能fix | 中等规模 | ✅ |

### 需要跳过的
| 原因 | 例子 | 说明 |
|------|------|------|
| Gerrit模式 | golang/go | 不接受GitHub PR |
| Blocklist | go-git, pre-commit, click | 已被限制 |
| Fix太复杂 | 改>3文件+涉及逻辑 | 能力不足 |

---

## 🔍 第一批候选仓库

### 验证结果（Step 1完成）

| 仓库 | Stars | Open Issues | 结论 | 下一步 |
|------|-------|-------------|------|--------|
| influxdata/influxdb-client-go | 654 | 23 | ✅ 可推进 | 查issues找fix |
| aws-amplify/amplify-cli | 2.8K | 830 | ✅ 大仓小修复在scope | 查typo/doc |
| kubernetes-client/python | 7.5K | 95 | ✅ k8s系可查简单fix | 确认Gerrit+查typo |

---

## 🚫 已知不候选（Blocklist）

| 仓库 | 原因 |
|------|------|
| go-git/go-git | GH blocked |
| pre-commit/pre-commit | GH blocked |
| pallets/click | GH blocked |
| cpython/cpython | 历史block |
| scipy/scipy | GH007关闭历史 |
| golang/go | Gerrit模式 |

---

## 🔍 下一轮重点

### 🔴 influxdata/influxdb-client-go
1. [ ] 查其issues，找typo/doc类issue
2. [ ] 读其CONTRIBUTING.md
3. [ ] 写fix

### 🟡 aws-amplify/amplify-cli
1. [ ] 搜索其代码中的typo/doc问题
2. [ ] 读其CONTRIBUTING.md
3. [ ] 找简单fix并提PR

### 🟡 kubernetes-client/python
1. [ ] 确认是否Gerrit模式
2. [ ] 搜索typo/doc类issue
3. [ ] 找简单fix并提PR

---

**下次更新：** 2026-05-01 下一轮PR攻关时
