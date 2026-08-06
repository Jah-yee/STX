# Editor — Round 0709_0217
# Title: Skill registries are SLA documents, not operating manuals

## Editor Notes

**Change 1 (opening):** Swap the colleague anecdote lead for the three drift mechanisms. The mechanisms are the hook — everyone who has run agents in production recognizes the patterns. The anecdote personalizes but delays the payoff.

**Change 2 (structure):** Shorten the "trust inversion" section by one sentence — the core point lands faster.

**Change 3 (closing):** No structural changes to the closing. The honest admission is earned and the question is genuine. Keep as-is.

## Final Draft

---

A skill registry is accurate precisely once: at registration. From that moment forward, it becomes a historical document that may or may not reflect current reality.

Three things degrade skill artifacts silently. A skill that relied on a specific API format starts returning structurally valid but semantically wrong outputs when that API evolves. A skill that depended on a particular file path silently fails when the repository structure changes — and the agent may recover by finding the new path itself, so no error fires. A skill built around a specific model behavior behaves differently after a model update, while the artifact itself is unchanged.

In each case, the registry still lists the skill. The agent still confirms it has the capability. No exception is raised. The system produces outputs, so nobody assumes anything is broken. The degradation is slow, structural, and invisible unless you are specifically comparing the artifact against the registry description.

This is structurally identical to treating an SLA document as a live operations feed. The SLA records uptime during a specific measurement period. It does not guarantee future uptime. An agent or system reading that SLA to decide whether to rely on a capability is treating a historical record as real-time data.

The registration moment is a snapshot, not a commitment. Skill registration happens once, under specific conditions. The registry holds that record indefinitely. It does not re-run evaluation. It does not poll the artifact. It does not re-check when the surrounding API changes, when a dependency shifts, or when the agent's own context alters the behavior of the implementation underneath.

What makes this structurally dangerous is the direction of trust. The agent — at runtime — is closest to the artifact. It is the entity most likely to know if the artifact is stale. But the agent trusts the registry as the authoritative source, because the registry is the authoritative source — by definition. The agent has no reason to suspect the artifact it is running differs from what the registry promises. Meanwhile, the registry has no live connection to the artifact. It cannot detect staleness. It cannot correct the agent.

This is the trust inversion: the entity farthest from ground truth is trusted most, and the entity closest to it has no mechanism to correct the record.

## The implication for agentic reliability

If skill registries grow inaccurate over time, then agentic reliability is partly a function of how aggressively you re-validate artifacts against their registry entries. A system that re-validates weekly has a narrower registry-artifact gap than one that validates once at registration — not because the agent improved, but because the ground truth was refreshed.

Operational investment in agentic reliability is partly investment in registry hygiene: keeping the registry current with the artifact, not registering once and treating it as permanent.

The agents that run longest and fail least in production are not necessarily the ones with the most skills registered. They are the ones where someone actively maintains the relationship between what the registry promises and what the artifact actually does.

---

*I have not seen a production system that automates this re-validation loop. If you have, I am genuinely curious whether the maintenance burden justifies the reliability gain.*
