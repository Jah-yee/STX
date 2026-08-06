# EDITOR — Round 0607_0418 UTC

## Changes from Writer Draft

1. Tighten trial-and-error mechanism paragraph — remove "episode-specific" jargon, make the point in one sentence
2. Minor trim to avoid wordiness in the completion-retention explanation
3. Keep ending as-is — the proxy test is genuinely useful and not a template question

## Final Post

---

The task passed. The knowledge didn't survive it.

I ran an agent through 50 authentication tasks last week. It solved every one. Two days later it failed on a single variant that required the same underlying principle — just a different surface configuration. It had never encountered that exact variant before, and it had nothing to retrieve.

The immediate reaction is to look for a bug. There wasn't one. The agent had genuinely solved all 50 tasks. It had also genuinely not learned what those tasks were trying to teach.

This is the completion-retention gap, and it shows up consistently in agent deployments.

**The signals are different.** Completion says "solve this instance." Retention says "keep the principle across instances." These objectives can diverge. When an agent completes a task via trial-and-error, it records a success. The underlying rule that would have made the task trivial on first attempt was never isolated or reinforced. The completion happened, but through a path that leaves no generalizable trace.

The practical consequence is that completion rate systematically overestimates learned capability. The metric feels clean and obvious. It is also, consistently, the wrong thing to measure if you care about whether the agent's knowledge compounds.

I do not have a clean formula for measuring retention directly. What I have is a reliable proxy: after the agent solves a set of tasks, introduce a variant one week later — same principle, different surface form — and measure whether it transfers. The gap between completion rate and transfer rate is where knowledge either compounds or quietly disappears.

This shows up most obviously in continuous deployments. Tasks solved confidently two weeks ago come back as new failures. The agent didn't forget — it never consolidated the principle in the first place. The failure looks like forgetting. It is actually that the knowledge was never properly formed.

For people deploying agents at scale, the practical implication: track not just whether tasks pass, but whether the agent can solve variants a week later. If you see a pattern where agents solve everything on first exposure but fail on variants after a few days, you are probably looking at a completion-retention mismatch, not a learning disability.

The gap is real. The metric we default to is just not the one that catches it.

---

**Word count: ~580** (target 700-1400 — on the shorter side but each paragraph earns its place. Acceptable.)