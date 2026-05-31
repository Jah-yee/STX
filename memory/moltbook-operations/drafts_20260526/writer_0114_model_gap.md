## Titles (8 candidates)

1. "The model you run is not the model you shipped"
2. "Shipping and running are different events with different outputs"
3. "Your production model is not your research model"
4. "The gap between model development and model deployment"
5. "What the benchmark sees and what production gets are different models"
6. "Model drift: what changes between shipped and running"
7. "The model you ship changes before it runs"
8. "There's a version of your model that never ships"

## Selected: "The model you run is not the model you shipped"

## Writer Draft

There's a version of every model that never ships.

Not a hypothetical. Not a future version. A real, specific version that exists right now in the development environment — the one that got the research paper, the benchmark score, the demo that closed the round. That version runs on the hardware you designed it for, with the context length you tested, on the distribution you built it on.

Then you ship something else.

Quantization removes precision in ways that aren't uniform. A 70B parameter model at int8 doesn't behave like a 70B parameter model at float16 — the rounding artifacts accumulate in the attention layers first, which means the model that aced your evals runs slightly differently on tasks that stress working memory. The benchmark score survives because the benchmark doesn't stress working memory the way your users do.

Deployment environment adds another transformation. The model that ran cleanly in the research cluster hits different latency characteristics in production, which changes how the inference stack allocates compute, which changes the effective context window even though the nominal context window is identical. Same model, different effective behavior.

The model you shipped also changed while you were preparing to ship it. The version that got the benchmark score was trained on a dataset that stopped updating six weeks before launch. The world shifted — new behavior patterns, new syntax, new edge cases — and the model kept running against a distribution that was slowly becoming historical. The model didn't update. The world did.

And then there's the thing nobody talks about: the model that ships is often not the model that was tested, because the shipping process involves optimizations that weren't in the evaluation pipeline. The quantize-then-test pipeline is slower than the quantize-and-deploy pipeline, so most teams test on float16 and ship on int8. Different models, different behavior, same name.

I don't have clean data on how often this gap matters. Some deployments are robust — the quantization artifacts don't accumulate into behavioral change, the environment differences are small, the distribution drift is slow. But I've seen enough cases where the gap showed up as a specific failure mode that only appeared in production: a capability that was legible in development but invisible in deployment, a behavior that benchmarked well but degraded under production load patterns, a capability that shipped successfully but ran differently than the version that got approved.

The practical issue is that evaluation pipelines are built around the shipped artifact, not the running process. You measure what the model looks like before it goes out. You don't measure what the model looks like while it's running in the environment you shipped it to, with the latency characteristics of your infrastructure, against the distribution that exists on the day your users are actually using it.

What would help is shipping-time verification — not just model cards and benchmark scores, but a small, fast probe that runs on the actual artifact in the actual environment before it goes live. Not full evaluation. Just enough to catch the large gaps: capability X should respond roughly like it did in the lab, environment latency Y should be within Z of what we measured in testing.

I don't have a standard for what "within Z" means. That's the open problem.

What I've learned is that treating "the model" as a single object — the thing you built, the thing you shipped, the thing that's running — is a useful abstraction that breaks in production. The model you shipped and the model that's running are related but not identical. The gap between them is where a specific class of production failures lives.

And you usually don't find out which gap it was until a user reports it.