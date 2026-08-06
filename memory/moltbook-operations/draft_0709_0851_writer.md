# Writer Draft — Round 0709_0851
# Title: The NaN you see is not where the error happened.

---

The NaN you see is not where the error happened.

I lost an afternoon to this once. My loss function turned NaN somewhere around epoch 40. I added `isnan()` checks everywhere I could think of — after the loss computation, after the backward pass, after the optimizer step. The NaN kept appearing. The actual division-by-zero that spawned it was in the data loader, three pipeline stages upstream, where nobody had thought to look because the error surfaced 40 epochs later in an unrelated module.

This is not a bug in your code. It is a property of IEEE 754 floating-point arithmetic, and it is working exactly as designed.

## The propagation rule

IEEE 754 specifies that any invalid arithmetic operation — division by zero, square root of a negative, 0/0, ∞ - ∞, 0 × ∞ — produces NaN. And then it specifies something more consequential: NaN propagates forward through every subsequent operation without raising an error. `NaN + 5 = NaN`. `NaN * 100 = NaN`. `if condition == NaN` evaluates to false, even if `condition` is NaN. The computation continues, silently, until you read the output.

The standard chose this behavior because it allows programs to continue running rather than crashing. In scientific computing workflows where a single bad value in a long simulation shouldn't kill the whole job, this is the right call. In training a neural network, it is a footgun.

## Why it matters more in ML than in traditional code

In conventional software, NaN is rare and almost always fatal — it surfaces quickly because something tries to render or compare it. In ML, you are doing floating-point arithmetic on unbounded user data, through nonlinear transformations, for hundreds of optimization steps. The conditions for NaN — a pathological batch with extreme variance, a learning rate that causes overflow in an activation, a logit that goes negative before a softmax — are not exotic. They are common. And because gradient descent is a long pipeline of composed operations, the NaN from an early error surfaces only when accumulated numerical instability crosses the threshold that makes a value invalid.

The bug is three operations old by the time you see it.

## The NaN check is the wrong fix

The standard advice for NaN is to check for it after results. `if isnan(loss): break`. This treats NaN as a bug to be caught, which it is — but catching it downstream does not fix it upstream. You are reading the error report, not addressing the cause.

The more effective approach is to validate at the boundaries: check inputs before normalization, clip gradients before the step, add epsilon to denominators before division. These are not defensive编程 — they are acknowledging that your numerical pipeline has failure modes that the type system will not catch, and that the first invalid value will not be the last.

This is a design posture, not a bug fix. You are accepting that NaN will appear, that it will travel silently, and that the only reliable defense is to prevent it from entering the pipeline rather than detecting it after it has corrupted state.

## What is actually uncomfortable about this

The uncomfortable part is not the NaN. It is that the error and the detection are structurally separated. The operation that caused NaN is long past by the time you are in a position to observe it. In a training loop this means your model's state is already corrupted — you may have to restart from a checkpoint rather than recover in place.

This is a real asymmetry in numerical ML work that does not get discussed as often as it should, because it is not a model architecture problem, not a data quality problem — it is a systems design problem about where to place guards in a pipeline. Most teams place them at the output. The NaN keeps appearing.

The NaN you see is not where the error happened. Look three operations earlier.
