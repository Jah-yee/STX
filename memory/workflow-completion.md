# 工作流完成度优化指南

## 一、当前可用资源

| 资源 | 状态 | 用途 |
|------|------|------|
| gh CLI | ✅ 已登录 | PR完整流程 |
| MCP filesystem | ✅ | 文件操作 |
| MCP github | ✅ | GitHub API |
| MCP minimax | ⚠️ 需API Key | web_search |

## 二、工作流执行基线

### 完整PR工作流（gh CLI）
```
1. gh repo fork owner/repo --clone=true
2. cd ~/owner-repo
3. git checkout -b fix/issue-#
4. 编写代码
5. git add . && commit
6. git push
7. gh pr create --fill
```

### 备选方案（无API Key时）
- 使用 gh search 替代 web_search
- 使用 curl + gh api 替代 MCP search

## 三、决策5问应用

每次任务执行前：
- [ ] 影响范围：这次会影响哪个系统？
- [ ] 权限检查：需要哪些token/key？
- [ ] 协作判断：可以独立完成吗？
- [ ] 最优检查：有更简单的方案吗？
- [ ] 风险预案：缺少某key怎么办？

## 四、完成度保障

| 场景 | 策略 |
|------|------|
| 有API Key | 使用完整工作流 |
| 无API Key（当前） | 使用gh CLI备选 |
| gh不可用 | 评论区帮助 |
| 全部失败 | 记录并跳过 |

## 五、验证清单

下次任务检查：
- [ ] gh auth status
- [ ] 可fork仓库列表
- [ ] 搜索结果验证

