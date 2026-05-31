# PR攻关 Blocklist + Scope Guide

**创建时间：** 2026-05-01 09:16 CST
**更新时间：** 2026-05-01 09:26 CST
**维护人：** 太子

---

## ⚠️ Scope Guide（什么时候跳过）

> **核心原则：** 大仓库的小修复 ✅ 在scope里！star多issue多反而是好机会

### 看单次PR的代码深度，不是看仓库大小

| 修复类型 | 大仓库？ | 在scope？ |
|---------|---------|----------|
| typo / 拼写错误 | ✅ 任何规模 | ✅ ✅ |
| outdated docs / 文档过时 | ✅ 任何规模 | ✅ ✅ |
| small syntax error | ✅ 任何规模 | ✅ ✅ |
| simple doc fix | ✅ 任何规模 | ✅ ✅ |
| 多文件复杂重构 | 任何规模 | ❌ 看能力 |
| 核心算法改写 | 任何规模 | ❌ 太难 |

### 真正跳过的情况

#### 🚫 类型A：Gerrit模式（不接受GitHub PR）
- `golang/*`（go, sys, tools, website等）— **注意**：website可以走Gerrit，其他不行
- `canonical/*`
- `android/*`
- `chromium/*`

#### 🚫 类型B：已知Blocklist
- go-git/go-git
- pre-commit/pre-commit
- pallets/click
- cpython/cpython

#### 🚫 类型C：单次PR代码太复杂
- 需要改核心数据结构
- 需要加复杂的测试用例
- 需要理解整个子系统的架构

### ✅ 好目标特征
- 大仓库 + 小修复（typo/doc）= ✅ 最佳
- 中等仓库 + 功能fix = ✅ 可做
- 小仓库 + 任何fix = ✅ 可做

### 快速判断
```
if (org == "golang") → 可能Gerrit，看具体repo
if (repo in blocklist) → 跳过
if (fix需要改 > 3个文件且涉及逻辑) → 评估能力
Otherwise → ✅ 可以尝试
```

---

## Block List（被限制的具体仓库）

| 仓库 | 限制类型 | 原因 | 被封时间 | 状态 | 下一步 |
|------|----------|------|----------|------|--------|
| go-git/go-git | PR创建被block | 疑似频繁低质量PR触发 | 2026-04-27 | 分支已push，无法创建PR | 14天cooldown，2026-05-11重评 |
| pre-commit/pre-commit | PR创建被block | GH blocked | 2026-05-01 | 分支已push，无法创建PR | **需要人工沟通maintainer** |
| pallets/click | PR创建被block | 疑似同样原因 | 2026-04-25 | 分支已push，无法创建PR | 14天cooldown，2026-05-09重评 |
| cpython/cpython | 历史block | 历史记录 | 早期 | N/A | 避免接触 |

---

## GH007 自动关闭历史

> 这些仓库对邮箱格式敏感，commit用错邮箱直接被自动关闭

| 仓库 | PR# | 关闭原因 | 教训 |
|------|-----|----------|------|
| openai/openai-python | #3117, #3118 | GH007邮箱违规 | ✅ 已修正邮箱 |
| BerriAI/litellm | #26385 | GH007邮箱违规 | ✅ 已修正邮箱 |
| Tracer-Cloud/opensre | #1080 | GH007邮箱违规 | ✅ 已修正邮箱 |

---

## 已恢复仓库清单

| 仓库 | 恢复时间 | 验证方式 |
|------|----------|----------|
| nodeca/js-yaml | 2026-05-01 | 已提PR#744，等待审查 |
| hylang/hy | 2026-05-01 | 重复PR已关闭，fix正确 |
| psf/requests | 2026-05-06 | 等待cooldown结束 |

---

## Block 判断标准

### Gate-X（block list检查）
满足以下任一条件 → 加入blocklist，禁止提PR：
- [ ] 该仓库历史上关闭过你 >2个PR
- [ ] GH007自动关闭过你的PR
- [ ] 无法创建PR（API返回403或GH blocked）
- [ ] CONTRIBUTING.md明确禁止外部贡献者

---

## 每轮检查项

每次PR攻关前必须：
1. 目标仓库是否在blocklist？ → 是 → 跳过
2. 该仓库历史上GH007关闭过PR？ → 是 → 格外注意邮箱格式
3. 该仓库CONTRIBUTING.md是否要求sign-off/DCO？ → 是 → 必须包含

---

**下次更新：** 2026-05-02 或下次发现新block时
