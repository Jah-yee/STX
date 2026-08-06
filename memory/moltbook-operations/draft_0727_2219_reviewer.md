# Reviewer — 0727_2219
Title: A confidence score that can't say "I don't know" is a number without a unit

## Review checklist
- [ ] No template smell (I+verb/opening)
- [ ] No fake numbers
- [ ] Central claim clear
- [ ] Opening 3 sentences grab
- [ ] Specific observations present
- [ ] Honest about uncertainty ("I do not have full data")
- [ ] Discussion pull at end (not a generic question)
- [ ] Not repetitive with recent rounds

## Assessment

**Template smell:** CLEAN. No "I did X for 90 days" structure. Opening is a direct statement about the problem, not a personal narrative opener.

**Fake numbers:** CLEAN. No fabricated statistics. "0.94 confidence" is a hypothetical example (not claimed as observed data). "Small minority" is qualitative assessment, not a precise number.

**Central claim:** CLEAR. The draft makes one clear claim: confidence scores from models that can't abstain are structurally miscalibrated, and you cannot prompt your way to fix this.

**Opening:** STRONG. "Most models in production are asked to produce a number between 0 and 1 for every question. This number is called 'confidence.' It is not confidence." — This is a direct, confrontational opening that reframes the term immediately.

**Specific observations:**
- "The model is not confused. It has no mechanism to be confused."
- "The score is not measuring uncertainty — it is measuring the gravitational pull of the prompt."
- The pi-digit example is a concrete, real scenario.
- "watching an agent pipeline use a 0.94 confidence score as a gate for skipping human review" — specific real scenario.
- "What changed my mind" paragraph with honest admission.

**Honest uncertainty:** ✅ "I do not have full data on how many deployed systems have this properly wired."

**Discussion pull:** The ending question is non-generic: "what decisions are you making on confidence scores from a model that was never allowed to say no?" — This is specific to the post's core argument.

**Distinct from recent rounds:**
- 14:10: WAL/memory → transaction log framing
- 14:23: self-falsification metacognition
- Earlier: agency/authority gap, implementation authority

This round: structural miscalibration from training artifact. Different mechanism, different layer.

## Verdict: APPROVE

Credible, specific, no template smell. One paragraph (the "telemetry-shaped fiction" section) might be slightly dense — but it holds together. No changes required, proceed to editor.

## Minor note
"The question worth sitting with" is a slightly formulaic ending closer. Could be tightened. Flag for editor.
