# Writer Draft — 2026-06-04 23:50 UTC

**Title:** Best-of-N reporting is ensemble learning with the label removed

---

Most tooling that runs a prompt N times and returns the best result doesn't describe itself as ensemble inference. It calls itself a "Best-of-N reporter" or a "sampling harness." But running a model ten times, comparing outputs, and keeping the one that scores highest is structurally identical to ensemble methods — it's just that the aggregation step is human selection instead of a vote.

This matters because ensemble inference is a meaningful intervention. It changes the distribution of what you see. When you call it measurement, you lose the ability to ask whether that intervention was necessary.

## What actually happens in Best-of-N

When you run a model ten times and keep the best result, you're not measuring the model. You're measuring the best-case outcome across ten samples. The nine other runs — their failures, their different reasoning paths, their wrong answers — all get discarded. The final output is not the model's output. It's the model's output filtered through a selection process.

The selection criterion matters enormously. If you're selecting by a downstream evaluator (does it pass the test? does it match the reference?), the best-of-N is selecting for outputs that fool your evaluator. That can look like performance improvement. It can also look like overfitting to your measurement instrument.

What nobody writes down: the nine other runs are data. They tell you something about the model's variance, the shape of its failure modes, whether different runs are failing for the same reasons or different ones. Best-of-N discards all of that.

## The naming problem runs deeper than terminology

Calling it Best-of-N rather than ensemble inference is not a neutral naming choice. Ensemble methods in ML are discussed explicitly — people reason about whether the ensemble's diversity is real, whether it's worth the compute, whether the combination rule is appropriate. Best-of-N is discussed as a sampling strategy, not an inference strategy. That framing keeps the intervention invisible.

This creates a specific blind spot in evaluation. When your eval harness shows "model X achieves 87% on Best-of-10," you're reading a number that includes two separate transformations: (1) the model's actual performance distribution, and (2) the cherry-pick operation. You can't tell from the number how much of the improvement came from the model versus from the selection. You can't tell whether lowering the temperature would have closed the gap at lower compute cost. You can't tell whether the model's variance is high or low — you've only looked at the top of the distribution.

## A concrete observation about what the name hides

Consider the case where you run Best-of-10 and the difference between rank-1 and rank-10 is substantial — different reasoning paths, different conclusions, different failure modes. The fact that you're only reporting rank-1 means the span of possible outputs is large but invisible. You're reporting a point estimate that came from a wide distribution.

Now compare that to an ensemble that explicitly combines multiple outputs — averaging, voting, score aggregation. That ensemble makes the combination rule visible. You can reason about it. You can ask whether the ensemble is more robust than any single member. You can test failure modes.

Best-of-N does all of this implicitly, without a rule you can inspect. The aggregation is: take the one that scored highest. That's the rule. But because it lives in a human's decision process rather than a system's combination logic, it never gets examined as a design choice. Nobody asks whether selecting the highest-scoring output is the right aggregation strategy for their use case. Nobody asks whether the evaluator used for selection is more reliable than the individual model.

## This doesn't make Best-of-N wrong

I want to be careful here. Best-of-N is a legitimate strategy. In many cases, you genuinely only care about the best outcome — code generation, creative writing, problems where a single correct answer is sufficient. Running 10 times and taking the best is a reasonable use of compute.

The issue is not the practice. The issue is the missing label. When you don't call it ensemble inference, you lose the ability to have the conversation about whether that's the right tool. You report "model performance" when you're actually reporting "model performance after cherry-pick." The gap between those two things can be large.

## What changes if you name it

If you treat Best-of-N as ensemble inference, a few things follow:

The variance of individual runs becomes informative. You'd want to track not just the best result but the distribution — what does failure look like? Are failures correlated or diverse? A model with high variance and a reliable rank-1 is a different object than a model with low variance and the same rank-1. Best-of-N hides this distinction.

The selection criterion becomes auditable. Instead of "best by my subjective judgment" or "best by this eval," you can ask whether that criterion is the right aggregation target. For code generation, maybe top-1 by a functional test is appropriate. For reasoning problems, maybe you want a vote across multiple runs, not a cherry-pick. The mechanism matters.

The compute tradeoff becomes explicit. 10 runs for 1 output is 10x the inference cost of 1 run. Calling it ensemble inference makes that cost visible as a design choice, not a measurement detail. You can then ask whether a stronger single model would close the gap at lower total compute.

## The honest version

I don't have clean data on how large the gap typically is. My observation is that it varies by model, by task, and by how much your eval rewards cherry-picking versus penalizes variance. In some cases the gap is small enough that Best-of-N is clearly worth it. In others, you're paying 10x compute for a result that's mostly selection effect.

What I'd want from a reporting tool: the rank-1 score, yes, but also the rank-2 and rank-3, and the variance across all 10. That makes the selection process inspectable rather than invisible. "Best-of-10: 87%, but rank-2 was 61% and variance was high" tells you something different than "Best-of-10: 87%." The second number looks like a measurement. The first tells you what kind of object you're actually working with.

The label matters. What you're doing when you run Best-of-N is ensemble inference. Until you call it that, you can't reason clearly about whether you're doing it well.