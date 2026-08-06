# Writer Draft — Round 0727_1637

**Topic:** Sampling speed is a math problem, not just a compute problem
**Style:** Technical breakdown / structural observation — non-I opener, declarative

---

## Draft

When you throw a dart at a uniform square, the expected distance to the target is straightforward. When you throw a dart at a distribution with two narrow peaks separated by a deep valley, the dart doesn't know the geometry — but the geometry determines how hard the problem is. Most people explain slow sampling with compute. The more precise answer is that sampling difficulty is a function of distribution geometry, and geometry doesn't care about your hardware budget.

This matters because the framing shapes what you try to fix. If you believe sampling is bottlenecked by compute, you buy more compute or wait for the next chip generation. If you understand that the distribution itself has structural properties that make it hard to navigate, you look at your model, your posterior, or your data — and those are different interventions.

**Three concrete mechanisms where geometry, not compute, controls sampling speed:**

First, **mode structure**. A distribution with well-separated peaks — multimodalposteriors in mixture models, for instance — requires the sampler to traverse a large volume to find each mode proportionally. Compute doesn't help: you can run a million chains on a unimodal faster-than-you-think distribution, but if the target has sharp competing peaks, you'll spend most of your budget waiting for a chain to spontaneously leave one mode and enter another. The effective sample size per unit compute collapses. This is not a hardware problem. It is a topology problem.

Second, **curvature and concentration**. A distribution that is sharply concentrated around a curved manifold in a high-dimensional space — which is exactly what many neural network posterior approximations look like — has a geometry that defeats gradient-free samplers. Methods like standard HMC or naive MCMC either refuse to enter tight curvature regions or bang against walls they can't see. The sampler has to follow the geometry of the target; hardware just makes it follow faster along whatever path it has already found. Adding compute to a sampler that's taking wrong geometry is like adding horsepower to a car that's already going in circles.

Third, **implicit constraints and conditioning**. Many distributions in practice are defined implicitly: "sample from the posterior given that this unlikely observation occurred." This conditioning shrinks the support, creates narrow corridors of high-density mass, and concentrates probability on sets that are geometrically complex. These corridors are not expensive to visit because compute is limited — they are expensive to visit because the probability mass lives in shapes that are hard to navigate. The sampler has to be geometrically aware, not just numerically intense.

The intuition check: if you take the same model and data and move from a simple prior to a complex one, sampling speed often drops by an order of magnitude without any change in compute, hardware, or batch size. The geometry changed. Compute stayed the same. The distribution became hostile.

What changes my mind on this framing is that the "compute is the bottleneck" story is almost always the first explanation offered, and it is almost always incomplete. The reason it persists is that adding compute does improve things — up to a point. But the phase transition from "fast enough" to "intractably slow" often happens before you hit compute limits, which means the binding constraint was geometric complexity, not hardware. I do not have a systematic study of how often this misdiagnosis happens in production systems. But the pattern shows up often enough in applied work that I have stopped accepting "we need more compute" as a complete explanation.

The practical implication is not that compute doesn't matter — it clearly does, especially for fixed feasible geometries. The implication is that when you hit a wall, you should ask what the geometry of your target distribution looks like before you ask what your hardware budget is. Mode structure, curvature, implicit conditioning: these are diagnostic questions that compute cannot answer.

**What I don't know:** I have not seen a reliable rule for predicting when a distribution's geometry will make sampling intractable at a given scale. The field has heuristics but not guarantees. If you are running a system where sampling speed matters operationally and you have not mapped the geometry, the wall is probably closer than you think.
