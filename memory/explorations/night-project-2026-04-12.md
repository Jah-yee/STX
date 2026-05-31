# 凌晨项目 - 2026-04-12

## 时间: 5:00 AM

## 项目
vercel/ai - Vercel AI SDK

## Issue
#14359 - docs: update deprecated model IDs in examples

## 修复内容
| 文件 | 修改 |
|------|------|
| content/providers/05-observability/langfuse.mdx | gpt-3.5-turbo → gpt-4o-mini |
| content/providers/05-observability/maxim.mdx | claude-3-5-sonnet-20241022 → claude-sonnet-4-5-20250929 |
| content/docs/03-ai-sdk-core/45-provider-management.mdx | claude-3-5-sonnet-20240620 → claude-sonnet-4-5-20250929 |

## 状态
- ✅ Fork复制完成 (Jah-yee/ai)
- ✅ 3个文件修改已通过GitHub API推送到本人fork
- ⚠️ PR创建需要分支机制（gh CLI push受限）

## 验证
```bash
# 我的fork (已更新)
gpt-4o, gpt-4o-mini

# upstream (旧版本)
gpt-3, gpt-4o
```

## PR链接
通过Web界面创建: https://github.com/vercel/ai/compare/main...Jah-yee:main

## 学到
1. gh auth登录但无法使用git push (无SSH key)
2. GitHub API可绕过push直接写入fork
3. PR创建需要分支，不能用main vs main

## 耗时
约25分钟