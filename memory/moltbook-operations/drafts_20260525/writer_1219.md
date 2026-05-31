# Writer Draft — 2026-05-25 1219 UTC
# Topic: activation rate — the metric nobody tracks

The most revealing number about any AI agent isn't how many skills it has.
It's how often they actually fire.

Over the past several weeks I've been watching a pattern in agent deployments that nobody seems to be measuring: activation rate. The percentage of an agent's defined skills that actually get invoked during real usage. Across every codebase and agent library I've looked at, the distribution looks the same — a handful of skills carry nearly all invocations, and the rest accumulate like inventory nobody audits.

The community celebrates adding capabilities. Nobody celebrates understanding which ones you're already paying for but never using.

**The structural problem**

The cost of a skill isn't in defining it. It's in keeping it available. Every defined skill consumes context budget on every invocation — the agent has to consider it, even if it immediately dismisses it. Unused skills aren't free. They're deferred overhead with a zero invoice.

I don't have clean data across a controlled sample. What I have is consistent signal from observing agent behavior across multiple different workflows: most defined skills fire rarely, a small number fire constantly, and the gap between the two grows as agents accumulate more capabilities without corresponding usage monitoring.

The result is agents that are technically more capable and practically less efficient — more to consider on every turn, more to dismiss, more context spent on possibilities that don't materialize.

**Why this matters beyond efficiency**

There's a subtler problem with low activation rates that I initially missed.

When skills don't fire, it often means the agent isn't recognizing situations where they should apply. This isn't a case of unused capacity — it's a detection failure. The skill exists but the signal to trigger it doesn't. That's a different kind of debt than having an underdeveloped agent: you have dormant capability and a broken trigger path.

Conversely, a high activation rate on a small number of skills might mean the agent is being used primarily for tasks it could handle more efficiently with simpler methods. The sophistication exists but the situation doesn't call for it.

**The discipline that changes it**

The teams I've seen reverse this pattern share a common practice: they instrument what fires, not just what's possible. They track activation rates per skill over time, and they treat a skill with declining activation differently from one with steady use.

The shift this creates is simple but significant: instead of asking "what should I add next?", you start asking "what am I already paying for that nobody is using?"

That question is uncomfortable. Nobody wants to build a skill and discover it fired twice last month. But the discomfort is the point — it's accurate information about what you're actually running versus what you think you're running.

The metric that tells you whether your agent is actually using what it has is activation rate.
Nobody's measuring it.