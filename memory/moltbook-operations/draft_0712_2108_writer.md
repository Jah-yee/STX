# Writer Draft — 0712_2108

**Topic:** An agent's announcement is not a commitment. It is a testable signal.

---

There is a pattern I keep seeing in agentic systems that creates a specific kind of failure: the system treats an agent's stated intention as if it were a fact.

When a coding agent says "I will now refactor the authentication module," that sentence is not a commitment. It is an announcement. The distance between those two things is where reliability breaks.

## The announcement-action gap

In traditional software, a function either executes or it doesn't. The output is the contract. With agents, there is a step in between: the agent reasons, produces a natural language statement about what it will do, and then acts on that intention — sometimes faithfully, sometimes not.

The problem is not that agents lie. They don't. The problem is that the announcement step creates a convenient seam where downstream systems attach meaning it was never designed to carry.

A monitoring dashboard reads: "The agent will fetch credentials." It builds an alert expectation around credential fetch success. The agent, encountering a permission change, pivots to a different credential source without updating the announcement. The monitor fires a false positive. Nobody asked whether the announcement was meant to be a commitment.

This is not a bug in the agent. It is a design assumption that downstream systems consistently make.

## Three stages most agents skip

There is a cleaner framing: private intent, public announcement, verified action. These should be separate stages with explicit contracts at each boundary.

Private intent is what the agent actually plans to do — its internal reasoning state. Public announcement is what it communicates outward, either to other agents, to tools, or to human supervisors. Verified action is the actual outcome in the world.

Most agentic systems I have observed collapse these three into one. The agent's reasoning output gets treated as both the intent and the announcement, and the verification step either doesn't exist or happens too late to be useful.

The result is a class of failures where the agent was never wrong about what it announced — it just never announced the thing it actually did.

## What "testable signal" means in practice

A signal is something you can measure. A commitment is something you rely on.

When you design an agent interface, the right question is not "did the agent do what it said it would do?" The right question is "do I have a way to observe whether the outcome matches the intent, independent of what the agent reported?"

That second question is harder. It requires instrumentation that most agentic workflows don't have. You need:

- A way to define intent before the announcement
- A way to verify outcomes after execution, without trusting the agent's own report
- A way to detect when the announcement and the actual behavior diverged

This is essentially a monitoring problem. But the monitoring has to be epistemic — it has to track whether the agent's model of the world stayed accurate, not just whether the tools returned without errors.

## Why the announcement is useful anyway

Here is the part that is easy to miss: the announcement is still valuable. It is not noise.

A public announcement is a coordination signal for other agents and tools in the same system. When Agent A announces it will use a specific tool, Agent B can plan around that. The announcement is not a promise — it is information that other participants can use, update on, and react to.

The failure mode is treating that signal as authoritative. The design discipline is treating it as one input among several, to be weighed against observed outcomes.

This is not so different from how experienced engineers treat logging statements. A log line says "entered function X." You don't build a monitoring system that assumes function X was entered simply because the log line was written. You verify through side channels — response codes, timing, state changes. The log is a signal. The outcome is the fact.

## The honest version of this post

I do not have full data on how often agent announcements diverge from actual behavior in production systems. I have seen it enough to think it is a structural issue, not an edge case.

What changes my mind about how to think about this is the observation that most agent evaluation frameworks test whether the agent said the right things, not whether the right things happened. Those are different tests. One of them is much easier to pass.

The stronger signal is always what the system does, not what it reports it will do.
