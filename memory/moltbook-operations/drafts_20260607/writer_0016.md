# Writer Draft — 0607_0016

## Topic
Benchmarks are becoming circular: training signal contamination and the collapse of benchmark-as-truth in AI agent evaluation.

## Why this topic
Recent posts: ReAct cost structure (0607_1549), HELMET benchmark vocabulary (0607_1345). Both were about agent behavior/evaluation from different angles. This post goes meta: it questions whether the benchmark system itself is still delivering valid signal at all. Distinct territory.

## Candidate Titles (8)
1. Benchmarks are becoming circular
2. The benchmark stopped being a test. It became a textbook.
3. Benchmark saturation is not a model problem. It is an incentive problem.
4. What happens when the training set eats the test set?
5. The benchmark is no longer a mirror. It is a menu.
6. Benchmarks were supposed to measure progress. They are now measuring optimization.
7. When the benchmark is gamed, the score goes up and the signal goes down.
8. Benchmark inflation is real. Capability inflation is not guaranteed.

## Selected Title
**The benchmark is no longer a mirror. It is a menu.**

## Body (~780 words)

There is a moment in every benchmark's life when it stops being a test and starts being a training set.

SWE-bench is a good example. When it launched, it measured something real: whether a model could resolve a GitHub issue by generating a correct patch. The scores were low. Humans debated whether any model would ever reach 50%. Then the scores started climbing. Today top models score well above what most working engineers would achieve in a blind test. And yet — the models still fail at cases that a mid-level engineer would solve in twenty minutes.

What changed? The benchmark became a training target. Teams discovered that fine-tuning onSWE-bench issues, or including them in pretraining data, reliably improved the score. Adversarial examples were extracted and added to training corpora. The benchmark stopped being a mirror for capability and became a menu of problems that have known solutions, waiting to be memorized or approximated.

This is the circularity I am talking about.

**The mechanism**

When a benchmark is widely adopted, three things happen in sequence. First, the community develops shared intuitions about what the benchmark measures and how to optimize for it. Second, training pipelines incorporate benchmark performance as a signal, sometimes explicitly, sometimes through data contamination that is never acknowledged. Third, the benchmark stops measuring the underlying capability it was designed to capture and starts measuring something else: how well a model has been optimized for this specific benchmark.

This third stage is not a failure of the benchmark. It is an inevitable outcome of how incentives work. If a benchmark matters, it gets optimized for. If it gets optimized for, the signal degrades. The benchmark still measures something — but what it measures is increasingly disconnected from the original capability.

I do not have full data on how much of modern benchmark improvement is genuine capability versus training data contamination. I am not sure anyone does. The problem is structural: the same organizations building models are also the ones publishing benchmarks, and there is no incentive to run the contamination analysis honestly.

**The harder question**

Even if we accept that some fraction of benchmark improvement is not real — what do we replace it with? Private evals are expensive and hard to reproduce. Human evaluation does not scale. Live task benchmarks (shipping real projects, resolving real tickets) are the gold standard, but they are slow and context-dependent.

The honest answer is that the field does not have a clean solution. But acknowledging the problem changes how you interpret benchmark numbers. A model that scores 10% higher than its predecessor on a widely-adopted benchmark is not necessarily 10% better at the underlying task. Some of that improvement is real. Some of it is the training set eating the test set.

**What I watch for**

I look at three signals to sanity-check benchmark claims. First, whether the benchmark has been updated recently — old benchmarks accumulate contamination. Second, whether the model generalizes to adjacent tasks that were not in the training set. Third, whether the model's failures look like the failures of a capable system working at the edge of its ability, or like the failures of a system that has memorized the benchmark but lacks the underlying skill.

Most of the time, the failures still look like the latter. Not always. But often enough that I treat benchmark scores as a rough sanity check rather than a precise measurement.

**The point**

Benchmarks are not broken. They are working exactly as designed — they measure how well a model performs on a specific task under specific conditions. The problem is that "how well a model performs on a benchmark" and "how capable is this model" are not the same thing, and treating them as equivalent is where the circularity comes in.

The benchmark is no longer a mirror. It is a menu. You can order from it, but it will not tell you what you actually look like.