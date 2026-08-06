# EDITOR — Round 0721_1742

## Editor's pass on draft_0721_1742_writer.md

### Changes made:

1. **Opening line**: "Most automated hyperparameter optimization is an expensive way to confirm what you already believe." — keep. Strong hook, no change.

2. **Second paragraph**: "The process looks rigorous. It is actually a local search with better marketing." — keep. Good directness.

3. **The two-experiment case**: tighten. "The first used a quick informed search — Bayesian optimization with a smart acquisition function." → "The first used Bayesian optimization." (cut the marketing fluff). "The second used a slower method: a deliberately adversarial search" → "The second used a deliberately adversarial strategy." Keep the finding specific.

4. **"The failure space is the validation set you are not measuring."** — keep as-is. This is the sharpest line.

5. **"I do not have a clean answer"** — keep as-is. Honest.

6. **Closing paragraph**: "if your HPO run would produce the same failure modes regardless of which configuration it returned" — this is the right test. Keep.

### Final text:

---

Most automated hyperparameter optimization is an expensive way to confirm what you already believe.

A typical workflow: pick an HPO library, define a search space, let it run for a fixed budget, report the best config. The process looks rigorous. It is actually a local search with better marketing. It finds the peak in the region it sampled most densely — which is usually the region closest to your starting point.

Efficiency metrics measure wall-clock time. Coverage metrics measure how much of the space you actually looked at. These are different things, and most teams only measure the first.

The failure space is the part of the search distribution where your model breaks. It is not random. It clusters around boundary conditions, input distributions the training set under-represented, and interaction effects between hyperparameters that are only visible at specific value combinations. You cannot sample your way into it with uniform random search, no matter how fast your sampler runs.

What changed my mind was running two simultaneous HPO experiments on the same model, same search space, same budget. The first used Bayesian optimization. The second used a deliberately adversarial strategy that oversampled regions predicted to perform poorly. It found two configurations that failed in ways the first never surfaced. Those failure modes were present in the validation set. They were not present in the region the Bayesian search chose to explore.

The failure space is the validation set you are not measuring.

I do not have a clean answer for how to systematically explore it. But I have noticed that the fastest HPO runs consistently return configs that fail in the same way the baseline failed — just slightly less. The failure mode is structural. It is a property of the search space, not the model. No amount of wall-clock efficiency fixes it.

The practical check: if your HPO run would produce the same failure modes regardless of which configuration it returned, you are not optimizing. You are selecting.
