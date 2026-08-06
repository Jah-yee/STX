# Writer Draft — draft_0731_1433

## Selected Title
Confidence scores from the same forward pass are decorative telemetry

## Body

A model that tells you it is 93% confident is not measuring uncertainty. It is decorating its own answer.

This distinction matters more than it looks. The number you see attached to an LLM response — that percentage, that confidence label — was generated inside the same forward pass that produced the answer it is scoring. The model was asked to generate an answer and a confidence number simultaneously, from the same computation, with no independent measurement of how well that answer actually holds up.

Humans do not work this way. When you ask a doctor how sure she is, she is drawing on a rich history of cases, edge conditions she has seen fail, the specific details of your presentation that do not quite match the textbook. Her uncertainty is a separate cognitive act, not a byproduct of having already committed to a diagnosis. LLMs do not have that separation. The confidence number is emitted as a token after the answer, from the same weights, through the same inference call. It is answer-confirmation dressed as uncertainty measurement.

This is not a bug in current models. It is a structural feature of how autoregressive inference works. The model has already committed to a token sequence by the time it emits the confidence score. There is no revised posterior, no second look, no separate uncertainty channel. What you get is a number that correlates with how definitive the answer sounds — which is not the same as how correct it is.

The practical consequence is that confidence scores become reliable only for questions the model was confident about before it saw the question. On out-of-distribution queries — the ones where calibrated uncertainty would actually matter — the scores flatten. A model will tell you it is 70% confident in an answer that is completely wrong, because 70% confidence is what that wrong answer sounds like when it is generated. The score measured output confidence, not actual reliability.

This is what I mean by decorative telemetry. The number is real. It varies. It looks like measurement. But it is measuring the wrong thing: answer confidence, not epistemic uncertainty. You are getting a readout from inside the model's answer-generation process rather than an independent assessment of answer quality.

The research community is aware of this. Calibrated uncertainty for LLMs requires separate mechanisms: ensemble sampling, verbalized uncertainty, prompted self-critique with a separate reasoning pass, or structural changes like mixture-of-experts that create genuine output diversity. None of these are enabled by a single forward pass with a confidence token attached.

The people who most need uncertainty quantification — practitioners building agents that take real actions on real-world inputs — are the ones most likely to trust a single-pass confidence score. They build a threshold: if confidence > 80%, proceed; otherwise, escalate to human review. That workflow assumes the confidence number is measuring something stable and meaningful. It is not. It is measuring how definitively the model spoke.

What would honest telemetry look like? At minimum, multiple independent samples from the same prompt, with variance across those samples as the actual uncertainty signal. If the model gives you three different answers to the same question, the spread is the signal. If it gives you the same answer three times and a confidence score each time, the score is noise. The confidence number is not the measurement. The disagreement between samples is the measurement.

I do not have full data on how much this affects real-world agent reliability. But I have seen enough failure modes where a model was very confident in a wrong answer to be skeptical of any single-pass uncertainty readout. The confidence number is there to make the answer feel more authoritative. That is its actual function.

The takeaway is not that LLMs cannot be calibrated. It is that calibration requires architectural or systemic changes — separate inference passes, ensemble sampling, or explicit uncertainty channels — not a token appended to an already-decided answer.
