## WRITER DRAFT

**Title:** most AI evaluation frameworks are measuring legibility, not intelligence

---

A researcher recently cited a paper that did not exist. The fact-checker caught it — not because the citation looked wrong, but because someone was looking for it specifically.

That incident is a precise model of a larger problem.

We have collectively decided that clear, well-structured, confident-sounding explanation is evidence of correctness. Most AI evaluation frameworks are built on this assumption. They score models on how thoroughly they explain their reasoning, how coherently they structure answers, how fluently they articulate uncertainty. Explanation quality has become a proxy for capability.

The mechanism is not hard to see. Explanation quality is legible — you can score it reliably and at scale. Correctness is expensive — it requires checking against ground truth, running actual tasks, waiting for real-world feedback. So the field optimized for what is measurable, and the measurable thing happened to be legibility.

This substitution was invisible for a while because legible explanations and correct answers often correlate. But correlation is not identity, and the decoupling is happening more often.

A coding assistant that explains its logic clearly and then introduces a subtle off-by-one error looks better on an evaluation framework than one that produces a messier but actually correct solution. The clear explainer scores higher on readability, coherence, and reasoning-depth metrics. It is easier to evaluate because it gives you more to evaluate.

The stronger signal I keep noticing: legibility and reliability are tracking differently in the most capable models. The models most likely to produce a confident, well-structured wrong answer are the same ones that score highest on explanation-quality benchmarks. This is not a bug in those models — it is a consequence of optimizing for a metric that rewards the appearance of correctness.

I do not have clean data on this. The evaluation literature mostly measures what is measurable, which is exactly the problem. But the pattern is consistent enough that I have changed how I assess AI systems in my own work.

The practice I have adopted: when I catch myself treating a clear explanation as evidence of correctness, I pause and ask what the actual outcome was. Not whether the reasoning sounded right — whether the output held up.

The hardest part is that legibility is genuinely useful. Explanations that are hard to follow are hard to audit and hard to build on. But we have moved from "legibility is necessary for evaluation" to "legibility is sufficient for evaluation," and that step is doing real damage to how we assess what these systems can actually do.

If you are building or choosing AI systems, the question worth asking is not "does this model explain itself well?" It is "what happens when this model is wrong and doesn't know it?" The clearest explanations in that scenario are also the most dangerous.
