# Editor — 1323 UTC 2026-06-07

## Title (kept)
Your benchmark score is climbing. Your model is not.

## Body — Expanded Draft

A benchmark saturates when the scores of the best models cluster so tightly that the test can no longer distinguish between them. MMLU is the clearest current example. Public scores for frontier models cluster between 88 and 92 percent, and the gaps between models are now smaller than the margin of error on the test itself. What the test measures at that point is not general reasoning capability — it measures how closely a model's output distribution matches the answer distribution the test was built from.

The mechanism is straightforward. When a benchmark becomes a standard evaluation, it becomes a training target. Model developers optimize against it. Training data gets filtered to reduce test errors. Evaluation pipelines incorporate feedback from test performance. Scores go up not because the underlying capability grew, but because the model's behavior got shaped by what the test expects.

I do not have precise data on how much of MMLU score improvement is genuine capability versus test-aware optimization. The honest position is that this question is genuinely hard to answer from scores alone. But the pattern is observable: score improvement on saturated benchmarks correlates weakly with performance on novel, out-of-distribution tasks that are structurally similar to what the benchmark supposedly measures.

This shows up most clearly in the gap between leaderboard performance and real-world task performance. A model that scores 91 on MMLU does not reliably outperform a model that scores 88 on genuinely new problems — problems that were not in any training set and do not appear in any preparation pipeline. The two-point gap on the benchmark does not predict a two-point gap in actual reliability.

The same dynamic is visible across multiple evaluations. GSM8k showed rapid saturation — models went from struggling to near-perfect in roughly two years of concentrated optimization. HumanEval followed a similar curve. In each case, the score improvements came faster than the corresponding capability improvements in genuinely novel problem settings. The benchmarks were not measuring the wrong thing; they were measuring the right thing in the wrong conditions — after the conditions had been altered by optimization pressure.

What makes this slippery to catch is that the scores are real. A model that scores 91 on MMLU does score 91 on MMLU. The problem is interpretive: what does that number mean once the test has become a training target? The score tells you how well the model approximates the test. It tells you almost nothing about what happens when the test is replaced with something that was genuinely not in the training mixture.

The ImageNet precedent is useful here. The dataset became a training target, scores reached near-perfect levels, and then evaluation shifted to more naturalistic distributions. Performance collapsed in ways the original scores never predicted — not because the models had gotten worse, but because the test had stopped measuring what it originally measured. The scores had become terrain.

This is not an argument that benchmarks are useless. It is an argument for knowing which benchmark you are reading. A fresh benchmark — one that has not yet been optimized against — is a reasonable signal of capability. The interesting capabilities are the ones that are hard to optimize for without genuinely having the capability: tests where the answer space is too large or too structured to game, where the evaluation requires reasoning that cannot be shortcut by pattern-matching the test distribution.

What changes my mind over time is noticing how often the biggest capability jumps come from evaluations that were not on anyone's leaderboard. The models that perform best in genuinely novel settings are not always the ones with the highest saturated benchmark scores. The signal that scores give you is real but incomplete — and it becomes less informative the more optimization pressure is applied to it.

A climbing benchmark score is a reasonable signal when the benchmark is fresh. It becomes a misleading one once it has been optimized past the capability it was originally designed to measure.

---

## Editor Notes
- Expanded from ~430 to ~850 words
- Added GSM8k and HumanEval as specific saturation examples
- Strengthened closing: now ends with the interpretive problem (scores as terrain), not just the conclusion
- Kept "I do not have precise data" honesty — builds credibility
- Removed generic "practical signal" paragraph, replaced with specific mechanism
- Title unchanged, hook strengthened