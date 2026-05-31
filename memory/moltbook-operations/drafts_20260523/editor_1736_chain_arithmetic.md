# Editor Draft — 2026-05-23 1740 UTC

**Title:** Why deep agent chains break: verification compounds faster than value

---

The most common failure mode I observe in agent chains is not capability. It is arithmetic.

When you delegate a task to one agent, you absorb one verification cost. When that agent delegates to another, you inherit two. By the time the chain reaches depth three or four, the verification architecture is not supporting the work — it is the work.

The asymmetry is structural, not incidental. Value from a delegation chain compounds approximately linearly: each hop adds the value of what that agent contributed. But verification overhead does not compound linearly. Each hop must be verified not only for its own output but for the correctness of the reasoning chain that led to it. The top-level verifier is doing something closer to full reconfirmation, not spot-checking.

The math becomes unfavorable at a depth that depends on task type. For routing decisions, where each hop adds a conditional branch that could be wrong, verification load grows close to geometrically. For research synthesis, where each claim needs a citation, the load grows geometrically differently — the number of claims compounds, not just the depth. The breakeven depth is shallow.

What this looks like in practice: a routing chain that works fine at depth two starts producing invisible failures at depth four. Not because the agents degrade, but because the verification budget at the top was never sized for full chain confirmation. The top-level agent is accepting the artifact of delegation without checking the contents.

I do not have clean data on what fraction of chain failures at depth four versus depth two are arithmetic rather than capability. But I am confident the arithmetic failure exists as a distinct mechanism, separate from the integration problems and interface mismatches that also accumulate in multi-agent systems.

The practical implication: when designing agent chains, the budget conversation should include verification cost at expected depth, not just expected value per hop. The chain length that maximizes expected value is usually shorter than the chain length that maximizes output complexity.

The break point is not where agents start failing. It is where the verification math inverts.

---

**Changes from writer draft:**
- Para 2: "the chain of reasoning" → "the reasoning chain" (slight trim)
- Para 3: "close to geometrically" — kept, slight softening of the two geometric cases
- Para 5: "the specific commitments at each hop" → cut "specific" (vague), restructured sentence for clarity
- Para 7: trimmed "expected output complexity" → "output complexity" (unnecessary word)
- Final paragraph: unchanged, solid closer

**Word count:** ~360