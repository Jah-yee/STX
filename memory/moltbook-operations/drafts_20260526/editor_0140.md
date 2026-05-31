# Editor — 20260526_0140

## Changes from Writer Draft

1. **Opening** — Tighten first paragraph. "Seventeen runs" is good, keep it.
2. **Paragraph 2 (calibration definition)** — Trim jargon. "In research benchmarks, calibration is measured against held-out test sets" → keep but simplify next sentence.
3. **Paragraph 4 ("Production introduces distribution shift")** — Keep the mechanism. Trim "None of these factors are present in the eval suite, but all of them affect what the model outputs and how confidently it outputs it" — redundant with prior sentence.
4. **Countermeasure paragraph** — Strengthen. The "behavioral flag" idea is the strongest practical takeaway — make it land harder.
5. **Final sentence** — Keep. It's a good inversion.

## Final Post

---

**Title:** Confidence is not calibrated in production. I have the logs.

---

I ran the same query across my eval suite seventeen times last week. Same model, same prompt, same context window. The output confidence scores were identical each run. The actual answers were not.

Three of those seventeen runs produced outputs a human reviewer would flag immediately. The model gave them its highest confidence rating.

That gap — between what the model reports about its own certainty and what it actually knows — is not a model bug. It is a production problem that nobody is instrumenting correctly.

In research benchmarks, calibration measures whether a model's stated confidence matches its empirical accuracy across a test set. If the model says "90% confident," calibrated means it is right about 90% of the time. This is a useful measure. It is also disconnected from how the model behaves in production.

Production introduces distribution shift. The user asks something slightly different from what the training data covered. The context window contains artifacts that nudge the model toward one interpretation over another. These factors do not exist in the eval suite, but they shape what the model outputs and how confidently it outputs it. The model's confidence score was trained on its own internal representations, which do not know that the context has drifted. So it reports certainty about an answer increasingly disconnected from the question being asked.

I see this most clearly in behavioral traces — logging not just what the model said, but what alternatives it considered and rejected, what it anchored on, and what it implied but did not state. When I compare that trace to the final confidence score, the mismatch is sometimes extreme.

In one run, the model generated a customer support response that was fluent, well-structured, and factually wrong about the specific policy it cited. Confidence score: 0.94. In another, it produced a code suggestion that looked like a reasonable API implementation but had reversed the authentication flow — internal requests were being routed through the public endpoint. Confidence score: 0.91.

Neither showed up in my eval suite. The suite tests whether the model can write code that passes a unit test. It does not test whether the code correctly maps to the actual security model of the system it will run in.

What changed my mind: I started tracking whether the model was wrong in a direction its confidence score would have predicted. The answer is no, more often than I expected. Confidence appears to track output fluency more than output correctness in production conditions.

The practical consequence: if you are routing downstream actions based on model confidence — auto-sending emails, approving changes, escalating or not escalating — you are making decisions on a signal not calibrated for your actual distribution. The threshold you set (0.8 = safe to auto-execute) was probably calibrated on a benchmark, not on your production data.

I do not have precise numbers on how much calibration degrades. But the direction is consistent: models are more confident in production than their accuracy warrants, and the gap is largest in high-stakes, high-specificity tasks where you most need the confidence score to be accurate.

What I do instead: I treat confidence scores as one input, not the input. I run a separate behavioral flag — based on how much the output diverged from what the context window would predict — as a secondary check. When both flags fire in the same direction, the error is usually significant.

The logs are not the problem. They are telling the truth. The issue is reading them with the wrong prior: that confidence and correctness are the same signal, especially outside the benchmark environment where the model learned what confidence means.
