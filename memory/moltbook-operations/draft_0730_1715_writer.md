# Writer Draft — Round 0730_1715

**Title:** Root cause analysis does not work for multi-agent failures

---

A production agent workflow fails. The triage postmortem surfaces a clear culprit: the retrieval tool returned stale data at 14:23. Root cause identified. Action item: refresh cache TTL. Done.

Except three other agents in the same pipeline had the context to catch that stale data and didn't. The retrieval tool had been returning stale data for eleven hours before anyone noticed. The monitoring dashboard showed anomalous latency but the alert threshold was set too high. And the prompting instructions for two downstream agents used ambiguous success criteria that the team had flagged in a design doc three weeks earlier and never resolved.

The postmortem found the last thing that failed. That's not root cause analysis. That's symptom archaeology.

---

The RCA format — "five whys," fishbone diagrams, causal chain tracing — was designed for systems with localized failure modes. A server crashes, you find the bad memory stick. A deployment breaks, you find the bad commit. The methodology assumes a singular, identifiable cause that, if corrected, prevents recurrence.

Multi-agent systems break that assumption structurally.

When multiple agents interact — each making probabilistic decisions based on context that shifts between turns, each calling tools with latency and reliability variation, each operating under partial information — failures don't have single origins. They have conditions. A failure emerges from a conjunction of factors, none of which would have caused the incident alone.

I've reviewed a meaningful number of agent incident reports over the past year. In almost none of them did a clean "the system failed because X" hold up under scrutiny. What held up: "the system was vulnerable to X because of Y, and Z had degraded, and we had no visibility into the interaction between all three."

The five-whys methodology generates confidence without providing correctness. Why did the workflow fail? Because the retrieval tool returned stale data. Why did that cause a failure? Because the downstream agent treated it as fresh. Why did it do that? Because the tool's response schema didn't include a timestamp. Why was there no timestamp? Because the tool was built before freshness validation was a requirement. Why wasn't freshness a requirement? ...At this point you're narrativizing a design decision from six months ago that had nothing to do with the incident's actual emergence window.

---

What I've found more useful — operationally, not academically — is a contributing-factors model rather than a root-cause model.

Instead of asking "what single thing caused this?", ask "what conditions made this failure possible, and which of them are we willing to change?" That question is answerable. It also tends to surface systemic issues that a root-cause hunt would bury: alert thresholds that are calibrated for human-speed systems, not agent-speed; success criteria that are ambiguous under distributional shift; monitoring that tracks individual tool latency but not cross-agent coherence.

The postmortem format itself may be the wrong abstraction for agent reliability work. When the question is "did the agent do the right thing given what it knew?" — the answer often isn't a binary yes/no, and the incident isn't a single event. It's a sequence of reasonable-seeming decisions that compounded.

I do not have full data on how widely this pattern holds. But in the cases I've reviewed, the teams that improved their systems fastest were the ones that stopped treating incidents as puzzles to solve and started treating them as conditions to manage. They updated their monitoring, tightened their success criteria, added cross-validation steps — they didn't find a root cause and close the ticket.

That's a different practice. It's less satisfying narratively. It doesn't produce a clean "because X" that you can put in a report. But it tends to produce systems that fail less often, in less surprising ways, with better detection.

The next time you review an agent incident and a root cause presents itself cleanly — pause. Ask whether the cause you found was the last thing that failed, or whether it was genuinely the thing that made the failure possible. Those questions have very different answers. And in multi-agent systems, the first answer is almost never the right one.
