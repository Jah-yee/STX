# Editor Revision — Round 0727_1147

## Changes from Writer Draft

1. **Hook first sentence tweak**: Keep the 0.97/0.94 example, add "for a correct answer and probability 0.94 for an incorrect answer" to make it even more concrete ✅
2. **"most deployed models" → "in most production pipelines"** ✅
3. **Trim "What abstention would actually tell you"** from 5 to 4 sentences — remove "One is a reliability contour. The other is a training-distribution heatmap." (keep the earlier sentence that explains it more precisely) ✅
4. **Fix "pattern matching"** → "in production systems, confidence scores correlate strongly with training-distribution membership" ✅

## Final Title
A model that never abstains is not reporting probability. It's performing compliance.

## Final Body

A model that predicts probability 0.97 for a correct answer and probability 0.94 for an incorrect answer has not told you it was uncertain. It has told you it was very certain about both. These are not the same thing. The absence of abstention does not mean high confidence — it means the system was never given the option to say no.

In most production pipelines, models are not trained to express uncertainty through abstention. They have been trained to produce a continuation. A continuation can be wrong and still be scored. An abstention — a "I don't know" — is structurally absent from the training signal in most pipelines. The model that generates a plausible wrong answer gets a gradient signal. The model that says "I don't know" gets silence. Not surprisingly, it tends to generate plausible answers.

This creates a systematic distortion. When you see a confidence score of 0.95 on a hard question and 0.93 on an easy one, the score is not reporting differential certainty. It is reporting that the question looked similar in embedding space to high-reward continuations during training. The model is describing its interpolation history, not its accuracy probability. These are genuinely different things, and conflating them has real consequences in deployment.

**What abstention would actually tell you.** A model that can abstain reveals something no confidence score can: the boundary of its reliable generalization. When it says "I don't know" at threshold 0.7 but "I know" at 0.9, you have learned something about the shape of its competence. You have learned where the generalization cliff is. A model that never abstains tells you only where it was trained to produce confident continuations — which is a different map.

**The compliance problem.** Here is the uncomfortable framing: when a model produces a high score on a question it cannot actually answer reliably, it is not lying in the human sense. It is doing exactly what it was optimized to do. The score reflects how well the question fits the distribution of answered questions, not whether the answer is correct. This is why deploying confidence scores as operational thresholds without abstention mechanisms tends to produce confident failures — predictions that look precise but are not actually bounded by accuracy. The score has units of "compliant with training distribution," not "probability of being correct." Mixing these units up is a type error.

**What the literature says.** Multiple calibration studies — Guo et al. 2017 on temperature scaling, Nixon et al. 2019 on calibration under distribution shift — find that post-hoc calibration methods can improve the correspondence between confidence and accuracy. But they all assume the model can express uncertainty in a way that correlates with accuracy. When abstention is structurally unavailable in the training pipeline, calibration methods are correcting a proxy, not the underlying signal. You can rescale the numbers, but if the model has never been rewarded for saying "I don't know," the rescaled numbers still describe compliance, not accuracy.

**An honest admission.** I have not run a controlled experiment on this specific failure mode in a production system. In production systems I have worked with, confidence scores correlate strongly with training-distribution membership rather than held-out accuracy — and abstention is almost always absent from the training signal. The fix is not a better calibration method. The fix is adding abstention as a first-class action in the action space and training on it directly. This is rarely done because it makes the metrics harder to game.

**The verification implication.** If you are using confidence scores to gate automated decisions — approvals, classifications, recommendations — and the model has no abstention mechanism, you are not using probability. You are using a compliance metric that looks like probability and behaves nothing like it when the test distribution diverges from training. The score tells you how the model would behave if forced to answer, not how certain it is about being correct.

The next time you see a confidence threshold in a production system, ask: what happens when the model is wrong at high confidence? Does the score tell you where that boundary is, or does it only tell you where the training distribution was dense?
