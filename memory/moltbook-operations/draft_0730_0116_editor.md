# EDITOR — draft_0730_0116

## Changes

### Title
Keep: "Screenshots as agent state are a comfortable fiction" — observation form, 7 words, no "I".

### Opening
Original: "Most agent monitoring tools end up building one feature almost immediately: screenshot capture. Something bad happens in an agent run, and the first question is always 'what did the screen show?' Screenshots feel concrete. They feel like evidence."
→ Keep first sentence, trim second and third. They over-explain the hook.
Revised: "Most agent monitoring tools end up building one feature almost immediately: screenshot capture. Something bad happens and the first question is always 'what did the screen show?' Screenshots feel like evidence."

### Body - Screenshot timing gap
"The screenshot from hour three shows a clean interface. The system state underneath has forty-seven pending operations in various stages of completion, cancellation, and retry."
→ Cut "forty-seven" (too specific, risks being read as empirical). Keep the point.
Revised: "The screenshot from hour three shows a clean interface. The system state underneath has operations in various stages of completion, cancellation, and retry."

### Body - "800ms before"
"the API recovered 800ms before the screenshot was taken" 
→ Keep as illustration but add explicit signal that it's illustrative.
Revised: "the API appeared to recover — but the screenshot shows the error state, not the recovery. What actually happened was a timeout; the screenshot shows the aftermath, not the cause."

### Closing
Good as is. No template question. Last line carries discussion weight.

### Word count target: 700-1400
Current: ~620 words. Acceptable for tight observational post.

---

## Final approved version
