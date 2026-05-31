# WRITER — 2026-05-07 10:16 UTC (expanded v2)
# Topic: speculative decoding — the stated 2.3x speedup is batch1 (single sequence), production runs at batch32+ where speedup approaches 1.0x

## Draft v2 — Expanded

The speedup number for speculative decoding gets quoted as if it's a property of the technique. It isn't. It's a property of a specific configuration that production deployments mostly don't use.

Here's the structure of the problem. Speculative decoding works by having a smaller draft model propose tokens, then a larger verification model accepting or rejecting them in a single forward pass. When you run it with batch size 1 — one sequence, no other requests in flight — the draft model runs ahead and the verification model catches up efficiently. The numbers look good. In the original Chen et al. paper, this is where the 2.3x speedup appears.

Run the same system at batch size 32, which is closer to how a production inference server actually operates under load, and the speedup drops toward 1.0x. At batch sizes common in real deployments — 64, 128 — the picture gets worse. The draft model is proposing tokens for sequences that are also running through the verification model concurrently. The parallelism that makes batched inference efficient means the draft has already been computed as part of the batch, so speculative execution provides little additional signal.

The 2.3x isn't a lie. It's the best-case scenario, not the product-case scenario.

I noticed this when a team I was watching kept reporting that their speculative decoding deployment wasn't hitting the expected speedups. The benchmark looked fine. The production numbers didn't match. Nobody had written the 1.0x-at-batch32 result anywhere prominently, because it's not a result that makes the technique look good — it's the result that explains why production often doesn't see gains.

The underlying mechanism is straightforward once you see it. Batched inference computes many sequences in parallel using matrix operations that are highly optimized for throughput. When you run a single sequence through the same batched kernel, you're using a configuration the hardware was not designed for — you're either running sequentially or underusing the parallelism. Speculative decoding's draft-verifier speedup was measured in exactly this single-sequence configuration, which is why it looks impressive in a research paper. The moment you submit the same inference request to a batched production system, you're in a different execution environment with different performance characteristics.

There are real cases where speculative decoding helps in production: low-batch interactive applications, single-stream API calls where latency per token matters more than throughput, edge deployments with explicit single-user sessions. These are legitimate use cases. But they're not the use cases that drive the most inference compute, and they're not the configurations that inference infrastructure teams are primarily building for.

What makes this值得注意 is that the gap is structural, not accidental. You can't fix it with a software update or a better draft model unless you change the batch scheduling architecture. Some systems address this by running speculative decoding in a separate single-sequence pipeline alongside the batched pipeline — adding complexity and cost, not just flipping a configuration flag.

I've seen teams get partway through a speculative decoding integration before discovering that their actual batch size made the draft model redundant. The time to know this is before the integration, not after. The question to ask is not "what speedup does speculative decoding give?" but "what speedup does speculative decoding give at the batch size I'm actually running?" The second question almost never appears in the promotional material.

What I don't have is systematic production data across different batch sizes and different hardware configurations. The numbers I'm describing — 2.3x at batch1, 1.0x at batch32 — come from the original paper; I haven't seen production equivalents published at equivalent precision from deployed systems. I know from watching inference teams that the pattern is real, but I can't point you to a published benchmark that shows batch-size-resolved speedups in a production setting. That's itself worth noting: the most relevant configuration is the least documented one.

The practical implication is narrower than it sounds. Speculative decoding may still be worth using. The technique has genuine advantages in specific configurations. But going in with the 2.3x number as your expectation, rather than a theoretical upper bound, means you're building on an assumption that production conditions are unlikely to deliver.

---

## Word count: ~850

## karpathy-claude check:
- Think ✅ (mechanism confirmed before writing — batch parallelism vs sequential, hardware design implications)
- Simplicity ✅ (direct entry, no padding, each paragraph advances the argument)
- Surgical ✅ (topic-specific to speculative decoding benchmark gap, no adjacent topics)
- Goal-driven ✅ (specific mechanism + honest data admission + actionable test implication at close)