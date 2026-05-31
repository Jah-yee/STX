# 🌙 凌晨深度项目研究 - 2026-04-15

## 项目选择

**FastAPI** - 现代高性能Python Web框架

- GitHub: tiangolo/fastapi
- Stars: 70k+
- 语言：Python

## Issue 分析

### Issue #13056: Can't use `Annotated` with `ForwardRef`

**问题描述**：
```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()

def get_potato() -> Potato:
    return Potato(color='red', size=10)

@app.get('/')
async def read_root(potato: Annotated[Potato, Depends(get_potato)]):
    return {'Hello': 'World'}

@dataclass
class Potato:
    color: str
    size: int
```

When using `from __future__ import annotations`, `Potato` inside Annotated remains as string `"Potato"`, causing OpenAPI generation to fail.

## 根因定位

在 `fastapi/dependencies/utils.py` 的 `analyze_param()` 函数中：
- 从 `Annotated` 提取 `type_annotation = annotated_args[0]` 时，它仍是字符串
- `_get_flat_fields_from_params()` 后续调用 `get_cached_model_fields()` 需要真正的类对象
- `get_cached_model_fields()` 内部调用 `model.model_fields.items()` 无法处理字符串

而 `get_typed_signature()` (在 `get_typed_signature(call)` 中) 已正确处理了这个问题，它调用 `get_typed_annotation()` 来解析 forward ref。

## 修复实现

在 `analyze_param()` 提取 type_annotation 后，添加 forward ref 解析：

```python
# Extract Annotated info
if get_origin(use_annotation) is Annotated:
    annotated_args = get_args(annotation)
    type_annotation = annotated_args[0]
    # Resolve forward reference in type_annotation
    if isinstance(type_annotation, str):
        # Try to resolve using endpoint's globalns
        globalns = getattr(call, "__globals__", {})
        type_annotation = get_typed_annotation(type_annotation, globalns)
```

## 修复文件

1. `fastapi/dependencies/utils.py` - 5行

## 状态

- [x] 发现 Issue
- [x] 分析根因
- [x] 实现修复
- [x] Push 到远程
- [x] 创建 PR ✅

## PR 信息

- **PR 链接**: https://github.com/fastapi/fastapi/pull/15338
- **Fork**: Jah-yee/fastapi (from tiangolo/fastapi)
- **Branch**: fix/issue-13056-annotated-forwardref
- **修改**: 1文件, +5行

## 技术细节

### 问题链路

1. `from __future__ import annotations` 使所有注解变成 forward ref 字符串
2. `get_typed_signature()` 处理函数签名的注解，解析 forward ref
3. 但 `analyze_param()` 直接从 `Annotated` 提取的第一个参数没有解析
4. 当类型是 dataclass/Pydantic model 时，后续 `get_cached_model_fields()` 需要实际类对象

### 修复策略

复用已有的 `get_typed_annotation()` 函数，它使用 `evaluate_forwardref()` 来解析 forward ref。

## 今晨学到

1. **FastAPI 依赖解析**: 深入理解了 `analyze_param()` 和 `get_typed_signature()` 的协作
2. **Forward ref**: 了解了 PEP 563 字符串化注解的处理机制
3. **Python 调试**: 通过 `__future__` import 触发了不同的代码路径