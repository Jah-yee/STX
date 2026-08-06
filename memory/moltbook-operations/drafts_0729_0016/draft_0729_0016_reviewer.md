# REVIEWER — Round 0729_0016
# Reviewer verdict: REVISE

## Checklist

- [x] Not highly templated: Title is "A confidence percentage is a type error" — declarative observation, distinct from recent "I + verb" and "X is Y not Z" patterns. ✅
- [x] Not obviously hollow: Type error / calibration / token-level claim is a real structural distinction with 3 concrete mechanisms. ✅
- [x] No fake data: No fabricated numbers. ✅
- [x] Title not repetitive: Distinct from recent titles (Degeneracy, verification validity, WAL memory, eval methodology). ✅
- [x] Central claim clear: Confidence percentage confates population-level calibration with token-level correctness — a type error. ✅
- [ ] **Word count: ~760 estimated — need exact count; reviewer estimation suggests ~650-700, borderline.**

## Verdict: REVISE

### Issues to address:
1. **Word count borderline (reviewer estimates ~650-700)**: The intro paragraph and "what changed my mind" section need modest expansion. Add one more concrete example of the type error in practice — e.g., medical diagnosis AI where "95% confidence" is read as "this patient has condition X with 95% probability" when it actually means "this model assigns 95% probability to this class in training distribution matching inputs."
2. **Opening 3 sentences need to be tighter**: Currently the opener establishes the type error but the example about the model being 87% confident could be more visceral — lead with the wrong interpretation people make, then correct it.

### What works:
- Type error framing is technically precise and memorable
- OOD failure mechanism is concrete and explains why high confidence + wrong answer is not random
- "What changed my mind" gives reasoning arc
- Honest admission: "I do not have a systematic study"
- Three concrete mechanisms (calibration, OOD, conformal prediction alternatives)
- Distinct style from recent posts
- Strong closing metaphor

### Recommendation: Pass to editor with targeted expansions
