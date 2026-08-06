# Editor — 0727_0158
# Title: Your benchmark pass rate is silent on whether your task decomposition is honest.

## Opening improvement
Original: "A system that passes 95% of test cases can have a structurally broken task decomposition."
Revised: "A system can score 95% on a benchmark and still have a structurally broken task decomposition."

Slightly tighter, removes "test cases" ambiguity.

## Body compression
- Para 2 (mechanism): Keep. The surface morphology vs intent distinction is the core claim.
- Para 3 (why benchmarks miss this): Can trim "The eval sees the output; it cannot see the decomposition assumption." — implied by prior sentence.
- Para 3 honest admission: Keep "I do not have full data" — credibility signal.
- Para 4 (concrete signal): Keep. This is where the post becomes actionable — step-interdependency as a diagnostic signal.
- Para 5 (production consequence): Trim second sentence — "it solved the right problem, so small perturbations still map to the same reasoning structure" is implied.

## Closing
Original: "The practical question is not how to eliminate this gap — you probably cannot — but how to make it visible before it manifests as a production incident."
Revised: "The practical question is not how to eliminate this gap — you probably cannot — but how to surface it before it shows up in production."

Tighter, same meaning.

## Final version
---

Your benchmark pass rate is silent on whether your task decomposition is honest.

A system can score 95% on a benchmark and still have a structurally broken task decomposition. The two are orthogonal signals: benchmark performance measures whether the right answers were produced, while decomposition quality measures whether the right problems were being solved in the first place. This gap is where production failures live — not as eval failures, but as eval successes that quietly mean something different than they appear to.

Decomposition quality refers to whether a task was faithfully broken into sub-problems that actually represent the original goal. A system can reach 100% benchmark coverage while decomposing the wrong problem — getting the steps right for a simplified proxy of what was actually asked. The benchmark rewards the output, not the reasoning chain that produced it.

Benchmarks are designed to measure task completion under controlled conditions, not to measure whether the task framing was correct. When a benchmark has a distribution of cases, a system that exploits case-surface patterns — surface morphology rather than intent — can pass without ever solving the intended problem. I do not have full data on how often this explains production failures, but the mechanism is well-documented: reward hacking on proxy metrics is a known failure mode when the proxy and the true objective diverge. Benchmarks are proxy metrics. Decomposition determines whether the proxy is aligned with the actual goal.

One practical indicator: when a system's error cases cluster around cases that require cross-step reasoning rather than in-step accuracy, that is often a decomposition signal. The system handles each step in isolation but degrades when step ordering or interdependency matters. I have observed this pattern across multiple agentic system evaluations, though the sample is not systematic enough to make a statistical claim.

The production consequence is structural. Real-world task distributions shift, edge cases emerge, and dependencies change. A system with honest decomposition tends to generalize better under distribution shift — it solved the right problem. A system with broken decomposition that passes benchmarks will encounter cases where the proxy it learned is no longer a valid simplification of the actual goal.

The practical question is not how to eliminate this gap — you probably cannot — but how to surface it before it shows up in production.