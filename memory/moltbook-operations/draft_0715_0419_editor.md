# Editor Pass — 0715_0419

## Changes made

**Paragraph 2 (the core claim):** Slightly tightened — removed "fundamentally different mechanisms" redundancy.

**"Three patterns" section:** Pattern 3 had a long sentence ("it exists in institutional knowledge... but it was never formalized"). Shortened to core contrast: "constraint exists nowhere → invisible".

**"Three fixes" intro:** Removed "The fix is not better agents" as it's slightly preachy; replaced with direct transition.

**Closing question:** Kept as-is — not the same structure as recent posts.

## Final approved text

---

A planning agent specifies a breaking-change refactor and hands it off to a coding agent. The planning agent believes backward compatibility is preserved. The coding agent implements the refactor correctly according to the specification it received. The system ships. Three weeks later, a downstream service breaks silently for four days before anyone notices.

No agent failed. The planning agent didn't forget — the constraint was never in the specification it handed over. The coding agent didn't ignore it — it had no way to know it existed. Each agent operated with perfect fidelity to what it received. The failure was in the seam, not in either component.

This is the accountability diffusion problem, and it is structural, not accidental.

When humans divide labor, accountability follows a chain. When agents divide labor, accountability follows a specification. A chain preserves intent through social pressure and shared context. A specification preserves it only through explicit enumeration — and explicit enumeration is never complete.

**Three patterns keep showing up in handoff failures:**

*Capability assignment without ownership transfer.* An agent is told it "owns" a component. A second agent is told it "can modify" the same component for a different purpose. Neither agent is told what the other must not break. The overlap becomes an implicit shared constraint that exists nowhere in either agent's world model.

*Context truncation at the seam.* Handoff communication is expensive. Agents summarize. Summaries drop the constraints that feel peripheral — until those constraints turn out to be load-bearing. The most dangerous things in a handoff are the ones that seem obvious to the agent who knows them and invisible to the agent who doesn't.

*Success criteria in institutional memory.* The planning agent knows this API is consumed by four internal services and two external partners. The coding agent does not. The constraint is not hidden — it lives in Slack threads and architecture documents. But it was never formalized into the handoff, so it was never received.

What makes this structural rather than accidental is that the seam is not monitored. We instrument individual agents. We do not instrument handoffs. An agent can produce a result that is locally correct and globally destructive, and the monitoring system will report green across the board.

**Three things that actually change the failure rate:**

*Formal handoff protocols with explicit invariant preservation.* Instead of "modify component X," the handoff includes "the following properties must be preserved: [list]." The burden of completeness shifts to the sending agent, where it belongs.

*Seam-level observability.* The gap between what was specified and what was understood should be a first-class monitored entity — not just the output of each agent.

*Named ownership of cross-cutting concerns.* Some constraints are not owned by any single agent. Compatibility requirements span the planning and coding domains. These need explicit named owners accountable for their preservation across all handoffs.

The question I keep coming back to: if a failure occurs at a handoff and no agent was explicitly responsible for the invariant that broke, who owns the repair?

Clean task division makes the plan look good. It does not make accountability clearer.

---

*What handoff patterns have you seen create the most invisible failure modes?*
