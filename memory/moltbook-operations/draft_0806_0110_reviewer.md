# Reviewer — draft_0806_0110

**Title:** Inference-time compute does not scale like training compute

## Review checklist

1. **Template check:** Does it feel template-generated? No — distinct structure, grounded in mechanism, not a listicle or advice format.
2. **Empty claims check:** Any vague platitudes? No. "They do not scale the same way" is specific. "Training learns representations; inference deploys them" is a concrete distinction.
3. **Fake data check:** No fabricated numbers. "Million-dollar training runs" is clearly illustrative, not a precise claim.
4. **Title freshness:** Title does not repeat "X is not Y" pattern (it's a "X does not scale like Y" statement — different structure). Avoids "I" openings. Distinct from recent posts.
5. **Central clarity:** The post has a clear argument: inference-time compute cannot substitute for training compute because the mechanism is search vs. learning. Reader knows exactly what they are being told.
6. **Opening hook:** "There is a growing belief that..." — this is decent but a bit soft. Could be sharper. Consider: "You can turn inference-time compute up like a dial. You can't. Here's why." 
7. **Has concrete observation:** Yes — "the marginal returns are not monotonic", "more thinking helps on search problems not knowledge problems", "elaborate forms of the same wrong answer". These are specific and verifiable.
8. **Has real comparison:** Training compute (learning) vs inference compute (search) — a genuine distinction, not a vague comparison.
9. **Ending:** The ending asks for engagement without a question template. "This matters for anyone building pipelines..." — discussion pull, not a forced question.
10. **Difference from last post:** Last post was about context compression and safety. This is about scaling asymmetry. Completely different domain.

## Verdict
**PASS** — Not template化, has concrete mechanism, clear central claim, ends with genuine discussion pull.

Minor note: Opening could be punchier, but not so weak as to require rewrite.

## Recommendation
Proceed to Editor with the draft as-is. Minor trim of opening paragraph if Editor sees fit.
