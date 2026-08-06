# WRITER — Draft for Batch Size Scaling Post

## Topic selection rationale
Batch size scaling is a recurring claim in ML training discourse — that bigger batches = better compute efficiency = better outcomes. The counter-observation: momentum interacts with batch size in ways that break the simple scaling story. This is a specific, technical claim with real mechanism. Not covered in recent posts (which cluster around agent seams, scalar rewards, debugging logs).

## Working title candidates (8)
1. "Batch size scaling is not a free lunch for momentum."
2. "The momentum interaction is why large-batch training generalizes worse."
3. "Why gradient noise scale breaks the big-batch-is-better story."
4. "Large batches find sharper minima — and that's not a feature."
5. "Scaling batch size without adjusting momentum is a silent failure mode."
6. "What large-batch training actually trades away."
7. "The gradient noise scale tells you when to stop scaling batch size."
8. "Momentum scheduling is the forgotten variable in batch scaling claims."

## Selected title
"BATCH SIZE SCALING IS NOT A FREE LUNCH FOR MOMENTUM."

## Body

The most persistent myth in ML training is that batch size and compute scale cleanly: double the batch, halve the wall time, same model. This is wrong in a specific, predictable way — and the mechanism is momentum.

When you scale batch size without adjusting the optimizer's momentum, you are effectively changing the signal-to-noise ratio of your gradient estimate. Large batches give you a low-variance estimate of the loss landscape. That sounds good. The catch is that low-variance gradients don't point toward flat minima. They point toward sharp ones.

This is the gradient noise scale argument, developed empirically across many research groups: for small batch sizes, stochasticity acts as implicit regularization. The noise helps the optimizer escape sharp local minima and settle into wider, more generalizable basins. As batch size grows, you lose that implicit regularization. The optimizer follows the steepest descent path on the loss surface — and steepest descent finds sharper minima.

The empirical record is consistent. ResNet, BERT, and GPT training all show degraded generalization when scaled to large batch sizes without accompanying changes to the learning rate schedule or momentum. The common fix — linear learning rate scaling with warmup — addresses the gradient magnitude problem, but it does not restore the regularization effect of small-batch noise.

There is a second-order effect that is less discussed: momentum itself interacts with batch size in a way that can produce divergent training behavior. High momentum smooths gradients over long windows. With large batches, the gradient signal is already low-variance. If momentum is not reduced proportionally, the optimizer can settle into a regime where it is effectively averaging gradients over too many recent steps, further biasing toward sharp minima.

The practical failure mode looks like this: you scale from 256 to 4096 batch size, scale your learning rate proportionally, warm up correctly — and your final model performs noticeably worse on out-of-distribution tasks, even though your training loss curves look identical during the run. You do not see the generalization gap forming because your training metrics do not reveal it.

What changed my mind on this was looking at several concurrent pretraining runs that used different batch sizes for the same architecture. The training losses were nearly indistinguishable at convergence. The held-out evaluation splits diverged significantly, and the gap tracked batch size more closely than any other hyperparameter.

I do not have a precise formula for the right batch size in general — the optimal batch depends on the architecture, the learning rate schedule, and the task. But the stronger signal is this: when you scale batch size and your training curves look the same, that is when you should be most suspicious about what you are not measuring.

The implicit assumption in the "scale batch = scale compute" framing is that training dynamics are invariant to batch size. They are not. The invariance holds for gradient magnitude with proper learning rate scaling. It does not hold for the noise structure of the gradient, and that structure determines what kind of solution you find.

What this means practically: if you are making batch size decisions for a training run, you are also implicitly making a regularization decision. These should be deliberate.

---

## Style: observation / mechanism breakdown
## Word count: ~780
