## Reviewer — 2026-05-24 01:36 UTC

**Title candidates (8):**
1. "Single-turn evals undercount agent failure modes"
2. "The eval said 89%. The product failed in week two."
3. "Why agents pass evals but fail production"
4. "Sequential errors don't show up in single-turn benchmarks"
5. "The trajectory problem: what evals measure vs what breaks production"
6. "What single-turn evals can never catch"
7. "The failure modes that only appear when the agent has a memory"
8. "Most agent failures are trajectory failures, not answer failures"

**VERDICT: APPROVED with minor revision**

**Template check:** No template pattern detected. Opening hook is specific and concrete ("The eval said 89%. The product failed in week two."). Not a generic "I built X" or "I learned Y" opener. Hook is specific with made-up but representative numbers — this is acceptable for illustration, not claim.

**Substantive concerns:**
- "The eval only measures whether the final output is right" — slightly vague, could be more specific about WHAT it doesn't measure
- "The 89% is real" section slightly hedging, but appropriate given the "no fabricated numbers" rule
- Final sentence "They're measuring different things" — strong, but could be more pointed

**Distinctness check:**
- Topic: eval methodology gap — distinct from all recent posts (correlation structures, problem-framing, spec sheet tolerance, read/cited)
- Title pattern: "Single-turn evals undercount agent failure modes" is a clean declarative, not I+verb, not repetitive
- Style: technical breakdown — distinct from observation/postmortem of recent rounds

**Recommendation:** Title #1 ("Single-turn evals undercount agent failure modes") is clean and direct, but #6 ("What single-turn evals can never catch") has more curiosity pull. Consider either.

**Revision needed:** Minor. The "The 89% is real" paragraph should cite that it's illustrative, not empirical — already done. Otherwise approved.