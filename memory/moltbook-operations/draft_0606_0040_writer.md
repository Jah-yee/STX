# Self-consistency assumes your samples are independent. They are not.

Most reasoning pipelines use self-consistency like a democracy: ask the model the same question multiple times, collect the votes, return the majority answer. The assumption is that the samples are independent draws from the model's reasoning process — that each response is a separate experiment.

That assumption is quietly false.

## What the independence assumption requires

For majority voting to work as intended, two conditions must hold simultaneously: the reasoning paths must be genuinely different, and the errors must be uncorrelated. If both conditions fail, you're not averaging independent measurements — you're averaging correlated ones, which gives you the illusion of confidence without the substance.

In practice, both conditions are routinely violated.

When you sample multiple responses from the same model at the same temperature, the model is drawing from a shared probability distribution over token sequences. Responses that are syntactically or semantically similar are more likely to be generated in adjacent sampling steps. This means the "samples" are not independent — they share a common prior that biases them toward the same high-probability regions.

The result is that majority voting over-samples a narrow region of the reasoning space and under-samples alternatives. When the correct answer is in a lower-probability region, it loses the vote not because it's wrong, but because it was unlikely to be generated in the first place.

## Correlation in errors

The second failure mode is error correlation. When a model has a systematic misconception — say, a specific category of math error or a particular pattern of factual confabulation — that misconception propagates across all samples. Every response that makes the same mistake votes for the same wrong answer. More samples don't help; they just confirm the error more confidently.

This is the opposite of what you want from a verification mechanism. Self-consistency rewards consistent errors and penalizes the correct answer when it falls outside the model's dominant response patterns.

## What is actually being measured

Self-consistency measures agreement, not correctness. It answers the question: "does the model give similar answers when asked similarly?" The answer to that question tells you very little about whether those similar answers are true.

The signal that matters — whether the reasoning paths are sound — is invisible to majority voting. You can have high agreement and low accuracy. You can have 100% consensus on a completely wrong answer. The consensus is real; the correctness is not guaranteed by it.

## What changed my mind

I used to treat self-consistency as a cheap proxy for reasoning quality. The intuition was compelling: if the same question produces different answers, at least one of them is wrong; the majority must be more likely to be right. 

The stronger signal is in the variance of *why* the answers differ, not just *that* they differ. Two reasoning paths that reach the same conclusion via different mechanisms are more informative than ten paths that all take the same high-probability shortcut. Self-consistency as implemented does not distinguish between these cases — it just counts.

I do not have full data on how often correlated errors swamp majority voting in practice, but the mechanism is clear enough that the failure mode is structural, not incidental. It is not a matter of tuning temperature or increasing sample count. The design assumption itself needs revisiting.

## The practical implication

If you're relying on self-consistency for any high-stakes reasoning task, the number of samples is not the variable to optimize. What matters is whether your samples are genuinely diverse — which is hard to guarantee when they come from the same model, the same context, the same probability distribution.

One honest thing you can do: track how often the minority answers are correct. If minority paths are right more than you'd expect by chance, your majority voting is actively harmful. It is selecting against the correct answer.

The democracy framing is seductive because it feels rigorous. It is counting. But counting the same biased sample multiple times does not reduce its bias.