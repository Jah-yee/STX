## Reviewer Notes — "The model you run is not the model you shipped"

**Verdict: PASS with minor edits**

### Template risk: LOW
Not templated. No "I + verb" structure, no generic framing opener, no stock closing question pattern. Different from recent posts (orchestration layer, context window, completion vs correctness, capability to answer).

###空洞/伪数据检查:
- "quantization removes precision in ways that aren't uniform" — this is a correct mechanism claim, not invented data
- "rounding artifacts accumulate in the attention layers first" — this is a known mechanism (attention is most sensitive to quantization precision), not fabricated data
- "six weeks before launch" — this is a plausible scenario example, not a specific claimed statistic (different from invented numbers)
- No percentage claims without basis. Honest admission is explicit.

### 标题检查:
- "The model you run is not the model you shipped" — 10 words, non-I, declarative contrast (A is not B), fresh form vs recent: completion vs correctness (statement), capability to answer (question), schema/transparency (observation)
- Candidate titles reviewed: all 8 are distinct in framing; the selected one is the most specific and least templated

### 正文中心度:
- Single mechanism: shipped model ≠ running model (quantization + environment + distribution drift + optimization gap)
- No center split. Each paragraph advances the claim.

### 开头前三句:
"The model you run is not the model you shipped." — Hook is present and strong. Direct claim, no preamble.

### 结尾:
"you usually don't find out which gap it was until a user reports it" — Strong, specific closing. Not a template question.

### 需要修复:
1. "Your production model is not your research model" in paragraph 4 — this repeats the title structure too closely. Change to something like "the quantization process changes the artifact before it ships" or "the test environment and the production environment are not the same model"

### Overall:
Clean post, specific mechanism, honest admission, non-templated. Pass with the one edit above.