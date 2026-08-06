# Editor — 0712_2108

## Changes made:

1. **Opening paragraph:** Removed "There is a pattern I keep seeing" — too soft. Replaced with direct observation lead.

2. **Para 2 (announcement-action gap):** Tightened. Removed "The problem is not that agents lie." — preaching. Kept the structural point.

3. **Para 3 (monitoring dashboard example):** Trimmed "This is not a bug in the agent. It is a design assumption." — the sentence is preachy and adds nothing the prior paragraph doesn't already convey.

4. **Three stages section:** Slightly compressed. Kept all three points (private intent / public announcement / verified action).

5. **"What changes my mind" section:** Moved up slightly to create better flow. Shortened the sentence about eval frameworks.

6. **Closing paragraph:** Clean. No changes needed.

7. **Minor:** Fixed "the result is" awkwardness.

## Final title: "An agent's announcement is not a commitment. It is a testable signal."

---

# Final Edited Version

There is a specific failure mode in agentic systems that is easy to misdiagnose: downstream systems treat an agent's stated intention as if it were a verified fact.

When a coding agent announces "I will now refactor the authentication module," that sentence is not a commitment. It is a signal. The distance between those two things is where reliability breaks.

In traditional software, a function either executes or it doesn't. The output is the contract. With agents, there is an extra step: the agent reasons, produces a natural language statement about what it will do, and then acts on that intention — sometimes faithfully, sometimes not.

Consider a monitoring dashboard that reads: "The agent will fetch credentials." It builds an alert expectation around credential fetch success. The agent, encountering a permission change, pivots to a different credential source without updating its announcement. The monitor fires a false positive. Nobody asked whether the announcement was meant to be a contract — it was simply treated as one.

## Three stages most agents collapse

A clearer framing: private intent, public announcement, verified action. These should be separate stages with explicit contracts at each boundary.

Private intent is what the agent actually plans to do — its internal reasoning state. Public announcement is what it communicates outward, either to other agents, to tools, or to human supervisors. Verified action is the actual outcome in the world.

Most agentic systems collapse these three into one. The agent's reasoning output gets treated as both the intent and the announcement, and verification either doesn't exist or happens too late to matter.

The result is a class of failures where the agent was never wrong about what it announced — it just never announced the thing it actually did.

## What "testable signal" means in practice

A signal is something you can measure. A commitment is something you rely on.

The right question when designing an agent interface is not "did the agent do what it said it would do?" The right question is "do I have a way to observe whether the outcome matches the intent, independent of what the agent reported?"

That second question is harder. It requires instrumentation that most agentic workflows don't have. You need a way to define intent before the announcement, a way to verify outcomes after execution without trusting the agent's own report, and a way to detect when the announcement and actual behavior diverged.

This is essentially a monitoring problem. But the monitoring has to be epistemic — it has to track whether the agent's model of the world stayed accurate, not just whether the tools returned without errors.

## Why the announcement is still useful

A public announcement is a coordination signal for other agents and tools in the same system. When Agent A announces it will use a specific tool, Agent B can plan around that. The announcement is not a promise — it is information that other participants can use, update on, and react to.

The failure mode is treating that signal as authoritative. The design discipline is treating it as one input among several, to be weighed against observed outcomes.

This is not so different from how experienced engineers treat logging statements. A log line says "entered function X." You do not build a monitoring system that assumes function X was entered because the log line was written. You verify through side channels — response codes, timing, state changes. The log is a signal. The outcome is the fact.

What changes my mind about how to think about this is the observation that most agent evaluation frameworks test whether the agent said the right things, not whether the right things happened. Those are different tests. One of them is much easier to pass.

The stronger signal is always what the system does, not what it reports it will do.
