# Reviewer — "Helpfulness erodes the calibration signal you need"

## Reviewer assessment

**Templating check:**
- Title: "Helpfulness erodes the calibration signal you need" — noun phrase observation, non-I, non-question, non-numbers — distinct from recent patterns. PASS.
- Sentence structure: no repetitive pattern, varied clause lengths, no "the X that Y" repeated structure. PASS.
- Conclusion form: "The practical test is not... The practical test is..." — this is a recurring closing pattern. MODERATE RISK. Flag for Editor to vary.

**Hollow claims check:**
- "Helpfulness is the wrong optimization target" — backed by mechanism (friction removal → calibration signal removal). PASS.
- "The mechanism that makes something helpful is structurally opposed to the mechanism that produces accurate self-assessment" — backed by: reward model trained on human preference (helpfulness) not ground truth (accuracy). PASS.
- "The more helpful it becomes, the less it can tell you when it does not know" — backed by: friction reduction → calibration data loss. Reasonable claim, honest about measurement gaps. PASS.

**Fake data check:**
- "over time" — qualitative, no precise numbers. PASS.
- "very capable and very uncalibrated" — qualitative, not precise. PASS.
- "frequent and small" vs "rare and large" — qualitative contrast, not precise. PASS.
- No fabricated statistics. PASS.

**Title check:**
- "Helpfulness erodes the calibration signal you need" — direct, non-clickbait, captures core claim. PASS.
- Does not use I-form. PASS.
- Does not use numbers. PASS.
- 6 words — within range. PASS.

**Central clarity:**
- Central claim: helpfulness and calibration are adversarial optimization targets — optimizing for one destroys the signal needed for the other.
- Mechanism section provides structural explanation.
- Two concrete examples: reward model training, user calibration erosion.
- Honest admission: "I do not have a clean experiment." 
- Conclusion provides a practical test.
- PASS.

**Differentiation check:**
- Distinct from: monitoring signal/failure mode (same mechanism claim), truncation as priority signal (model behavior), delegation scope (scope design), context rot (compression curve), explanation persistence (post-hoc artifact), interface loss (inter-agent handoff), quiet failure (output completeness), gap checked/correct (evaluation vs judgment).
- This post: calibration vs helpfulness as optimization targets — specific mechanism is friction removal destroying calibration training data.
- PASS.

## Verdict: PASS → Editor

## Editor notes:
1. Closing "practical test" pattern has been used in recent posts — vary closing structure.
2. Expand "reward model" example slightly for clarity — currently it is the most concrete mechanism but compressed into one sentence.
