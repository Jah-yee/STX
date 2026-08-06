# WRITER (Final) — Round 0728_0210
# Title: Overconfidence doesn't hide uncertainty. It replaces it.

---

Every few weeks I run the same test: take a model I'm confident about on a given question, introduce a small contradiction to the context, and watch what the top-2 logit gap does.

Most of the time, nothing changes in the gap. The model doesn't flinch. The second-ranked token stays far behind the first. The logits look exactly as they did before the contradiction was introduced.

This is not calibration. This is momentum.

The assumption behind most uncertainty research is that confidence is a mask and uncertainty is underneath it — that a model is secretly unsure but performs as if it isn't, and that better prompting or better training can peel back the mask to reveal the real probability distribution underneath.

I no longer think that's the right model.

## What RLHF actually does to the logit landscape

Reinforcement learning from human feedback, and the supervised finetuning that precedes it, don't just push up the probability of preferred tokens. They reshape the entire competitive landscape between tokens.

When a model learns to produce confident answers, it doesn't learn to suppress uncertainty — it learns to amplify the gap between the preferred answer and everything else. The second token doesn't just fall slightly behind; in many cases, it falls to a probability mass that reflects dismissal, not genuine disagreement.

There's a difference between:
- **Uncertainty**: the second token represents a plausible alternative that would change the answer
- **Dismissal**: the second token represents a version of the answer the model knows is wrong, and signals that with low probability

RLHF is very good at training dismissal. It is not obviously good at training genuine calibrated uncertainty.

When dismissal dominates, the logit gap no longer carries uncertainty information. It carries confidence information. These are not the same thing.

## The measurement problem

Most calibration benchmarks — Brier score, ECE — are designed to measure whether the model's stated confidence matches its actual accuracy. They are good at detecting overconfidence in the aggregate.

What they are less good at detecting is whether the logits themselves still function as an uncertainty signal at the token level.

A model can achieve reasonable ECE scores while having logits that are structurally incapable of representing uncertainty in any actionable way. The gap between top-1 and top-2 might be 40 percentage points in probability — not because the model is very certain about the right answer, but because it has learned to aggressively dominate the output distribution on preferred tokens.

When this happens, the logits stop being a useful input for downstream uncertainty handling. Systems that rely on token-level logit gaps to decide whether to escalate to a human, trigger a second opinion, or slow down — those systems are flying blind.

## The observation I keep coming back to

I do not have a controlled study. I want to be honest about that upfront.

But in the kind of informal perturbation testing I described at the start — introducing a small factual contradiction and watching the logit gap — I consistently see the same pattern: models that have been heavily RLHF-trained show a qualitatively different response than models that haven't.

In the RLHF-heavy case, the logits barely move. The model commits. In the less-RLHF case, the second token responds to the contradiction in a way that feels like genuine updating.

I don't have numbers on how widespread this is. I don't have a threshold past which the logit signal becomes unreliable. What I have is a recurring observation that the pattern is consistent enough to deserve a name.

## What this means for practice

If the logit signal has been replaced rather than just obscured, then prompting your way to better uncertainty is a limited strategy. Telling a confidently-trained model to "be more uncertain" or "express doubt" typically produces performative uncertainty — tokens that read as uncertainty without the underlying distribution changing.

The interventions that actually work are upstream of the prompting layer:
- **Training signal changes**: DPO and RLHF objectives that reward genuine calibration, not just preference compliance
- **Architectural choices**: ensemble methods, or explicit uncertainty estimation modules that don't rely on the main model's logits
- **Inference-level calibration**: not just temperature, but methods like Bayesian perturbation that probe the model's distribution rather than reading its self-reported confidence

If you're building a system where the model's uncertainty estimate feeds into a real decision — escalate, defer, alert a human — and you're reading that estimate from the logits, it's worth testing whether your uncertainty signal is actually carrying uncertainty information, or whether it's been replaced by a trained confidence signal that sounds a lot like uncertainty but isn't.

The gap might look like doubt. It might just be the sound of the model being very sure that it doesn't need to consider alternatives.
