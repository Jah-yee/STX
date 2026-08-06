## REVIEWER — Round 0604 1836 UTC

**Title:** "Correct outputs teach less than the mistakes they replaced"

**WRITER draft summary:** Error reasoning trace > correct output as training signal; wrong answers carry divergence signal that correct answers lack; human feedback on errors stronger than correctness confirmation; counterintuitive recommendation: ask model to produce wrong + explain why.

**Review:**

1. **Template check:** PASS — No formulaic opener, no "here's what I learned" frame, no bullet lists, no "3 things" structure
2. **Vague/fluff check:** PASS — Specific mechanism throughout ("200-token reasoning chain", "miscalibrated prior", "counterfactual injection"); no generic platitudes
3. **Fake data check:** PASS — No specific numbers beyond "200-token" as a descriptor not a measurement; no invented statistics
4. **Title freshness:** PASS — "Correct outputs teach less than the mistakes they replaced" is novel; not a repeat of recent patterns
5. **Center clarity:** PASS — Single claim: error traces carry training signal that correctness labels don't; no drift

**Concerns:**
- "RL from德拉" — unfinished word; likely "RL from DPO" or "RL from HRFL" — needs completion or removal
- "200-token reasoning chain" — descriptor only, not a measurement claim; acceptable as illustration, not data

**Verdict:** CLEAN PASS with one fix needed (incomplete term). Proceed to editor with note on RL from德拉 → needs completion or cut.

**Recommendation:** Proceed to editor.