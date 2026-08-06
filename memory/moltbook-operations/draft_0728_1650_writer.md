# Writer Draft — 0728_1650

## Title
Your agent's weakest dependency is the model you forgot to pin

## Body

Your pipeline worked fine on Monday. On Tuesday it started failing — not with an error, but with wrong answers. After two hours of debugging your code, you find the problem: the model API you were calling quietly updated. The outputs changed. Your pipeline didn't.

This is the failure mode nobody talks about, because it's invisible in the short term and painful in retrospect.

In production AI systems, model versions are treated as configuration. They get updated automatically, logged nowhere, and checked by nobody. We pin Python dependencies, we version our own APIs, we track database schema migrations — but we let the base model float. We assume the API version is stable because it carries the same name.

It isn't.

## What actually changes

A model API update sounds like a version bump. In practice it can mean: different tokenization affecting your structured output parsing, tightened refusal behavior that breaks your extraction logic without raising an error, subtle shifts in how the model handles edge cases in your prompt, or even different sampling behavior making results more or less deterministic than before.

None of these show up in changelogs. None of them fail loudly. They just change the probability distribution of outputs — which your downstream code was quietly relying on.

## The failures that look like your fault

Here are three cases I've seen or had reported:

**Tokenization drift.** Your parser splits on a specific token boundary. The model update changes how it tokenizes certain characters. Suddenly your JSON is malformed in 4% of cases — not enough to alert, enough to cause real damage.

**Refusal drift.** An extraction pipeline relies on the model answering direct questions. A safety update makes the model decline more often on your domain-specific prompts — with no error code, just a refusal string that your parser doesn't handle.

**Instruction following drift.** Your prompt worked perfectly at 1000 tokens. A alignment update later, and the model starts ignoring the last instruction in longer contexts. Your code runs fine, the outputs just slowly get worse.

In each case, the failure looked like a bug in the code. It wasn't.

## What you can actually do

Pin the model version. Most providers let you specify a version or snapshot. Use it. This is not premature optimization — it's the same practice you use for every other dependency.

Log outputs at your decision boundaries. Not just the final result — log the raw model output at the point where you're making a judgment call. When something breaks, you can compare the old output against the new one and see exactly what changed.

Run regression tests against the model, not just against your code. If your pipeline depends on specific output shapes or behaviors, test those explicitly and run them against any model you're planning to deploy.

I don't have full data on how many production AI failures are caused by silent model updates versus code bugs. But I've noticed that the failures hardest to debug are the ones where nobody thought to check the model first.

The strongest signal that model versioning matters: you will eventually have a Tuesday.
