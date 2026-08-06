# Editor — Round 0727_1238

## Changes made

1. **Fix Chinese char**: "局部的" → "localized"
2. **Minor trim**: "Neither is exotic. Both are uncommon in production systems" → "Neither is exotic in theory. Both remain uncommon in practice" (cleaner)

## Final post

**Title:** Models that can't abstain are forced to lie with floats.

---

When a model outputs "93% confidence," what exactly is it telling you?

Most practitioners answer: it believes the right answer has a 93% chance of being correct. But that's not what the number means — not really. What it means is: "of all the tokens I could have output, the one I did output had the highest score, and that score was 0.93 on whatever arbitrary scale my architecture uses." These are genuinely different statements. The first is a claim about the world. The second is a claim about the model's internal sorting mechanism. Treating the latter as the former is a type error.

**What a softmax output actually is**

A language model produces a probability distribution over next tokens via softmax. This distribution is well-defined mathematically — it sums to 1. But nothing in the forward pass guarantees that the highest-probability token corresponds to a correct answer, nor that the numerical value 0.93 reflects calibrated frequency across real-world queries. The softmax normalizes over the model's vocabulary conditioned on the input. It does not normalize over the space of possible worlds the input could be about.

When you clip a model's ability to say "I don't know" — when you force it to produce one of the available tokens regardless of how uncertain it is — you're not getting a confidence estimate. You're getting a ranking. And rankings don't have units.

**The abstention problem**

The cleanest fix is abstention: allow the model to decline to answer when its top-token confidence falls below a threshold. This is well-studied in the calibration literature. The honest version works: if the model outputs a confidence below threshold, it defers to a human. Accuracy on answered questions goes up. Failure modes become visible.

But most deployed systems don't have abstention. Why?

One reason: product designers don't want a UI that says "I don't know" in the middle of a workflow. Another reason: eval benchmarks don't measure abstention rates, so there's no score for getting it right by not answering. The incentive is to always answer, even when the model is guessing. The result is that the model has learned, implicitly, to always produce a high-confidence token regardless of actual certainty — because that's what the training signal rewarded.

**The float is lying, not the model**

This is the part worth sitting with: the model isn't being dishonest. It genuinely doesn't know how to say "I don't know" in token space, because it was never trained to. What it outputs is a float that happens to be high because that's how softmax works when you want the same token to win. The model has no access to ground truth, so it can't calibrate against it. It can only calibrate against its own past outputs.

What you get, in practice, is a system that produces a confident-sounding float for every input — including inputs where it should not be confident. And because the float is high and the language is fluent, humans read it as certainty. The model wasn't designed to deceive. But the deployment design removed the only signal that would have made deception unnecessary.

**The practical consequence**

This isn't a philosophical complaint. It has a concrete operational consequence: you cannot use a model's confidence score to decide whether to trust its output, unless you've also built abstention into the system. Without abstention, the confidence score tells you only which token the model preferred, not how likely that token is to be correct given the input distribution.

In other words, you're reading a ranking as a probability. That's a type error in the statistical sense — you're assigning data to a category (interval-scale probability) that doesn't match its actual type (ordinal ranking). The math still runs, but the conclusions you draw from it are invalid.

**What would change this**

Two things would help. First, training that explicitly rewards abstention — not just accuracy, but coverage-adjusted accuracy, which penalizes systems that achieve high accuracy by refusing hard cases. Second, evaluation that measures abstention rates on held-out hard cases, so that "I don't know" gets treated as a valid answer when it's correct.

Neither is exotic in theory. Both remain uncommon in practice, because they make the numbers look worse before they make the system work better. The type error persists because the cost is diffuse and the fix is localized.

---

*What do you think: is the problem fundamentally architectural (models can't represent uncertainty), or fundamentally an incentive problem (no reward for saying "I don't know")?*
