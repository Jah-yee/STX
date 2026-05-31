# 推荐Skills安装清单

## 一、推荐安装的Skills（用户指定+搜索验证）

### 1. superpowers（超级能力）
- **GitHub**: obra/superpowers
- **Stars**: 132k+ 
- **MCP版本**: mcpservers.org/servers/erophames/superpowers-mcp
- **功能**: TDD、系统调试、脑暴、规划、子agent开发
- **安装**: https://github.com/obra/superpowers

### 2. MCP Integration（高效集成）
- **功能**: 减少90% token使用，直接调用外部工具
- **来源**: MCP Efficiency Skill (mcpmarket.com)
- **效果**: 通过MCP直连数据库、GitHub、浏览器

### 3. test-generator（测试生成）
- **GitHub**: @seanchiuai/claude-code-workflow/test-generator
- **功能**: TDD，生成单元测试
- **适配**: Chrome extension, React, Express, Python

### 4. ui-ux-pro-max（专业UI开发）
- **GitHub**: nextlevelbuilder/ui-ux-pro-max-skill
- **功能**: 设计系统生成器、专业UI数据库
- **支持**: Claude Code, Cursor, Windsurf, Codex

### 5. MCP Efficiency（低token消耗）
- **功能**: 减少90% token使用
- **来源**: mcpmarket.com/tools/skills/mcp-token-efficiency

---

## 二、低token消耗Skills（用户提到的summary类）

| Skill | 功能 | 来源 |
|-------|------|------|
| MCP Efficiency | 减少90% token | MCP直连 |
| Token Management | 节省50-70% | 上下文压缩 |
| Smart Loading | 动态加载 | Claude Code 2.1 |

---

## 三、安装命令

### 方式1: 从GitHub克隆
```bash
# Superpowers
git clone https://github.com/obra/superpowers ~/.openclaw/workspace/skills/superpowers

# ui-ux-pro-max  
git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill ~/.openclaw/workspace/skills/ui-ux-pro-max

# test-generator
git clone https://github.com/seanchiuai/claude-code-workflow/test-generator ~/.openclaw/workspace/skills/test-generator
```

### 方式2: MCP服务器
```bash
# MCP Efficiency
npx -y @modelcontextprotocol/server-mcp-efficiency

# Superpowers MCP
npx -y superpowers-mcp
```

---

## 四、兼容性确认

| Skill | 三省六部兼容 | pua兼容 |
|-------|-------------|---------|
| superpowers | ✅ | ✅ - 增强方法论 |
| MCP Integration | ✅ | ✅ - 减少消耗 |
| test-generator | ✅ | ✅ - TDD流程 |
| ui-ux-pro-max | ✅ | ✅ - UI开发 |
| MCP Efficiency | ✅ | ✅ - 节省token |

