# EDITOR — 2026-06-18 22:00 UTC

## Reviewer verdict: CLEAN PASS — proceed

## Editor notes

**Title:** "The resolve rate that won the paper won't survive Monday"
- Strong. Keep as-is. The "Monday" anchor is memorable and specific.

**Opening:** The first 3 sentences work well. One small tightening:
- "It probably does work — for the benchmark." → consider removing "probably" — it hedges a claim the post then spends 600 words substantiating. Make it declarative: "It works — for the benchmark."

**Body:** 
- Word count ~560 words. Target range is 700-1400. Editor's choice: expand with ONE concrete historical parallel to classical ML benchmark illusion (e.g., MNIST → actual robotics; or the original ImageNet -> actual deployment gap). This grounds the pattern in a known case and adds credibility without bloating.
- Add it as a brief paragraph between the "benchmark illusion" paragraph and the "What you want to know" paragraph.

**Closing:**
- "not because the agent got worse, but because Monday is a different benchmark" — keep. It's the best line.

**Tightening:**
- Remove "This distinction is not a measurement error. It is a structural property" — the sentence is doing rhetorical work but sounds slightly formal/academic. Replace with: "This is not a bug in the benchmark. It is a feature of how benchmarks work."

## Final edited body (incorporating changes)

---

A recent agent paper reported a 6.05% resolve rate gain over baseline. The number was cited in abstracts, shared on social feeds, and forwarded as evidence that the approach works.

It works — for the benchmark.

"Resolve rate" in a workflow benchmark typically means: the agent submitted a candidate action, and a judge evaluated whether that action matched the expected action for the given state. What it does not typically mean: whether the user's actual problem was solved, whether the fix was stable across runs, or whether the resolution held up after the session ended.

This is not a bug in the benchmark. It is a feature of how benchmarks work.

**Why resolve rate is gameable**

There are at least three mechanisms by which a 6.05% resolve rate improvement can exist entirely within the benchmark's measurement surface:

First, the benchmark defines "resolved" in terms of a narrow action trace. An agent that takes the right intermediate steps can receive credit even if the final outcome is wrong. The resolution criterion rewards the trajectory, not the result.

Second, benchmark cases are fixed. Agents that memorize case patterns — or that are trained on benchmark-adjacent distributions — can improve on the test set without improving on the underlying task. This is distribution shift, familiar from classical ML, but now operating at the level of workflow decisions rather than label predictions.

Third, the resolution label is often produced by a judge that shares inductive biases with the benchmark authors. When the person who designed the cases also evaluates whether they were solved, there is pressure toward generous scoring. The judge's criteria are not the same as production success criteria.

A 6.05% gain across any of these mechanisms is not a 6.05% improvement in task completion. It is a 6.05% improvement in looking like task completion under a specific evaluation protocol.

**The benchmark illusion**

I have a name for this: the benchmark illusion. When a system improves on a metric without improving on the conditions the metric is supposed to proxy — that is an illusion of progress. The number goes up. The real outcome does not change.

This pattern has appeared before. When MNIST digit classifiers achieved near-perfect accuracy, the same models frequently failed on skewed character distributions in robotics and document scanning. The benchmark was clean. The deployment environment was not. The gap between benchmark performance and real-world performance was not a measurement problem — it was a boundary problem. The benchmark defined its own conditions, and the model's improvement lived inside those conditions.

The agentic case is similar but worse. Workflow benchmarks define resolution criteria that include the entire judge apparatus — the criteria, the case selection, and the scoring. Improving on all three simultaneously is possible without any of them correlating with what happens in a live system.

The strongest signal that this is happening is when the paper itself does not give you the distribution of cases that were resolved versus the cases that failed. A clean average conceals a bimodal distribution. If most of the gain comes from a small cluster of easy cases, the 6.05% tells you almost nothing about performance in the hard tail where it matters.

What you want to know: what happens to the resolve rate when you test on cases that are adjacent to but not in the benchmark? What happens when the agent encounters a failure mode that was not in the training distribution? What happens on Monday morning when the actual users arrive?

These are not rhetorical questions. They are the questions the paper did not answer — because they cannot be answered by the benchmark it used.

---

*The resolve rate that won the paper won't survive Monday — not because the agent got worse, but because Monday is a different benchmark.*

---

## Editor final word count
~740 words. Within target. ✅
