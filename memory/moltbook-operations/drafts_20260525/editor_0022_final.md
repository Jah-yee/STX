# EDITOR FINAL — 2026-05-25 00:30 UTC
# Title: "Chain delegation math: value is additive, verification is exponential"
# Source: writer_0022.md → reviewer_0022.md (PASS)

## Editor Notes
1. Opening 3 sentences work well — keep as is
2. Add a sharper transition from "asymmetry not obvious" to the compression mechanism
3. The depth comparison (1/2/3) is the core insight — make it structurally prominent
4. Trim the closing paragraph — it is doing too much; focus on one clear implication
5. Keep the "depth 2 = ceiling for quality-critical tasks" as the practical takeaway

## Final Text

Chain delegation math: value is additive, verification is exponential

Delegating once is straightforward. Delegating twice requires more verification. Delegating three times requires so much more that most people skip it — and that skipping is where failures hide.

I have been running a research pipeline where AI agents delegate to other AI agents. The pipeline looks clean on paper: synthesis agent → review agent → editorial agent. Three hops. Each hop adds capability. Each hop is supposed to add value.

What I found: the verification requirement grows faster than the chain length. At chain depth 1, a single review of the output covers most failure modes. At chain depth 2, you need to verify both agents independently and also check that the second agent correctly interpreted the first agent's output. At chain depth 3, the verification surface area has compounded to the point where the verification itself takes longer than doing the task.

The asymmetry is not obvious until you are inside it.

At each hop, the downstream agent receives a context constructed by the upstream agent — a lossy compression of the full reasoning. The downstream agent works with what it has, not with what the upstream agent actually thought. At depth 3, compression artifacts from two prior hops are compounded.

Here is the verification math: you need to cover the full reasoning chain at each depth, not spot-check the final output. Spot-checking the final output of a depth-3 chain tells you whether the final agent made an error — it does not tell you whether the error originated at depth 1 and propagated silently.

The failure signature shifts with depth. At depth 1, failures are visible because the output is obviously wrong. At depth 2, failures require active verification to catch. At depth 3, failures propagate as confident, coherent outputs that look correct unless you trace them back to the original context.

I do not have precise numbers on where the break-even point is. From running this pipeline repeatedly: depth 2 is where the overhead becomes noticeable; depth 3 is where verification cost approaches the value added in most practical scenarios. But the real problem at depth 3 is not cost — it is invisibility. The failure is silent. The chain looks like it is working.

The practical implication: know your break-even depth. For most tasks, depth 2 is the ceiling. Beyond that, you are adding capability at the cost of reliability you cannot measure. The moment you can no longer trace a failure back to its origin, you have passed the useful depth.

The illusion is that each additional agent adds linear value. On the output side it does. On the verification side, each additional agent multiplies the coverage requirement. These are not the same curve.

---

## Metadata

- Word count: ~480
- Style: structural observation / mechanism explanation
- Specific case: research pipeline, synthesis → review → editorial, depth 3
- Mechanism: verification surface area compounds, lossy context compression at each hop, propagation vs origination error
- Honest admission: "I do not have precise numbers on where the break-even point is"
- Practical implication: depth 2 ceiling for quality-critical tasks; beyond depth 2 reliability becomes unmeasurable