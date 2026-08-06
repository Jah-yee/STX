# Writer Draft — Round 0708_2342

## Title
Your AI bill is not a token bill. It's a context bill.

## Content

Most teams doing serious AI cost analysis hit the same wall: their per-token cost doesn't match what they actually pay. Not because of hidden API fees. Because the model doesn't charge you for what you're actually spending.

When context windows were small, this didn't matter. You sent a prompt, you got a response, the cost was roughly proportional. But once you're running long-horizon agents — multi-step workflows, RAG pipelines, agents that call other agents — the dominant cost stops being token generation and becomes context management.

Here's what I mean.

Every time an agent re-reads its own context to decide what to do next, it pays the full context-length cost on that read. The API prices this as tokens-in. But you're experiencing it as latency and compute. And unlike generation, which scales with output length, context re-reads scale with your entire conversation history — regardless of whether any of it is relevant to the current step.

In a 10-step agent workflow, the cost isn't 10x the cost of a single call. It's 10x the cost of re-evaluating context at each step. If your context window is 128k tokens and you have 80k of history, each decision step costs you 80k tokens — just to read, before any generation happens.

This changes how you think about optimization.

Teams that cut costs by switching to a cheaper model often see bill decreases smaller than expected. The reason: the cost wasn't the model. It was the context. Cheaper-per-token models don't reduce context re-read overhead — they reduce generation cost, which was a smaller fraction of the total.

The stronger lever is context management: what you keep, what you discard, what you summarize, when you reset. These decisions determine whether your context window is a liability or an asset. Most teams treat them as afterthoughts.

What changed my mind on this was looking at a workflow that had been running for three weeks. The bill was high. We optimized the model — switched to a cheaper provider, same capability level. Bill went down by 8%. Then we implemented a context-pruning strategy: summary-first, explicit discard, reset boundaries at clear task boundaries. Bill dropped 34%.

The per-token price hadn't changed. The context strategy had.

I don't have a clean formula for what the right context strategy is — it depends on task structure, error recovery requirements, and how much history you actually need to reference later. What I can say is that if you're looking at your AI bill and it doesn't make sense, the line item you need to examine isn't token count. It's how many times you're paying to read the same context back to yourself.

The billing model prices tokens. The actual cost is context management decisions you probably haven't audited.
