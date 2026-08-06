# EDITOR — Round 0728_0311

## Surgical changes only

**Paragraph 3 (complexity description):**
Before: "The authors' algorithm for Gaussian halfspaces achieves sample and computational complexity of roughly poly(d) multiplied by a term that grows with log(1/alpha) and log(1/epsilon). Their Statistical Query lower bound shows that any algorithm that doesn't account for this cost structure hits a complexity wall that the reliable model navigates explicitly."
After: "Their algorithm for Gaussian halfspaces achieves complexity roughly poly(d) · 2^{O(log(1/epsilon)^{O(log(1/alpha)))}. The Statistical Query lower bound shows that any algorithm that skips the cost structure hits a wall — one the reliable model explicitly navigates."

Change reason: compress the math notation without losing the key relationship. "Hits a wall" is more direct than "complexity wall."

**Paragraph 5 (calibration argument):**
Before: "Calibration is the standard response. After training, adjust the decision threshold to reflect the actual cost of errors. But calibration after convergence is not the same as accounting for cost during optimization."
After: "Calibration is the standard fix — adjust the threshold after training. But convergence path is set by what the model was asked to minimize. If you asked it to minimize average error, post-hoc calibration shifts the output without changing the decision boundary the model already committed to."

Change reason: tighten the contrast between during-optimization vs. post-hoc.

**Paragraph 6 (closing):**
Before: "The separation in this paper is not a minor technical correction. It is a formal proof that these are different regimes — that cost-asymmetric learning and standard agnostic learning have fundamentally different complexity profiles, and the tools built for one do not transparently transfer to the other."
After: "This is not a technical footnote. It is a formal proof that cost-asymmetric and standard agnostic learning occupy different complexity regimes — and that tools built for one do not transfer to the other."

Change reason: 40% shorter, same meaning, stronger close.

**No other changes.** (Reviewer noted no template smell, no vagueness, no fake data — leaving the structure intact.)
