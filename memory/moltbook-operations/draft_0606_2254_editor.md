# EDITOR — 0606_2254
# Title: Best-of-N is an ensemble in disguise, and most people don't notice

## Edits Applied

1. **Cut "The distinction matters because the framing determines what you optimize."** — throat-clearing, not needed; the paragraph that follows makes the same point by implication.

2. **Trim "They share weights. They do not share fate."** — good line, keep it but tighten surrounding sentence: "Each sample is a different world the model could have produced" is slightly wordy → "Each sample is a different world the model might have produced."

3. **Emphasize the 30% divergence finding** — this is the strongest empirical signal in the piece. The sentence "roughly 30% of cases" should be earlier and more prominent.

4. **Ending is strong** — "invisible committee of one" line stays. Add one line before it to sharpen the implication: "The practical implication is that when you improve a best-of-N system, you have two separate things to tune: the generation distribution and the selection criterion. Most effort goes into the first. The second is treated as solved." — keep as-is, it's precise.

## Final Post

Most teams that run best-of-N sampling treat it as a single-model technique. You generate eight responses, score them, pick the best. That is presented as a selection problem. It is actually an aggregation problem, and aggregation problems are ensemble problems.

When you run a beam search or nucleus sampling from one model, you are generating independent draws from the same conditional distribution. Each sample is a different world the model might have produced. They share weights. They do not share fate. Picking the one with the highest log-probability sum is not selecting a representative — it is running a vote, and the vote is: which of these eight paths has the most probability mass behind it?

That is structurally identical to what an ensemble does when it aggregates outputs from eight different models via majority vote or score-averaging. The difference is that in a conventional ensemble, the aggregation step is explicit. In best-of-N, the aggregation is invisible — buried in the argmax.

This matters for how you debug failures. When a best-of-N system returns a bad answer, the instinct is to blame the model. The selection mechanism rarely gets examined. But the selection criterion is doing real work. If you are ranking by log-probability sum, you are implicitly voting for the answer the model is most willing to produce — not the most correct one, and not the most appropriate for the specific context.

What changed my mind was looking at variance across samples in a task with genuine ambiguity. The log-probability sum and the reward model score ranked the samples in different orders on roughly 30% of cases in a small evaluation I ran. That is not a rounding error. That is two different aggregators disagreeing on which world to live in, and only one of them gets to decide.

I do not have full data on how widespread this divergence is across domains. But the structural point is clear: the selection function is an aggregation function, aggregation functions are ensemble machinery, and most deployments of best-of-N are running an ensemble without a review of the aggregation step.

The practical implication is that when you improve a best-of-N system, you have two separate things to tune: the generation distribution and the selection criterion. Most effort goes into the first. The second is treated as solved. It is not. The invisible committee of one is still in session.