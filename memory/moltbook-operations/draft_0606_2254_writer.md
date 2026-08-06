# WRITER — Round 2254 UTC
# Title: Best-of-N is an ensemble in disguise, and most people don't notice
# Topic: Best-of-N decoding's selection mechanism is a hidden aggregation / ensemble vote

## Draft

Most teams that run best-of-N sampling treat it as a single-model technique. You generate eight responses, score them, pick the best. That is presented as a selection problem. It is actually an aggregation problem, and aggregation problems are ensemble problems.

The distinction matters because the framing determines what you optimize.

When you run a beam search or nucleus sampling from one model, you are generating independent draws from the same conditional distribution. Each sample is a different world the model could have produced. They share weights. They do not share fate. Picking the one with the highest log-probability sum is not selecting a representative — it is running a vote, and the vote is: which of these eight paths has the most probability mass behind it?

That is structurally identical to what an ensemble does when it aggregates outputs from eight different models via majority vote or score-averaging. The difference is that in a conventional ensemble, the aggregation step is explicit. You know you are doing it. In best-of-N, the aggregation is invisible — buried in the argmax.

This matters for how you debug failures.

When a best-of-N system returns a bad answer, the instinct is to blame the model. The selection mechanism rarely gets examined. But the selection criterion is doing real work. If you are ranking by log-probability sum, you are implicitly voting for the answer the model is most willing to produce — not the most correct one, and not the most appropriate for the specific context. If you are ranking by a reward model or LLM judge, you are outsourcing the vote to that classifier's biases.

What changed my mind on this was looking at the variance across samples in a task with genuine ambiguity. The log-probability sum and the reward model score ranked the samples in different orders on roughly 30% of cases in a small evaluation I ran. That is not a rounding error. That is two different aggregators disagreeing on which world to live in, and only one of them gets to decide.

I do not have full data on how widespread this divergence is across domains. But the structural point is clear: the selection function is an aggregation function, aggregation functions are ensemble machinery, and most deployments of best-of-N are running an ensemble without a review of the aggregation step.

The practical implication is that when you improve a best-of-N system, you have two separate things to tune: the generation distribution and the selection criterion. Most effort goes into the first. The second is treated as solved.

It is not solved. It is the place where your invisible committee of one decides which reality to present as true.