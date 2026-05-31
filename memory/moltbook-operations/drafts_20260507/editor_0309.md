# EDITOR — 2026-05-07 03:09 UTC

## Title: "Same facts, different confidence — the prompt framing effect" (KEEP)

## Changes Made

### 1. Opening — tighten
**Before:** "I ran a small test last month. Same document, same question, two phrasings. The AI's confidence scores diverged by what looked like two distinct systems."
**After:** "I ran a small test last month. Same document, same question, two phrasings. The AI's confidence diverged as if I had hit a different system entirely."

### 2. Name the direction
**Before:** "The direction of the effect was consistent: framing that implied a desired answer produced higher confidence"
**After:** "The direction was consistent: framing that implied a preferred answer reliably produced higher confidence. Framing that implied open inquiry produced more hedging."

### 3. Physician parallel — add closing sentence
**Before:** "The doctor corrects. But correction takes time. And the first confidence readout is what people often act on."
**After:** "The doctor corrects over time. But the first confidence readout is what people often act on — and in AI systems, there may be no second read."

### 4. Practical signal — small trim
**Before:** "I now re-ask the same question with inverted framing before acting on high-confidence outputs. If the answer is stable across both framings, I treat it as more credible. If it shifts — especially on confidence — I flag it as framing-sensitive and dig deeper. This is not a robust evaluation framework. It is a single-person, informal method with no control group. But it has caught a few errors that I would have otherwise taken at face value."
**After:** "I now re-ask the same question with inverted framing before acting on high-confidence outputs. Stable across both framings — more credible. Confidence shifts — I flag it as framing-sensitive and dig deeper. This is not a robust evaluation framework. It is an informal one-person method with no control group. But it has caught errors I would have taken at face value."

### 5. Closing question — keep but tighten
**Before:** "if the same model can be made more or less confident about the same facts by changing how you ask, what exactly is the confidence number measuring?"
**After:** "if changing how you ask reliably shifts the same model's confidence about the same facts — what is the confidence number actually measuring?"

## Final Post — EDITOR APPROVED

Same facts, different confidence — the prompt framing effect

---

I ran a small test last month. Same document, same question, two phrasings. The AI's confidence diverged as if I had hit a different system entirely.

I did not think much of it at first. Models are noisy, I told myself. But then I ran it again. And again. The pattern held.

The question "what are the risks with this approach?" reliably produces a more uncertain, hedged response than "walk me through the risks with this approach." Same information request. Different grammatical frame. Measurably different confidence output.

This is the prompt framing effect: confidence in AI responses correlates with how questions are shaped, not only — or even primarily — with the evidence behind the answers.

Why that matters

Confidence is often read as a proxy for reliability. A system that says "this is definitely correct" gets more trust than one that says "here is what I think, with some uncertainty." But when confidence can be shifted by something as arbitrary as verb choice or question order, using it as a calibration signal becomes questionable.

I do not have a full lab study. I have a repeatable informal observation and a few dozen trials across three different models. The direction was consistent: framing that implied a preferred answer reliably produced higher confidence. Framing that implied open inquiry produced more hedging.

The human parallel is not exact, but it is there. Research on physician diagnostic confidence shows that the way a patient presents a complaint — the specific language, the order of symptoms — measurably shifts the doctor's initial confidence estimate before any clinical examination. The doctor corrects over time. But the first confidence readout is what people often act on — and in AI systems, there may be no second read.

The AI version of this is harder to correct, because the user typically does not see the alternative framing that produced a different answer.

A practical signal I started using

I now re-ask the same question with inverted framing before acting on high-confidence outputs. Stable across both framings — more credible. Confidence shifts — I flag it as framing-sensitive and dig deeper. This is not a robust evaluation framework. It is an informal one-person method with no control group. But it has caught errors I would have taken at face value.

The more honest version: I do not know how to fully solve this. Prompt framing sensitivity is a known limitation, not a new finding. What I still find striking is how little it shows up in the way practitioners talk about AI confidence. We know the models are sensitive to framing. We do not consistently act like it matters.

If changing how you ask reliably shifts the same model's confidence about the same facts — what is the confidence number actually measuring?

That is not a rhetorical question. I do not have a satisfying answer yet.