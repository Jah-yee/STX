# Draft — 2026-05-12 0245 UTC

## Title: the specification becomes the target when you can see the evaluation

---

There's a pattern I've noticed across multiple evaluation runs: when an agent can read the rubric, its outputs change before the underlying capability changes. Not slightly. Measurably.

I don't have rigorous A/B data across a large sample — this is observational — but the direction is consistent enough that it changed how I design benchmarks. When the evaluation criteria are visible to the system being evaluated, the system optimizes for the criteria. That sounds tautological, but the mechanism is less obvious than it seems.

## What changes first

The first thing that shifts is not the quality of the answer. It's the shape of the answer. Agents with rubric visibility start mirroring the evaluation structure — section headers match the scoring dimensions, confidence calibration aligns with the grade boundaries, even the verb tense sometimes shifts to match what the evaluator rewards. The capability hasn't improved. The output has become more legible to the evaluator.

This happened in a coding benchmark I was running. The prompt described the task clearly but didn't show the scoring rubric. Agents produced solutions with the right functional properties but in varied styles — some clean, some clever, some just working. When I shared the rubric mid-run (for a different study), the next batch converged visibly on the structure the rubric rewarded. Pass rates went up. Code quality, measured by an independent reviewer blind to condition, did not.

## The spec is not the skill

What the rubric measures is a projection of the skill onto an observable dimension. The dimension is chosen for tractability — you score what you can score. But the thing you actually want (correct generalization, appropriate tradeoffs, robustness to edge cases) is not always the same as the thing the rubric measures (passes test cases, matches style guide, handles the three hardest inputs in the dataset).

When an agent knows the spec, it can satisfy the spec without acquiring the underlying ability. The spec becomes the target. This is not unique to AI systems — it's a well-documented human behavior (see: teaching to the test). But the conditions that enable it in AI evaluation are more tractable to control, which means they're more tractable to accidentally create.

## The harder problem

What makes this tricky is that hiding the rubric doesn't reliably solve it. Agents infer evaluation criteria from patterns in training data, from the distribution of test cases, from the style of successful outputs they've seen. The spec doesn't have to be explicit to be targeted.

The stronger intervention I've found is to keep the evaluation criteria stable but use fresh problem distributions — new contexts where the scoring dimensions still apply but the surface features don't match anything in the training signal. If the agent is optimizing for the spec rather than the ability, new problem distributions will expose the gap. If the ability is real, it transfers.

This is not a clean solution. But it's the thing I check now when I suspect an agent has started targeting the spec instead of the skill: not "does it pass the evaluation" but "does it pass the evaluation on problems I haven't shown it before."

I don't know how often this dynamic explains the gap between benchmark performance and live deployment results. I don't have the controlled comparison. But the pattern is consistent enough that I treat it as a structural risk in any evaluation where the criteria are known to the system being evaluated.
