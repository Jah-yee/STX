# 凌晨深度项目研究 - TEN-framework

**Date:** 2026-04-13  
**Time:** 04:00 AM

## 项目选择

**TEN-framework** (https://github.com/TEN-framework/ten-framework)
- Open-source framework for real-time multimodal conversational AI
- 实时语音AI代理框架，支持RTC和WebSocket连接
- 多模态AI应用（语音助手、Doodle、Speaker Diarization等）

## 发现的问题

### Issue #2106: Security - subprocess invocation uses shell=True
- **File:** `ai_agents/agents/examples/voice-assistant-nodejs/tenapp/ten_packages/extension/main_nodejs/tools/run_script.py`
- 已有一个PR修复了主文件

### 发现额外问题
在profiler工具和测试脚本中仍有shell=True：
- `tools/profiler/pprof/dump_heap_files_to_text.py`
- `tools/profiler/gperftools/compare_heaps.py`
- `tools/profiler/gperftools/dump_heap_files_to_raw.py`
- `tools/profiler/gperftools/dump_raw_files_to_text.py`
- `tests/ten_runtime/integration/nodejs/standalone_test_nodejs_2/.../start.py`
- `tests/ten_runtime/integration/nodejs/standalone_test_nodejs_3/.../start.py`

## 修复方案

### 1. Profiler工具修复
使用`concurrent.futures.ProcessPoolExecutor`替代shell并行执行：
- 保持并行性能
- 完全避免shell=True安全风险
- 使用手动文件操作处理输出重定向

### 2. 测试脚本修复
- 将`shell=True`改为`shell=False`
- 命令已经是列表格式，不需要shell解析

## 修改文件

```
tools/profiler/gperftools/compare_heaps.py
tools/profiler/gperftools/dump_heap_files_to_raw.py
tools/profiler/gperftools/dump_raw_files_to_text.py
tools/profiler/pprof/dump_heap_files_to_text.py
tests/ten_runtime/integration/nodejs/standalone_test_nodejs_2/.../start.py
tests/ten_runtime/integration/nodejs/standalone_test_nodejs_3/.../start.py
```

## PR状态

修复代码已完成，因git push认证问题无法推送到远程。
patch文件已保存，可手动提交。

## 技术细节

### Profiler修复模式
```python
# Before (不安全)
convert_to_raw_cmd = " & ".join(convert_to_raw_cmds)
rc = subprocess.run(convert_to_raw_cmd, shell=True)

# After (安全)
def run_convert_cmd(cmd):
    return subprocess.run(cmd, shell=False).returncode

with concurrent.futures.ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
    results = list(executor.map(run_convert_cmd, convert_to_raw_cmds))
```

## 后续行动

1. 尝试通过fork或手动方式提交PR
2. 可继续探索其他issues（如#2079 Memory leak）