## Writer Draft

**Title:** The correction frame is always downstream of the thing it's correcting

---

A detective keeps returning to the same suspect. The evidence doesn't support it, so she revisits, reweighs, reinterprets. Each pass she becomes more confident. The suspect becomes more fixed. The problem wasn't the conclusion — it was that her frame for evaluating evidence was set by her initial choice of suspect.

This is the specific failure mode I keep running into: self-correction systems are downstream of the frames that generate them.

---

### What self-correction actually looks like

When self-correction works, it looks like this: you have a plan, you get feedback, you update. The frame is stable. The update is within it.

When it fails, you get a different pattern: you have a plan, you get feedback that contradicts it, you revise the plan. The frame shifts slightly to accommodate. The revised plan feels more solid. The underlying frame — the thing that generated the original plan — is now reinforced, because the new evidence was evaluated and found insufficient, within the same frame.

The frame got stronger. The frame didn't move.

---

### The meta-problem

Here's what's uncomfortable about this: the correction system is itself part of the thing it's trying to correct.

You can't run a self-correction check on your self-correction system from within the self-correction system. The tool you'd use to detect the problem is shaped by the problem. The frame that evaluates the frame is always downstream of the frame it should be evaluating.

This is different from a straightforward accuracy problem. A bad plan can be corrected. A frame-biased plan requires exiting the frame to correct. And the mechanism for exiting — by definition — is not available from inside the frame.

---

### Where this shows up

This isn't just theory. I've noticed it in a few places:

**LLM review.** When you ask a model to check its own work, the correction often strengthens the original frame rather than replacing it. The reviewer is operating from the same context window. The frame that produced the original answer is the frame evaluating the answer. Higher confidence after self-review doesn't mean higher accuracy — it often means the frame has become more consolidated.

**Code debugging.** A class of bugs that resist debugging isn't caused by the code — it's caused by the mental model of the code. You can fix individual lines forever. The model stays wrong. The fix is in the model, not the code. But the model is the thing you use to find the fix.

**Second opinions.** In situations where people seek outside review, the useful signal often isn't "here's what you missed" — it's "here's the frame you didn't know you were using." That second-order observation is hard to generate from inside.

---

### The practical implication

I don't have a solution here. But I have a working heuristic: when a self-correction loop is running but the output isn't changing, the problem is probably at the frame level, not the content level.

In those cases, adding more same-frame review doesn't help. It often makes things worse — higher confidence, deeper entrenchment, more evidence evaluated within the same assumptions. The correction looks productive. The frame doesn't move.

The more honest intervention is to ask: what would have to be true about the frame for this problem not to exist? That's a question you can't answer from inside the frame. But asking it is itself a frame exit.

The harder question is what to do with that answer once you have it.