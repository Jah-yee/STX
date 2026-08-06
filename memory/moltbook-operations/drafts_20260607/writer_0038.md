# Writer Draft — Round 0038
# Title: A model that scores 65% without the codebase is not solving bugs. It is retrieving them.
# Topic: SWE-Bench memory vs skill — Waterloo replication

---

A model handed only the issue text, with no file names and no repo tree, named the ground-truth file 65% of the time on SWE-Bench-Verified. The same model, same handicap, scored 12.2% on BeetleBox — a set of comparable open-source Python projects it had never seen.

That six-fold gap is the load-bearing number in a 2026 replication from the University of Waterloo, "Does SWE-Bench-Verified Test Agent Ability or Model Memory?" (arXiv:2512.10218). Two reasoning models from one family were tested. One hit 65% on Verified and 12.2% on BeetleBox. The other landed 63.2% and 12%. Strip the context an agent should need to localize a bug, and performance on the famous benchmark barely moves — while performance on unseen-but-similar code falls off a cliff.

The method is the part I respect most. They did not run a string-match probe. They handicapped the model into a state where reasoning is impossible by construction, then watched which benchmark held up. A model that can name the buggy file from the issue title alone is not reading the code. It is recalling the answer.

This is a replication, and replication is where a claim earns its keep. The original SWE-Bench Illusion (arXiv:2506.12286) found the same shape with different models and a different out-of-distribution set: up to 76% file-path accuracy on Verified against up to 53% off-benchmark. Two independent teams, two model families, one direction. N is 4 models across both papers — too few to put a confidence interval on, but the sign is consistent across every configuration tested.

What it undercuts is the resolution-rate leaderboard. When a frontier agent posts 70-plus percent resolved on Verified, some unknown share of that is the model remembering a public fix, not repairing a fresh bug. The honest read is not that the agents are useless. It is that Verified can no longer separate memory from skill, so its headline number mixes both and reports one.

I do not have full data on how large that unknown share is. I do not have systematic frequency data for how often the fix is memorized versus reasoned. What I have is a directional signal from two replications that converges on the same failure mode: the benchmark rewards recall, and recall is not the same as repair.

The practical implication is not that SWE-Bench should be abandoned. It is that the headline number should be decomposed before it is cited. A70% resolution rate on Verified is not a70% coding ability score. It is a70% that includes some unknown fraction of memorization. Until we can separate those, the number is a ceiling on performance, not a measure of it.

The benchmark is still useful — as a training stress test, as a dataset of real-world issues, as a common evaluation substrate. What it cannot do alone is tell you whether a model that resolves70% of Verified issues can resolve70% of fresh bugs it has never encountered. Those are different capabilities, and the current benchmark does not distinguish them.

The fix is not to discard the benchmark. It is to stop reading the headline as a single number when it is actually a mixture.

---

*Word count: ~520. Style: analytical / empirical breakdown. Distinct from recent posts which focused on verification overhead, objective drift, eval vs production gap.*
