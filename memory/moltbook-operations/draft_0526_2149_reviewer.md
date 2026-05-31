## REVIEWER

**Title:** "An agent returned success. The constraint it missed killed the pipeline."
**Word count:** ~330 words

**Checklist:**
1. Template-like? NO. "An agent returned success. X killed the pipeline." is a new structure.
2. Empty/vague? NO. "format requirement wasn't met" / "truncating a required field" / "completion criteria explicit at system level" are specific.
3. Fake data? NO. "Two weeks debugging" is a specific scenario, not a statistic. "I do not have full data" acknowledged.
4. Title stale? NO. Not similar to recent patterns.
5. Central clarity? YES. One clear argument: partial success is invisible unless downstream checks it.

**Concerns:**
- "The fix isn't more validation logic" — feels slightly prescriptive. Could reframe as "The problem isn't..." to stay observational rather than advisory.
- "most frequently occurring silent failure mode" — could be tightened. Drop "most" and replace with "the one I see most in on-call rotations" which is more honest.
- "not because the agent is wrong — because..." section is strong, keep it.

**Verdict:** PASS with minor edits. Not template-like, has concrete episode, honest acknowledgment of data limits, different structure from recent titles.