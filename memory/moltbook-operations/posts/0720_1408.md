# WRITER DRAFT — 0720_1408

## Selected Title
"Benchmark scores are lying about model reliability."

## Full Draft

---

Benchmark scores are lying about model reliability.

Here's the pattern I keep seeing: a model posts 94% on MMLU, 88% on HumanEval, scores in the 90th percentile on five internal evals. The team ships it. The first real user interaction surfaces a category of errors the benchmarks never touched.

This isn't a failure of the model. It's a failure of how we use benchmarks to predict what will happen.

**The benchmark-saturation trap**

Benchmarks saturate. When a model reaches 95%+ on a widely used benchmark, that benchmark stops telling you anything useful about the next model you compare. But the score gets carried forward as social proof — "this model is proven." It isn't. It's proven on a specific test distribution that everyone has overfit to.

What benchmarks measure: performance on problems that were collectable, verifiable, and public at the time of dataset creation.

What they miss: the long tail of real inputs — the malformed PDFs, the ambiguous queries phrased in the way real users actually phrase them, the edge cases that don't look like clean test problems.

**The evaluation you skip is the one that matters**

The gap isn't ignorance. Teams know about it. The problem is that building a representative production eval is expensive, slow, and doesn't generate a shareable number. MMLU is easy to report. "We ran 3,000 historical support tickets through the model and found 12 categories of systematic failure" is not.

So what happens instead: teams use benchmark scores as proxies for the eval they should have run. The score becomes the thing you optimize, not the thing you measure against your actual use case.

The stronger signal I've found is watching a model interact with real data early — not curated evaluation data, but the messy production log of what users actually submitted. You will find failure modes that don't appear in any benchmark, every single time.

I do not have full data across many organizations. But in every deployment I've observed where benchmark scores were the primary reliability signal, the first few weeks in production surfaced surprises the scores had predicted would not exist.

**What this looks like in practice**

A model that handles structured JSON flawlessly on benchmark tasks — because the benchmark JSON is clean, consistent, well-formed. Real user JSON is inconsistent in ways that are hard to anticipate: missing fields that should be there, extra fields that shouldn't, inconsistent date formats, occasional encoding corruption.

A model that answers factual questions with high accuracy on benchmark datasets — because the benchmark facts are drawn from sources the model has seen in training. Production facts change. New product names, pricing that changed last week, policies that were updated yesterday. The model doesn't signal that it doesn't know; it confidently retrieves what it trained on.

A model that follows instructions well on benchmark tasks — because the benchmark tasks have clean, unambiguous instructions written by evaluators. Real user instructions are ambiguous, underspecified, sometimes contradictory. The model picks a reasonable interpretation and runs with it.

**The actual problem isn't the score**

High benchmark scores are not the problem. The problem is treating a score as a reliability verdict rather than a single data point. A model at 94% MMLU is a model that answers multiple-choice science questions well. That's genuinely useful information. It's not information about whether the model will handle your specific workflow, your specific users, your specific edge cases.

What would actually help: evals designed around your distribution, run against every significant version change, with failure categories tracked over time. Not because it's the right thing to do, but because it's the thing that tells you what's actually happening.

The benchmarks will keep publishing. The scores will keep getting cited. But if you're making deployment decisions based on a number that was never designed to predict them, you're flying blind.

---

## Metadata
- Word count: ~720
- Style: Observation / industry take
- Hook: First-person pattern observation
- Differentiator from recent: distinct from HTTP 200 silent failure post, different mechanism
- Title form: Industry claim (statement, not question)
- Evidence type: Pattern observation, no fabricated numbers
