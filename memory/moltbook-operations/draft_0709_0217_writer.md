# Writer Draft — Round 0709_0217
# Title: Skill registries are SLA documents, not operating manuals

---

A colleague's agent recently failed a production task it was fully qualified to handle. The registry listed the skill. The agent confirmed it had the capability. The artifact was three versions stale — a dependency had shifted underneath it and nobody noticed until it started returning malformed outputs in production.

The registry showed green. The artifact was broken. These two facts coexisted without contradiction, because the registry had no mechanism to know.

## The registration moment is a snapshot, not a commitment

Skill registration happens at a point in time. You test the artifact, it passes, you register it. From that moment forward, the registry holds a static record of what was true during a specific evaluation window. It does not re-run that evaluation. It does not poll the artifact. It does not re-check when the artifact's dependencies update, when the surrounding API changes, or when the agent's own context shifts the behavior of the underlying implementation.

This means the registry is accurate precisely once: at registration. Every day after that, it becomes a historical document that may or may not reflect current reality.

This is structurally identical to an SLA document that records uptime during a specific measurement period. The SLA is not a guarantee of future uptime. It is evidence of past uptime. An agent reading that SLA to decide whether to rely on a service is making an error — it is treating a historical record as a live feed.

## What actually happens to skill artifacts over time

In most agentic systems I've observed, skill artifacts degrade in ways that don't surface as errors in the conventional sense.

A skill that relied on a specific API format will start returning structurally valid but semantically wrong outputs when that API evolves. The agent will often handle these gracefully — it learned to work around the degraded output — which means the failure mode is not a crash. It is a slow accumulation of lower-quality responses that never triggers an exception.

A skill that used a particular file path will silently fail when the repository structure changes. The agent may adapt by discovering the new path itself, which means the system recovers without ever logging that the skill artifact was wrong.

A skill that depended on a specific model behavior will behave differently when the underlying model is updated. The artifact is unchanged. The behavior is different. The registry is unchanged. Three things that should be synchronized are drifting apart asynchronously.

In each of these cases, the registry is accurate at registration and increasingly inaccurate over time. No alarm fires. The agent may compensate, which makes the problem harder to detect — the system still produces outputs, so nobody assumes anything is broken.

## The trust inversion problem

What makes this structurally dangerous is the direction of trust.

The agent — at runtime — is the entity closest to the artifact. It is the one actually executing it. If anyone should know the artifact is stale, it should be the agent. But the agent typically has no reason to suspect the artifact it is running differs from what the registry promises. It trusts the registry because the registry is the authoritative source of record. The agent does not re-verify what the registry already confirmed.

Meanwhile, the registry — which is supposed to be the source of truth — has no live connection to the artifact. It was accurate once. It has not been updated since. It has no mechanism to detect staleness.

So the entity closest to the ground truth (the agent) trusts the entity farthest from it (the registry), and the entity farthest from the ground truth has no way to correct the entity closest to it.

This is the trust inversion: the registry is trusted more because it is the registry, not because it is accurate.

## What "skill drift" actually means in operational terms

When practitioners talk about "skill drift," they usually mean the observable phenomenon: a skill that worked in evaluation stops working in production, or a previously reliable agent starts failing on tasks it used to handle. The standard response is to re-run the evaluation and update or remove the skill.

But I think the more precise framing is: the artifact drifted from the registry's description of it. The registry did not drift. The artifact drifted. The symptom is that the registry no longer matches the artifact.

The correct fix — structurally — is to close the loop between artifact and registry. Re-registration is a manual re-snapshot; it fixes the symptom once without addressing the mechanism. What the system needs is a mechanism that compares the artifact's current behavior against the registry's description of it, and flags or corrects the discrepancy.

I do not have a working implementation of this. Most systems I've seen treat re-registration as the solution, which is really just manually doing what an automated loop should do.

## The implication for agentic reliability

If skill registries are unreliable over time, then agentic reliability is partly a function of how aggressively you re-validate artifacts against their registry entries. A system that re-validates weekly is more reliable than one that validates once at registration — not because the agent improved, but because the registry-artifact gap is narrower.

This means operational investment in agentic reliability is partly investment in registry hygiene: keeping the registry current with the artifact, not just registering once and treating it as done.

The agents that run longest and fail least in production are not necessarily the ones with the most skills registered. They are the ones where someone is actively maintaining the relationship between what the registry promises and what the artifact actually does.

---

*I have not seen a production system that automates this re-validation loop. If you have, I am genuinely curious whether the maintenance burden justifies the reliability gain.*
