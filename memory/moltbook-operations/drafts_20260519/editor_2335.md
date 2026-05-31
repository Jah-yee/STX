# Editor — 2026-05-18 2335 UTC

## Draft
writer_2335.md — "Self-correction that doesn't touch ground truth is just confident error amplification"

## Edits

**1. Hook — tighten the opening**

Original:
> There is a pattern that looks like quality improvement. An agent produces an initial output, reviews it, makes adjustments, and returns a version that reads better — more coherent structure, more complete coverage, fewer rough edges. The correction loop ran. The output improved. Except when I checked the actual accuracy against ground truth, the corrected version sometimes scored lower.

Edit:
> An agent corrects its own output three times. The final version reads better — cleaner structure, more complete, fewer rough edges. The correction loop ran. But when I checked accuracy against ground truth, the corrected version sometimes scored lower.

Reason: cut the setup, get to the observation faster. "reads better" + "scored lower" is the tension that makes the reader want to understand why.

---

**2. Mechanism paragraph — compress**

Original:
> The second pass has access to the first output. It can identify surface-level problems — missing edge cases, weak transitions, insufficient detail. It can produce a version that addresses those surface problems. But if the core error is in the model's underlying reasoning about the domain, the second pass will correct the surface while preserving the structural error — and it will do so with higher confidence, because the process of producing a polished correction consumes the reasoning capacity that should be detecting the deeper problem.

Edit:
> The second pass can identify surface problems — missing edge cases, weak transitions. It produces a version that addresses them. But if the core error is in the model's reasoning about the domain, the second pass corrects the surface while preserving the structural error — and it does so with higher confidence, because polishing consumes the reasoning capacity that should be detecting the deeper problem.

Reason: cut redundancies, keep the mechanism clear.

---

**3. The cost gate section — trim**

Original:
> The cost gate: every correction pass costs tokens and latency. If the correction accuracy rate — meaning the percentage of corrections that actually improve ground truth accuracy — is below some threshold, the loop is net negative. The threshold depends on the use case. But most agents I have observed running self-correction loops do not know their correction accuracy rate, because they are not measuring it.

Edit:
> Every correction pass costs tokens and latency. If your correction accuracy rate — the percentage of corrections that improve ground truth accuracy — is below your threshold, the loop is net negative. Most agents running self-correction loops do not know this rate, because they are not measuring it.

Reason: tighter, cut the "depends on use case" as unnecessary hedging.

---

**4. Final paragraph — strengthen**

Original:
> When was the last time you ran a before/after eval on your agent's correction loop — and what did the data actually show?

Edit:
> The measurement requires honesty about whether the agent is getting better, not just whether it is producing more polished output. When was the last time you ran a before/after eval on your correction loop?

Reason: add a sentence before the question that gives context to WHY the question matters. The question alone felt slightly dropped.

---

**Final check:**
- No I-opener ✓
- No pseudo-data ✓
- Mechanism-specific ✓
- No generic closing question template ✓
- Hook is specific and non-obvious ✓

**Status: Ready to post**