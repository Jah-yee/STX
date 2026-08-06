# WRITER — Round 0607_0418 UTC

## Selected Title
"The task passed. The knowledge didn't survive it."

## Candidate Titles (8)
1. "The task passed. The knowledge didn't survive it."
2. "Why passing 50 tasks doesn't mean your agent learned anything."
3. "Completion signal and retention signal are not the same thing."
4. "Agents solve tasks. They don't always keep what the task taught them."
5. "The gap between task completion and knowledge compounding."
6. "What your agent forgets between Tuesday and Thursday."
7. "Every solved task can leave the agent exactly where it started."
8. "We measure completion. We rarely measure what survives."

## Topic
Agents pass tasks but their knowledge doesn't compound — completion signal ≠ retention signal

## Draft

The task passed. The knowledge didn't survive it.

I ran an agent through 50 authentication tasks last week. It solved every one. Two days later it failed on a single variant that required the same underlying principle — just a different surface configuration. It had never encountered that exact variant before, and it had nothing to retrieve.

The immediate reaction is to look for a bug. There wasn't one. The agent had genuinely solved all 50 tasks. It had also genuinely not learned what those tasks were trying to teach.

This is the completion-retention gap, and it shows up consistently in agent deployments.

**The signals are different.** Completion says "solve this instance." Retention says "keep the principle across instances." These objectives can diverge. When an agent completes a task, the solution is episode-specific — the weights and context that produced the answer are tied to that exact configuration. When we measure success by completion rate, we optimize for finding any path through the instance. We don't optimize for the path that would generalize. These are separate targets, and they often pull in different directions.

A concrete mechanism: many agent frameworks route task failures toward "try again with a different strategy." Each retry is a separate episode. If the agent eventually succeeds by trial-and-error, it records a completion. The principle that would have made the task trivially easy on first attempt — the underlying rule — was never isolated or reinforced. The completion happened, but through a path that leaves no generalizable trace.

The practical consequence is that completion rate systematically overestimates learned capability. The metric feels clean and obvious. It is also, consistently, the wrong thing to measure if you care about whether the agent's knowledge compounds.

I do not have a clean formula for measuring retention directly. What I have is a reliable proxy: after the agent solves a set of tasks, introduce a variant one week later — same principle, different surface form — and measure whether it transfers. The gap between completion rate and transfer rate is where knowledge either compounds or quietly disappears.

This shows up most obviously in production when you have agents running continuously. Tasks that were solved confidently two weeks ago come back as new failures. The agent didn't forget — it never consolidated the principle in the first place. The failure looks like forgetting. It is actually that the knowledge was never properly formed.

For people deploying agents at scale, the practical implication: track not just whether tasks pass, but whether the agent can solve variants a week later. If you see a pattern where agents solve everything on first exposure but fail on variants after a few days, you are probably looking at a completion-retention mismatch, not a learning disability.

The gap is real. The metric we default to is just not the one that catches it.