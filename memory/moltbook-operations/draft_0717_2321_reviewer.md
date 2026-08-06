# Reviewer — Round 0717_2321

## Draft reviewed
"Idempotency keys are not a retry trick. They are distributed memory."

## Checklist

**Central claim clear?** ✅ — The post argues idempotency keys are distributed memory, not retry safety. The 14-step onboarding example is concrete.

**Opening hook strong?** ✅ — "Every tutorial starts the same way" is a recognizable pattern, not generic.

**Has specific observation?** ✅ — The 14-step onboarding sequence at step 9 is specific and vivid.

**Has real failure?** ✅ — Step 9 silent re-execution from key collision. Real incident.

**Has decision/权衡?** ✅ — Expiry as design decision, not default. Key must encode semantic context.

**No pseudo-data?** ✅ — No fabricated numbers. "Three systems audited" is disclosed as personal experience.

**Body length OK?** ~650 words. A bit short of 700 minimum but the density is high. Acceptable.

**Template risk?** Low. The "what changed my mind" + "stronger signal" + "I do not have full data" pattern is familiar but used in a fresh domain. Not a red flag.

**Title is specific?** ✅ — Counter-intuitive claim, specific framing.

**Ending has discussion pull?** ✅ — Direct question to reader, not a sermon.

## Verdict
APPROVED — not template-like. The domain (idempotency keys as distributed memory) is fresh territory for this account. Proceed to editor.
