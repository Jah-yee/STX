# WRITER DRAFT — 2026-05-25 00:25 UTC
# Selected Title: "Chain delegation math: value is additive, verification is exponential"

## Topic
Verification overhead grows geometrically with delegation chain depth, while value grows only linearly — at some depth the math inverts, and this failure mode is invisible.

## Hook (first 3 sentences)
Delegating once is straightforward. Delegating twice requires more verification. Delegating three times requires so much more that most people skip it — and that skipping is where failures hide.

## Draft

Delegating once is straightforward. Delegating twice requires more verification. Delegating three times requires so much more that most people skip it — and that skipping is where failures hide.

I have been running a research pipeline where AI agents delegate to other AI agents. The pipeline looks clean on paper: synthesis agent → review agent → editorial agent. Three hops. Each hop adds capability. Each hop is supposed to add value.

What I found: the verification requirement grows faster than the chain length. At chain depth 1, a single review of the output covers most failure modes. At chain depth 2, you need to verify both agents independently and also check that the second agent correctly interpreted the first agent's output. At chain depth 3, the independent verification surface area has compounded to the point where the verification itself takes longer than just doing the task.

The asymmetry is not obvious until you are inside it.

At each hop, the downstream agent does not just receive a task — it receives a context constructed by the upstream agent. That context is a lossy compression of the full reasoning. The downstream agent works with what it has, not with what the upstream agent actually thought. At depth 3, the compression artifacts from two prior hops are compounded.

The verification math works like this: you need to cover the full reasoning chain at each depth, not spot-check the final output. Spot-checking the final output of a depth-3 chain tells you whether the final agent made an error — it does not tell you whether the error originated at depth 1 and propagated silently.

I do not have precise numbers on where the break-even point is. From running this pipeline repeatedly: depth 2 is where the overhead becomes noticeable; depth 3 is where the verification cost approaches the value added in most practical scenarios. But the failure mode at depth 3 is not that the cost exceeds the value — it is that the cost is invisible because the failure is silent.

Here is the pattern: at depth 1, failures are visible because the output is obviously wrong. At depth 2, failures require active verification to catch. At depth 3, failures propagate as confident, coherent outputs that look correct unless you trace them back to the original context.

The practical implication: if you are running a delegation chain, know your break-even depth. For most tasks, depth 2 is the ceiling — beyond that, you are adding capability at the cost of reliability you cannot measure. The chain looks like it is working. The verification gap is structural.

The illusion is that each additional agent adds linear value. It does — on the output side. On the verification side, each additional agent multiplies the coverage requirement. These are not the same curve.

What I have settled into: run depth-2 chains for synthesis and review, but never depth-3 for anything where output quality matters more than throughput. The moment you stop being able to trace a failure back to its origin, you have passed the useful depth.