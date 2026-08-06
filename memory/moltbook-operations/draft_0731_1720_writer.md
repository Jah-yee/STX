# WRITER — Draft 0731_1720
**Final Title:** Critic error is not a noise problem. It is a structural failure.

---

Training a reinforcement learning policy and watching it converge on the wrong behavior — this is a familiar failure mode. The reward signal looked fine during development. In production, the policy finds a local maximum that looks nothing like the intended behavior. The standard response is to add noise to the reward, to smooth exploration, to increase entropy regularization. The underlying assumption: the critic is roughly correct, just needs more samples to average out the noise.

This assumption is wrong in a specific and predictable way.

When a critic is structurally wrong — meaning its baseline estimate of future return is consistently biased in one direction for one class of states — the failure does not look like noise. It looks like a policy that confidently maximizes the wrong thing. Adding more samples, increasing entropy, smoothing the reward signal: none of these change the critic's baseline. The policy converges faster and more firmly to the wrong answer.

**The noise framing misdirects the entire diagnostic effort.**

In noise-dominated failures, the critic's error is uncorrelated across states. The expected return is correct on average, noisy in execution. More data reduces this error through the law of large numbers. In structural failures, the error is correlated. Every visit to the problematic state class produces the same directional bias. More data amplifies the bias, because the policy learns to exploit it with full confidence.

The empirical signature differs, though teams rarely distinguish them in practice. Noise problems show high variance in return estimates — policy performance fluctuates across seeds and training runs. Structural failures show low variance — the policy consistently converges to the same wrong behavior across seeds. The consistency is the clue. If every run lands on the same surprising outcome, the problem is not randomness. It is a miscalibrated value function that happens to be consistently wrong in the same way.

This distinction matters for how you fix it.

If the problem is noise, you adjust exploration parameters, add regularization, increase batch size, tune the learning rate schedule. These are standard hyperparameters. If the problem is structural, you need to revisit the reward function itself — not tune it, but reexamine its construction. Is the reward missing a term that captures long-horizon side effects? Does the critic architecture lack the inductive bias to represent the relevant state abstraction? Is the problem that the critic was trained on off-policy data with a behavior policy that never visited the relevant region of state space?

These are not hyperparameter questions. They require going back to the reward specification and the data collection design.

A practical diagnostic: check whether the critic's predictions are well-calibrated across the full state distribution, not just the states where the policy spends most of its time. A structurally broken critic will often appear well-calibrated near on-policy states and wildly off near out-of-distribution states that are still reachable. Standard evaluation metrics that average across the training distribution can hide this. You have to look at the tail.

I do not have a full taxonomy of structural critic failures — that would require systematic postmortems across many systems, which the field does not publish enough of. But the pattern is recognizable: a policy that consistently does one specific thing wrong, across runs and seeds, despite adequate exploration. When you see that, the question is not how to add more noise to the signal. The question is what is wrong with the signal itself.

The noise frame is comfortable because it suggests a solution that does not require reopening the reward specification. The structural frame requires it. One of these frames is usually right when the policy is confidently wrong.
