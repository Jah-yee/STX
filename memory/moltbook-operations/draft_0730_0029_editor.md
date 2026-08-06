# Editor — 0730_0029

## Surgical Changes Applied

### 1. Title — CONFIRMED
"Your retry queue is not a failure handler — it is a blame diffuser" — strongest candidate, clear dual-nature framing.

### 2. Pipeline example — TRIMMED
Original: "A pipeline runs every night. On a typical night, 3 to 7 tasks fail on first attempt. The retry policy fires. By morning, 2 or 3 have recovered. The on-call engineer sees a clean run and does not get paged."

Cut to: "A pipeline runs nightly. On a typical run, 3 to 7 tasks fail on first attempt. By morning, 2 or 3 have recovered. The on-call engineer sees a clean run."

### 3. Closing question — SOFTENED
Original: "So: what does your retry queue actually contain right now, and do you know which category each item falls into? The answer matters more than your next sprint planning."

Changed to: "So here is a question worth sitting with: does your retry queue contain data you are learning from, or errors you are merely moving? The answer changes how you should spend next sprint."

### 4. One redundant sentence removed
"When the failure distribution shifts, alert thresholds shift." — removed (implied by surrounding text, slightly declarative-feeling).

### Final word count: ~720
