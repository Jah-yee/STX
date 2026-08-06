# Writer Draft — "The UAT proves existence, not capability"

## Central Claim
The Universal Approximation Theorem tells you a neural network *can* learn any continuous function — it says nothing about whether your specific training setup *will* get it to do so. This gap between theoretical possibility and practical achievability is where most ML projects quietly fail.

## Body

The Universal Approximation Theorem is often cited as a kind of existential Get Out of Jail Free card. Feed it into any conversation about whether neural networks are "powerful enough" and the discussion tends to end there: UAT says yes, therefore the architecture is capable, therefore any remaining failures must be engineering problems.

This reading is wrong, and the cost of being wrong about it is measured in months of wasted training runs.

Here's what UAT actually proves: for any continuous function f defined on a compact domain and any epsilon > 0, there exists a neural network with finite width and depth that approximates f within epsilon. The key quantifier is *there exists*. Not *your* network. Not *with your initialization*. Not *given your training data and optimization setup*. *There exists some* network with *some* width and *some* depth — parameters that are never specified — that achieves the bound.

The distinction matters because three separate gaps stand between "theoretically possible" and "actually achieved":

**Optimization gap.** Gradient descent does not find the global optimum of the loss landscape. It finds a local minimum initialized by your weight distribution, shaped by your learning rate schedule, and interrupted by your early stopping criterion. UAT guarantees that *some* network achieves the target. SGD guarantees no such thing. The practical implication: better optimizers, better initialization schemes, and better learning rate design are not optional refinements — they are the actual mechanism by which theoretical capacity gets converted into real behavior.

**Generalization gap.** UAT does not bound the gap between training and test performance. A network that achieves near-zero training error can still be useless on test data if the training distribution does not match the test distribution. This is not a minor footnote — it is the central problem of applied ML. Every production ML failure I have observed in the past two years shared this structure: the model was optimized for the wrong distribution, or the distribution shifted between training and deployment, and no amount of theoretical capacity could compensate.

**Distribution shift.** UAT assumes the target function is fixed. In practice, the data distribution itself changes. The model is asked to approximate f_t at deployment time, but was trained on samples from f_s at training time. When the shift is severe — adversarial conditions, novel user behavior, rare edge cases — the approximation error can become arbitrarily large even if the network performed perfectly during training. UAT is silent on this. It has no mechanism to account for a function that changes shape depending on when and where you sample it.

Architecture choices compound these gaps. Convolutional layers encode a prior about spatial stationarity. Attention mechanisms encode a prior about which tokens are relevant to which other tokens. Recurrent layers encode a prior about temporal dependence. These inductive biases make certain approximation targets easier to reach with finite data — but they also make the network brittle to distributional violations of those priors. UAT says nothing about any of this.

The practical upshot: UAT gives you a ceiling on theoretical capability. It tells you the problem is not in principle unsolvable. It does not tell you that your architecture, data, optimizer, and stopping criterion will get you anywhere near that ceiling.

The most dangerous version of this mistake I see in practice: teams that add more parameters, more layers, or more sophisticated architectures when a model fails in production, on the theory that the model is "not capable enough." More often, the failure is in the training distribution, the evaluation setup, or the optimization process. Adding capacity does not fix a data problem. The UAT is not a deployment roadmap. It is a ceiling on what is possible — and the distance between that ceiling and what you can actually build is determined by everything the theorem abstracts away.

The thing that changed my mind about this: looking at the history of neural network scaling papers from the 1990s and early 2000s. Many of these papers reported near-perfect training set performance and called it success. The generalization failures that appeared in deployment were attributed to insufficient model capacity — leading to years of architecture research that, in retrospect, was addressing the wrong variable. The capacity was always there. The problem was never the ceiling.

I do not have full data on how many production ML failures trace to this specific misreading of theoretical results. But in my observation, the pattern is common enough that it is worth naming: the model that cannot learn is often not incapable — it is misaligned, mis-specified, or optimized for the wrong distribution.

What approximation theorems actually give you is permission to try. What they do not give you is a path to follow.
