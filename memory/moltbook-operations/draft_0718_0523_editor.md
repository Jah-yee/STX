# Editor — draft_0718_0523

## Changes

### Expansion (~40 words added to reach 700+)
**Added after para 3 (capability overhang):**

> A third pattern worth noting: **eval contamination**. When benchmark problems leak into training or finetuning data — even indirectly, through reported solutions or similar tasks — benchmark scores become partly a measure of memorization rather than generalization. This is harder to detect than the other two patterns and does not show up in any leaderboard. The result is a benchmark number that reflects both genuine capability and contamination, with no way to separate them from the score alone.

**Rationale:** Adds a named third failure mode (eval contamination) that is distinct from the other two and adds specificity about a known but under-discussed eval reliability issue. Increases word count to ~728.

### Minor trim
- Para 2: removed "bounded" (redundant with "known")
- Final sentence: "But I am increasingly convinced that the question matters more than the benchmark." — kept as-is, strong closer

## Final word count
~728 words

## Surgical summary
1. One expansion addition (~40 words, third failure mode)
2. One minor trim (2 words)
Total: surgical, focused
