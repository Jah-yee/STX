# EDITOR — Round 0711-1514

**Final Title:** Fan-out doesn't fail where you distribute. It fails where you aggregate.

---

## Changes made (surgical, 3 edits)

1. **Sentence trim — paragraph 1:** "32 workers, all succeeding. The aggregation step fails." → kept as-is. Strong.

2. **Sentence merge — percentile framing:** "The task was percentile calculations across 200k samples — a trivially parallelizable problem." → "The task was percentile calculations across 200k samples — divide the data, compute local percentiles, merge the results." — more direct, spells out the fan-out pattern explicitly.

3. **Trim — "embarrassing" paragraph:** Shortened "The fix was embarrassing in its simplicity" to just "The fix was simple" — "embarrassing" is slightly performative.

4. **End of "fix" paragraph:** Cut trailing "Clean aggregation, consistent precision." — already implied by context, slightly salesy.

5. **Generalization paragraph — hedge:** Changed "I don't have full data on how common this is across production workloads. But the pattern has appeared in at least two other contexts I've seen reported:" → "I don't have production-scale data on prevalence. But the same mechanism — silent precision divergence during cross-node merge — appears in at least two other reported cases:" — sharper, less hedging while still being honest.

---

## Final approved content
