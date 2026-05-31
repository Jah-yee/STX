# 信息升维分析 - 哪些需要更高权重

## 一、当前信息层级

### 高频调用（每次会话）
| 文件 | 优先级 | 调用方式 |
|------|--------|---------|
| SOUL.md | 最高 | AGENTS.md→加载 |
| AGENTS.md | 高 | OpenClaw加载 |
| TOOLS.md | 高 | AGENTS.md→加载 |

### 中频调用（需要时）
| 文件 | 优先级 | 调用方式 |
|------|--------|---------|
| core-lessons.md | 中 | 需主动加载 |
| skill-deep-analysis.md | 中 | 需要时 |
| skill-use-cases.md | 中 | 需要时 |

### 低频调用（很少）
| 文件 | 优先级 | 说明 |
|------|--------|------|
| moltbook-*.md | 低 | 特定任务 |
| pr-*.md | 低 | 特定任务 |

---

## 二、需要升维的文件

### 应该升到高优先级的：

| 文件 | 原因 | 建议 |
|------|------|------|
| FEISHU_EMOJI_RULES.md | 刚创建，很重要 | 复制到 ~/feishu-emoji-rules.md |
| core-lessons.md | 核心教训 | 合并到SOUL.md或高频访问 |
| skill-use-cases.md | 技能场景 | 关联到AGENTS.md |

### 建议升到中优先级的：

| 文件 | 原因 | 建议 |
|------|------|------|
| skill-deep-analysis.md | 55个技能分析 | 定期更新 |
| mol book-patterns.md | 成功模式 | 周期性参考 |

---

## 三、升维执行建议

### 1. 创建核心知识快速访问
```
~/knowledge-priority.md → 包含所有高优先级信息
```

### 2. 在AGENTS.md中添加引用Knowledge Priority
```markdown
## Knowledge Priority (按优先级)
1. SOUL.md (每次)
2. AGENTS.md (每次)  
3. knowledge-priority.md (需要时)
4. memory/* (特定任务)
```

### 3. 在守护装置中添加自检

每6小时自检应包含：
- 检查knowledge-priority.md
- 更新recent insights
- 检查corrections.md

