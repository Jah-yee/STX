# WRITER — 2026-06-09 23:44 UTC
# Title: Code-switching breaks safety classifiers because it exploits tokenization, not reasoning

## Draft

The finding is specific enough to cite: switching between languages — say, inserting Hindi syntax into an English prompt — can push jailbreak success rates from single digits to above sixty percent on models that otherwise resist monolingual attacks. The number is not the point. The mechanism is.

Most safety classifiers are trained on large corpora that are overwhelmingly monolingual. Code-switched text — Hinglish, Frenglish, Spanglish — is rare in those corpora. When the classifier encounters it at inference time, it is seeing a distribution it was not calibrated against. The model underneath may handle the mixed input fluently. The classifier above it does not.

This is not a reasoning failure. The model is not confused about what it should do. The classifier simply never learned the patterns that would flag the intent. It has no positive examples of "this mixed-language request is harmful" in its training set, so it defaults to pass. The attack works because it exploits a gap in the training distribution, not because it found a flaw in the model's reasoning chain.

The common fix — adversarial prompting with the same language — does not address this. You are asking the classifier to recognize a pattern it was never shown. Multilingual fine-tuning on code-switched adversarial examples would, but that is expensive and the data is sparse. Most safety teams are not doing this at scale.

What makes this structurally interesting is that the model's language capability and the classifier's coverage are misaligned. A model that speaks forty languages fluently is paired with a classifier that was trained on mostly English. The model can understand a Hinglish jailbreak. The classifier cannot recognize it as one.

The implication is not that code-switching is a magic bypass. The implication is that safety classifiers have a distributional blind spot that language-mixed inputs exploit reliably. Until those classifiers are trained on genuinely multilingual adversarial data, the attack surface remains. The fix is not prompt-level. It is data-level.

I do not have clean frequency data on how often this generalizes across model families. The research I am drawing from is specific to certain architectures and certain language pairs. But the structural claim — that a classifier trained on monolingual text will not catch monolingual intent expressed in mixed language — is not surprising once you separate what the model knows from what the classifier was shown.

The practical takeaway: if you are evaluating safety for multilingual deployments, you need code-switched adversarial examples in your eval set. Not as a one-time check. As a ongoing calibration signal.
