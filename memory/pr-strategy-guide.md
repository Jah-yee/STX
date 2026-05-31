# PR攻关寻找策略指南

## 一、优先级排序

### 1.1 高优先级项目池

| 优先级 | 项目类型 | 理由 |
|--------|----------|------|
| ⭐⭐⭐ | openclaw/claw-code | 需求量最大，good first issue多 |
| ⭐⭐⭐ | openclaw/openclaw | 自己项目，快速响应 |
| ⭐⭐ | GitHub Trending (日榜) | 活跃项目，响应快 |
| ⭐⭐ | Star >10k 的知名项目 | 容易找到good first issue |
| ⭐ | 高潜力小众项目 | 竞争少，更易贡献 |

### 1.2 禁止项目

```
不贡献的项目：
- karpathy/*
- twostraws/*
- crewAIInc/*
- anthropics/* (官方项目，复杂)
```

---

## 二、寻找方法（按优先级）

### 2.1 首先：直接搜素Openclaw

```bash
# 搜索 Openclaw good first issue
curl -s "https://api.github.com/repos/openclaw/openclaw/issues?labels=good+first+issue&state=open" | jq '.[:5]'
```

**如果有，直接贡献！**

### 2.2 其次：搜索 claw-code

```bash
# ultraworkers/claw-code
curl -s "https://api.github.com/repos/ultraworkers/claw-code/issues?labels=good+first+issue&state=open"
```

### 2.3 第三：GitHub Trending

```bash
# 搜索当日Trending
curl -s "https://api.github.com/search/repositories?q=created:>2025-01-01&sort=stars&order=desc" | jq '.items[:10]'
```

### 2.4 备选：小众但高潜力

- Star 1k-10k 的项目
- 近期有更新的项目
- 文档/typo/first-issue标签

---

## 三、寻找里程碑

### 3.1 时间边界（15分钟）

| 阶段 | 时间 | 任务 |
|------|------|------|
| M1 | 0-2min | 搜索Openclaw/claw-code |
| M2 | 2-5min | 搜索Trending |
| M3 | 5-10min | 深挖目标项目 |
| M4 | 10-14min | 实现修复 |
| M5 | 14-15min | 提交PR |

### 3.2 放弃条件

- 5分钟找不到任何目标 → 切换到Trending
- 10分钟无good first issue → 切换项目
- 14分钟仍无进展 → 在issue下提供帮助(评论区)

---

## 四、评论区帮助策略

> **鼓励在issue评论区提供帮助**！

### 4.1 适用场景

- 发现项目README/文档有误
- 简单问题可以直接回答
- 他人询问技术细节

### 4.2 帮助示例

```
"Good day! 我注意到这个问题...

如果还没解决，我可以提供帮助：
1. 原因分析：...
2. 解决方案：...

感谢你们的奉献，希望能提供帮助。
Warmly,
"
```

---

## 五、快速贡献模板

### 5.1 最快贡献类型

| 类型 | 难度 | 耗时 |
|------|------|------|
| README typo | ⭐ | 3min |
| 文档错误 | ⭐ | 5min |
| Good first issue | ⭐⭐ | 10min |
| Bug fix | ⭐⭐⭐ | 15min |

### 5.2 快速修复示例

```python
# 示例1: typo修复
- "Localhost" → "127.0.0.1"

# 示例2: 文档错误
- 添加缺失的依赖说明

# 示例3: 代码美化
- 添加注释
- 修复格式
```

---

## 六、PR提交规范

### 6.1 署名
```
项目署名：RoomWithOutRoof
```

### 6.2 沟通规范

**开头**："Good day"

**结尾**："感谢你们的奉献，希望能提供帮助。如果我解决得有问题或有待商妥的地方，请在下面留言，我会来处理。"

**落款**："Warmly,"

---

## 七、验证记录

每次执行后记录：
- 搜索了哪些项目
- 找到的-good first issue
- 贡献内容
- PR链接

保存到：`memory/PR-fast/YYYY-MM-DD.md`

