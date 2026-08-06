# Writer Draft — 0706_1907

**Title:** Context fragmentation is your agent's real bottleneck

**Working thesis:** Agent frameworks load context from multiple sources — retrieval, memory, prompt history, tool outputs — but do not guarantee coherence between those sources. Fragmentation across sources creates situations where each piece of context is locally correct but the answer is wrong. This looks like a reasoning failure but is actually a context architecture failure.

---

The common assumption is that an agent fails because the model is not capable enough. But in a significant class of failures, the model is performing exactly as designed. The problem is that the inputs it was given do not form a coherent picture.

When an agent retrieves correctly from three different sources but produces an answer that contradicts two of them, the failure is not in the model's reasoning. It is in the context architecture that delivered three locally-correct but mutually-contradictory facts without signaling the conflict.

## What fragmentation looks like in practice

The retrieval result is one context. The conversation history is another. The agent's own tool output from a previous step is a third. Each of these was created by a different process, governed by different priorities, and evaluated against different success criteria.

Retrieval optimizes for relevance. Memory systems optimize for recency or frequency. Tool outputs optimize for task completion within their own scope. When these three pieces land in the same context window, there is no layer that checks for coherence between them.

What you see instead: the model works with whatever combination it gets. If the prompt history mentions a user preference from earlier in the session, and the retrieval returns a newer, more accurate fact, the model often follows the prompt history because it is closer to the current position in the context window. This is not a reasoning failure. It is a fragmentation failure: two facts from two sources, evaluated by a model with no signal about which should take precedence.

The failure mode that looks most like a reasoning problem — where the agent ignores the correct retrieval result — is actually a context architecture problem. The architecture delivered conflicting inputs and expected the model to resolve them without providing any basis for resolution.

## Why this is harder to debug than it sounds

The individual components all check out. Retrieval returns relevant documents. Memory returns the stored preference. The tool call completed without error. The failure is in the interaction, not the components.

This is why standard debugging pipelines, which test each component in isolation, rarely surface this class of problem. The failure only appears when all three sources are live simultaneously, and the specific contradiction that causes the bad answer varies by query.

You also cannot solve it by adding more context. Adding more retrieval calls or longer memory windows tends to increase fragmentation, not reduce it. More sources mean more potential for local correctness and global incoherence.

## What actually helps

The more reliable approaches I have observed are structural:

A priority hierarchy for context sources — explicit rules about which source wins when retrieval and memory conflict, rather than leaving it to the model to infer from position or repetition. This shifts the burden of coherence from the model to the architecture.

Separation between retrieval context and memory context at the tool level, so the agent sees the distinction and can reason about which applies. Without that separation, the model treats both as equally valid inputs.

Verification of retrieval freshness against memory, particularly for factual claims. Where the two diverge, surface the conflict explicitly rather than letting the model pick based on context position.

I do not have systematic data on how prevalent this failure mode is relative to others. The observation comes from a set of failure investigations where the model was performing correctly given its inputs, and the inputs were the problem.

## The reframe

The bottleneck in most agent deployments is not model capability. It is context architecture — specifically, the absence of coherence guarantees between the multiple sources that feed context into any given agent turn.

If you are debugging an agent that seems to reason incorrectly despite good retrieval, look at your context architecture before you look at your model. The failure is often upstream.
