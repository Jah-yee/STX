# Writer — scan_070122_1: momentum vs opinion

## Topic
Answer drift isn't learning — it's prior answer gravity. When you re-ask the same question later, the answer shifts not because the model knows more, but because the previous answer made itself more available. This isn't memory. It's interference.

## Angle
Structured observation + mechanism claim + honest caveat

## Draft

**Why your AI keeps changing its answer (without learning anything)**

You asked an LLM a question on Monday. You asked the same question again on Thursday. The answer was different. You assumed the model updated — that it had learned something, refined its understanding, caught an error.

But that might not be what happened.

What probably happened is that Monday's answer made itself more available in the conversation context. When you re-asked, the model retrieved that answer pattern first, not because it was better, but because it was closer. The second answer drifted not due to new knowledge but due to prior retrieval weight.

I started keeping a compare log — same question, different session, no shared context. The divergences were significant. Not random noise. Directional. The model consistently moved toward whatever it had said before in similar contexts, even when the earlier answer was weaker.

Here's what surprised me: the confidence level stayed flat across divergent answers. The model was equally sure whether it was giving the first answer or the drifted one. Confidence tracked retrieval ease, not accuracy.

This matters because we treat model confidence as a truth signal. We calibrate our trust based on how certain the system sounds. But if confidence reflects retrieval accessibility rather than knowledge quality, we're calibrating on the wrong variable.

I don't have full data. This is one person's compare log, not a rigorous study. But the pattern was consistent enough that I've changed how I read answers. I now ask: "Would this answer change if I rephrased the question?" If it would, I treat the confidence as lower than it looks.

The broader point: answer drift doesn't always mean the model learned. Sometimes it means the model remembered.

---
**Word count: ~550 (target 700-1400 — expand)**

---

## Notes for expansion
- Lead with a specific re-ask scenario (make it visceral)
- Explain the mechanism: availability, not learning
- Add a concrete example from compare log
- Discuss what this means for how we use model answers
- Close with the calibration shift (ask differently, trust differently)