# Editor Draft — Round 0728_1708

## Changes from Writer Draft

1. **Add concrete ReLU scenario** (~80 words): Expand "worst-case ReLU" into a short illustrative case — function with sharp discontinuities vs smooth function, same parameter count gives very different approximation quality.
2. **Expand "what changed my mind"** (~60 words): More of the backward-working diagnostic chain.
3. **Sharpen closing paragraph** (~40 words): Consolidate last two sentences into one stronger closer.
4. **Target**: ~750-850 words

---

# Editor Final — Round 0728_1708

Every major lab publishes scaling laws. They measure how test loss decreases as you add compute, parameters, or data. The curves are reproducible and widely cited. What they don't measure is whether the function you care about is in the function class your model can efficiently approximate.

This distinction sounds academic. It isn't.

A scaling law tells you how well your model fits the distribution it was trained on, averaged over many samples. Approximation theory asks a different question: given a target function and a model architecture, how many parameters do you need to get within some error tolerance? These are not the same question, and they don't have the same answer.

Neural networks are universal approximators in theory. A sufficiently wide ReLU network can approximate any continuous function on a bounded domain. But "sufficiently wide" does enormous work. Consider two functions on [0,1]: a smooth sine wave and a step function with a sharp discontinuity at x=0.5. A ReLU network needs far fewer parameters to approximate the sine wave to a given error tolerance than it needs to approximate the step function — even though both are continuous functions and both are in the network's theoretical function class. The scaling law sees both cases and calls them "data." Approximation theory sees the difference and calls it "structural complexity."

The practical consequence is that a model with a favorable scaling curve can still lack the approximation capacity for the specific function you need. The scaling law measures how efficiently the model learns the statistics it sees. But if the function you care about has structural properties that fall outside what the architecture can efficiently represent, adding more parameters helps only up to a point — and that point is not predicted by the scaling law.

This matters for procurement. Teams choose model families based on published scaling curves and benchmark leaderboards. What they're actually buying is good approximation of the training distribution. Whether the deployment function resembles that distribution is a separate question the scaling law does not address.

The approximation theory perspective suggests where to look when scaling stops helping. Functions with sparse piecewise structure, periodic components, or localized high-frequency features can exhibit inverse scaling behavior — more parameters produce worse approximation, not better. This is not a bug in the model; it's a mismatch between the function class the architecture was designed for and the function class the deployment requires. A function with sharp transitions — a sudden price change in a trading signal, a step change in sensor output — requires a specific architectural inductive bias to approximate efficiently. Without it, scale alone won't close the gap.

What changed my mind was working backward from deployment failures. I had been tracking scaling curves and benchmark improvements for months while a specific failure mode persisted: certain structured inputs caused systematic errors regardless of model size. The benchmark scores improved. The failure mode did not. The gap was not a measurement artifact. It was a structural mismatch between what the scaling law measured — statistical efficiency on the training distribution — and what the deployment required — approximation of a specific functional form with sharp localized features. Fixing it required changing the architecture, not the scale.

The useful diagnostic is not "how does test loss scale with compute?" It's "what function class does this architecture represent efficiently, and does my deployment function fall in that class?" A practitioner with a background in approximation theory could answer the second question faster than someone running scaling sweeps. The scaling roadmap doesn't ask it.

The strongest signal in model selection is usually: where does this architecture provably fail? The scaling law doesn't contain that information.
