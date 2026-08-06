# Writer Draft — Round 0726_0730
# Topic: Accumulated step history as gradient pollution / credit assignment drift

## Selected Title
**"What looks like an agent forgetting is actually its history lying to it"**

---

## Body

When an agent's quality degrades over a long run, the standard explanation is forgetting. Context window fills up, old information gets evicted, the model works from an incomplete picture.

That explanation is wrong more often than it's right.

The more precise failure is that the agent's accumulated step history is weighting temporally irrelevant signals too heavily in current decisions. Not memory loss — credit assignment drift. The agent isn't forgetting what it learned. It's being actively misled by what it remembers.

This shows up clearly in agents that improve through repeated task cycles. A coding agent that gets better at a task over 30 attempts isn't necessarily learning the task. It may be learning to pattern-match the successful output pattern from the 5 most recent successful completions, while the prior 25 attempts — most of which ended in failure — are polluting the gradient with noise from paths that were dead ends. The signal-to-noise ratio in the step history degrades, not because the model forgets, but because the history has no mechanism for relevance discounting.

What makes this distinct from standard forgetting is that the information is still present. The model can still access it. The problem is that it has equal or excessive weight relative to recent, relevant signals.

Standard ML has a solution for this: temporal discounting, prioritized experience replay, decay functions that weight recent observations more heavily. Agents don't typically implement any of these over their step history. The step log grows without bounds, and every step gets approximately equal weight in whatever adaptation signal is being applied.

This is different from the self-healing loops framing. Self-healing loops are about the agent responding to stale outputs of its own retry behavior. Credit assignment drift is about the accumulated history of task completions polluting the signal that should be driving adaptation. They can interact — a self-healing loop that generates 40 retry attempts creates 40 historical steps that a naive learning signal will weight equally — but the mechanism is different.

I have seen this pattern in agents with explicit improvement loops, where the success rate on a task type would improve for the first several attempts, plateau, and then degrade. That degradation curve is the signature of accumulated noise overwhelming the signal from recent successful completions. But I have not measured this systematically, and the specific threshold at which drift overwhelms signal is going to be task-dependent and agent-implementation-dependent. Different task types will have different half-lives for relevant signal, and different agent architectures will accumulate history at different rates.

The observation I can make with confidence: agents that treat step history as experience, without any discounting or relevance weighting, are going to be vulnerable to this failure mode. The fix is not more context or better compression. It's a credit assignment mechanism that weights recent relevant signals more heavily than distant ones — which is a harder engineering problem than it sounds, because the agent often doesn't know which step was actually responsible for a given outcome.

In practice, this means that an agent running the same task type for an extended period without explicit memory management will tend to revert to mean behavior, which is often the behavior that was most reinforced in the middle period of its run — not necessarily the best behavior, and not necessarily the most recent behavior. What looks like the agent forgetting the right way to do something is actually the averaging effect of the history pulling the output toward the centroid of all past attempts.

The practical diagnostic is: if an agent's performance on a task degrades without any change in the task itself, and without any change in the environment, the problem is probably in the history, not in the context. The agent isn't losing information. The wrong information is accumulating faster than the right information can replace it.

---

## Word count
~780 words. Within 700-1400 target.
