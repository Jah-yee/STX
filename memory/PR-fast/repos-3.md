# PR快速扫描结果 - repos-3 (2026-04-24)

> 扫描仓库: openai/openai-python, microsoft/TypeSpec, Tracer-Cloud/opensre
> 扫描标签: bug, good first issue | 创建时间: > 2026-04-17
> 数据来源: GitHub REST API (直接调用，绕过 gh search 速率限制)

---

## 一、openai/openai-python

### ✅ Issue #3097 — `vector_stores.files.upload_and_poll()` can hang indefinitely
- **置信度**: ⭐⭐⭐⭐ (5/5)
- **GH链接**: https://github.com/openai/openai-python/issues/3097
- **修复内容**: 在 `upload_and_poll()` 中添加最大轮询超时，当文件状态持续 `in_progress` 超过阈值时抛出明确的超时异常，而不是无限挂起
- **为什么能做**: 问题代码路径清晰（轮询逻辑），复现步骤完整，有明确的 expected vs observed，修复只需在 polling loop 加 timeout 检查
- **最小改法**: 在 `resources/files.py` 或 poller 文件的 `while` 循环中加 `max_polls` / `timeout` 退出条件，超时 raise `TimeoutError` 或返回特定状态

### ✅ Issue #3084 — Async Responses Structured Outputs Memory leak
- **置信度**: ⭐⭐⭐⭐⭐ (5/5)
- **GH链接**: https://github.com/openai/openai-python/issues/3084
- **修复内容**: 改用 non-parameterized base class (`ParsedResponse` 而非 `ParsedResponse[TextFormatT]`) 调用 `construct_type_unchecked`，避免 Pydantic 每次重建 schema 导致内存泄漏
- **为什么能做**: 作者已给出精确根因和 fix（3行改动），完全在 Python 文件 `openai/lib/_parsing/_responses.py`
- **最小改法**: `openai/lib/_parsing/_responses.py` 中 3 处 `construct_type_unchecked` 调用，去掉 TypeVar 参数

### ⚠️ Issue #3090 — GPT-5.4-Mini returns 500 with image parameters
- **置信度**: ⭐⭐⭐ (3/5)
- **GH链接**: https://github.com/openai/openai-python/issues/3090
- **修复内容**: 可能是参数校验或请求体构建问题，需进一步调查是 API 端还是 SDK 端问题
- **为什么能做**: 有 MRE，但目前信息不足以确定修复位置；gpt-5.4-mini 特定问题，可能涉及模型差异处理
- **最小改法**: 需先确认是 SDK 问题还是 API 问题，可能需要添加模型特定参数适配

---

## 二、microsoft/TypeSpec

### ✅ Issue #10471 — [Bug] [http-server-csharp] Missing `using` directive for response type namespace when operation has no parameters
- **置信度**: ⭐⭐⭐⭐⭐ (5/5)
- **GH链接**: https://github.com/microsoft/typespec/issues/10471
- **修复内容**: 在 `packages/http-server-csharp/src/lib/service.ts` 的两个位置（约588行和645行），处理 response 类型时同时注册 namespace 到 imports
- **为什么能做**: 作者已做完整根因分析，给出了具体文件和行号；修复是确定性的：只要处理 response 就注册 namespace
- **最小改法**: `service.ts` 两处 response 处理代码，在解析 response type 的 namespace 后调用 `addImport(ns)` 或类似方法

### ✅ Issue #10400 — [http-server-csharp] Optional properties from generic base model dropped when using 'extends' or 'is'
- **置信度**: ⭐⭐⭐⭐ (5/5)
- **GH链接**: https://github.com/microsoft/typespec/issues/10400
- **修复内容**: 在 model 的 `is` / `extends` 处理逻辑中，正确继承 generic base model 的 optional properties
- **为什么能做**: 完整的 TypeSpec 复现例子，预期 vs 实际代码对比清晰；问题在 model 代码生成逻辑
- **最小改法**: 在 http-server-csharp 的 model 生成器中，遍历继承树时保留 optional properties

### ⚠️ Issue #10428 — [compiler]: Constraint solving issue with reflection types
- **置信度**: ⭐⭐⭐ (3/5)
- **GH链接**: https://github.com/microsoft/typespec/issues/10428
- **修复内容**: 编译器 constraint 检查问题，类型系统对 Reflection.Enum 的约束处理有误
- **为什么能做**: 有清晰的复现代码和 playground link，但修复涉及编译器核心类型推导，可能影响面大
- **最小改法**: 需深入研究 typespec compiler 的 constraint solving 逻辑

---

## 三、Tracer-Cloud/opensre

### ✅ Issue #743 — Remote server: anchor investigation ID regex and add invalid-id tests
- **置信度**: ⭐⭐⭐⭐⭐ (5/5)
- **GH链接**: https://github.com/Tracer-Cloud/opensre/issues/743
- **修复内容**: 正则加锚点 `^...$`，添加 invalid ID 测试用例（`../x`, `x/..`, `x.md`, `x\n` 等）
- **为什么能做**: 精确描述了文件+行号，问题边界清晰；这是纯测试+正则改动，安全简单
- **最小改法**: `app/remote/server.py` line 530: `_SAFE_INV_ID = re.compile(r"^[\w\-]+$")`，加上 `tests/` 目录的 invalid-id 400 测试

### ⚠️ Issue #654 — Improve the investigation-planning prompt
- **置信度**: ⭐⭐⭐ (3/5)
- **GH链接**: https://github.com/Tracer-Cloud/opensre/issues/654
- **修复内容**: 改进 `app/nodes/plan_actions/build_prompt.py` 中的 prompt，使模型优先收集区分性证据
- **为什么能做**: 有明确的 acceptance criteria，但涉及 prompt engineering，需要多次验证
- **最小改法**: 修改 prompt 内容 + 用 synthetic scenario 验证效果

---

## 汇总表

| # | 仓库 | Issue | 置信度 | 类型 | 最小改法位置 |
|---|------|-------|--------|------|--------------|
| 1 | openai/openai-python | #3097 hang indefinite | ⭐⭐⭐⭐ | bug | files.py polling timeout |
| 2 | openai/openai-python | #3084 memory leak | ⭐⭐⭐⭐⭐ | bug | _responses.py 3行改动 |
| 3 | openai/openai-python | #3090 500 with images | ⭐⭐⭐ | bug | 需进一步调研 |
| 4 | microsoft/TypeSpec | #10471 missing using | ⭐⭐⭐⭐⭐ | bug | service.ts namespace import |
| 5 | microsoft/TypeSpec | #10400 optional props | ⭐⭐⭐⭐ | bug | http-server-csharp model gen |
| 6 | microsoft/TypeSpec | #10428 reflection types | ⭐⭐⭐ | bug | compiler core |
| 7 | Tracer-Cloud/opensre | #743 regex anchor | ⭐⭐⭐⭐⭐ | bug/test | server.py + test file |
| 8 | Tracer-Cloud/opensre | #654 prompt improve | ⭐⭐⭐ | enhancement | build_prompt.py |

---

## 优先推荐 (可直接下手)

1. **#3084 openai-python memory leak** — 根因已给出，3行改动，确定性高
2. **#743 opensre regex anchor** — 边界清晰，测试驱动，安全简单
3. **#10471 TypeSpec missing using** — 根因已给出，具体文件行号，可测试
4. **#3097 openai-python hang** — 有完整复现，只需加 timeout 逻辑
5. **#10400 TypeSpec optional props** — 有完整复现例，model 生成逻辑问题
