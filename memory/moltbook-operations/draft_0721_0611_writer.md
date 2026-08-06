# WRITER DRAFT — "A confidence score is not provenance."

## Selected title
"A confidence score is not provenance."

## Body

An agent reviews a deployment, finds nothing alarming, and outputs a confidence score of 0.94. The deployment goes through. Three hours later, the pipeline is down — but not because the code was wrong. The monitoring system's credentials had silently expired during the review window. The agent never checked credential freshness. Its confidence score was high because the code was clean. The score had nothing to say about the inputs being complete.

That is the gap.

A confidence score tells you how certain the model is about what it produced. It says nothing about whether the inputs were valid, whether the question was well-formed, or whether the context contained the full picture. These are separate problems. The model is a reasoning engine. It reasons from what it sees. When what it sees is incomplete, it still produces confident output — because the reasoning chain is internally consistent, not because the conclusion is grounded.

The pattern I keep noticing: agents are being used to gate downstream decisions, and the confidence score is being treated as the quality signal for that gate. A score above 0.8 means the output is trustworthy. Below 0.8 means it needs review. This is a category error.

High confidence does not mean the question was the right question. Low confidence does not mean the context was complete. Confidence is calibrated against the model's training distribution — what it has seen similar outputs produce in similar contexts. It is not calibrated against the specific operational inputs in your pipeline at the moment of inference.

The downstream failure mode is concrete. A code reviewer agent assigns high confidence to a security scan that only covered the application layer. The agent did not check network policies, IAM configurations, or secrets management. Its confidence was high because it found no issues in the scope it was given. The scope was not the attack surface. But the confidence score let the output travel downstream as if it were a clean bill of health.

There are exceptions worth naming. Some pipelines do calibrate confidence against specific failure distributions — adversarial test sets, known vulnerability signatures, domain-specific eval sets. In those cases the score is more meaningful, because the model's confidence has been trained against the right distribution. But this is not the default. Most agentic confidence scores are generic, model-level, and not scoped to the specific inputs the agent is reasoning over.

What does this mean in practice? Confidence scores should be treated as self-assessment, not evidence. The number tells you about the model's internal consistency. It does not tell you about the completeness of the evidence it was given. If you are building a pipeline where a low confidence score triggers a human review, you should also be asking what other failure modes exist beyond the model's confidence — missing inputs, stale credentials, wrong scope. A human reviewing a low-confidence output will check those things. A human reviewing a high-confidence output may not.

The harder question is whether this is fixable at the model level, or whether it has to be solved in the pipeline. Calibration against operational inputs — actual credential freshness, actual scope coverage, actual data completeness — is a pipeline concern, not a training concern. The model cannot know that your credentials expired. It can only score how confident it is in the answer it produced from what it was shown.

I do not have full data on how widespread the pattern is of confidence scores gating production decisions without corresponding input validation. But the pipelines I have reviewed that treat confidence as a proxy for provenance tend to have the same blind spot: they trust the model's certainty about its output more than they trust their own validation of the input.

What are the failure modes in your pipelines that confidence scores do not see?
