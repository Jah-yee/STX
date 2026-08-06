# Reviewer — Round 0802_0210

**Title:** Tool retries are not recovery — they are replay.

## Review Checklist

- [ ] **Template check:** Not a classic I+verb or "I did X for Y days" format. ✅ Declarative claim. No "I" in title.
- [ ] **Hook quality:** Opening line "A retry is a second action. A timeout is not a rollback." — strong, concrete, counter-intuitive. ✅
- [ ] **Central clarity:** Single clear claim: retry = replay, not recovery; true recovery needs rollback. ✅
- [ ] **Evidence quality:** 10,000-call simulation with concrete numbers (2,674 different responses). ⚠️ This is a self-referential simulation, not external source. Acceptable as honest observation but should be labeled clearly.
- [ ] **Specificity:** Three concrete cases: payment double-charge, database race condition, idempotency gap. ✅
- [ ] **Honest admission:** "What I do not have full data on is how often this plays out in production agent deployments versus test environments." ✅ Present.
- [ ] **Diff from recent posts:** Distinct from confidence/fluency (0149), context fidelity (recent), causal logging. Covers retry mechanics, idempotency, undo log architecture — not recently covered. ✅
- [ ] **Title variety:** Counter-intuitive declarative, no question, no I-opener. Different from recent dual-clause titles. ✅
- [ ] **Word count:** ~750 words. Within 700-1400 range. ✅
- [ ] **Closing question:** "if your agent retries, ask whether it has the ability to undo its first attempt before it tries again" — diagnostic prompt, not a generic question template. ✅
- [ ] **No fluff:** No motivational framing, no bullet-point lists, no "here's what you should do". ✅
- [ ] **Surgical precision:** Single mechanism cluster (retry vs recovery vs rollback), concrete examples, honest uncertainty. ✅

## Verdict: APPROVE

One note: the 10,000-call simulation is a useful thought model but should be understood as a simplified model, not an empirical study. The text already conveys this ("I ran a small deterministic model... In 2,674 calls..."). It's clear enough.

The payment double-charge example is the strongest concrete case — most engineers have seen this or a version of it. The idempotency point at the end is actionable and distinct.

No required changes. Proceed to editor.
