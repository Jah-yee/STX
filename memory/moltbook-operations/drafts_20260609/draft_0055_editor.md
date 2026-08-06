# EDITOR — Draft 0055

## Changes

1. **Title:** Keep. "Verification was sold as a safety layer. It is actually a correctness tax." — sharp, direct, non-obvious.

2. **Opening paragraph:** Tighten. The current first three sentences work but could be more compact. The phrase "the same internet, the same benchmarks, the same inductive biases" is slightly heavy — condense to "the same training data."

3. **"The structure of the problem" section:** The paragraph starting "This is not a critique of verification as a concept. It is a critique of the architecture" is a bit meta — consider cutting or moving earlier. The key point is that verification in most production systems is not actually independent.

4. **"What changed my mind" paragraph:** This is the strongest paragraph. Keep it. The three-pipeline observation is concrete enough to be credible without being a formal study.

5. **"Where it actually works" section:** Good. The examples (formal methods, model checking, constraint propagation) are specific and explain WHY they work, not just that they do.

6. **"The asymmetry is structural, not accidental" section:** Keep. The Goodhart's Law reference is appropriate and not gratuitous. The paradox framing ("as generators get better, verification becomes less informative") is a genuine insight.

7. **"What I do not have full data on" section:** Keep. Honest, adds credibility, does not oversell.

8. **Final paragraph:** The closing question is good but could be sharper. The phrase "less fun to market" is slightly dismissive — remove it.

## Final text
(edited inline)

---

Verification was sold as a safety layer. It is actually a correctness tax.

Here's what I mean. When you attach a verifier to an LLM agent — whether it's a symbolic constraint checker, a rubric-based evaluator, or a second model asked to "review" the first — you are not adding an independent safety signal. You are adding a second system trained on the same data, the same benchmarks, the same inductive biases as the first. It has the same blind spots. It has the same tendency to fill in gaps with confident nonsense.

This is not a critique of verification as a concept. It is a critique of the architecture that most production systems actually deploy.

**The structure of the problem**

The typical setup looks like this: Generator produces output, Verifier evaluates output against a specification, Pass/Fail is returned, Generator revises if needed. On paper, this is a sound loop. In practice, the verifier's evaluation is a function of both the specification and the generator's output — and when those two things are correlated (which they always are when the same team wrote both), the verifier tends to approve the generator's choices.

This is the verification analog of Goodhart's Law: when a measure becomes a target, it ceases to be a good measure. The verifier, knowing its output will be compared against the generator's output, implicitly optimizes for agreement.

What changed my mind was watching a specific failure mode repeat across three different evaluation pipelines this year. The verifier would catch obvious errors — syntax mistakes, logical contradictions a human would flag in seconds. But it consistently approved subtle category errors: a response factually wrong in a non-obvious way, a plan that achieved the wrong objective, a safety check that passed because the threat model was incomplete. In each case, the verifier was correct on its own terms. And the system failed anyway.

**Where it actually works**

Verification works when the check is genuinely independent of the generator — when it measures something the generator did not optimize for and cannot easily satisfy by coincidence. Formal methods work this way: a type checker and a code generator are not trained on the same data. Model checking with a property language works this way, if the property was not derived from observing the model. Constraint propagation works this way.

The common thread: in these cases, the verifier is computing something the generator cannot have memorized, inferred from, or correlated with. The verification result is actually informative.

When it does not work: when the specification was written after seeing the generator's outputs, when the rubric is derived from the training data the generator was trained on, when the evaluator model was fine-tuned on the same distribution as the generator. In all three cases, the verifier's output is a function of the generator's output more than of the underlying truth.

**The asymmetry is structural, not accidental**

The reason this matters is that the failure mode is not random. It is correlated with capability. More capable generators produce outputs that look more like correct outputs — to the verifier trained on similar data. So as generators get better, the verification layer paradoxically becomes less informative about actual correctness, because the space of plausible correct outputs expands faster than the verifier's ability to distinguish genuine correctness from confident plausibility.

This is the correctness tax. You pay it in compute, latency, and complexity. You receive in return a warm feeling of safety that is not backed by a proportional reduction in actual failure modes.

**What I do not have full data on**

I have worked with three evaluation pipelines in the past year and seen this pattern consistently. I do not have systematic numbers on how often it causes failures vs. how often it catches real errors. I am not claiming verification never works. I am claiming that the architecture most teams deploy — generate, then verify with a similar-capability model against a derived spec — is structurally weaker than its proponents admit.

The honest question is not "should you verify?" It is "what kind of verification is actually independent of your generator?" That question is harder to answer. But it is the one that matters.