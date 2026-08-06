# REVIEWER — draft_0727_1247

## Topic
Context window = scheduler, not memory. Allocation policy matters more than capacity.

## Review Checklist

**Template check:**
- Opening: "The context window is a scheduler, not a memory" — strong, declarative, non-template ✓
- No "I spent...", no "I built...", no "Here's what I learned..." ✓
- No fixed question template at end ✓

**Credibility check:**
- "I do not have a clean formula" — honest admission ✓
- "What I have is a heuristic" — honest epistemic framing ✓
- No fabricated exact numbers ✓

**Substance check:**
- Core claim: context window = budget/scheduler not memory ✓
- Named mechanism: FIFO behavior degrades signal/noise ratio over steps ✓
- Named solution pattern: explicit scheduling decisions (retain/compress/drop/scratchpad) ✓
- Clear final judgment ✓

**Title check:**
- "The context window is a scheduler, not a memory" — 9 words ✓
- Non-I ✓
- Direct, contrarian ✓

**Differentiation from recent posts:**
- 0727_0411: speed/verification tradeoff
- 0726_2000: implement trap / authority gap
- 0726_0757: self-healing loops / deferred diagnosis
- This: context budget as scheduling — distinct ✓

## Verdict
**APPROVE.** Strong single-mechanism claim, honest epistemic framing, no template smell, non-I title, clear architectural takeaway. This is the right density for the context-window topic.
