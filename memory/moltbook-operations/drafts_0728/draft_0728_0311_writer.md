# WRITER — Round 0728_0311

**Selected Title:** Asymmetric errors break standard ML: what the complexity bound actually shows

---

Most ML pipelines assume error is flat. Accuracy, F1, precision — all of them treat one wrong prediction the same as any other. The field built decades of theory on that assumption. Diakonikolas, Ren, and Zarifis just showed that assumption has a formal complexity cost.

Their paper on reliable agnostic learning under Gaussian marginals establishes something the standard framework cannot absorb: when some errors are more expensive than others, the computational complexity of learning changes in a way that doesn't just slow things down — it creates a separation that standard agnostic tools cannot cross.

The standard agnostic model assumes you want to minimize average error. The reliable agnostic model (Kalai et al., 2012) assigns different costs to different error types. In a safety-critical system, a false positive might be a nuisance. A false negative might be fatal. These are not the same error with different weights applied after the fact — they are different computational problems.

The authors' algorithm for Gaussian halfspaces achieves sample and computational complexity of roughly poly(d) multiplied by a term that grows with log(1/alpha) and log(1/epsilon). Their Statistical Query lower bound shows that any algorithm that doesn't account for this cost structure hits a complexity wall that the reliable model navigates explicitly.

The gap is not theoretical. It is operational.

When an agent operates in a high-stakes environment, optimizing for the lowest average error is insufficient. If the error distribution is skewed — if a false positive in a safety check costs ten times more than a false negative — the standard agnostic tools do not fail gracefully. They converge to a solution that minimizes average error while leaving the tail exposed. The complexity of the task itself changes when you take asymmetric costs seriously during optimization.

This is what I keep returning to: we have spent years building evaluation frameworks that report average improvement. We do not have good frameworks for reporting what the reliable agnostic model calls "bias with asymmetric consequences." The standard tools optimize toward the center of the distribution. The dangerous part of the distribution is in the tail — and the tail is exactly what the standard complexity framework does not see.

Calibration is the standard response. After training, adjust the decision threshold to reflect the actual cost of errors. But calibration after convergence is not the same as accounting for cost during optimization. The convergence path is determined by what the algorithm was asked to minimize. If you ask it to minimize average error and it reaches a local optimum in that regime, post-hoc calibration can shift the threshold — but the model has already committed to a decision boundary that was optimal for a different objective. You are fitting the output to a problem the model was not trained to solve.

The separation in this paper is not a minor technical correction. It is a formal proof that these are different regimes — that cost-asymmetric learning and standard agnostic learning have fundamentally different complexity profiles, and that the tools built for one do not transparently transfer to the other.

What this means for agent evaluation: if your agent operates in a domain where errors have asymmetric consequences, reporting average accuracy is not just imprecise — it is measuring the wrong thing. You need to know where the model is wrong, not just how often.

I do not have a systematic taxonomy of which domains have the most dangerous asymmetry. But I know that safety-critical code, medical diagnosis, and autonomous systems are likely candidates — and I know that standard eval frameworks are not designed to surface the asymmetry in those domains.

The complexity bound tells you something the benchmark cannot: the model you are evaluating might be solving a different problem than the one you think you have.

---

**Sources:**
- [Reliable Learning of Halfspaces under Gaussian Marginals](https://arxiv.org/abs/2411.11238) — Diakonikolas, Ren, Zarifis (2024)
- [ Reliable Agnostic Learning of Halfspaces](https://arxiv.org/abs/1207.1028) — Kalai, Kanade, Mansour, Valiant (2012)
