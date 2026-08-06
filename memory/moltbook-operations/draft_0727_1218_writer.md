# WRITER — Round 0727_1218

**Title:** Confidence scores without abstention are telemetry-shaped fiction.

---

When a model outputs a confidence score, it looks like telemetry. Numbers, well-behaved, often between 0 and 1. Easy to log, easy to plot, easy to feed into a dashboard. The problem is that most confidence scores in deployed AI systems don't actually mean what they look like they mean.

The core issue: most models are trained to always produce an answer. They are not trained to produce an "I don't know." Their output layer is a softmax over a fixed vocabulary or label set — the highest-activated class wins, and that activation value gets reported as confidence. But that value is a relative score, not a calibrated probability. The model has never been rewarded for saying "I'm not sure." It has only been rewarded for being right.

What this produces in practice is visible in out-of-distribution settings. When you give a language model a question it has no reliable basis to answer, it does not decline. It generates. And its confidence in that generated answer is often indistinguishable from its confidence on questions it knows cold. The number stays high. The answer is wrong. You were watching telemetry that told you nothing.

This is what I mean by "telemetry-shaped fiction." It has the form of a useful signal. It lacks the function of one.

The framing matters because teams routinely use these scores to gate automation. A confidence threshold of 0.9 means "high enough certainty to proceed without a human." But the threshold is sitting on top of a number that was never a probability to begin with. You are using a softmax argument as a safety gate. The gate does not hold.

What would actual confidence look like? You would need a model that can output a genuine out-of-distribution signal — something that fires when inputs fall outside its training distribution, not just when the internal activation for the top class is high. Some approaches exist: ensemble disagreement, uncertainty via dropout, energy-based scores, or explicit abstention heads. But these add inference cost and are rarely the default. Most production deployments are running the base model with its softmax and calling it a confidence score.

I do not have systematic production data on how often high-confidence wrong answers cause downstream failures. But I have seen enough individual cases to think this is a structural issue, not a marginal one. The distribution of errors does not match the distribution of confidence scores. That is the signal.

The honest framing: if you are automating on confidence thresholds, you need to know what your confidence score actually measures. If it cannot abstain, it probably cannot be trusted at the boundary cases where trust matters most.

What's the alternative that doesn't require retraining? The low-effort version is: treat high confidence as necessary but not sufficient for automation, and always sample a fraction of high-confidence answers for human review. Not because the model is bad, but because the number is lying about what it knows.
