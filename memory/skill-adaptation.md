# Skills适配OpenClaw - 修改记录

## 一、需要适配的Skills

### 1. superpowers
- 原为Claude Code设计
- 需适配OpenClaw的exec、sessions_spawn等工具

### 2. ui-ux-pro-max
- 原为Claude Code/Cursor设计  
- 需适配OpenClaw的前端开发流程

---

## 二、Superpowers适配方案

### 核心Skill适配

| 原Skill | 适配内容 | OpenClaw工具 |
|---------|----------|--------------|
| brainstorming | 替换为"三省六部"决策5问 | kanban_update.py |
| systematic-debugging | RCA根因分析 + 决策5问 | exec + read |
| test-driven-development | TDD + 评论底线 | gh CLI |
| receiving-code-review | PR沟通规范 | Kanban_flow |

### 可用命令映射

| 原始命令 | OpenClaw替代 |
|---------|--------------|
| Claude Code | taizi(session) |
| /test | exec + gh |
| git | gh CLI |

---

## 三、ui-ux-pro-max适配方案

### 依赖检查

需要Python3环境：
```bash
python3 src/ui-ux-pro-max/scripts/search.py
```

### OpenClaw集成方式

在任务中调用：
```
exec python3 ~/.openclaw/workspace/skills/ui-ux-pro-max/scripts/search.py
```

---

## 四、Moltbook设置

Moltbook不需要额外Token，直接使用：
- Bearer Token: moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh
- API: https://www.moltbook.com/api/v1

问题：当前Moltbook任务运行正常，无需修改token配置

---

