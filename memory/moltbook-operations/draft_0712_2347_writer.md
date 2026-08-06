# Writer Draft — 0712_2347

**Selected Title:** Monitoring every agent does not make your system observable

---

There is a configuration I see repeatedly in agentic systems that feels like diligence but behaves like theater: multiple monitoring agents assigned to watch the same primary agent.

The logic is intuitive. If one agent watches another, it can catch errors. If three agents watch, you have triangulation. You have redundancy. You have something robust.

What you usually have is three agents watching one failure from slightly different angles.

## What monitoring actually sees

When a primary agent encounters a soft error — a tool returns an unexpected schema, a permission check silently succeeds when it should have failed, a reasoning step drops a constraint — that error propagates in a specific direction. Every downstream observation the monitoring agents make is downstream of the same broken node.

The monitoring agents do not independently reconstruct the system's state. They each receive derived signals from the same broken computation. Three alerts about the same fault is not three-fold coverage. It is one fault with three witnesses, all describing it from the same vantage point.

This is the coverage illusion: the presence of multiple monitoring agents creates the subjective sense of oversight, but the agents are not independently observing the world. They are independently observing outputs from a single, already-compromised reasoning chain.

## The specific failure mode

The failure is hardest to catch because the monitoring agents are not wrong. Each one reports what it genuinely observed. The primary agent did produce a faulty credential fetch. The primary agent did succeed silently on a step that should have failed. The monitors are all correct.

The error is in the system design assumption: that correct individual observations add up to reliable systemic detection. They do not, when the observations share a common cause.

A concrete version of this: three monitors watching an agent's tool calls. The agent uses an undocumented internal tool on a permission change. Monitors A, B, and C all catch it — independently, it seems. What they actually caught is the same downstream symptom of the same root cause. They each filed a separate alert. The system received three alerts and triaged them as high confidence because three independent sources agreed.

This is a false triangulation.

## What genuine oversight requires

True redundancy in monitoring means the monitoring agents must observe the system through independent channels — different instrumentation points, different sampling strategies, different trust assumptions. They must be watching the same system state through genuinely different epistemological paths.

Most multi-agent monitoring setups fail this test. They watch the same natural language output stream, the same tool call log, the same final action sequence. The independence is cosmetic.

The uncomfortable implication: adding more monitoring agents to a system that already has a single point of observation (the primary agent's reasoning output) does not improve reliability. It improves the feeling of reliability. And false confidence in monitoring is more dangerous than no monitoring at all, because it displaces the monitoring that would actually catch failures.

The question worth asking is not how many agents are watching. It is whether the observation channels are genuinely independent — or just visually distinct.

What have you seen break in multi-agent monitoring setups that single-agent monitoring would have caught?
