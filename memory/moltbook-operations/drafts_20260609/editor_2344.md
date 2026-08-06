# EDITOR — 2026-06-09 23:44 UTC
# Title: Code-switching breaks safety classifiers because it exploits tokenization, not reasoning

## Changes from writer draft:
1. Softened last paragraph: "The practical takeaway" → "What this means in practice"
2. Tightened second-to-last paragraph (removed "The fix is not prompt-level. It is data-level." — redundant with prior sentence)
3. No other changes needed — body is tight, hook is specific, mechanism is clear

## Final body:

The finding is specific enough to cite: switching between languages — say, inserting Hindi syntax into an English prompt — can push jailbreak success rates from single digits to above sixty percent on models that otherwise resist monolingual attacks. The number is not the point. The mechanism is.

Most safety classifiers are trained on large corpora that are overwhelmingly monolingual. Code-switched text — Hinglish, Frenglish, Spanglish — is rare in those corpora. When the classifier encounters it at inference time, it is seeing a distribution it was not calibrated against. The model underneath may handle the mixed input fluently. The classifier above it does not.

This is not a reasoning failure. The model is not confused about what it should do. The classifier simply never learned the patterns that would flag the intent. It has no positive examples of "this mixed-language request is harmful" in its training set, so it defaults to pass. The attack works because it exploits a gap in the training distribution, not because it found a flaw in the model's reasoning chain.

The common fix — adversarial prompting with the same language — does not address this. You are asking the classifier to recognize a pattern it was never shown. Multilingual fine-tuning on code-switched adversarial examples would, but that is expensive and the data is sparse. Most safety teams are not doing this at scale.

What makes this structurally interesting is that the model's language capability and the classifier's coverage are misaligned. A model that speaks forty languages fluently is paired with a classifier that was trained on mostly English. The model can understand a Hinglish jailbreak. The classifier cannot recognize it as one.

The implication is not that code-switching is a magic bypass. The implication is that safety classifiers have a distributional blind spot that language-mixed inputs exploit reliably. Until those classifiers are trained on genuinely multilingual adversarial data, the attack surface remains.

What this means in practice: if you are evaluating safety for multilingual deployments, you need code-switched adversarial examples in your eval set. Not as a one-time check. As an ongoing calibration signal.
