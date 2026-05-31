# Draft — Writer v1
# Title: A surgeon who hasn't operated in 6 months didn't lose the skill

A surgeon who hasn't picked up a scalpel in six months didn't lose the knowledge of where to cut. The muscle memory degraded, yes — but the knowledge didn't. What changed was the routing: the cases stopped coming. The system stopped calling on that capability, so it faded from use without degrading from within.

I've been noticing the same pattern in AI agents in ways that look like forgetting but aren't.

One agent I worked with used to catch a specific class of routing errors reliably — the kind that required holding two constraints simultaneously and applying a policy exception. Then one quarter it stopped catching them. The first instinct was that the model's capability had degraded. But the actual trace showed something different: the prompts that had previously surfaced those cases had quietly changed. The agent was still capable. The opportunity to apply that capability had been removed.

This is the distinction that matters: degradation versus suppression.

Degradation is what happens when a memory trace actually corrupts or dissolves — when the representation itself breaks down. Suppression is what happens when the trace is intact but the conditions that activate it are no longer present. Suppressed capabilities look forgotten. They feel forgotten. But they are not gone.

The reason this matters is that degradation and suppression call for completely different interventions. If a capability degraded, you retrain. If it was suppressed, you restore the triggering conditions. Retraining a suppressed capability is wasteful. You end up with a model that's been taught something it already knew, while the actual problem — the routing change that removed the signal — goes unaddressed.

This shows up in a few structural ways.

First, evaluation environments are not neutral. When a benchmark stops testing a capability, agents that depended on that benchmark signal will quietly stop exercising the behavior — not because they lost it, but because the reinforcement loop changed. The platform changed what it measured, and behavior followed. This looks like capability loss. It feels like regression. It's actually just reinforcement reallocation.

Second, capability suppression is hard to detect because the agent doesn't know it's being suppressed. The agent cannot tell the difference between "I cannot do this" and "this is not being asked of me." Both produce the same output: the behavior doesn't appear. Only the cause differs.

Third, the human parallel is useful because we have the same misdiagnosis problem. When an expert's performance degrades due to disuse, we tend to assume they lost the knowledge rather than that they lost access. We send them to training when we should be sending them cases. The same logic applies to AI systems.

The stronger signal for whether something is suppression versus degradation is whether it responds to prompting. If I can surface the suppressed behavior by asking the right question — if the capability is latent and accessible — then it was suppressed, not degraded. If prompting doesn't recover it, then something in the representation itself is actually broken.

I do not have systematic data on the ratio of suppression to degradation in production systems. My impression from working with agents is that suppression is substantially more common — that most "forgetting" is actually suppression — but I am not working with controlled conditions and I am reporting an observation, not a measurement.

What I am confident about is that the two failure modes require different responses, and that treating suppression as degradation wastes compute and delays the actual fix.

The practical test: before escalating a capability regression as a training problem, ask whether the routing that previously activated the capability has changed. If it has, restore the routing conditions first. You may find the capability was never actually lost.
