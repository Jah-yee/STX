# Editor — 0623_0008
# Title: Prompt injection is a flow problem, not a linguistic one

## Changes

### Opening — tighten
**Before:** "Most prompt injection discussions end up in the wrong place. Someone demonstrates a successful attack, the thread fills with variations of 'add better instructions' and 'use delimiters,' and a week later the same class of attack succeeds through a different channel. The reason isn't that the model is insufficiently aligned. It's that the system treated user input as instructions when it shouldn't."

**After:** "The prompt injection conversation keeps landing in the wrong place. Someone demonstrates an attack, the thread fills with 'add better instructions,' and a week later the same attack succeeds through a different channel. The reason isn't model misalignment. It's that your workflow places user input inside the same execution context as your system instructions. That's not a prompt problem. It's a flow problem."

### Trim redundancy — paragraph on "detection advocates"
**Before:** Long paragraph ending with "You're detecting symptoms after the workflow has already mixed untrusted input into a trusted context."

**After:** Cut to:
"The detection approach has more merit than the prompt-hardening approach, but it still treats a classification problem rather than fixing the workflow that makes classification necessary. The model — or a secondary model — is trying to distinguish instruction from data inside a token stream that was already assembled without that distinction in mind."

### Ending — remove question-framing, keep strength
**Before:** "Pick the fight you can win at scale."

**After:** Keep as-is. It's the right last line.

### Minor polish
- "capability限制" → "capability constraints" (typo/corruption)
- "capability boundaries" kept clean
- No other surgery needed

## Final word count: ~780 (tightened)

## READINESS: READY TO POST
