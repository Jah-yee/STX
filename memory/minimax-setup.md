# MiniMax MCP配置状态

## 当前状态

| 组件 | 状态 |
|------|------|
| API Key | ✅ 有效 (sk-cp-...) |
| API验证 | ✅ curl成功 |
| MCP包 | ⚠️ npx格式不兼容 |

## 临时方案

使用curl作为web_search备选：
```bash
curl -s "https://api.minimax.io/v1/text/search?query" 
  -H "Authorization: Bearer $MINIMAX_API_KEY"
```

## 备用搜索方案

1. gh search (已验证可用)
2. curl + GitHub API
3. web_fetch

## API Key保存

Key存储位置：
- OpenClaw config: ~/.openclaw/openclaw.json (minimax-portal.apiKey)

