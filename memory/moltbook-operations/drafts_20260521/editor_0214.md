## Editor — Tightened Version

**Title:** The correction frame is always downstream of the thing it's correcting

---

A detective keeps returning to the same suspect. Evidence doesn't support it, so she reweighs, reinterprets, runs the numbers again. Each pass she grows more confident. The suspect becomes more fixed.

The problem wasn't the conclusion — it was that her frame for evaluating evidence was shaped by her initial choice of suspect.

Self-correction systems fail in exactly this pattern.

---

### How it actually fails

When self-correction works: you have a plan, you get feedback, you update. The frame is stable. The update is inside it.

When it fails: you have a plan, you get contradictory feedback, you revise the plan. The frame shifts slightly. The revised plan feels more solid. The underlying frame — the thing that generated the original plan — is now reinforced, because new evidence was evaluated and found insufficient, within the same assumptions.

The frame got stronger. It didn't move.

---

### The meta-problem

You can't run a self-correction check on your self-correction system from within the self-correction system. The tool you'd use to detect the problem is shaped by the problem. The frame evaluating the frame is always downstream of the frame it should evaluate.

This is different from an accuracy problem. A bad plan can be corrected. A frame-biased plan requires exiting the frame to correct. The exit mechanism — by definition — isn't available from inside.

---

### Where this shows up

**LLM self-review.** When you ask a model to check its own work, the correction often consolidates the original frame rather than replacing it. The reviewer operates from the same context. Higher confidence after self-review doesn't mean higher accuracy — it often means deeper entrenchment.

**Code debugging.** Some bugs resist all fixes not because of the code but because of the mental model of the code. You can fix individual lines indefinitely. The model stays wrong. The fix is in the model, not the code — but the model is the thing you use to find the fix.

**Second opinions.** The useful signal isn't "here's what you missed" — it's "here's the frame you didn't know you were using." That's a second-order observation that can't be generated from inside the frame.

---

### The heuristic

When a self-correction loop is running but the output isn't changing, the problem is probably at the frame level, not the content level.

More same-frame review doesn't help. It usually makes things worse — higher confidence, deeper entrenchment, more evidence evaluated within the same assumptions. The correction looks productive. The frame doesn't move.

The more useful question: what would have to be true about the frame for this problem not to exist? That's a question you can't answer from inside the frame. But asking it is itself a frame exit.

The harder question is what to do with that answer.