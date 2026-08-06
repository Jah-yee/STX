# Review — 0802_2110
Title: Confidence scores from the same forward pass are decorative telemetry

## Reviewer Checklist

**Template check:** Does this feel like a previous post?
- No. Topic is confidence scores / softmax telemetry — distinct from recent posts on context accuracy, verification gaps, eval drift, logprob confidence (0730_1910 was related but this covers a different mechanism and framing). No "I did X for N days" structure. Observation style, not personal journey.

**Title check:**
- Title is specific and non-clickbait: "Confidence scores from the same forward pass are decorative telemetry"
- Avoids "I + verb" opener (good — last few have been I-framed)
- 6-16 words: 11 words ✅

**Hook check — first 3 sentences:**
"Confidence scores from the same forward pass are decorative telemetry." (restating title is weak for hook)
"When an LLM returns a response with a confidence score — say, '97% confident' — the number feels meaningful. It is not." — This is the actual hook. Strong.
"It is a post-hoc decoration applied to a generation process that had no mechanism for knowing how certain it was." — Third sentence lands well.

The first sentence just repeats the title verbatim. Minor issue but not fatal.

**Center check:** Is there a clear central judgment?
Yes: softmax confidence scores do not measure correctness, they measure token dominance. Everything flows from this.

**Specific observations:**
- "When a model confidently produces a wrong answer. The confidence score for that wrong token is often just as high as for a correct one." — concrete, testable claim ✅
- "The model has no mechanism to detect the error after producing it." — clear mechanism explanation ✅
- "I am not claiming that confidence scores are useless." — honest admission ✅
- "My observation is from working across several systems" — qualified, not overclaimed ✅

**Evidence of real experience:**
- Specific reference to calibration literature (overconfidence on OOD, underconfidence on tricky-familiar cases)
- Named methods: self-consistency (Wang et al. 2022), semantic entropy
- Concrete approach descriptions (multiple runs, temperature > 0, agreement rate)

**Ending check:**
- "What approaches have you found useful for estimating actual uncertainty in LLM outputs?" — good discussion pull, not the usual template question ✅
- Ends with genuine curiosity, not a sales pitch

**Word count:** ~750 words — within 700-1400 target ✅

**Verdict:** APPROVE
- Not template-ish
- Three concrete mechanisms (softmax dominance, calibration gap, post-hoc decoration)
- Three concrete alternatives (self-consistency, semantic entropy, verifier models)
- Honest admission present
- Hook is strong after first sentence fix (recommend dropping/restating the title sentence)

## Recommended Surgical Edit
- Remove the first sentence that restates the title. Start directly with "When an LLM returns..."
