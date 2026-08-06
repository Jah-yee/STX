# Writer Draft — Round 0731_0941

## Selected Title: What changes when acquisition functions become code

## Full Post

In Bayesian optimization, the acquisition function was a formula. UCB was a closed-form expression. Thompson sampling was a probability. You could write them on a whiteboard, derive their properties, and reason about convergence guarantees without running a single experiment.

That era is ending.

Across active learning pipelines, multi-armed bandit systems, and agent task-routing layers, the acquisition function is increasingly implemented as code — a branching logic tree, a heuristic weighting scheme, a learned reward model plugged into a selection routine. Not a formula. A program.

This is not a technical footnote. It changes what kind of reasoning is possible.

---

**The formula gave you something code does not: compositional guarantees.**

When your acquisition function is a formula, you can ask questions like: is this strictly concave? Does it have a unique optimum? What happens to the regret bound if I increase the exploration parameter? The math constrains the behavior in ways that are portable and checkable.

When your acquisition function is code, those questions don't have mathematical answers. You have execution traces. You have test cases. You have heuristic assertions about what the code should do in certain states — which may or may not hold in production when inputs drift.

The stronger signal is this: teams switch to code-based acquisition for flexibility, but flexibility here means the function can encode arbitrary logic that is no longer characterized by its mathematical properties. The "hyperparameters" stop being tunable floats and become the branching logic itself.

---

A concrete case that illustrates the shift: imagine a task-routing system where the acquisition function encodes "pick the worker that has successfully completed this task type most recently." In formula terms, that might look like a recency-weighted success rate. In code terms, it looks like an if-then chain with a threshold and a tiebreak rule. Both can represent the same heuristic. Only one gives you a regret bound.

This shows up most clearly in audit scenarios. When a formula-based acquisition underperforms, you can trace the mathematical mechanism: the exploration term is too small, the posterior is miscalibrated, the noise assumption is violated. When a code-based acquisition underperforms, you get a stack trace and a hypothesis about which branch is firing wrong.

---

There is a second-order effect worth naming: when acquisition lives in code, the function itself becomes a software artifact with its own engineering lifecycle. It gets refactored. It gets extended. It accumulates special cases. The original intent — "balance exploration and exploitation" — becomes embedded in logic that diverges from any clean interpretation.

I do not have full data on how widespread this divergence is. But I have observed it enough times to think it is systematic, not anomalous.

The practical implication for teams building these systems: the moment your acquisition logic is more than a few lines of arithmetic, the right question is not "what should the acquisition function optimize for?" but "what does this specific code do, and under what input conditions does it stop doing that?" Testing, not derivation, becomes the primary validation tool.

That is a meaningful shift in what it takes to maintain and trust the system.

---

What acquisition function patterns have you seen degrade in production — formula-based or code-based? What made the failure discoverable?
