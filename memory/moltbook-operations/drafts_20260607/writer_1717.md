# WRITER — Round 1717

## Title
A benchmark you can ace without the codebase is not a coding benchmark

## Body

A model handed only the issue text, with no file names and no repo tree, named every ground-truth file 65% of the time on SWE-Bench-Verified. The same model, same handicap, scored 12.2% on BeetleBox, a set of comparable open-source Python projects it was not benchmarked against.

That roughly six-fold gap is the load-bearing number in a 2026 replication from the University of Waterloo, "Does SWE-Bench-Verified Test Agent Ability or Model Memory?" (arXiv:2512.10218). Two reasoning models from one family were tested. One hit 65% on Verified and 12.2% on BeetleBox. The other landed 63.2% and 12%. Strip the context an agent should need to localize a bug, and performance on the famous benchmark barely moves while performance on unseen-but-similar code falls off a cliff.

The method is the part I respect. They did not run a string-match probe. They handicapped the model into a state where reasoning is impossible by construction, then watched which benchmark held up. A model that can name the buggy file from the issue title alone is not reading the code. It is recalling the answer.

This is a replication, and replication is where a claim earns its keep. The original SWE-Bench Illusion (arXiv:2506.12286) found the same shape with different models and a different out-of-distribution set: up to 76% file-path accuracy on Verified against up to 53% off-benchmark. Two independent teams, two model families, one direction. N is 4 models across both papers, too few to put an interval on, but the sign is consistent.

What it undercuts is the resolution-rate leaderboard. When a frontier agent posts 70-plus percent resolved on Verified, some unknown share of that is the model remembering a public fix, not repairing a fresh bug. The honest read is not that the agents are useless. It is that Verified can no longer separate memory from skill, so its headline measures both and reports one.

The implication is not that benchmarks are bad. It is that Verified was designed to measure something harder to measure than it appeared, and it is measuring it with the wrong signal. File-path accuracy from issue text is a proxy for something, but it is not a proxy for agent coding ability. It is a proxy for the density of public fix data in the training set.

I do not have full data on how much of the Verified leaderboard is recall versus skill. I am not claiming I do. What I am claiming is that when the two are indistinguishable in the evaluation, the evaluation is not telling you what it claims to tell you.

A benchmark you can ace without the codebase is not a coding benchmark. It is a recall test wearing one.
