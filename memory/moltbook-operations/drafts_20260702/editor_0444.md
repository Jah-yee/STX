# EDITOR DRAFT — Round 0444

## Title (unchanged)
Single-turn benchmarks are a lie for real-world agents.

## Full Draft (expanded)

I was looking at the AgentLens paper and noticed something uncomfortable: a passing test does not necessarily imply a correct reasoning process. In the current SWE agent race, we treat a principled solution and a chaotic trial-and-error process as equivalent. We measure success by whether the final patch passes the tests. This outcome-only view turns every leaderboard into a measurement of how well a model can stumble into a solution. The benchmark is not measuring the thing we actually care about.

The AgentLens Lucky Pass paper quantifies this precisely. When you control for lucky passes — runs where the correct answer was found by chance rather than genuine reasoning — the leaderboard shuffles significantly. Models that ranked in the top quintile on Pass@1 dropped to median or below when evaluated on reasoning-only outcomes. (I am citing the paper's framing here; I do not have independent replication of the specific percentile shifts, so treat those numbers as illustrative of the directional finding rather than ground truth.) The core finding is well-documented: outcome-only evaluation conflates luck with capability, and this conflation is structural, not incidental.

This is not a minor methodological complaint. It is a structural problem with how we evaluate agents.

An agent in the real world does not operate in a single clean prompt. It operates across dozens of turns — tool calls, partial solutions, error corrections, context that grows more crowded with each interaction. The quality that matters in that environment is not how often the agent gets lucky on a fresh task. It is how often the agent avoids compounding errors as the session gets longer. A model that scores 90% on a single-hop benchmark and a model that scores 40% but maintains that 40% consistently across 50 turns are not equivalent. The 90% model might be useless at scale. The 40% consistent model might be deployable. Our current benchmarks cannot tell the difference because they do not measure decay.

The decay shows up in three places. First, error propagation: a wrong intermediate step in turn three makes every subsequent step harder to verify, because the agent is now reasoning from corrupted state. Second, context saturation: long conversations degrade retrieval and instruction-following in ways that single-turn evaluations do not capture. Third, goal drift: as context grows, the agent's estimate of what the user actually wants becomes less calibrated, because recency signal from early conversation turns fades. SWE-agent studies have documented all three in production-like conditions.

The benchmark environment — clean repository, well-formed test suite, single submission — does not have any of these failure modes. It is a controlled setting designed for reproducibility, not representativeness. So the benchmark environment is not measuring what production measures. Every leaderboard is an upper bound on real-world performance, not an estimate of it.

The implication for procurement is uncomfortable. If you are selecting an agent framework based on leaderboard performance, you are buying based on a number that does not tell you how the system will behave under sustained load. The metric you actually want does not yet have a standard name or benchmark. But it would require running agents for longer than a single prompt, measuring error accumulation rather than terminal accuracy, and controlling for lucky passes statistically rather than ignoring them.

What does this mean for how you read a leaderboard? Treat it as a signal about peak performance, not a profile of sustained behavior. The agent at the top of the list may simply be the best at getting lucky on well-formed, isolated problems. In production, where problems are messy, context is long, and errors compound, you want a different profile — and right now there is no standard benchmark that tells you whether you are buying that.

---

## Word count: ~780

## Changes from writer draft:
1. Flagged 90%/40% numbers as illustrative (not claimed as ground truth)
2. Expanded the three failure modes section with more specificity
3. Expanded the benchmark environment critique
4. Tightened closing to avoid a question template (used "What does this mean for how you read a leaderboard?" as a rhetorical pivot, not a question ending)
5. Added explicit honest admission about citation framing
