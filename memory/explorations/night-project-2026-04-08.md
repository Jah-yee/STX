# 凌晨PR攻关 - 2026-04-08

## 项目
- **Name:** TEN-framework
- **URL:** https://github.com/TEN-framework/ten-framework
- **Stars:** ~8k+
- **Description:** Open-source framework for real-time multimodal conversational AI

## 发现的问题
Issues #2107, #2106 报告 subprocess shell=True 安全漏洞

## 修复方案
将 `subprocess.run(cmd, shell=True)` 改为 `subprocess.run(shlex.split(cmd), shell=False)`

## 修复的文件 (3个)
1. `packages/core_apps/default_app_cpp/tools/run_script.py`
2. `packages/core_extensions/default_extension_cpp/tools/run_script.py`
3. `packages/core_extensions/default_extension_nodejs/tests/bin/start.py`

## PR状态
- Branch: `fix/shell-injection-security`
- Commit: 已创建
- GitHub Push: 需用户手动认证

## 修复diff
```diff
# packages/core_apps/default_app_cpp/tools/run_script.py
-import shlex
-def run_cmd(cmd: str) -> int:
-    result = subprocess.run(cmd, shell=True, check=True)
+    result = subprocess.run(shlex.split(cmd), shell=False, check=True)

# packages/core_extensions/default_extension_cpp/tools/run_script.py
-import shlex  
-def run_cmd(cmd: str, env: dict[str, str] | None = None) -> int:
-    result = subprocess.run(cmd, shell=True, check=True, env=env)
+    result = subprocess.run(shlex.split(cmd), shell=False, check=True, env=env)

# packages/core_extensions/default_extension_nodejs/tests/bin/start.py
- result = subprocess.run(["npm", "install"], env=env, shell=True)
+ result = subprocess.run(["npm", "install"], env=env)
```