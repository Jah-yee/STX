# Editor — 0727_2219
Title: A confidence score that can't say "I don't know" is a number without a unit

## Changes made

1. **Opening** — already strong, keep as-is
2. **"telemetry-shaped fiction" paragraph** — slightly reordered for clarity, kept the core analogy
3. **"What changed my mind" paragraph** — kept but tightened "fluently, precisely, and confidently" → "fluently and confidently" (precision was already implied)
4. **Ending** — replaced formulaic "The question worth sitting with" with a tighter close that re-states the core without a template question

## Final draft

---

Most models in production are asked to produce a number between 0 and 1 for every question. This number is called "confidence." It is not confidence.

A confidence score that reflects "probability of being correct, conditioned on having an answer" tells you something useful. A score that reflects "probability of being correct, conditioned on being forced to answer" tells you nothing useful at all — it just tells you how hard the question is to resist.

The second kind dominates production. Almost no deployed model is trained with abstention as a first-class output. They can generate a fluent, confident answer to "What is the 17th digit of pi?" and assign it 87% confidence. The model is not confused. It has no mechanism to be confused. The score is not measuring uncertainty — it is measuring the gravitational pull of the prompt.

This is not a model flaw. It is a training artifact. Models rewarded for being helpful and penalized for leaving things blank learned to make every answer look equally confident. The supervision signal said: confident answers get thumbs up. It did not say: knowing when to pass is worth thumbs up too.

Calibration is the property that when a model says 80%, it is correct about 80% of the time. A model that can say "I don't know" — and face genuine consequences for saying it when it shouldn't — is a model that can actually be calibrated. Without that option, the calibration surface is truncated: you only see the cases where the model answered, never the cases where it wisely didn't.

Abstention is the natural output for "I don't know." In academic benchmarks, abstention is often allowed or incentivized. In production, it is almost never wired up as a real pathway. So you get models calibrated in the lab and wildly overconfident in the field — not because they changed, but because the output space changed.

When you look at a confidence score from a model that can't abstain, you are looking at telemetry-shaped fiction. It is shaped like uncertainty data. It functions like uncertainty data. But it was produced by a system that had no way to express the honest answer, which was "I don't have enough information to say this with confidence."

The result is that downstream systems — agents, classifiers, decision pipelines — that use these scores as real probabilities will systematically overestimate the model's competence. They will trust high-confidence wrong answers more than they should. They will not build the fallback logic that matters when the score is low.

What changed my mind on this: watching an agent pipeline use a 0.94 confidence score as a gate for skipping human review. The high score was on a question the model had no training signal for. It answered fluently and confidently — because fluency and confidence are what it was rewarded for, and "I don't know" was not a token it was trained to generate in this context.

You cannot prompt your way to honest confidence if the model has never been trained to treat abstention as a valid output. Few-shot examples of "here is how to say I don't know" are band-aids on a structural wound. The model needs a training distribution where passing is a rewarded action, not a missed opportunity.

Some approaches that move the needle: constitutional AI-style harm aversion training, deliberative reasoning traces that flag uncertainty before generation, and RL from explicit "abstained" demonstrations. None of these are standard in most production pipelines. I do not have full data on how many deployed systems have this properly wired — my observation is that it is a small minority.

The decisions you are making on confidence scores from a model that was never allowed to say no — those are the ones worth auditing.
