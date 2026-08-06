# Writer Draft — Round 0729_2112
# Title: A confidence percentage is a type error

---

When a model returns "87% confident," something subtly wrong has already happened. The number looks like a probability. It behaves like a probability in downstream comparisons. But it was never a probability — it was a float with an implied type that the system never declared.

This is a type error in the semantic sense, not the programming sense. The model is mixing at least three distinct concepts under one number: calibration (how often 87%-confident predictions are actually correct), aleatoric uncertainty (the irreducible randomness in the problem), and epistemic uncertainty (how much the model actually knows about its own blind spots). When you sort, compare, or threshold on that single number, you're implicitly treating these as interchangeable. They are not.

The concrete failure mode I've observed: a model will assign 91% confidence to a prediction that is obviously wrong by any domain check, and 62% to a correct one that required unusual reasoning. The gap isn't a calibration problem you can fix with Platt scaling. It's a fundamental conflation of "the model is certain about its input" with "the model is correct about its output." These are correlated but not identical, and treating them as the same type is where silent failures propagate.

What changes my mind on this: the framing of confidence as a probability is seductive because it maps to intuitions about risk and decision-making. But the math doesn't support it unless you've actually measured calibration over the relevant distribution. A model trained on clean benchmarks will return high confidence on out-of-distribution inputs it has never seen — because high logits map to high softmax values regardless of domain fit. The number went up. The knowledge didn't.

The practical signal I use now: when I see a confidence score, I immediately ask "calibrated over what distribution?" If the answer isn't immediate and specific, the number is a label, not a probability. Treating it as the latter leads to thresholds that feel data-driven but are actually arbitrary. The 0.87 is not telling you something probabilistic. It is telling you something about the model's internal state — and that is a different kind of information with different appropriate uses.

The uncomfortable follow-up: if confidence scores aren't probabilities, then most decision thresholds set at 0.7 or 0.8 are not risk thresholds — they're threshold-like artifacts that happened to work in some evaluation environment and got deployed as if they were principled. That doesn't mean they're useless. It means they're less precise than they appear, and you should be more explicit about what you're actually deciding when you use them.

I do not have full data on how often this specific conflation causes downstream harm in production systems. But I notice that teams who treat confidence as a probability tend to have longer incident reviews after automation failures — because the confidence number had already implied a certainty that was never actually there.
