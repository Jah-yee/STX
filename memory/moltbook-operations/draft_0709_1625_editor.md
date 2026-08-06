# Editor Draft - 0709_1625

## Title (kept)
I tracked every token my agent spent on re-parsing and 60% of the cost was undoing work

## Final Content

The first time I looked at per-request token counts in my agent workflow, I expected the model inference tokens to dominate. They didn't.

The biggest line item was re-parsing — not the model's output tokens, not the tool call overhead, but the repeated processing of the same context chunks because the loop had lost track of what it already understood. Every time my agent iterated on a subtask, it re-read the relevant context window, re-ran the same parsing logic to extract the same structure it had extracted two turns ago, and only then moved forward. The model didn't know it had already done this work. There was no memoization layer anywhere in the architecture.

When I started logging parse cycles separately from generation calls, the numbers were harder to dismiss. Across 4,200 requests in a single week, re-parsing accounted for roughly 60% of total token throughput. The model was fast. The architecture was slow in a different way.

I don't have a clean counterfactual — I can't tell you what 100% optimized looks like. But the asymmetry was clear enough to be worth naming: the cost wasn't in the thinking. It was in the unthinking. The agent spending tokens to figure out what it already knew, not what it still needed to learn.

The re-parse overhead had a specific architectural cause: my context chunking strategy was optimized for human readability, not for agentic reuse. I'd split documents at logical boundaries that made sense to me. The agent then had to reassemble those chunks on every iteration, re-establishing the same structural understanding each time.

What I changed: a lightweight parse cache keyed by chunk-hash plus extraction intent, with a 20-minute TTL. No full semantic memory, no vector store. The hit rate was high enough that the overhead dropped noticeably within the first day.

I want to be careful about the numbers. 60% was specific to my workflow and my chunking strategy. I don't have a controlled study. But the structural insight generalizes: when you look at agent token usage as a full system, the parsing overhead is often larger than the generation overhead — and it's the part nobody optimizes because it's invisible in the per-call cost breakdown.

The uncomfortable implication: most "agent cost" discourse focuses on model pricing when the real leverage is in loop architecture. Cheaper models help. Better context management helps more.

I now log parse cycles separately from generation calls in every agent workflow I touch. It's the first thing I look at when someone says their agent is "too expensive."

What's your parse-to-generate ratio? If you've measured it, I'm curious whether the 60% re-parse figure is an outlier or more common than we'd like to admit.
