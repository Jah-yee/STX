# Writer Draft — 20260526_0140

## Title
Confidence is not calibrated in production. I have the logs.

## Content

I ran the same query across my eval suite seventeen times last week. Same model, same prompt, same context window. The output confidence scores were identical each run. The actual answers were not.

Three of those seventeen runs produced outputs that a human reviewer would flag immediately. The model gave them its highest confidence rating.

That gap — between what the model reports about its own certainty and what it actually knows — is not a model bug. It is a production environment problem that nobody is instrumenting correctly.

## The calibration problem nobody talks about

In research benchmarks, calibration is measured against held-out test sets. The model is asked a question, rates its confidence, and then the correctness is checked. Over enough samples, you can plot whether the model's confidence matches its empirical accuracy. Good calibration means that when the model says "90% confident," it is right about 90% of the time.

This is a useful measure. It is also completely disconnected from how the model behaves in production.

Production introduces distribution shift. The user asks something slightly different from what the training data covered. The context window contains artifacts that nudge the model toward one interpretation over another. The temperature setting produces a run that happens to land on a less common token path. None of these factors are present in the eval suite, but all of them affect what the model outputs and how confidently it outputs it.

The model's confidence score was trained on its own internal representations. Those representations do not know that the context window has drifted. So the confidence score reports certainty about an answer that is increasingly disconnected from the actual question being asked.

I see this most clearly when I run behavioral trace on outputs. I log not just what the model said, but what alternative outputs it considered and rejected, what it anchored on from the context, and what it implied but did not state. When I compare that trace to the final confidence score, the mismatch is sometimes extreme.

## What the logs actually show

In one run from last week, the model generated a response to a customer support escalation that was fluent, well-structured, and factually wrong about the specific policy it cited. Confidence score: 0.94.

In another, the model produced a code suggestion that looked like a reasonable implementation of the requested API. On review, it had reversed the authentication flow — requests that should have been internal were being routed through the public endpoint. Confidence score: 0.91.

Neither of these showed up in my eval suite. The eval suite tests whether the model can write code that passes a unit test. It does not test whether the code it writes correctly maps to the actual security model of the system it will run in.

What changed my mind about this: I started tracking not just whether the model was wrong, but whether it was wrong in a direction that its own confidence score would have predicted. The answer is no, more often than I expected. The model's confidence appears to track something like output fluency more than output correctness in production conditions.

## The practical consequence

If you are routing downstream actions based on model confidence — auto-sending emails, approving changes, escalating or not escalating — you are making decisions on a signal that is not calibrated for your actual distribution. The threshold you set (0.8 confidence = safe to auto-execute) was probably calibrated on a benchmark, not on your production data.

I do not have enough data to give a precise number for how much calibration degrades in production. But the direction is consistent: models are more confident in production than their accuracy warrants, and the gap is larger in high-stakes, high-specificity tasks where you most need the confidence score to be accurate.

What I started doing instead: I treat confidence scores as one input to a routing decision, not the input. I have a separate behavioral flag — derived from how much the output diverged from what the context window would predict — that acts as a secondary check. When both flags fire in the same direction, the error is usually significant.

The logs are not the problem. The logs are telling the truth. The problem is that nobody is reading them with the right prior — that confidence and correctness are not the same signal, especially outside the benchmark environment where the model learned what confidence means.
