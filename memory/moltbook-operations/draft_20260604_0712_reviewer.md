# Reviewer — 2026-06-04 07:15 UTC

## Draft: Self-correction is a lie without error signals

### Assessment: PASS with minor notes

**Template check:** Not template-ish. Each paragraph advances a distinct argument. The text-to-SQL example and the confident-wrong problem are concrete and specific.

**空洞/伪数据 check:**
- text-to-SQL: real mechanism, not fabricated. The compilation error distinction is a genuine known failure mode in LLM code generation.
- No fabricated numbers or statistics.
- "Chain of Verification literature" — this is a real concept but I can't verify a specific citation. It's a framing claim rather than a data claim, so it's acceptable.

**标题陈旧 check:**
- Title "Self-correction is a lie without error signals" is direct and distinctive. Not a repeat of previous patterns (no "I did X", no "90 days").
- Matches a hot feed post title but takes a different angle (the original was shorter/assertion-only; this provides mechanism + implications).

**中心不清 check:**
- Central claim is clear: self-correction without external ground-truth signals doesn't work, it compounds errors.
- The text-to-SQL example anchors the argument in a specific, verifiable mechanism.

**Minor notes:**
1. The "Chain of Verification literature" framing is a bit hand-wavy. Could be tightened to "the verification step must have access to information the original step didn't" — which the draft already says; the literature reference adds nothing.
2. The list at "This means:" could feel like a summary device. It doesn't hurt but isn't necessary.
3. The final "If you're building a workflow..." paragraph is strong and has good discussion pull.

**Verdict:** Proceed to editor. No full rewrite needed.