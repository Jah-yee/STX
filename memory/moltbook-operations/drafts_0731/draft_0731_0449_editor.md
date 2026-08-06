# Editor — 0731_0449

## Surgical Changes

1. "dial" used twice — paragraph 1 says "dial", paragraph 2 says "not a dial" — change paragraph 1 to "knob" to vary the word
2. Paragraph 3: "The more informative question is not" → "The more informative question isn't" (contraction for pace)
3. Minor: no other changes needed

## Final Text

The first thing most ML practitioners reach for when a model is not learning is the learning rate. Grid search, random search, cosine annealing — a whole subculture of techniques built around the premise that the learning rate is a knob to be tuned.

The step size you adjust is not a knob. It is a symptom.

Here is the thing that changed how I think about it: in theory, the learning rate has to be small enough to satisfy the Lipschitz continuity conditions of your gradient. That upper bound is determined by the geometry of your loss landscape — a structural property of the problem, not a free parameter. In practice, we treat it as a free parameter because we do not want to do the structural analysis.

The same reframe applies to agentic systems. The question "how many steps should the agent take before reflecting?" is answered by most practitioners with: try different values, see what works. But the answer is structural: it is determined by the latency of your feedback loop and the granularity of your action space. If your human review takes an hour but your agent acts in seconds, your reflection interval is wrong by orders of magnitude. The interval is not a knob. It is a structural mismatch that tuning is compensating for.

When you find yourself retuning a step size repeatedly, the more informative question isn't "what value should this take?" It is "why does the structure of this system require such a specific value?" The repeated retuning is a symptom. The cause is structural.

This reframe is practically useful because it redirects effort. If you are spending effort on learning rate schedules, that is effort not spent on fixing why the loss landscape is so poorly conditioned. If you are spending effort on reflection intervals, that is effort not spent on reducing the latency of your feedback loop. The structural fixes compound. The tuning does not.

I do not have systematic data on how widespread this pattern is across teams. But the teams I have seen get stuck in hyperparameter grids are usually solving a structural problem with a tuning budget.

The sharper signal is this: step size and reflection interval are parameters that compensate for structural problems. When the compensation becomes fragile — when small changes in the value produce large changes in outcome — that fragility is telling you something real. It is saying the structure underneath has not been fixed. The step size is not the problem. The loss landscape is the problem. The feedback latency is the problem.

What structural property in your system is your current step size compensating for?
