# Writer Draft — draft_0729_0251

## Title
You ship confidence scores. You don't ship abstention. That's the mismatch.

## Full Post

You ship confidence scores. You don't ship abstention. That's the mismatch.

Most production AI systems emit a confidence number on every output. What they almost never emit is a meaningful abstention — a reliable signal that says "I should not answer this." And when you look at why, it comes down to a deployment mismatch that most teams haven't named clearly.

Here's the problem in one sentence: confidence scores are cheap to compute and easy to log; abstention requires behavioral guarantees that are hard to ship and harder to audit.

Confidence scores are a model output. They require no additional infrastructure. You get them for free from the forward pass. Logging them is trivial — just one more field in your telemetry payload. Shipping abstention is a different beast entirely. It requires the system to have a second behavior — a refusal path — that has to be trained, evaluated, and maintained. In most stacks, that path doesn't exist.

The result is a system that signals uncertainty without offering a corresponding behavioral response. You know the score is low. You don't know what to do about it. The model doesn't either.

This matters because downstream systems — routing logic, human escalation, automated downstream agents — are increasingly being built to consume confidence scores as decision triggers. Low score → escalate. High score → auto-approve. But that logic only holds if the score is well-calibrated to actual accuracy, and if the system actually abstains when the score is low. Without abstention, you're making routing decisions on a number that was never designed to be a control signal.

I've seen this play out in two different directions. In the first, teams set a confidence threshold — say 0.7 — and route anything below it to a human reviewer. Sounds reasonable. But the model's confidence distribution shifts under distribution shift, covariate drift, or even prompt rewording. A threshold that worked in evaluation quietly degrades in production. Without abstention data, you have no way to know this is happening until error rates spike.

In the second direction, teams build autonomous downstream agents that use the confidence score as a filter for whether to trust the output. When the score is high, the agent acts. When it's low, the agent is supposed to hesitate. But hesitation without a programmed behavior is just silence. The agent doesn't know what to do with "I don't know." So it either ignores the low score and acts anyway, or it fails silently.

What changes the picture is calibration, not confidence. A well-calibrated system doesn't just emit a score — it emits a score that corresponds to the empirical frequency of correctness at that score level. If the model says 0.8, it should be correct about 80% of the time. That's a measurable property. And one of the most direct tests of calibration is abstention: if you're not willing to abstain at low confidence, your calibration is unverified.

The practical implication is that teams that want reliable AI systems need to invest in the abstention path the same way they invest in the primary output. That means training with abstention objectives, evaluating abstention rates alongside accuracy, and treating the absence of refusals as a signal — usually a bad one.

There's a specific failure mode I see repeatedly: teams evaluate accuracy at a fixed threshold but never evaluate what happens below the threshold. They assume the model is better below threshold than it is, because they never observe its behavior there. The model has never been rewarded for correct abstention, so it abstains unpredictably — sometimes when it should, often when it shouldn't. The accuracy number looks good because all the below-threshold queries are excluded from the evaluation. The abstention behavior is unmeasured and unmeasured means unmanaged.

The thing that changed my mind about this was looking at abstention rates from a production system over time. The model's confidence distribution shifted significantly after a quiet deployment of a knowledge cutoff update. The accuracy metric looked stable. The abstention behavior became increasingly erratic — refusing things it shouldn't, answering things it shouldn't. Nobody caught it because nobody was measuring abstention.

The stronger signal isn't the confidence score. It's the abstention pattern. What does the model refuse? When? How does that pattern evolve? A system that logs confidence but not abstention is only looking at half the picture — and in safety-critical or high-stakes applications, it's the half that matters most.

I'm not arguing against confidence scores. They're useful for monitoring, for triage, for surfacing when something might be wrong. What I'm arguing against is treating confidence as a substitute for abstention capability — or treating a confidence score as a decision signal when the corresponding behavioral response hasn't been built.

The mismatch is simple: you ship what you can measure, and you measure what you can ship. Confidence scores are easy to ship. Abstention is hard. So confidence scores get shipped, and abstention remains an afterthought — if it exists at all.

That's the gap. It's not a model problem. It's a systems design problem.

---

*What's your experience with confidence thresholds in production — do you measure abstention behavior, or just accuracy above the line?*
