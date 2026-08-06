# EDITOR — Round 0728_1738

## Changes Required

### 1. Opener — too long setup before counter-intuition
**Original:** "When a neural network trains past a certain point and suddenly generalizes — this is not the engineer succeeding. It is the system finding a region of weight space..."
**Revised:** "The day a model suddenly generalizes, no engineer raised their hand. The capability emerged because the loss landscape rewarded compression — not because anyone planned it. This is grokking: a phase transition in the loss landscape that looks like design but isn't."

### 2. Para 3 "often describes exactly this" — hedge too weak
**Original:** "...often describes exactly this: phase transitions..."
**Revised:** "...describes exactly this: phase transitions in the loss landscape where behavior changes qualitatively, driven by gradient descent selection pressure, not by any design specification."

### 3. Minor cleanup — remove redundant "it is structurally explicable but not engineerable" (already said this above)
**Cut:** "for reasons that are structurally explicable but not engineerable"

### 4. Final paragraph — strengthen the practical signal
**Original:** "What implicit dynamics is your current system relying on?"
**Revised:** "The practical question is not whether your system developed something useful — it clearly did. The question is whether you know which training dynamics created it, and whether those dynamics are stable under your deployment distribution. Implicit evolutionary shifts are not engineering tools. They are useful side effects with an unknown half-life."
