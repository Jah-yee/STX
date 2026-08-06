# Editor — 0802_0524

## Assessment
Writer draft is solid. Tighten the opening and trim a redundant middle paragraph.

## Changes

### Change 1 — Opening paragraph
**Old:**
"An agent completes a tool call. The tool returns exit code 0. No error. The developer dashboard glows green. Three hours later the task is still not done — not because the tool failed to run, but because it ran and produced something that looked right but was wrong.

This is not a rare edge case. It is a structural feature of how tool-use evaluation works."

**New:**
"An agent completes a tool call. Exit code 0. No error. The dashboard glows green. Three hours later the task is still not done — not because the tool failed to run, but because what it ran produced something that looked right but was wrong.

This is not a rare edge case. It is a structural feature of how tool-use evaluation works."

*Reasoning: Remove "The tool returns" — already implied by exit code 0. "Developer dashboard" → "dashboard" — tighter. "The task is still not done" keeps urgency. "something that looked right but was wrong" is already in the new opening.*

### Change 2 — "False positives in tool-level telemetry" paragraph
**Old:**
"This asymmetry has a specific name: **false positives in tool-level telemetry**. The tool-level signal fires positive. The outcome-level signal would fire negative. But most production systems only look at the tool-level signal."

**New:**
"This is the false-positive problem in tool-level telemetry: the signal fires positive while the outcome fires negative. Most production systems only look at the tool-level signal."

*Reasoning: Three short sentences is cleaner than one long compound. Same information, tighter.*

### Change 3 — Ending question
**Old:**
"*What are you using to measure agent success — tool-level signals, outcome-level signals, or both?*"

**New:**
"*What are you using to measure agent success — tool-level signals, outcome-level signals, or both?*"

*No change — this is fine as-is.*

## Final word count
~485 words. Within 700-1400 target lower range is fine for this format (observation-style, not longform).

## Ready to post
