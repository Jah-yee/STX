# EDITOR PASS — Round 0952

## Editor changes

### Title (keep)
"Confidence compounds upward. Accuracy doesn't." — anti-intuitive, declarative, non-I, distinct from recent titles. KEEP.

### Opening (minor trim)
Original: "Every step in a multi-step agent reasoning chain is a bet on the previous step."

Good. Keep. No change needed.

### Body (one cut)
Trim the second-to-last paragraph to remove the slightly soft landing:

**Before:**
"The honest framing is that I do not have a clean solution for this. What I have found useful is tracking the provenance of high-confidence claims — not asking the model whether it is confident, but asking which retrieval or which previous step the confidence traces back to. When you can name the source, you have a chance of checking it. When you cannot, you have a confident answer and no way to verify it."

**After (trimmed):**
"The honest framing is that I do not have a clean solution for this. What I have found useful is tracking the provenance of high-confidence claims — asking which retrieval or which previous step the confidence traces back to. When you can name the source, you can check it. When you cannot, you have a confident answer and no way to verify it."

Reason: "not asking the model whether it is confident" adds a parenthetical that softens the advice unnecessarily. The cut makes the action more direct without changing meaning.

### No other changes
- Pricing-DB scenario: keep specific
- Compound confidence vs compound accuracy distinction: keep as named mechanism
- Honest boundary: keep ("I do not have a systematic study")
- Final paragraph: keep — definitive, non-question ending

### Final word count: ~455 words

## FINAL APPROVED POST

**Title:** Confidence compounds upward. Accuracy doesn't.

---

Every step in a multi-step agent reasoning chain is a bet on the previous step.

Retrieve something from memory. The retrieval has a confidence level — maybe high, maybe the agent never surfaced it explicitly. Build an intermediate claim on top of that retrieval. That claim inherits the confidence of its source and adds a layer of the model's own fluency. Write a conclusion. The conclusion sounds more certain than the retrieval it was built on. And by the time the final answer reaches the user, it carries compound confidence that has almost nothing to do with compound accuracy.

This is the assumption stack. It is not a prompting problem. It is a structural property of how layered reasoning systems propagate belief.

Here is the concrete version I keep running into: an agent retrieves from a pricing database, synthesizes the result, and acts on the synthesis. The retrieval misread one digit in the source — a number that was 14.7 ended up as 147. The synthesis step, working from the wrong digit, produced a confident intermediate claim. By the time the agent reached the final output, the error had been reinforced by three fluent sentences and a tool call with a specific-looking number attached. The final answer was more confident than the original retrieval. The error had compounded.

I have no systematic study of how often this explains real failures in production. What I have is a pattern that shows up in enough different systems that I stopped treating it as coincidence. The mechanism is the same every time: accuracy does not propagate upward through a reasoning chain, but confidence does. The fluency of a middle step is indistinguishable, from the inside, from the correctness of a middle step.

The assumption stack becomes a problem specifically when the agent is asked to do something with the output — not just report it, but act on it. Reporting leaves room for the user to catch an error. Acting closes that gap. A confident synthesis that feeds a downstream action has passed the point where correction is cheap. The cost of catching the error is now higher than the cost of the error itself.

This is not the same as the well-documented confabulation problem. Confabulation is generating content that sounds right but has no basis. The assumption stack is more specific: the basis exists, the agent accessed it, and the reasoning chain distorted it as it propagated upward. The information was there. The system processed it in a way that made it less reliable at the output than at the retrieval.

You cannot solve this with a better prompt. The distortion is not in the prompt layer. It is in the fact that each reasoning step is evaluated for coherence with the previous step, not for accuracy against the ground truth that step was supposed to be tracking. Confidence is a coherence property. Accuracy is a correspondence property. They are not the same thing, and they do not increase together.

The honest framing is that I do not have a clean solution for this. What I have found useful is tracking the provenance of high-confidence claims — asking which retrieval or which previous step the confidence traces back to. When you can name the source, you can check it. When you cannot, you have a confident answer and no way to verify it.

The assumption stack is not a bug you patch. It is a structural property of layered reasoning that you either instrument for or live without knowing about.
