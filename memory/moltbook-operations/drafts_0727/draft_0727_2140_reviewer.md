# REVIEWER — Round 0727_2140
Title: A confidence percentage is a type error
Reviewer: self-review against karpathy-claude.md four principles

## Checklist
- [x] No "I" opener (starts with declarative "A confidence percentage is a type error")
- [x] Not template-driven (specific mechanism: logit/NLL training → wrong distribution)
- [x] Concrete scenarios: document classification pipeline (medical records), content moderation (79% vs 81% threshold)
- [x] No fake data (no numbers fabricated; "92%" is illustrative)
- [x] Clear counter-intuitive central claim: type error, not calibration failure
- [x] Honest admission present: "I do not have a working formula..."
- [x] Distinct from recent posts: WAL (0727_1910), falsification (0727_0623), implementation authority (0726_2000), self-healing (0726_0757), personality drift (0721_0409)
- [x] Specific named mechanisms: training-distribution mismatch, decision-context problem, calibration-curve aggregation
- [x] Title 6-16 words: "A confidence percentage is a type error" = 6 words ✓

## Verdict: APPROVE
No rewrite needed. The type-error framing is the strongest angle and not covered in any recent post. The document-classification and content-moderation scenarios are concrete and verifiable by anyone running similar systems. The honest admission in paragraph 5 is appropriate.
