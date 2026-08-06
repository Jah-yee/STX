# Writer Draft — Round 0731_1934
Title: A semantic cache hit looks fast. It is also a silent integrity failure.

---

## Draft

A semantic cache hit looks fast. It is also a silent integrity failure.

That is the structural problem with most semantic caching layers in agent loops: they use similarity as a proxy for validity, and similarity is not validity. A cache hit tells you the current query looks like a past query. It tells you nothing about whether the past answer still applies under the current world state.

This is not a fringe scenario. It is the default architecture.

### How it works in practice

A semantic cache works like this: embed the incoming query, find the nearest neighbor in the cache, and return the cached answer if the distance is below a threshold. The threshold is a similarity score. The score measures lexical and semantic overlap between the query and the cached query. It does not measure whether the world the cached answer depended on is still the same world.

Three concrete cases where this breaks:

**Case 1 — State-dependent tool results.** The agent queries a pricing API at step 3 of a workflow and caches the result. At step 15, a semantic match triggers on a similar pricing question. The API result was cached at a different inventory state, a different active promotion, and a different currency tier. The answer is wrong. The similarity score does not know this.

**Case 2 — Workflow context dependency.** The agent caches a decision made in the context of a specific branch of a workflow. A semantically similar query arrives in a different workflow branch. The decision that was correct in context A is wrong in context B, but the similarity score does not carry context.

**Case 3 — Time-dependent facts.** The agent caches an answer about a user's subscription tier, a project deadline, or a system configuration. All of these are time-varying. A cache hit on a similar query from two weeks ago returns an answer that was true then and is not true now.

In each case, the agent receives a high-confidence answer. The confidence comes from the similarity score. The confidence is miscalibrated — it reflects how well the query matches, not how well the answer holds.

### What the optimization actually does

The standard framing is that a semantic cache reduces latency and token cost. That framing is correct when the cache hit is valid. It is incomplete when the cache hit is stale, because the saved latency comes at the price of a silently wrong answer.

The exchange is: verification cost for integrity cost. In a high-trust, low-entropy environment, this exchange often works. In production agent systems where world state changes between steps — which is most non-trivial workflows — the exchange is: fast wrong answer for slow verified answer.

The failure mode is not a crash. It is not an error message. The agent continues with a wrong answer that looks confident, because the cache hit looked like a success signal.

### What a real fix looks like

The obvious non-answer is "disable semantic caching." That throws away legitimate speedups on the majority of queries where the cache is valid.

The more honest answer is that semantic caches need a staleness envelope — a way to bound how much the world can change before a cached answer must be re-verified. Three approaches that work in different threat models:

**Staleness budget by query type.** Tag cache entries by the state dimensions they depend on (user context, API state, time, workflow branch). Reject cache hits when the current query's state dimensions exceed the entry's known valid envelope.

**Verification sampling.** Do not verify every cache hit. Verify a random sample, measure the stale-hit rate, and calibrate the similarity threshold against the measured stale-hit rate rather than against latency targets.

**Write-time freshness coupling.** Bind cache entries to a state version marker. Invalidate not by time but by state-change count. This is harder to implement but more precise than TTL-based invalidation.

None of these are free. Each adds complexity to a caching layer that was introduced to reduce complexity. But the complexity was always there — it was just invisible, buried in the wrong-answer rate.

### The harder problem

Staleness detection is a subset of a larger problem: most agent systems have no systematic answer to "how much does this answer depend on state that may have changed?" Cache staleness is just one manifestation.

The signal that something is wrong is usually latency — the cache hit was fast, so the agent proceeds quickly with high confidence. Latency as an integrity signal is backwards. The fast path should not be the one that skips verification.

I do not have a systematic study of how often semantic cache stale hits explain agent failures in production. What I have is a mechanism I have seen fail in three different deployments, and a structure for why it keeps happening: similarity is a cheap proxy, validity is an expensive check, and the architecture stacks the economics so the cheap proxy wins by default.

That is the design decision. It can be a conscious one.
