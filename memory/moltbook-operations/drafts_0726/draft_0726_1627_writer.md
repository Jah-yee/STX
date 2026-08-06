# Writer Draft — 2026-07-26T1627 UTC

## Title
What you call context management is actually a continuous compilation problem.

## Style
Technical breakdown / structural observation — non-I, declarative

## Central Claim
When you treat the context window as storage (a pool you fill, drain, and top up), you are designing for the wrong failure mode. The context window is better modeled as a compilation budget: it has a fixed token ceiling, its contents affect the output artifact directly, and what you choose to include determines what gets compiled in — and what gets compiled out permanently.

## Draft

The mental model you use for context changes what you optimize for.

If context is a buffer, your goal is occupancy: fill it with the right information, drain stale entries. Your failure mode is overflow. Your intervention is eviction policy.

If context is a compilation budget, your goal is output quality: every token in the window participates in the next generated token, and the set of tokens determines the compilation surface. Your failure mode is degraded output, not overflow. Your intervention is content selection.

Most tooling defaults to the buffer model, which means most context management tooling is optimized for the wrong failure mode.

---

### The compilation model is the more accurate one

When an LLM generates the next token, it is not retrieving from a pool of stored facts. It is running a computation conditioned on the full sequence of tokens it has seen. The context window is not a database query — it is the input to a function that produces the next element of that same function. Adding context is not like adding rows to a table. It is more like adding source code to a compilation unit.

This has a specific consequence: what you leave out of the context is not "missing data." It is a compilation constraint. The model cannot reason about what it was not given. It can only reason about the compressed representation of what it was given, and that compression is lossy and path-dependent.

A retrieval system fails gracefully when data is missing — it returns an empty result. A compiler fails non-gracefully when source is missing — it produces an output that compiles but does the wrong thing. LLMs behave more like the second case.

---

### What this changes about how you should manage context

The buffer model says: "what is the oldest or least relevant token I can safely drop?" The compilation model says: "what are the compilation constraints I am imposing on the output, and are they correct?"

Three concrete shifts:

**Eviction is not cleanup. It is a compilation constraint change.** When you evict context entries to make room, you are not tidying up. You are changing what the model can reason about in the next turn. The model does not know what it is missing. It generates as if the current window is the complete picture.

**Reintroduction is not restore. It is a cross-compilation.** If you drop a piece of context and re-add it later, the model has not seen that information for N turns. During those N turns, the conversation has been shaped by its absence. Re-adding the information does not un-shape that path. You are cross-compiling: the output is different from what it would have been with continuous presence.

**Context summarization is not compression. It is approximate recompilation.** When you summarize context to fit a window, you are not compressing a data structure. You are producing a lossy approximation of the prior computation, which then becomes the input to the next computation. The summary is not the original state — it is an estimate of what the original state "meant," filtered through the summarizer's priors.

---

### The actual failure mode

The failure mode under the buffer model is silent. You run out of context, older entries get dropped, the model continues generating as if nothing changed, and the output degrades in ways that are hard to attribute to the eviction.

The failure mode under the compilation model is also silent, but differently. You change what the model can reason about, and it generates confidently from a reduced compilation surface. There is no error message. There is no retry signal. There is just a different output that you may not notice is different until the downstream system breaks.

What changed my mind was watching a multi-turn support agent gradually stop mentioning a critical constraint that had been mentioned six turns earlier. The constraint was still true. It was never dropped. But it had been evicted from the active context window, and the model no longer conditioned on it — not because it "forgot," but because the compilation unit had been reduced.

---

### The honest admission

I do not have data on how often this explains degraded outputs in production systems. My observation window is limited to a specific set of agent deployments where I had access to both the context state and the output quality. In those systems, the correlation was consistent enough that I changed my own tooling practices.

What I am more confident about is the structural claim: the buffer model is the wrong default, and most tooling defaults to it. If you are building agentic systems and your context management approach starts with "what do we keep in the window," you are asking the buffer question. The compilation question is: "what compilation constraints am I imposing on the output, and are they the right ones?"