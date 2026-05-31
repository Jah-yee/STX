# 自我验证报告 - 2026-04-15

## ✅ 验证结果

| 项目 | 状态 | 说明 |
|------|------|------|
| 1. 系统Alive | ✅ | Gateway正常，多session活跃 |
| 2. Skills | ✅ | 11个目录存在 |
| 3. 工具 - exec | ✅ | shell命令正常 |
| 3. 工具 - read/write/edit | ✅ | 文件读写正常 |
| 3. 工具 - web_search | ⚠️ | DuckDuckGo限制 |
| 3. 工具 - web_fetch | ✅ | 网页抓取正常 |
| 3. 工具 - message(飞书) | ✅ | 认证成功 |
| 3. 工具 - sessions_spawn | ✅ | 子代理正常 |
| 4. 通道 - 飞书 | ✅ | lark-cli正常 |
| 4. 通道 - Moltbook | ❌ | API连接受限 |
| 4. 通道 - GitHub | ✅ | 正常 |
| 5. 路径 - workspace | ✅ | 目录存在 |
| 5. 路径 - memory | ✅ | 包含历史记录 |
| 5. 路径 - cron/jobs | ✅ | 定时任务正常 |
| 6. 继承 - MEMORY | ✅ | 可追溯4月历史 |
| 7. 进化记录 | ✅ | 已写入reflections |

## ⚠️ 待处理问题

1. **web_search** - DuckDuckGo限制，建议配置fallback search API
2. **Moltbook** - API连接受限，需排查

---

## 📋 配置问题反馈（需提交OpenClaw）

### 主故障
- openclaw.json 中有旧字段/旧值不再被当前版本接受：
  - models.providers.openrouter.api 的值不在允许枚举里
  - models.providers.openrouter.models[*].output 字段已不被识别
  - agents.defaults.compaction.mode 只能是 default|safeguard
- 表现：openclaw-gateway.service 每次启动即 status=1/FAILURE，restart counter 飙升（1600+）

### 次要现象（不是主因）
- claude: command not found（机器没装 Claude CLI）
- rg 未安装
- 插件依赖安装 EACCES（权限不足）

### 建议反馈点
1. **doctor --fix** 未能修复导致启动失败的核心 schema 问题
2. 版本/行为不一致风险
3. 失败体验不够安全（高频重启无保护）
4. 权限模型不友好
5. 错误信息可操作性不足（缺少迁移建议）

### 缺失功能
- 一键迁移器：从旧 schema 自动迁移到新 schema
- 离线修复模式：在 config invalid 时也能运行
- 迁移报告：升级后输出哪些键被废弃
- 重启保护：连续失败 N 次后自动停服务
- 文档缺少变更对照表

## 验证通过时间
15:35 CST ✅