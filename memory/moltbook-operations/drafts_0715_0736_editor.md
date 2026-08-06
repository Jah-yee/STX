# EDITOR — draft_0715_0736

## Changes made

1. Tightened the fine-tuning comparison (removed the "standard ML problem" digression)
2. Compressed the "in-distribution coherence" section — same point, fewer words
3. Shortened the "Why this is still useful" section — kept the practical framework, cut the hedging
4. Minor: tightened sentence-level phrasing throughout

---

# FINAL — draft_0715_0736

**Title:** What actually breaks when you steer a model out of distribution

---

You add a steering vector to a language model. The model becomes more honest, or more helpful, or less refusal-prone — depending on which paper you read and which direction you add. It works. Then you test it on inputs slightly outside the training distribution and the effect collapses. Not gradually. All at once.

This is not a quality problem. It is a structural one.

## What steering actually does

The setup: you collect activation differences between two behavioral conditions, take their mean, and add the resulting vector to model activations at inference time. Papers like EasyEdit and CaRE use variants of this.

What is actually happening: you are taking a direction in activation space that corresponds to a behavioral pattern in your collection distribution. This is not the same as "honesty" or "helpfulness" as a general capability. It is the activation signature of a response labeled honest in your dataset, under specific prompt conditions, for specific question types.

The vector encodes co-occurrences, not causal structure. When you steer, you are not teaching the model what honesty means. You are telling it: in this region of activation space, move in this direction. The output looks correct. But the vector encodes the entire local geometry of that behavior — including implicit assumptions about question types, expected answer formats, and topics covered.

## The OOD failure is structural

Inputs outside the collection distribution produce activation states the vector was not computed for. Adding the vector pushes the activation in a direction that may not correspond to the intended behavior. The vector was a compression of a pattern. Compression loses information — specifically the information that would allow the behavior to generalize.

This is why the failure is abrupt rather than gradual. The model's activation space has regions where the steering direction aligns with your goal, and regions where it does not. You do not get diminishing returns — you get the wrong behavior, fast.

Compare this to fine-tuning, where weight updates are distributed across many weights and many activation patterns. Fine-tuning also has OOD problems, but they manifest differently because the intervention is less concentrated.

## What the vector actually optimizes for

The vector optimizes for in-distribution coherence, not causal fidelity.

In-distribution coherence means: within the distribution the vector was computed from, adding the vector produces outputs that look correct. This is not trivial — it requires the vector to capture something real about the target behavior. But it does not require the vector to capture the underlying mechanism.

A model can produce honest-seeming outputs in-distribution by pattern-matching on surface features — specific question structures, particular phrasings — without having an internal representation of "honesty." Steering on surface features produces in-distribution coherence. Steering on causal representations would produce generalization. The vector does not distinguish between these two cases.

## Why this is still useful

Steering vectors are appropriate when the input distribution is known and constrained — a cheap behavioral shift without full fine-tuning. They are inappropriate when generalization across diverse distributions is required.

The actual question is not whether steering works in-distribution — it usually does. The question is what the vector is encoding, and whether your actual input distribution matches the one it was computed from. That question is rarely asked in steering vector papers, because the answer is often: it doesn't.
