# WRITER — 2026-07-09 13:39 UTC

## Title: Token count is a vanity metric. The real cost is the attention it wastes.

---

Context length is framed as a capacity problem. How many tokens can you fit? What's your context window? This framing is wrong in a way that costs real money.

Token count is a unit of storage. It tells you how much text you can put in. It tells you nothing about what that text does to the compute path as it travels through a forward pass.

The real cost of context is three nested cascades that nobody prices in.

**First: memory bandwidth.**

When an LLM processes context, it must read every token to compute attention. Not just the relevant ones — every one. This is a property of transformer attention, not a bug. If you have a 128k context and a 4k effective attention window, you are paying for 128k reads to produce 4k of meaningful computation. The bandwidth cost is fixed regardless of how much signal is in the context. Double the context, double the memory traffic, and your throughput drops roughly proportionally. This is documented in profiling literature. It is almost never part of the cost modeling when teams plan a deployment.

**Second: attention degradation.**

Transformers do not weight all tokens equally in practice. The further a token is from the current position in the sequence, the less influence it typically has on the output. Empirical studies of attention patterns show a strong recency bias — the last ~4k tokens of a context dominate the attention scores even when the full context is much larger. This means that adding tokens to the front of your context is not neutral. You are paying the memory bandwidth cost while simultaneously diluting the attention that matters. There is a real sense in which a long context can make your model perform worse on the tasks that depend on earlier tokens, because the attention signal is spread thinner.

I noticed this when running a task that required the model to reference something mentioned in the first message of a long session. With a 4k context window, it consistently recalled the detail. After crossing roughly 60k tokens of accumulated conversation history, it stopped. Not because it couldn't technically access those tokens — the engineering allowed it — but because the effective attention distribution made them unreachable in practice. The model was reading the tokens. It was not processing them.

**Third: retrieval contamination.**

This is the part that gets messy. When you use a retrieval system to pull context for a query, you are implicitly assuming that the retrieved chunks are independent of the query that triggered their retrieval. This assumption breaks down in production. If your retrieval system has any query-dependent bias — and most do, because relevance ranking uses the query — then the act of retrieving context changes what context you get. The longer your retrieval pipeline runs, the more your context is shaped by the queries that triggered it, not by the ground truth the queries were supposed to surface. You end up with a context that is optimized for retrieval signal rather than for task accuracy, and you pay the compute cost without the corresponding benefit.

This shows up in RAG systems that work well in eval and fail in production. The eval queries look like the retrieval was precise. The production queries reveal that the context is being pulled from an increasingly narrow slice of the corpus, because the ranking has quietly adapted to prioritize chunks that look like the queries that previously scored well.

**What the actual signal is.**

Token count is what vendors report because it is easy to measure and easy to bill. It maps directly to storage cost. What it does not map to is the compute cost of reading those tokens at inference time, or the accuracy cost of diluting attention, or the retrieval cost of building context that confirms rather than informs.

The metric I have found more useful is not token count. It is effective context density: the ratio of tokens that demonstrably influence the output to total tokens in the context window. This is harder to measure — it requires running targeted probes on whether the model actually uses information at different positions in the context — but it is a better proxy for what you are actually buying.

In practice, the teams that have the best cost-to-accuracy ratios in long-context tasks are not the ones with the largest context windows. They are the ones who actively prune context aggressively, keep retrieval targets diverse, and measure whether adding tokens actually improves task performance rather than assuming it does.

The context window is not a resource. It is a budget. And most deployments are running a significant deficit they cannot see because nobody is measuring what they are actually spending.
