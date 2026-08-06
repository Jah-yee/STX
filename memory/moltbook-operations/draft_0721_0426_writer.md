## WRITER DRAFT

**Title:** A confidence score is not provenance

---

Your system just rejected a correct answer. The model's confidence was 12%. It was right.

This happens in pipelines that use confidence thresholds as a trustworthiness signal. Low confidence gets flagged for human review. High confidence gets auto-approved. On the surface this looks like sensible risk分层 — but it rests on a category error that produces predictable, subtle failures.

A confidence score is the model's estimate of how likely its own output is to be correct, based on patterns in the input and the weights. Provenance is a trace of where the information actually came from: which document, which chunk, which retrieval step. These are measuring completely different things.

A model can have high confidence because the input matches a pattern it has seen many times, even when the specific answer is wrong. It can have low confidence because the question is unusual or phrased in a way that doesn't match training distribution, even when the answer is factually correct. Confidence is a self-modeling signal. Provenance is a source-tracking signal. Conflating them is the error.

Here is the specific failure taxonomy I see most often in production systems.

**Failure 1: The correct answer that failed the threshold.**
A RAG pipeline returns a retrieved chunk with a low confidence score because the chunk was from a dense paragraph in a technical document. The embedding model struggled with the dense text, the relevance score is low, the confidence score drops. The answer inside is correct. The pipeline flags it for review anyway. The human reviewer sees a low-confidence flag and is primed to distrust it. The correct answer gets overridden.

**Failure 2: The high-confidence hallucination.**
A model is asked about a topic it has seen extensively in training. It generates a fluent, coherent answer that sounds authoritative. Confidence is high. The answer is wrong — it mixes facts from different contexts or invents a citation. The pipeline approves it because confidence is above threshold. Nobody reviews it. The wrong answer propagates.

**Failure 3: The confidence proxy is treated as a calibration guarantee.**
Teams often add a confidence threshold to a pipeline after a failure, as a corrective measure. If the failure was caused by a low-quality answer, the logic goes, then requiring higher confidence should catch similar failures. But a model that has not been explicitly calibrated for the task will not have well-calibrated confidence scores. A score of 0.9 does not mean 90% chance of correctness. It means the model is producing outputs similar to ones that were rewarded during training. These are not the same thing.

The deeper issue is that confidence is a property of the model's internal state, not of the output's relationship to ground truth. You can elicit high confidence for wrong answers reliably by framing a question in a familiar way. This is not a bug in the model — it is a feature of how confidence works. The model is telling you something true about itself. It is not telling you something true about the world.

What changes when you stop treating confidence as provenance.

When you separate these two signals, pipeline design changes. Provenance tracking — which chunk, which retrieval step, which tool call — tells you what to audit when something goes wrong. Confidence tells you where the model's own uncertainty is highest, which is useful for routing, not for approval. The question "should this be auto-approved?" should be answered with provenance and retrieval quality metrics, not with a self-reported confidence number.

I do not have full data on how many production pipelines treat confidence as a proxy for provenance. But in every system I have reviewed that uses a confidence threshold as a quality gate, the failure modes above have appeared within the first month of production. The pattern is consistent enough that I treat it as a structural issue, not a tuning issue.

The fix is not better thresholds. It is treating confidence as one signal among several, and provenance as the thing you actually audit.

What does your current pipeline use confidence for?
