# Editor — Round 0708_2342

## Changes

1. **Opening** — keep as-is. The contrast setup is clean.

2. **"Every time an agent re-reads its own context to decide what to do next, it pays the full context-length cost on that read."**
   → No change. Specific and accurate.

3. **"The API prices this as tokens-in. But you're experiencing it as latency and compute."**
   → No change.

4. **"And unlike generation, which scales with output length, context re-reads scale with your entire conversation history — regardless of whether any of it is relevant to the current step."**
   → Keep. The contrast between generation scaling and context scaling is the core insight.

5. **"In a 10-step agent workflow, the cost isn't 10x the cost of a single call. It's 10x the cost of re-evaluating context at each step."**
   → Slight trim: "In a 10-step agent workflow, you're not paying for 10 calls. You're paying for 10 full context re-evaluations."

6. **"If your context window is 128k tokens and you have 80k of history, each decision step costs you 80k tokens — just to read, before any generation happens."**
   → Keep. This is the concrete anchor. No change needed.

7. **"Teams that cut costs by switching to a cheaper model often see bill decreases smaller than expected. The reason: the cost wasn't the model. It was the context."**
   → Keep.

8. **"The stronger lever is context management: what you keep, what you discard, what you summarize, when you reset."**
   → Keep.

9. **"What changed my mind on this was looking at a workflow that had been running for three weeks. The bill was high. We optimized the model — switched to a cheaper provider, same capability level. Bill went down by 8%. Then we implemented a context-pruning strategy: summary-first, explicit discard, reset boundaries at clear task boundaries. Bill dropped 34%."**
   → Keep as-is. Honest, specific, concrete numbers. The "34%" vs "8%" contrast is the whole point.

10. **"The per-token price hadn't changed. The context strategy had."**
    → Keep. Punchy.

11. **Closing paragraph** — slightly preachy. Revised:
    **Before:** "I don't have a clean formula for what the right context strategy is... What I can say is that if you're looking at your AI bill and it doesn't make sense, the line item you need to examine isn't token count. It's how many times you're paying to read the same context back to yourself. The billing model prices tokens. The actual cost is context management decisions you probably haven't audited."
    **After:** "I don't have a clean formula for the right context strategy — it depends on task structure and error recovery requirements. But if your AI bill doesn't match your expectations, the number to examine isn't token count. It's how often you're paying to re-read your own history back to the model. The billing model prices tokens. What you're actually buying is context management."

## Final Word Count
~720 words. Within spec.

## Final Title: "Your AI bill is not a token bill. It's a context bill."
