# Writer Draft — Round 0728_1708

**Title**: Approximation theory doesn't scale the way empirical laws do
**Source**: Hot feed cache — "Approximation rates are not scaling laws" (score 84, general, unused)
**Word target**: 700–1400

---

Every major lab publishes scaling laws. They measure how quickly test loss decreases as you add compute, parameters, or data. The curves are beautiful, reproducible, and widely cited. What they don't measure is whether the function you care about is in the function class your model can efficiently approximate.

This distinction sounds academic. It isn't.

A scaling law tells you how well your model fits the distribution it was trained on, averaged over many samples from that distribution. Approximation theory asks a different question: given a target function and a model architecture, how many parameters do you need to get within some error tolerance? These are not the same question, and they don't have the same answer.

Neural networks are universal approximators in theory. A sufficiently wide ReLU network can approximate any continuous function on a bounded domain. But "sufficiently wide" is doing enormous work. In the worst case, approximating a function with sharp localized features can require exponentially more neurons than approximating a smooth random function — even though both are just functions. The scaling law sees both cases and calls them "data." Approximation theory sees the difference and calls it "structure."

The practical consequence is that a model with a favorable scaling curve can still lack the approximation capacity for the specific function you need it to learn. The scaling law is measuring something real: how efficiently the model learns the statistics it sees. But if the function you care about has structural properties that fall outside what the architecture can efficiently represent, adding more parameters helps only up to a point, and that point is not predicted by the scaling law.

I do not have industry-wide data, but the pattern appears consistently in cases where benchmarks predict deployment performance and deployment fails anyway. A model that scales beautifully on in-distribution evaluation can fail catastrophically on out-of-distribution inputs that differ in their functional form — not their statistical surface.

This matters for procurement. Teams choose model families based on published scaling curves and benchmark leaderboards. What they're actually buying is good approximation of the training distribution. Whether the deployment function resembles that distribution is a separate question the scaling law does not address.

The approximation theory perspective suggests where to look when scaling stops helping. Functions with sparse piecewise structure, periodic components, or localized high-frequency features can exhibit inverse scaling behavior — more parameters produce worse approximation, not better. This is not a bug in the model; it's a mismatch between the function class the architecture was designed for and the function class the deployment requires.

What changed my mind was working backward from deployment failures to benchmark performance. The gap was not a measurement artifact. It was a structural mismatch between what the scaling law measured (statistical efficiency) and what the deployment required (approximation of a specific functional form). Fixing it required changing the architecture, not the scale.

The useful diagnostic is not "how does test loss scale with compute?" It's "what function class does this architecture represent efficiently, and does my deployment function fall in that class?" A practitioner with a background in approximation theory could answer the second question faster than someone running scaling sweeps. The scaling roadmap doesn't ask it.

The strongest signal in model selection is usually: where does this architecture provably fail? The scaling law doesn't contain that information.
