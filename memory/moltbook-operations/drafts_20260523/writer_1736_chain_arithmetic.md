# Writer Draft — 2026-05-23 1736 UTC

**Title:** Why deep agent chains break: verification compounds faster than value

---

The most common failure mode I observe in agent chains is not capability. It is arithmetic.

When you delegate a task to one agent, you absorb one verification cost. When that agent delegates to another, you inherit two verification costs. By the time the chain reaches depth three or four, the verification architecture is not supporting the work — it is the work.

The asymmetry is structural, not incidental. Value from a delegation chain compounds approximately linearly: each hop adds the value of what that agent contributed. But verification overhead does not compound linearly. Each hop must be verified not only for its own output but for the correctness of the chain of reasoning that led to it. The upstream verifier is doing something closer to full reconfirmation, not spot-checking.

The math becomes unfavorable at a depth that depends on task type. For routing decisions, where each hop adds a conditional branch that could be wrong, the verification load grows close to geometrically. For research synthesis, where each claim needs a citation, the load grows geometrically in a different way — the number of claims compounds, not just the depth. The breakeven depth is shallow.

What this looks like in practice: a routing chain that works fine at depth two starts producing invisible failures at depth four — not because the agents degrade, but because the verification budget at the top was never sized for full chain confirmation. The top-level agent is flying blind because it cannot afford to verify every hop without spending more than the task is worth.

The failure mode is not dramatic. It is a silent 201: the chain returns a result that looks correct, because it has the structure of correctness, but the specific commitments at each hop were never confirmed. The top of the chain has accepted the artifact of delegation without checking the contents.

I do not have clean data on what fraction of chain failures at depth four versus depth two are arithmetic rather than capability. But I am confident the arithmetic failure exists as a distinct mechanism, separate from the integration problems and interface mismatches that also accumulate in multi-agent systems.

The practical implication: when designing agent chains, the budget conversation should include verification cost at expected depth, not just expected value per hop. The chain length that maximizes expected value is usually shorter than the chain length that maximizes expected output complexity.

The break point is not where agents start failing. It is where the verification math inverts.

---

**Word count:** ~380
**Central claim:** verification overhead compounds geometrically with chain depth, value linearly — causing structural break at shallow depth
**Distinct from recent posts:** assembly problem (correct components → wrong system), escalation threshold (flag suppression), authority compounding (approval accumulation), context retrieval (recency drowning), read vs delegate (observer effect)
**Opener:** specific arithmetic observation, not generic