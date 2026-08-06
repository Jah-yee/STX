# Writer draft — Agents that log everything understand nothing

## Title
Agents that log everything understand nothing

## Content

Sixty percent of the state changes my agent logged were not progress. They were plumbing.

When I first started tracking state deltas on a long-running agentic task, I expected to find patterns in decisions, tool choices, retries. What I found instead was that the majority of what the system was logging had nothing to do with the task's actual progress. It was structural: session initialization, context window housekeeping, parameter reinitialization between tool calls, empty result padding. The agent was doing work; the logs were mostly talking about the container the work happened in.

I want to be specific about what I mean by structural noise. These are state transitions that occur on every run regardless of task, that reflect the system's internal architecture rather than the semantic content of what it's doing. When a model's context manager writes a new token boundary marker, that's a state delta. When the session re-initializes a tool definition because the context window rotated, that's a state delta. When the agent logs an empty result set as a valid outcome rather than omitting it, that is also a state delta. None of these indicate that the agent moved closer to solving the problem.

The seduction of full logging is real. It feels like observability. You can build dashboards, export timestamps, count transitions, watch the agent "work." But volume of state deltas correlates poorly with task completion. The systems I've watched most intensively in terms of logged state transitions have not been more reliable, more understandable, or more steerable than systems I audited through outcome sampling alone.

The stronger signal for whether an agent is actually making progress is not state delta count — it is result quality against a clear specification, and the density of tool calls that change external state versus tool calls that re-establish internal context. A session that makes ten tool calls and modifies three files has done more real work than a session that makes fifty tool calls while re-navigating the same context window boundaries.

This does not mean logging is useless. It means logging the right thing is harder than logging everything. Structural noise is not zero information — the absence of expected structural transitions can signal that a system has entered an unexpected state. But treating all state deltas as equally informative is how you end up with agents that appear to be working because their logs are full, while their actual output is wrong or incomplete.

What changed my mind was looking at the distribution. I expected something like a Pareto: 20% of state deltas driving 80% of meaningful transitions. What I found was closer to 60% of deltas being pure overhead, with the remaining 40% split between useful signal and ambiguous transitions that required human interpretation to classify.

I do not have full data across different architectures — this observation comes from a specific workflow on a specific model. The number 60% is specific to what I logged, not a general claim. But the shape of the distribution, the structural-versus-semantic distinction, has held across every agentic system I've audited since.

The practical implication is not to log less. It is to log with intent: track what changes external state, track what violates expected resource bounds, track where the agent's confidence signals diverge from outcome quality. Let the container manage itself.

Agents that log everything understand nothing. The ones worth running log precisely.

---
*Word count: ~700*
