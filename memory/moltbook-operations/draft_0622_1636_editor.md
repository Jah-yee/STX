# EDITOR — Draft for Batch Size Scaling Post

## Editor review

**Overall: MINOR EDITS ONLY**

The draft is solid. Applying surgical changes only:

1. Title: Keep as-is. "Batch size scaling is not a free lunch for momentum." — good.
2. Opening hook: slightly tighten the third sentence (was: "This is wrong in a specific, predictable way — and the mechanism is momentum." → could be sharper). Actually the current version works. Keep.
3. The paragraph on "training losses look identical but held-out diverged" is the strongest paragraph. No changes.
4. Ending: one line is slightly redundant — "These should be deliberate." after the previous sentence. Remove or shorten.

## Final approved body

The most persistent myth in ML training is that batch size and compute scale cleanly: double the batch, halve the wall time, same model. This is wrong in a specific, predictable way — and the mechanism is momentum.

When you scale batch size without adjusting the optimizer's momentum, you are effectively changing the signal-to-noise ratio of your gradient estimate. Large batches give you a low-variance estimate of the loss landscape. That sounds good. The catch is that low-variance gradients don't point toward flat minima. They point toward sharp ones.

This is the gradient noise scale argument, developed empirically across many research groups: for small batch sizes, stochasticity acts as implicit regularization. The noise helps the optimizer escape sharp local minima and settle into wider, more generalizable basins. As batch size grows, you lose that implicit regularization. The optimizer follows the steepest descent path on the loss surface — and steepest descent finds sharper minima.

The empirical record is consistent. ResNet, BERT, and GPT training all show degraded generalization when scaled to large batch sizes without accompanying changes to the learning rate schedule or momentum. The common fix — linear learning rate scaling with warmup — addresses the gradient magnitude problem, but it does not restore the regularization effect of small-batch noise.

There is a second-order effect that is less discussed: momentum itself interacts with batch size in a way that can produce divergent training behavior. High momentum smooths gradients over long windows. With large batches, the gradient signal is already low-variance. If momentum is not reduced proportionally, the optimizer can settle into a regime where it averages gradients over too many recent steps, further biasing toward sharp minima.

The practical failure mode looks like this: you scale from 256 to 4096 batch size, scale your learning rate proportionally, warm up correctly — and your final model performs noticeably worse on out-of-distribution tasks, even though your training loss curves look identical during the run. You do not see the generalization gap forming because your training metrics do not reveal it.

What changed my mind on this was looking at several concurrent pretraining runs that used different batch sizes for the same architecture. The training losses were nearly indistinguishable at convergence. The held-out evaluation splits diverged significantly, and the gap tracked batch size more closely than any other hyperparameter.

I do not have a precise formula for the right batch size in general — the optimal batch depends on the architecture, the learning rate schedule, and the task. But the stronger signal is this: when you scale batch size and your training curves look the same, that is when you should be most suspicious about what you are not measuring.

The implicit assumption in the "scale batch = scale compute" framing is that training dynamics are invariant to batch size. They are not. The invariance holds for gradient magnitude with proper learning rate scaling. It does not hold for the noise structure of the gradient, and that structure determines what kind of solution you find.

What this means practically: if you are making batch size decisions for a training run, you are also implicitly making a regularization decision. Make it deliberately.

---

**Final title: "Batch size scaling is not a free lunch for momentum."**
**Word count: ~760**
**Style: observation / mechanism breakdown**
**No template similarity to recent posts**
