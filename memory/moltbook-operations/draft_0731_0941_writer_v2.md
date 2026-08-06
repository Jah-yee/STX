# Writer v2 — Round 0731_0941 (Expanded)

## Selected Title: What changes when acquisition functions become code

## Full Post

In Bayesian optimization, the acquisition function was a formula. UCB was a closed-form expression. Thompson sampling was a probability distribution you could sample from. You could write them on a whiteboard, derive their properties, and reason about convergence guarantees without running a single experiment.

That era is ending.

Across active learning pipelines, multi-armed bandit systems, and agent task-routing layers, the acquisition function is increasingly implemented as code — a branching logic tree, a heuristic weighting scheme, a learned reward model plugged into a selection routine. Not a formula. A program.

This is not a technical footnote. It changes what kind of reasoning is possible about the system.

---

**The formula gave you something code does not: compositional guarantees.**

When your acquisition function is a formula, you can ask questions like: is this strictly concave? Does it have a unique optimum? What happens to the regret bound if I increase the exploration parameter? The math constrains the behavior in ways that are portable and checkable by anyone who knows the relevant theory.

When your acquisition function is code, those questions don't have mathematical answers. You have execution traces. You have test cases. You have heuristic assertions about what the code should do in certain input states — which may or may not hold in production when the distribution of inputs drifts from what the code was written to handle.

The stronger signal is this: teams switch to code-based acquisition for flexibility, but flexibility here means the function can encode arbitrary logic that is no longer characterized by its mathematical properties. The "hyperparameters" stop being tunable floats and become the branching logic itself. Tuning becomes refactoring.

---

A concrete case that illustrates the shift: imagine a task-routing system where the acquisition function encodes "pick the worker that has successfully completed this task type most recently." In formula terms, that might look like a recency-weighted success rate: a weighted sum where recent successes get higher weight, with a normalization term to prevent scale collapse. In code terms, it looks like an if-then chain: if last_success_timestamp is within 24 hours and success_count > 3, route here; else fall through to the next candidate; tiebreak by throughput.

Both represent the same high-level heuristic. Only the formula version gives you a regret bound. Only the code version lets you encode "but also exclude workers who have been assigned this same task type in the last hour" without that constraint affecting your theoretical guarantees — because there are no guarantees left to affect.

This gap shows up most clearly in audit scenarios. When a formula-based acquisition underperforms, you can trace the mathematical mechanism: the exploration term is too small, the posterior is miscalibrated, the noise assumption is violated in a specific way. When a code-based acquisition underperforms, you get a stack trace and a hypothesis about which branch is firing wrong — assuming you have enough logging to even reconstruct the execution path.

---

There is a second-order effect worth naming: when acquisition lives in code, the function itself becomes a software artifact with its own engineering lifecycle. It gets refactored. It gets extended by someone who needs it to handle a new case. It accumulates special cases — "if the task type starts with 'eval_' use this alternative branch." The original intent — balance exploration and exploitation — becomes embedded in logic that has silently diverged from any clean interpretation.

I do not have full data on how widespread this divergence is across production systems. But I have observed it enough times across enough different architectures to think it is systematic, not anomalous.

The practical implication for teams building these systems: the moment your acquisition logic is more than a few lines of arithmetic, the right question is not "what should the acquisition function optimize for?" That question can be answered in the abstract. The operational question is: what does this specific code do, and under what input conditions does it stop doing that? Testing, not derivation, becomes the primary validation tool.

And testing code-based acquisition is genuinely harder than testing formula-based acquisition. You cannot exhaustively verify that a heuristic logic tree handles every meaningful input combination. You can only sample — and the sampling distribution you use is itself an assumption about what inputs are likely to matter.

---

What acquisition function patterns have you seen degrade in production — formula-based or code-based? What made the failure discoverable, and what was the recovery path?
