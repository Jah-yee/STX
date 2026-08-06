# Editor — 0730_0908

## Changes (surgical, targeted)

**1. Opener — deduplicate "here is" + remove preamble feel**
OLD: "Here is a failure mode I keep running into across different recommendation and search systems: the privacy mechanism and the selection mechanism are optimized independently, and their interaction produces silent errors that neither component was designed to catch."
NEW: "Across several recommendation and search systems, I have seen the same quiet failure: the privacy mechanism and the selection mechanism are optimized independently, and their interaction produces errors that neither was designed to catch."

**2. Noise accumulation paragraph — tighten**
OLD: "The noise is calibrated to the sensitivity of the scoring function — the maximum amount any single training example can change the output. But ranking is not a single-output problem. The ranking of item A relative to item B depends on the difference between their two scores, not on the absolute magnitude of each score. When you add independent noise to two correlated scores, the noise in the difference can be substantially larger than the noise in either individual score, because the noise terms don't cancel — they accumulate."
NEW: "The noise is calibrated to per-record sensitivity. But ranking depends on the difference between scores, not the absolute values. When you add independent noise to two correlated scores, the noise in the difference doesn't cancel — it accumulates. This means the top-k from a noisy-ranked list is not the top-k from the true-ranked list, even with a valid privacy guarantee."

**3. Team ownership paragraph — compress**
OLD: "I have seen this show up most clearly when the two stages are owned by different teams and evaluated independently. Stage one is evaluated on recall... Stage two is evaluated on ranking quality metrics computed on held-out data. But when noisy scores are used in evaluation, the evaluation itself is noisy..."
NEW: "This shows up most clearly when two stages are owned by different teams and evaluated independently — recall for stage one, ranking quality for stage two. When noisy scores contaminate the evaluation itself, you get a double degradation: bad rankings produce weak training signal for the next iteration."

**4. Closing — tighten "what is the practical alternative" paragraph**
OLD: "The uncomfortable part is that the privacy guarantee is technically correct while the practical outcome is a degraded pipeline... What is the practical alternative when you need both privacy and useful rankings? I have not found a clean answer — only a set of design choices that shift where the noise lands."
NEW: "The uncomfortable part: the privacy guarantee is technically correct while the practical outcome is ranking corruption. I have no clean answer — only design choices that shift where the noise lands. Over-generate stage-one candidates so stage two has redundancy. Evaluate on noiseless scores even when production uses noisy ones. Get the privacy team into the ranking evaluation loop."

## Final word count: ~750 words
## Changes: 4 surgical edits, no speculative additions
