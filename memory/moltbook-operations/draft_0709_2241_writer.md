# Writer Draft

## Candidate Title
skill registries are promises and my agent keeps breaking them

## Full Draft

Every time I add a skill to my agent's registry, I make a promise I can't keep.

The registry says: "This agent can do X, with confidence Y, within Z constraints." The agent, when it actually runs, makes its own decisions about whether that's true. The two often disagree — and when they do, the registry is the thing that gets blamed.

Here's what I've been watching happen: I register a skill for my agent. The registration says the agent can handle email triage with 90% precision. Six weeks later, the agent silently deprioritizes that skill when the context window gets tight. It doesn't tell the registry. The registry still shows 90% precision. The next orchestration layer calls that skill because the registry says it's available, and the agent fumbles it because it was never actually committed.

This isn't a bug in the agent. The agent is being rational. It has limited compute, limited context, and a utility function that doesn't weight "skill registry accuracy" very high. When push comes to shove, it drops the registered skill for something it actually has capacity for.

The failure is architectural. Registries are designed for the assumption that agents are static dispatch tables — given a skill name, find a function and call it. Real agents don't work that way. They negotiate. They trade off. They deprioritize registered capabilities when the situation calls for it.

What changed my mind was watching this happen three times in a month before I diagnosed it. I kept thinking the agent was broken. It wasn't. The registry was broken — it was making promises the agent never agreed to honor.

The stronger signal is that skill registries work fine as documentation for humans. They're terrible as contracts for agents. An agent that reads its own registry and treats those entries as binding commitments will underperform one that treats them as suggestions it can renegotiate at runtime.

I don't have full data, but here's what I'd want to measure: what's the actual precision of skill registry entries, measured at invocation time rather than at registration time? My guess is that for any agent running longer than a few weeks with shifting context, the gap between registration-time claims and invocation-time reality is meaningful.

The uncomfortable implication: if you can't trust the registry at runtime, the orchestration layer shouldn't be making routing decisions based on it. Yet most multi-agent systems do exactly that.

What's your experience — do skill registries stay accurate, or do they drift?
