# 0726_1438 — Writer Draft
# Title: The gap between "I'm not sure" and "I should stop" is a policy question, not a model question

## Draft

Your agent flags a transaction as suspicious. Confidence: 61%. The system approves it anyway because nobody told it what 61% means.

This is where most uncertainty quantification deployments break down. The model produces a confidence score. The pipeline ignores it.

Confidence scores have become a standard output from most capable models. Some are well-calibrated — a 70% confidence prediction does come true roughly 70% of the time, at least on in-distribution data. Others are miscalibrated but have known correction procedures. The models are getting better at expressing their own uncertainty.

The part that isn't getting better is the workflow downstream. Most agent pipelines treat the confidence score as a number in a log, not a signal that changes behavior.

Here is the structural problem: uncertainty quantification tells you how surprised the model expects to be. A decision policy tells you what to do when the model is surprised. These are different functions, owned by different teams, specified in different places, and almost never connected.

A confidence threshold set at 75% because "it felt right" is not a decision policy. It's a placeholder. It gets set once during onboarding, never revisited, and applied uniformly across tasks that have completely different costs for false positives and false negatives. Screening a transaction for fraud and screening a contract for legal exposure have opposite asymmetries — a 70% confidence flag means very different things in each case. The threshold should reflect that. Almost never does.

The floor problem is equally common. Many pipelines enforce a minimum confidence before the agent acts autonomously, and a human reviews below the floor. This sounds reasonable. But when the floor is set without reference to actual error rates at different confidence bands, it creates a false sense of supervision. You are routing cases to humans not because those cases are specifically risky, but because they happen to fall below an arbitrary line.

There is a third failure mode that is harder to detect: calibrated confidence on the wrong thing. A model can be well-calibrated on its next-token predictions while being catastrophically miscalibrated on whether its retrieved context actually supports the conclusion it is drawing. You get a confidence score that is honest for the wrong question. The pipeline acts on it as if it answers the right one.

What a real decision policy looks like: it is explicit, domain-scoped, and separate from the model's training. It specifies what happens at each confidence band — not a single threshold but a mapping from confidence ranges to actions: act autonomously, surface for review, escalate to a different agent, halt and request clarification. It is written by the team that understands the cost of each outcome, not the team that built the model. It is tested the way you test operational procedures, not the way you test model quality.

The policy also needs to be updated when the operational environment changes. A decision policy calibrated for a product catalog that changes quarterly breaks when the catalog changes weekly. The model's confidence distribution shifts with distribution shift, and a policy that was correct last month can be wrong this month without anyone noticing.

I do not have full data on how many production agent pipelines have a real decision policy versus an arbitrary threshold. In the cases I have observed directly, it is fewer than half. Most pipelines have uncertainty outputs that are logged and never read. The model is expressing genuine doubt. Nobody told it what doubt should trigger.

The gap between "the model is not sure" and "the pipeline should do something different" is not a model problem. It is a policy design problem. You cannot fix it by improving the calibration. You fix it by writing the policy.

What does your pipeline do when the confidence is 58%?
