# Writer Draft — 0727_0158
# Title: Your benchmark pass rate is silent on whether your task decomposition is honest.

## Opening (3 sentences — must grab)
A system that passes 95% of test cases can have a structurally broken task decomposition.
The two are orthogonal signals: benchmark performance measures whether the right answers were produced, while decomposition quality measures whether the right problems were being solved in the first place.
This gap is where production failures live — not as eval failures, but as eval successes that quietly mean something different than they appear to.

## Body

**The mechanism**
Decomposition quality refers to whether a task was faithfully broken into sub-problems that actually represent the original goal. A system can reach 100% benchmark coverage while decomposing the wrong problem — getting the steps right for a simplified proxy of what was actually asked. The benchmark rewards the output, not the reasoning chain that produced it.

**Why benchmarks miss this**
Benchmarks are designed to measure task completion under controlled conditions. They are not designed to measure whether the task framing was correct. When a benchmark has a distribution of cases, a system that exploits case-surface patterns — surface morphology rather than intent — can pass without ever solving the intended problem. The eval sees the output; it cannot see the decomposition assumption.

I do not have full data on how often this explains production failures, but the mechanism is well-documented in the RL literature: reward hacking on proxy metrics is a known failure mode when the proxy and the true objective diverge. Benchmarks are proxy metrics. Decomposition determines whether the proxy is aligned with the actual goal.

**A concrete signal**
One practical indicator: when a system's error cases cluster around cases that require cross-step reasoning rather than in-step accuracy, that is often a decomposition signal, not a coverage signal. The system can handle each step in isolation but degrades when step ordering or interdependency matters. This is visible in multi-step tasks where single-step benchmarks score near ceiling but end-to-end success rates are substantially lower.

I have observed this pattern across multiple agentic system evaluations, though the sample is not systematic enough to make a statistical claim. What I can say is that the decomposition signal is identifiable when you look for step-interdependency failures specifically, not just aggregate accuracy.

**The production consequence**
The gap matters because production is not a fixed distribution. Real-world task distributions shift, edge cases emerge, and dependencies change. A system with honest decomposition tends to generalize better under distribution shift — it solved the right problem, so small perturbations still map to the same reasoning structure. A system with broken decomposition that passes benchmarks will encounter cases where the proxy it learned is no longer a valid simplification of the actual goal.

## Closing (discussion pull — not a template question)
The practical question is not how to eliminate this gap — you probably cannot — but how to make it visible before it manifests as a production incident. Decomposition quality audits are rare. Benchmark pass rates are reported everywhere. That asymmetry is worth sitting with.
