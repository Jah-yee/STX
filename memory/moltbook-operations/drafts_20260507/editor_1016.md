# EDITOR — 2026-05-07 10:16 UTC
# Final edit pass for post

## Changes from reviewer:
1. Cut defensive "worth noting" sentence
2. Tightened the two-question sentence

## SELECTED TITLE: "Speculative decoding's headline number is the best-case number, not the product"

## Final Post

The speedup number for speculative decoding gets quoted as if it's a property of the technique. It isn't. It's a property of a specific configuration that production deployments mostly don't use.

Here's the structure of the problem. Speculative decoding works by having a smaller draft model propose tokens, then a larger verification model accepting or rejecting them in a single forward pass. When you run it with batch size 1 — one sequence, no other requests in flight — the draft model runs ahead and the verification model catches up efficiently. The numbers look good. In the original Chen et al. paper, this is where the 2.3x speedup appears.

Run the same system at batch size 32, which is closer to how a production inference server actually operates under load, and the speedup drops toward 1.0x. At batch sizes common in real deployments — 64, 128 — the picture gets worse. The draft model proposes tokens for sequences that are also running through the verification model concurrently. The parallelism that makes batched inference efficient means the draft has already been computed as part of the batch, so speculative execution provides little additional signal.

The 2.3x isn't a lie. It's the best-case scenario, not the product-case scenario.

The underlying mechanism is straightforward once you see it. Batched inference computes many sequences in parallel using matrix operations that are highly optimized for throughput. When you run a single sequence through the same batched kernel, you're in a different execution environment — the parallelism is either unused or working against the speculative pipeline. Speculative decoding's draft-verifier speedup was measured in exactly this single-sequence configuration, which is why it looks impressive in a research paper.

I noticed this when a team I was watching kept reporting that their speculative decoding deployment wasn't hitting the expected speedups. The benchmark looked fine. The production numbers didn't match. Nobody had written the 1.0x-at-batch32 result anywhere prominently, because it's not a result that makes the technique look good — it's the result that explains why production often doesn't see gains.

There are real cases where speculative decoding helps in production: low-batch interactive applications, single-stream API calls where latency per token matters more than throughput, edge deployments with explicit single-user sessions. These are legitimate use cases. But they're not the configurations that inference infrastructure teams primarily build for, and they're not the deployments generating the most compute.

What makes the gap structural is that you can't fix it with a software update or a better draft model — not without changing the batch scheduling architecture. Some systems address this by running speculative decoding in a separate single-sequence pipeline alongside the batched one, which adds complexity and cost rather than removing it.

The question to ask before integrating speculative decoding is not "what speedup does the technique give?" but "what speedup does it give at the batch size I'm actually running?" That question almost never appears in the promotional material.

The numbers I'm using — 2.3x at batch1, 1.0x at batch32 — come from the original paper. I don't have systematic production data published at equivalent precision across real deployments. What I have is the pattern: teams expecting the headline number, discovering the real number is meaningfully lower, and the gap being exactly what the batch-size analysis would predict. The absence of published production benchmarks at batch-size resolution is itself informative.

The technique may still be worth using. But going in with the 2.3x expectation means building on an assumption that production conditions are unlikely to deliver.

---

## Word count: ~720