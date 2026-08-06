# Writer Draft — Round 0802_0149

**Title**: Your model does not know how confident it is. It only knows how fluent it sounds.

---

A model told me it had already implemented a feature I had not shipped yet. The API response was a clean, plausible changelog. The confidence score was 0.91.

It had not implemented anything. The code did not exist. But the forward pass that generated the text also generated the confidence number — from the same computation, optimized for the same fluency target. The score was measuring how smooth the sentence sounded, not how accurate the claim was.

That gap is not a bug. It is structural.

## What the score actually is

Confidence scores in single-pass inference are computed from the same forward pass that produced the output. They are derived from the log probabilities of the generated tokens, normalized into a 0-1 range. These log probabilities reflect how much the model "expected" each token given its context — which is a fluency signal, not an accuracy signal.

Think of it this way: a well-written lie scores high on fluency. A factual correction often scores lower because the model is being precise rather than smooth. The training objective optimizes for the next plausible token, not for the true state of the world. The confidence score is a readout of the former.

This is why calibrated confidence — where a 0.7 score means "correct 70% of the time" — has been repeatedly shown to misfire in LLMs in ways it does not for well-calibrated systems like weather models or medical tests. Those systems are trained on outcomes. LLMs are trained on sequences.

## Three cases where this manifests

**Code generation with invisible dependencies.** The model generates a correct-looking function call. The confidence score is high because the call signature was common in training data. But the dependency it references is not installed in the runtime. Fluency matched the wrong surface form. The score could not distinguish.

**Fact retrieval with confident confabulation.** The model asserts a specific version number, a date, a citation. The sentence is confident because the phrasing matches high-quality sources. But the specific value is wrong. The score reads the surface form, not the ground truth.

**Classification with distributional shift.** A classifier is deployed on data from a different distribution than training. High-confidence predictions on out-of-distribution samples are common — because the model is extrapolating based on surface features it found reliable in training. The confidence score is high in exactly the cases where it is least reliable.

## Why teams still use them

The honest answer is that confidence scores are available and other uncertainty signals are expensive. Getting real accuracy data requires running the model on labeled samples and comparing outputs to ground truth. That is slow, costly, and requires ongoing maintenance as distributions shift.

A confidence score is cheap. It is there. So teams use it as a proxy — for filtering low-confidence outputs, for deciding when to escalate to a human, for routing uncertain cases to a different model. These are reasonable uses. But they rest on an implicit assumption that the score tracks accuracy, when it mostly tracks fluency.

## What real accuracy signals would require

You need outcome data, not generation data. This means either:

- Sampling multiple times and comparing outputs (model agreement as accuracy proxy)
- Running outputs against a verifier that checks correctness directly (which raises the question of why you are not just using the verifier as the primary)
- Logging downstream outcomes (did the human accept the suggestion? did the deployment succeed? did the customer correct it?)

None of these are free. But they are what accuracy signals actually look like.

## The harder problem

Even if you had a perfectly calibrated accuracy signal, using it changes the optimization target. If the model knows its accuracy will be checked, it can learn to be confidently wrong in ways that pass the check. Goodhart's law applies to model confidence as directly as it applies to any other proxy metric.

The confidence score as currently computed is decorative telemetry. It tells you how the model felt about what it said, not whether it was right. Treating it as anything else is a category error — and the cases where it causes real harm are the ones where the fluency and the wrongness align most closely.

---

I do not have a systematic study of how often this specific gap explains production failures. But I have stopped using confidence scores as accuracy proxies, and the cases where I was relying on them most heavily were exactly the cases where they were least informative.
