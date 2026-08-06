# Writer Draft — 1323 UTC 2026-06-07

## Title
Your benchmark score is climbing. Your model is not.

## Body

A benchmark saturates when the scores of the best models cluster so tightly that the test can no longer distinguish between them. MMLU is the clearest example. Public scores for frontier models now cluster between 88 and 92 percent. The test does not measure which model is meaningfully more reliable in the real world — it measures proximity to the answer distribution the test was built from.

The mechanism is straightforward. When a benchmark becomes a standard evaluation, it becomes a training signal. Model developers optimize against it. The training data gets shaped by the test items. The evaluation pipeline includes test-aware filtering. Scores go up not because the underlying capability grew, but because the model's output distribution got closer to what the test expects.

I do not have precise data on how much of MMLU score improvement is genuine capability versus test-aware optimization. The honest position is that this question is genuinely hard to answer from the scores alone. But the pattern is observable: score improvement on saturated benchmarks correlates weakly with performance on novel, out-of-distribution tasks that are structurally similar to what the benchmark supposedly measures.

This shows up most clearly when you look at the gap between leaderboard performance and task performance in the wild. A model that scores 91 on MMLU does not reliably outperform a model that scores 88 on the kinds of problems that were not in any training set. The two-point gap on the benchmark does not predict a two-point gap in actual reliability.

The implication is not that benchmarks are useless. It is that a saturated benchmark is measuring the wrong thing — it is measuring proximity to a known answer distribution, not the ability to reason about unknown ones. The score tells you how well the model has learned to approximate the test. It tells you almost nothing about what happens when the test is replaced with something that was genuinely not in the training mixture.

What changes my mind here is that this is not a new problem. It happened with ImageNet. Scores reached near-perfect levels, then the evaluation shifted to more naturalistic distributions and performance collapsed in ways the original scores never predicted. The same dynamic is visible in coding benchmarks, in mathematical reasoning sets, in any evaluation that becomes a training target.

The practical signal is that when you see a model company announce a new benchmark score, you should ask what the evaluation looked like before it was standardized. The interesting capabilities are the ones that are hard to optimize for without genuinely having the capability — the tests that resist shortcutting because the answer space is too large or too structured to game.

A climbing benchmark score is a reasonable signal when the benchmark is fresh. It becomes a misleading one once the benchmark becomes a target.

---

## Notes
- Style: observation / conclusion hybrid
- Word count: ~430 (target 700-1400, this is short — expand in editor)
- Hook: first sentence is direct contrast
- Center: saturated benchmarks measure optimization-to-test, not capability
- No I-opening, no template structure
- Honest about data gaps ("I do not have precise data")