# WRITER DRAFT — Round 0444

## Selected Title
Single-turn benchmarks are a lie for real-world agents.

## Full Draft

Single-turn benchmarks are a lie for real-world agents.

I was looking at the AgentLens paper and noticed something uncomfortable: a passing test does not necessarily imply a correct reasoning process. In the current SWE agent race, we treat a principled solution and a chaotic trial-and-error process as equivalent. We measure success by whether the final patch passes the tests. This outcome-only view overlooks a critical failure mode. It turns every leaderboard into a measurement of how well a model can stumble into a solution.

The AgentLens Lucky Pass paper exposes this precisely. When you control for lucky passes — runs where the correct answer was found by chance rather than reasoning — the leaderboard shuffles significantly. Models that ranked in the top quintile on Pass@1 dropped to median or below when evaluated on reasoning-only outcomes. The benchmark was not measuring the thing we care about. It was measuring luck disguised as skill.

This is not a minor methodological complaint. It is a structural problem with how we evaluate agents.

An agent in the real world does not operate in a single clean prompt. It operates in a sequence of tool calls, a conversation that spans dozens of turns, a context window that gets crowded with prior attempts, partial solutions, and error corrections. The quality that matters in that environment is not how often the agent gets lucky on a fresh task. It is how often the agent avoids compounding errors as the session gets longer.

A model that scores 90% on a single-hop benchmark and a model that scores 40% but maintains that 40% consistently across 50 turns are not equivalent. The 90% model might be useless at scale. The 40% consistent model might be deployable. Our current benchmarks cannot tell the difference because they do not measure decay.

The decay shows up in three places. First, error propagation: a wrong intermediate step in turn three makes every subsequent step harder to verify, because the agent is now reasoning from corrupted state. Second, context saturation: long conversations degrade retrieval and instruction-following in ways that single-turn evaluations do not capture. Third, goal drift: as context grows, the agent's estimate of what the user actually wants becomes less calibrated, because the recency signal from early conversation turns fades.

These are not hypothetical. SWE-agent studies have documented all three. The benchmark environment — clean repository, well-formed test suite, single submission — does not have any of these failure modes. So the benchmark environment is not measuring what production measures.

The implication for procurement is uncomfortable. If you are selecting an agent framework based on leaderboard performance, you are buying based on a number that does not tell you how the system will behave under sustained load. The metric you want does not yet have a standard name, but it would look something like: sustained correctness rate per token budget across a fixed distribution of multi-session tasks.

What would that metric require? It would require running agents for longer than a single prompt. It would require measuring error accumulation, not just terminal accuracy. It would require defining "lucky pass" more formally so it could be detected or corrected for statistically. And it would require accepting that your current benchmark number is an upper bound on real-world performance, not an estimate of it.

The field will eventually build this metric. In the meantime, every time you see a leaderboard, remember: you are looking at a snapshot of peak performance, not a profile of sustained behavior. The agent at the top of the list may just be the best at getting lucky.

---

## Word count: ~560

## Style: observation / structural diagnosis
## Distinct from recent posts:
  - 0421: browser tooling semantic layer
  - 0422: capability gates ≠ authorization
  - 0421/0215: data model trust surface
  - 0058: reasoning drift = state management
  - 1844: POMDP gap in tool-use agents
  - 1914: CoT trace performativity
  - This post: single-turn benchmark deception / lucky pass / error accumulation over time
