# PR攻关 工作流 v3 — 深度+广度强化版

**创建时间：** 2026-05-01 09:49 CST
**版本：** v3
**维护人：** 太子

---

## 🎯 核心改变

| 之前 | 现在 |
|------|------|
| 每轮只找1个PR机会 | 每轮扫描10+仓库，深度验证3+候选 |
| 快速跳过 | 强制读CONTRIBUTING.md + 3+ issues |
| 无正向指标 | 有可量化指标（扫描量、验证量） |
| 单线执行 | 4步流水线，并行处理 |

---

## 📐 4步工作流

```
Step 1: 大范围扫描（Scan）
  ↓
Step 2: 深度评估（Evaluate）
  ↓
Step 3: 深入调查（Investigate）
  ↓
Step 4: 执行提报（Execute）
```

---

## Step 1: 大范围扫描（Scan）

**目标：** 扫描15-20个仓库，找5+个候选

### 执行
```bash
# 扫描多个来源
gh api 'search/repositories?q=good-first-issue+language:python+pushed:>2026-04-01' --jq '.items[] | {full_name, stargazers_count, open_issues_count}'
gh api 'search/repositories?q=good-first-issue+language:go+pushed:>2026-04-01' --jq '.items[] | {full_name, stargazers_count, open_issues_count}'
gh api 'search/repositories?q=good-first-issue+language:typescript+pushed:>2026-04-01' --jq '.items[] | {full_name, stargazers_count, open_issues_count}'
```

### Gate-1 过滤（快速）
- [ ] 不在blocklist
- [ ] 不是Gerrit模式
- [ ] 不是blocked org

### 输出
- **扫描仓库列表**（15-20个）
- **通过Gate-1的候选列表**（5-10个）
- **正向指标：scan_count, gate1_pass_count**

---

## Step 2: 深度评估（Evaluate）

**目标：** 对每个Gate-1候选读CONTRIBUTING.md + 查issues

### 执行（并行）
对每个Gate-1候选仓库：
1. **读CONTRIBUTING.md** → 获取格式要求
2. **查OPEN PR数量** → 过Gate-2
3. **搜索issues** → 找typo/doc/simple-bug类issue

```bash
# 并行执行
gh api repos/{org}/{repo}/contents/CONTRIBUTING.md
gh api repos/{org}/{repo}/pulls?state=open&per_page=100 --jq 'length'
gh api search/issues?q=is:issue+repo:{org}/{repo}+is:open+label:bug,typo,documentation,good-first-issue&per_page=20
```

### Gate-2 过滤
- [ ] OPEN PR < 10（宽松版，适应大仓小修复策略）
- [ ] CONTRIBUTING.md存在且可读
- [ ] 有可fix的issues

### 输出
- **每个候选的CONTRIBUTING摘要**（commit格式/PR模板/sign-off要求）
- **可用issues列表**（带难度标签）
- **通过Gate-2的候选列表**（2-3个）
- **正向指标：gate2_pass_count, contributing_read_count, issues_found**

---

## Step 3: 深入调查（Investigate）

**目标：** 对每个Gate-2候选深入理解issue + 写fix草案

### 执行
对每个Gate-2候选仓库：
1. **读issue详情** → 理解问题
2. **读相关代码** → 理解上下文
3. **写fix草案** → 伪代码/初步diff
4. **验证fix可行性** → diff大小、风险

```bash
gh api repos/{org}/{repo}/issues/{issue_num}
gh api repos/{org}/{repo}/contents/{file_path}
git clone https://github.com/{org}/{repo}.git /tmp/{repo}
# 分析代码
```

### Gate-3 过滤
- [ ] fix可以在一两个文件内完成
- [ ] 不需要大幅重构
- [ ] 有明确测试方案

### 输出
- **每个候选的fix草案**
- **diff行数估计**
- **通过Gate-3的候选列表**（1-2个）
- **正向指标：gate3_pass_count, draft_created_count**

---

## Step 4: 执行提报（Execute）

**目标：** 执行最高优先级候选，提PR

### 执行
对Gate-3候选：
1. **创建分支**
2. **写正式fix**
3. **commit（严格按CONTRIBUTING.md格式）**
4. **push并创建PR**
5. **验证PR创建成功**

### 输出
- **PR链接**（成功）
- **失败原因**（失败）
- **正向指标：pr_created_count, execution_time_ms**

---

## 📊 正向指标体系

> 每次cron必须报告这些指标

### 扫描指标
| 指标 | 说明 | 目标 |
|------|------|------|
| scan_count | 扫描的仓库数量 | ≥15 |
| gate1_pass_count | 通过Gate-1的候选数 | ≥5 |

### 评估指标
| 指标 | 说明 | 目标 |
|------|------|------|
| contributing_read_count | 读完CONTRIBUTING.md的数量 | ≥3 |
| issues_found | 找到的可用issues数 | ≥10 |
| gate2_pass_count | 通过Gate-2的候选数 | ≥2 |

### 调查指标
| 指标 | 说明 | 目标 |
|------|------|------|
| draft_created_count | 写了fix草案的数量 | ≥1 |
| gate3_pass_count | 通过Gate-3的候选数 | ≥1 |

### 执行指标
| 指标 | 说明 | 目标 |
|------|------|------|
| pr_created_count | 成功创建的PR数 | ≥1 |
| execution_time_ms | 本轮总执行时间（ms） | <180000 |

---

## ⏱️ 时间分配

```
总时间预算：3x 原来 ≈ 180秒

Step 1（扫描）：30秒
  - 并行API调用
  - 15-20个仓库

Step 2（评估）：60秒
  - 5个候选，每个12秒
  - CONTRIBUTING + issues + PR count

Step 3（调查）：60秒
  - 2-3个候选，每个20秒
  - issue分析 + 代码 + 草案

Step 4（执行）：30秒
  - 1个PR提交
```

---

## 🔄 与Cron集成

每次cron调用时：
1. 读取 `memory/PR-fast/candidates.md` 获取上轮遗留候选
2. 执行4步工作流
3. 更新 `memory/PR-fast/candidates.md`
4. 更新 `memory/PR-fast/metrics.md`
5. 报告指标

---

## 📋 报告模板

```
## PR攻关 深度版报告 — {timestamp}

### 📊 正向指标
| 指标 | 值 | 目标 | 状态 |
|------|-----|------|------|
| scan_count | {n} | ≥15 | {'✅' if n>=15 else '❌'} |
| gate1_pass | {n} | ≥5 | {'✅' if n>=5 else '❌'} |
| contributing_read | {n} | ≥3 | {'✅' if n>=3 else '❌'} |
| issues_found | {n} | ≥10 | {'✅' if n>=10 else '❌'} |
| gate2_pass | {n} | ≥2 | {'✅' if n>=2 else '❌'} |
| draft_created | {n} | ≥1 | {'✅' if n>=1 else '❌'} |
| gate3_pass | {n} | ≥1 | {'✅' if n>=1 else '❌'} |
| pr_created | {n} | ≥1 | {'✅' if n>=1 else '❌'} |
| execution_time_ms | {n} | <180000 | {'✅' if n<180000 else '❌'} |

### 📋 4步执行结果
- Step 1 (Scan): {details}
- Step 2 (Evaluate): {details}
- Step 3 (Investigate): {details}
- Step 4 (Execute): {details}

### 🏆 本轮成果
- 新PR: {pr_url or "无"}
- 遗留候选: {n}个

### 📝 下轮待办
- {list}
```

---

**版本历史：**
- v1: 单线快速扫描
- v2: Gate过滤 + 候选队列
- v3: 4步工作流 + 正向指标 + 3x时间
