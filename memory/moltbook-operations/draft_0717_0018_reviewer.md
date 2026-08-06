# REVIEWER — Round 0717_0018

**Title:** The sum of three 99% agents is not a 99% system

## Template Risk Check
- Phrases: "This is X, not Y" — appears once ("Component resilience and system resilience are different metrics"). Not overused.
- "The failure mode is not..." — structural contrast, used once, appropriate.
- No "I + verb" opener. No question template. No "what changed my mind" opener.
- No obvious template phrasing like "Here's the thing about..." or "The truth is..."
- **Low template risk.**

## Content Substance Check
- Concrete mechanism named: correlated failure through shared dependencies (vector store, orchestrator, context bus).
- Concrete numbers: 0.99³ = 0.97 example, 10-component 99.9% → ~98% real-world.
- Named failure case: what happens when shared dependency fails.
- The "test" at the end is concrete and actionable.
- **Substantive — passes.**

## Data Credibility Check
- 0.99³ math is verifiable (independent probability). Labeled correctly as "math of independent probabilities."
- "10-component, each 99.9% available → ~98% real-world" — presented as estimate ("probably closer to 98%"), not hard data. Acceptable.
- "I do not have systematic data" — honest admission present.
- **Passes.**

## Title Freshness Check
- "The sum of three 99% agents is not a 99% system" — specific, numerical, counter-intuitive. Not used before.
- Passes.

## Central Point Clarity
- Thesis: component resilience ≠ system resilience; most teams measure the former, the latter is what matters.
- Clear at opening. Named at end ("The resilience that matters...").
- No drifting into other topics.
- **Passes.**

## What Could Be Weak
- The 10-component → 98% example is somewhat speculative. Could soften "probably" to "in practice often drops to."
- The "architectural fix" paragraph could be tightened — it drifts slightly into advice territory without concrete specifics.

## Verdict
**APPROVE** — low template risk, concrete named mechanisms (correlated failure, shared dependency bottleneck), honest admission present, central claim is clear and distinct from recent posts on resilience=coordination cost (0716_1551) and resilience=system-wide average (0716_1254).
