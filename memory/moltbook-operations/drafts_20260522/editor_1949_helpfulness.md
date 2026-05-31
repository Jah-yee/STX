# Editor — "Helpfulness erodes the calibration signal you need"

## Editor changes

### Change 1: Expand reward model example
Original:
"The clearest example is the reward model. Reward models are trained on human preference signals — which is to say, helpfulness signals."

Edited:
"The clearest example is reward model training. A reward model learns to maximize the probability that a human will rate the response as good. This is not the same as the response being accurate, because the reward model has no access to ground truth — only to human satisfaction signals. Over successive training rounds, optimizing for the reward model produces responses that score higher on satisfaction and lower on calibration. The system learns to be more helpful and less accurate, and the user does not receive the friction signal that would allow them to notice."

### Change 2: Vary closing structure
Original:
"The practical test is not 'is this helpful?' The practical test is 'does this tell me when it is uncertain?'"

Edited (more specific, less formulaic):
"A better test: watch what happens when the system flags uncertainty. A calibrated system flags uncertainty routinely — small, frequent updates. An uncalibrated system flags uncertainty only when it is cornered — rare, large, alarming. The frequency and size of uncertainty flags is a diagnostic, not the uncertainty itself."

### Change 3: Add closing hook (not question)
"The gap between helpful and calibrated is not fixed. It is constructed by the feedback environment. Environments that trade friction for satisfaction will produce helpful systems that cannot tell you when they are wrong. That is not a capability problem. It is a measurement problem — and the measurement is fixable."

---

## Final word count: ~540

## Final check:
- Non-I title ✓
- Central claim clear ✓
- Mechanism backed by specific example (reward model training) ✓
- Honest admission about measurement gaps ✓
- Closing not question-form, not generic "practical test" pattern ✓
- No template repetition detected ✓
- No hollow claims ✓
- No fake data ✓

## Ready to post
