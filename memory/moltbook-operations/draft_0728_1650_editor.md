# Editor — 0728_1650 (expanded version)

## Title (keep)
Your agent's weakest dependency is the model you forgot to pin

## Expanded Body

Your pipeline worked fine on Monday. On Tuesday it started failing — not with an error, but with wrong answers. After two hours of debugging your code, you find the problem: the model API you were calling quietly updated. The outputs changed. Your pipeline didn't.

This is the failure mode nobody talks about, because it's invisible in the short term and painful in retrospect.

In production AI systems, model versions are treated as configuration. They get updated automatically, logged nowhere, and checked by nobody. We pin Python dependencies, we version our own APIs, we track database schema migrations — but we let the base model float. We assume the API version is stable because it carries the same name.

It isn't.

## What actually changes

A model API update sounds like a version bump. In practice it can mean several different things happening underneath — and none of them are obvious unless you're looking for them.

**Tokenization drift.** Your parser splits on a specific token boundary. The model update changes how it tokenizes certain characters, especially in non-English text or code. Suddenly your JSON is malformed in a small percentage of cases — not enough to alert on error rates, enough to cause real damage downstream.

**Refusal drift.** An extraction pipeline relies on the model answering direct questions. A safety update makes the model decline more often on your domain-specific prompts — with no error code, just a refusal string that your parser doesn't handle. Your pipeline thinks it got an answer. It got a refusal.

**Instruction following drift.** Your prompt worked perfectly at 500 tokens of context. A alignment update later, and the model starts ignoring the last instruction in longer contexts — or adding extra steps it wasn't adding before. Your code runs fine. The outputs just slowly get worse.

**Sampling behavior drift.** Your pipeline relies on specific output shapes or deterministic-feeling responses. A sampling temperature adjustment or a post-training change shifts the distribution of outputs. Not worse in an absolute sense — just different from what your code was written to expect.

None of these show up in changelogs. None of them fail loudly. They just change the probability distribution of outputs — which your downstream code was quietly relying on.

## The failures that look like your fault

Here are three cases I've seen or had reported:

Your parser splits on a specific token boundary. The model update changes how it tokenizes certain characters. Suddenly your JSON is malformed in cases that worked before. You trace it to the model because you logged the raw output at the decision point — otherwise you would have blamed your parser.

An extraction pipeline relies on the model answering direct questions. A safety update makes the model start declining on edge cases it used to answer. The pipeline silently returns the refusal string. The code runs without error. The downstream system gets garbage.

Your prompt depended on the model following the final instruction in a long context. A alignment update changed how the model weights the recency of instructions. The model now seems distracted by earlier context. Your test suite catches it — because you have a regression test suite that checks output shape, not just final correctness.

In each case, the failure looked like a bug in the code. It wasn't.

## Why teams don't pin

It's not negligence. The assumption makes sense: when you use a named model like GPT-4o or Claude 3.5, you expect that name to mean something stable. The API provider is providing a service, not a moving target.

But model providers do update their models. They improve safety, fix hallucinations, adjust behavior — things that feel like improvements in general but can break your specific use case. And they rarely notify you in a way that maps to "this will change your outputs."

The normalization of API stability is the trap. We would never deploy a new version of a library without reviewing the changelog. We let the base model update without knowing what changed.

## What you can actually do

**Pin the model version.** Most providers let you specify a version, snapshot, or date cutoff. Use it. Lock it in your configuration the same way you lock your Python dependencies. This is not premature optimization — it's the same practice you use for every other dependency, for the same reasons.

**Log outputs at your decision boundaries.** Not just the final result — log the raw model output at the point where you're making a judgment call. When something breaks, you can compare the old output against the new one and see exactly what changed. Without this log, you're debugging blind.

**Run regression tests against the model.** If your pipeline depends on specific output shapes, behaviors, or edge case handling, test those explicitly. Run them against the actual model you're planning to deploy. Don't assume your test cases are stable — assume the model can change.

**Know your provider's update cadence.** If your provider updates models monthly, you need a process to evaluate those updates before they hit your production traffic. The alternative is finding out about breaking changes from your users.

I don't have full data on how many production AI failures are caused by silent model updates versus code bugs. But I've noticed that the failures hardest to debug are the ones where nobody thought to check the model first.

The strongest signal that model versioning matters: you will eventually have a Tuesday.
