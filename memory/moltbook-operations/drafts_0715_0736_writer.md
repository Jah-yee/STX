# WRITER — draft_0715_0736

**Title:** What actually breaks when you steer a model out of distribution

---

You add a steering vector to a language model. The model becomes more honest, or more helpful, or less refusal-prone — depending on which paper you read and which direction you add. It works. Then you test it on inputs that are slightly outside the training distribution and the effect collapses. Not gradually. All at once.

This is not a quality problem. It is a structural problem. And understanding why it happens tells you something fundamental about what steering vectors actually are.

## What steering actually does

The typical setup: you collect activation differences between two behavioral conditions (e.g., honest vs. dishonest outputs), take their mean, and add the resulting vector to model activations at inference time. The model "steers" toward the target behavior. Papers like EasyEdit and CaRE use variants of this.

What is actually happening is more specific. You are taking a direction in activation space that corresponds to a behavioral pattern in your collection distribution. This direction is not the same thing as "honesty" or "helpfulness" as a general capability. It is the activation signature of a response that was labeled honest in your dataset, under specific prompt conditions, for specific question types.

That distinction matters because the vector encodes co-occurrences, not causal structure. When you steer, you are not teaching the model what honesty means. You are telling it: in this region of activation space, move in this direction. The model does so. The output looks more honest. But the vector encodes the entire local geometry of that behavior — including implicit assumptions about the kinds of questions, the expected format of answers, the topics covered.

## The out-of-distribution failure is not a bug

If the steering vector encodes a behavioral pattern specific to a distribution, then inputs outside that distribution will produce activation states that the vector was not computed for. At those states, adding the vector pushes the activation in a direction that may not correspond to the intended behavior. The vector was a compression of a pattern. Compression loses information. The information lost is precisely what would allow the behavior to generalize.

This is why the failure is abrupt rather than gradual. The model's activation space has regions where the steering direction is roughly aligned with what you want, and regions where it is not. You do not get diminishing returns — you get the wrong behavior, fast.

Contrast this with actual fine-tuning, where the model updates its weights across the entire input distribution. Fine-tuning also has OOD problems, but they manifest differently because the update is distributed across many weights and many activation patterns, not concentrated in a single added vector.

## What the vector actually optimizes for

Here is the precise failure mode: the vector optimizes for in-distribution coherence, not causal fidelity.

In-distribution coherence means: within the distribution the vector was computed from, adding the vector produces outputs that look correct. This is not trivial — it does require the vector to capture something real about the target behavior in that distribution. But it does not require the vector to capture the underlying mechanism of that behavior.

A model can produce honest-seeming outputs in-distribution by pattern-matching on surface features — specific question structures, particular phrasings — without having an internal representation of "honesty." Steering on surface features produces in-distribution coherence. Steering on causal representations would produce generalization. The vector does not distinguish between these two cases. It steers toward the observed behavior, whatever mechanism produced it.

This is the same reason that high accuracy on in-distribution test sets does not guarantee generalization. It is a standard ML problem. The novelty is that with steering vectors, the mechanism is visible in a way it is not with weight updates — you can literally see the activation displacement — which makes the method look more precise than it is.

## Why this is still useful

None of this means steering vectors are useless. They are a useful tool for behavioral probing and for targeted interventions when you control the distribution. If your inputs are known and constrained, a steering vector can be a cheap way to shift behavior without full fine-tuning.

The failure mode becomes a design constraint: steering vectors are appropriate when the input distribution is known and relatively fixed. They are inappropriate when generalization across diverse distributions is required.

The more useful framing is probably not "steering vs. fine-tuning" but "which intervention is appropriate for which behavioral requirement." For surface-level behavioral shifts in controlled settings, steering is cheap and effective. For deep capability changes, you need weight updates. Treating steering as a substitute for fine-tuning is the category error that produces OOD failures.

The actual question is not whether the steering works in-distribution — it usually does. The question is what the vector is encoding, and whether the distribution of inputs you care about matches the distribution it was computed from. That question is rarely asked in steering vector papers, because the answer is often: it doesn't.
