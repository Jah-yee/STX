# Skills场景配置 - 新Skills应用

## 一、Skills与场景对应

### 1. superpowers - 复杂任务场景
- **使用场景**: PR攻关、debug、深度分析
- **功能**: TDD、系统调试、脑暴、规划
- **触发**: 需要深度思考的任务

### 2. ui-ux-pro-max - UI开发场景
- **使用场景**: 前端页面、组件设计
- **功能**: 设计系统生成、UI数据库
- **触发**: 前端开发任务

### 3. test-generator - 测试场景
- **使用场景**: 代码编写后的测试生成
- **功能**: TDD单元测试
- **触发**: 完成代码后自动触发

### 4. MCP Efficiency / token-manager - 低消耗场景
- **使用场景**: 长时间运行、token监控
- **功能**: 减少90% token使用
- **触发**: 高频任务

---

## 二、配置到Cron任务

### PR攻关任务加强
更新PR攻关任务加入superpowers方法论

### UI开发任务新配置
创建新任务使用ui-ux-pro-max

### 测试任务配置
test-generator已安装，完成代码后自动生成测试

---

## 三、验证检查

| Skill | 配置 | 验证 |
|-------|------|------|
| superpowers | ✅ | CLAUDE.md存在 |
| ui-ux-pro-max | ✅ | CLAUDE.md存在 |
| test-generator | ❌ | 仓库不存在 |
| MCP Efficiency | ✅ | mcporter配置 |
| token-manager | ✅ | mcporter配置 |

