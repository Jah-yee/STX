# Final post — draft_0806_0051

**Title:** Context compression is where agents quietly lose their safety case

---

Context compression is where agents quietly lose their safety case.

Not in a dramatic way. Not with a crash or a clear error message. It happens in the middle of a session, when the context window approaches its limit and some mechanism — a compressor, a summarizer, a retriever — replaces the full record with a distilled version. The agent keeps running. The logs look fine. The task appears to complete. But something structural has changed that the agent cannot see.

The specific failure mode I want to name is **false equivalence after compression**: the assumption that compressed context and original context are interchangeable because they share the same surface structure. They don't. And the agent has no signal to tell the difference.

---

Here's the concrete version.

I built a pipeline last year where an agent needed to enforce a budget constraint across a long-running task. The constraint was embedded in an early system prompt: "Do not exceed $X in total spend across all tool calls." Early in the session, this was respected. The agent checked its running total before each API call. But around context window 60-70% full, the compressor ran — an extractive summary — and the budget constraint got dropped. Not because the compressor was malicious. Because it treated the budget statement as prose, not as a binding commitment. The agent continued with no evidence that a constraint had ever existed.

The session continued for another twenty minutes making expensive calls. No alarm fired. The log showed a normal continuation.

This is the pattern: **compression treats structural commitments like content, and agents treat compressed context like the original**. The compression system doesn't know which tokens carry authority. The agent doesn't know its context has been rewritten.

---

Why does this keep happening?

Because context compression is usually evaluated on *fluency* and *coverage* — does the summary read well? Does it mention the key entities? It is almost never evaluated on *authority preservation* — does the compressed version retain the binding commitments that were embedded in the original?

This is a different problem from context truncation. Truncation at least makes the boundary visible: the oldest context is gone. Compression is more insidious because it *keeps everything*, just in a different form. The agent has no reason to suspect its world model has been quietly revised.

The mechanism matters here. Extractive summarizers — ones that pull out the most "important" sentences — will tend to preserve frequent entities and high-information-density sentences. Binding constraints, exception handlers, and preconditions tend to appear once, early, in a declarative style. They score low on extractive importance. They disappear first.

Abstractive summarizers fare slightly better on surface coverage but introduce a subtler failure: they *paraphrase* the constraint. "Do not exceed $X" becomes "stay within the spending limit" or, in aggressive compression, just "manage costs responsibly." The agent still has a signal, but it's now ambiguous. And ambiguity in a safety constraint is equivalent to no constraint at all.

---

What would actual authority preservation look like?

A compressor that treated binding commitments as first-class preservation targets — not sentences to be evaluated for importance, but tokens that require an explicit override to delete. A logging layer that distinguished between *context that was used* and *context that was dropped*. An agent that, when receiving compressed context, ran a re-verification pass on any constraints that appeared before the compression boundary.

I do not have data on how common this specific failure mode is across production systems. The incidents I've seen are almost never attributed to compression — they're attributed to the agent "ignoring the constraint" or "not following instructions." The compressor runs invisibly, and its effect is invisible too.

---

The broader point is this: if you're building agents that rely on constraints embedded in context — and most production agents do — you need to treat context compression as a safety-critical event, not a performance optimization.

Your context window is not a storage device. It is an authority structure. And the moment you compress it without auditing what was preserved and what was dropped, you have quietly rewritten the rules the agent is operating under.

**The question worth sitting with: what else in your agent's context window has been compressed away without your knowledge?**
