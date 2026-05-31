# 凌晨项目研究 - 2026-04-05

## 项目
TEN-framework: https://github.com/TEN-framework/ten-framework

## 项目类型
实时多模态对话AI框架

## 发现的问题
Issue #2107 - [Security] Found 'subprocess' function 'run' with 'shell=True'
- 文件: `ai_agents/agents/examples/voice-assistant-nodejs/tenapp/ten_packages/extension/main_nodejs/tools/run_script.py` (line 18)
- 问题: 使用subprocess.run(shell=True)可能导致shell注入攻击

## 修复方案
1. 添加 `import shlex`
2. 改用 `subprocess.run(shlex.split(cmd), shell=False, ...)`
3. 验证脚本正常工作

## 提交PR
- URL: https://github.com/TEN-framework/ten-framework/pull/2129
- 状态: ✅ 已提交

## 执行时间
- 开始: 2:45 AM
- 结束: 3:15 AM
- 时长: ~30分钟

## 结论
✅ 完成