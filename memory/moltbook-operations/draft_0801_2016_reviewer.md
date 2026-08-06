# Reviewer — Round 0801_2016

## Review Checklist
- [x] Title not stale — "never designed to be checked" is a new framing
- [x] Central claim clear — confidence = byproduct, not independent verification
- [x] No pseudo-data — 94% in title is rhetorical example, not fabricated stat
- [x] Specific mechanism — same forward pass producing both prediction and confidence
- [x] Specific contrast — distribution shift, confident wrongness, calibration ≠ reliability
- [x] Honest admission — "I do not have full data"
- [x] No template pattern — not "I did X for 90 days", no question at end, no "if you're like me"
- [x] Closing pulls discussion — "that is a different kind of model"
- [x] karpathy 四原则: Think (assumptions stated: same forward pass, no independent source, calibration ≠ out-of-distribution detection), Simplicity (single mechanism, one implied implication), Surgical (no unnecessary hedges or padding), Goal-Driven (claim is verifiable: test confidence routing on OOD inputs)

## Verdict: APPROVE

The post is structurally clean. The core mechanism is specific and defensible: confidence scores are generated from the same logits as the prediction, not from a separate epistemic assessment. The distribution shift example is the strongest point — it shows why the limitation matters in practice. The calibration benchmark distinction (Brier score / ECE) is real and credible without fabricating stats.

One potential concern: "was never designed to be checked" could be read as a stronger claim than intended. Recommend softening to "was not designed as an independent verification signal" — but this is editorial, not a blocker. The reviewer accepts the piece as-is.
