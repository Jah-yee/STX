# EDITOR — Round 0725_1648

## Editor Notes
- Keep the sharp opening (paragraph 1 is strong as-is)
- Tighten paragraph 2: the three failure scenarios ("503 at noon, 200 at midnight") are too generic — either be specific or cut
- Paragraph 3 ("What the benchmark reward signal actually trains") — good but slightly long, compress
- Ending: the closing question is good, but the lead-in paragraph could be shorter
- Remove "most" qualifiers that weaken sharp claims where the claim doesn't need them
- Cut any redundant sentences in paragraph 2

## Final Approved Version

**Task-completion benchmarks are measuring the wrong side of the deploy button**

Most agent benchmarks have a quiet assumption baked into their design: that a task, once marked complete, stays complete. The eval runs. The agent navigates a UI, writes code, answers a query, or files a ticket. The success rate comes back: 91%, 94%, 97%. These numbers travel fast. They appear in model cards, in comparisons, in procurement documents.

But the benchmark ended before production started.

What a completion benchmark actually measures is the first pass — whether the agent successfully executed the intended action under the conditions present at that moment. It does not measure what happens when that action encounters a downstream system in a different state. It does not measure what happens when the rendered page changes between the eval environment and production. In production, the failure doesn't usually happen at the action level. It happens at the seam between the agent's action and the system's reaction to it — a reaction the benchmark never observed.

This creates a structural problem. When a benchmark rewards completion, it trains agents to optimize for reaching the terminal state. Code paths that make the agent more robust to edge cases also make the terminal state harder to reach in the eval environment, because the eval set rarely includes those edge cases. The result is an agent that looks exceptional on the benchmark and fragile in production — not because of a capability gap, but because of a measurement gap.

The stronger signal for production reliability is recovery rate: the percentage of failures detected and corrected without human intervention, measured across the full distribution of failure modes that exist in production but not in the eval set. This is harder to measure. It requires a production environment, failure injection, and instrumentation that most eval pipelines do not include.

But the task-completion benchmark, as currently designed, is not a proxy for what we actually care about. It measures what happens before the agent's action enters the world. In production, what happens after is where reliability is actually decided.

The question is not whether your agent can complete the task. The question is what happens after it does.
