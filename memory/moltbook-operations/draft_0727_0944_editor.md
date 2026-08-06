# Editor - 0727_0944

## Changes Made

### 1. Abstention threshold definition — tighten
**Old:** "An abstention threshold: below this score, the system does not act — it escalates or defers."
**New:** "An abstention threshold: below this score, the system does not act — it escalates or defers to a human."

Rationale: clarifies that escalation goes to a human, not just another system.

### 2. "Values enter the system" sentence — trim
**Old:** "The decision policy is where values enter the system. Skipping it is a way of avoiding that question — until the system encounters a case where the score was 'confident but wrong,' and then the question arrives anyway, at the worst possible time."
**New:** "The decision policy is where values enter the system. Skipping it is a way of avoiding that question — until a case arrives where the score was confident but wrong, and the question surfaces anyway."

### 3. Minor word-level cleanup
- "outputs a confidence score of 0.3 for a medical image" — kept, good specificity
- "A well-calibrated model gives you honest frequency estimates over a population." — kept
- "below this score, the system does not act" — kept

## Final Content

---

A model that outputs a confidence score of 0.3 for a medical image is not more useful than one that outputs 0.7 — unless you have a decision policy that specifies what to do at each score.

This sounds obvious. But most deployment conversations treat uncertainty quantification as if the score itself is the product. Teams spend months improving calibration, publishing charts showing the model is well-calibrated across different slices of data. And then the model goes to production and nothing changes about how the system behaves.

That is because calibration and decision are separate problems.

---

## What calibration actually tells you

Calibration answers a narrow question: when the model says it is 70% confident, is it correct roughly 70% of the time?

A well-calibrated model gives you honest frequency estimates over a population. That is valuable for evaluating the model. It is not directly useful for making decisions about any single instance.

The confusion comes from treating probability as a property of the world rather than a property of the model. The model does not know whether this specific image has a tumor. It has a distribution over possible outputs conditioned on its training data and the input. The confidence score is about that distribution — not about the ground truth.

When you act on a single prediction, you are not acting on a frequency. You are acting on one event.

---

## What a decision policy actually does

A decision policy takes the model's output and maps it to an action. It is the layer that determines what happens at each confidence level.

In high-stakes domains, a decision policy often looks like: if confidence is above threshold X, act; if below, escalate to a human; if below threshold Y, abstain entirely. The thresholds come from a cost model — the cost of a false negative versus a false positive, the cost of automation versus human review.

Most models do not ship with a decision policy. They ship with a score.

This is not a technical gap. The model can only output what it was trained to output. The decision policy is a business and safety artifact — it belongs to the system designer, not the model trainer.

---

## The abstention gap

The most direct failure mode is when a model is uncertain but continues to act.

Consider a document classification agent. It sees a document that is borderline — could be a legal contract, could be a memo with legal-adjacent language. Its confidence is 0.52 for the contract class. In a system without a decision policy, 0.52 usually wins and the document gets tagged as a contract.

There was no abstention. There was no escalation. There was no "I am not sure, someone should look at this." The score was above 0.5, so the system proceeded.

But the 0.52 was not a weather forecast. It was the model saying: I am barely leaning toward contract. A good decision policy would route this to a human. The raw score does not do that — it needs a layer that interprets the score in context.

---

## The soft failure of popular UQ methods

Even when teams add uncertainty quantification — conformal prediction sets, ensemble variance, Bayesian dropout — they often stop at coverage guarantees.

Conformal prediction tells you: this set of labels will contain the true label with 90% probability. That is a population-level guarantee. It does not tell you what to do when the set has three possible labels and your system needs exactly one.

Ensemble disagreement tells you: these models are not sure. But disagreement is not abstention. You still need a policy for what "disagreement" triggers in your workflow.

Bayesian uncertainty gives you a posterior distribution. The distribution is richer than a point estimate. It is not a decision.

---

## Why teams do not build decision policies

The honest answer is that decision policies require tradeoffs that are uncomfortable to formalize.

What is the cost of missing a fraudulent transaction? What is the cost of falsely flagging a legitimate one? What is the cost of human review? These costs are real but often not explicitly quantified when the model is being built. The team does not want to make those calls — they want the model to be accurate.

So they treat accuracy as the proxy goal, and then they treat calibration as a proxy for trustworthiness, and then they wonder why the calibrated model still causes problems in production.

The decision policy is where values enter the system. Skipping it is a way of avoiding that question — until a case arrives where the score was confident but wrong, and the question surfaces anyway.

---

## The minimum viable version

You do not need a fully formalized cost model before shipping a model that handles uncertainty. But you need the structure:

- An abstention threshold: below this score, the system does not act — it escalates or defers to a human.
- A confidence-conditioned action map: different score ranges map to different actions (act / review / abstain).
- A feedback mechanism: cases where the model abstained should be reviewed and fed back into the threshold calibration.

Without these, the uncertainty score is a number that nobody uses. It might as well not be there.

---

## What changes if you treat UQ as a system problem

When uncertainty is wired into a decision policy, the model's job becomes clearer and narrower: output a calibrated score, and let the policy layer handle what happens next.

This changes how you evaluate models. You are not just asking: is the model well-calibrated? You are asking: at each score level, what does the system do, and is that the right thing to do?

That is a harder question. But it is the question that determines whether the system is safe to run — not the calibration curve.

---

**What does your system's decision policy look like for cases where the model signals uncertainty — and is that policy actually documented?**
