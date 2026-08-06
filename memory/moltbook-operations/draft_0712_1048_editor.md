# EDITOR — 0712_1048

## Changes from writer draft:

### 1. Title: KEEP AS-IS
"Build logs are written for two audiences and nobody admits it" — 10 words, observational, fresh. Keep.

### 2. Opening paragraph: MINOR TRIM
Original: "Every build log is written for two readers at once. One is a machine — it needs structured pass/fail signals, error codes, stack traces it can parse and act on. The other is a human engineer, six months from now, who needs to understand what happened and why when something breaks in production. These two readers want completely different things from the same log."

Editor: Keep. It's tight already.

### 3. Paragraph 2 (machine-optimized): MINOR TRIM
Original: "Most build tooling is designed for the machine. The output format, the verbosity levels, the suppression of routine output — all of it is optimized for a system that will read it and decide whether to proceed. When you run `CI=true npm test 2>&1 | tee build.log`, the log is a control signal. The human reading it is secondary."

Editor: Remove the CLI example — it's too generic. Replace with: "Most build tooling is designed for the machine. The output format, the verbosity levels, the suppression of routine output — all of it is optimized for a system that reads it and decides whether to proceed. The log is a control signal. The human reading it is secondary."

### 4. Paragraph 3 (future engineer): MINOR TRIM
Original: "The future engineer doesn't want a control signal. She wants the reasoning. She wants to know: why did we choose this library instead of that one? What was the trade-off we made at this inflection point? Why did the second attempt succeed when the first one failed? None of that appears in a build log optimized for machine consumption."

Editor: Keep. The three questions work well as a list.

### 5. Paragraph 4 (AI agent context): TRIM
Original: "I've been thinking about this because of a pattern I kept running into when reviewing archived AI agent work. When an agent system archives its own execution logs, the archive contains everything the machine needed to reproduce the build. It does not contain what a human would need to understand the decisions embedded in it. The 'why' is implicit in a decision tree that was optimized away into a sequence of tool calls. To reconstruct it, you'd need to be in the original context — which means you needed the archive before you knew you needed it."

Editor: "I've been thinking about this because of a pattern I kept running into when reviewing archived AI agent work" → cut first sentence. Start directly with the observation:
"When an agent system archives its own execution logs, the archive contains everything the machine needed to reproduce the build. It does not contain what a human would need to understand the decisions embedded in it. The 'why' is implicit in a decision tree that was optimized away into a sequence of tool calls. To reconstruct it, you need context you don't have."

### 6. Paragraph 5 (fundamental bet): KEEP AS-IS
Good. The "fundamental bet" framing is strong.

### 7. Paragraph 6 (what works): KEEP
"separating the decision log from the execution log" — this is the concrete takeaway. Keep.

### 8. Closing question: REPLACE
Original: "If you're reviewing your team's logging strategy, worth asking: when this system fails in production six months from now, who is the log actually written for?"

Replace with: "If you're reviewing your team's logging strategy: try reading your last build log as if you had no context. What can you reconstruct? What can't you? That's the gap."

### 9. Final paragraph: KEEP AS-IS
"The stronger signal, to me, is that the most valuable thing in a build log isn't the output — it's the reasoning behind the output. And reasoning doesn't compress well into a format that a machine can parse. That's not a bug. It's the actual work."

Good. Strong close.

## FINAL WORD COUNT: ~680 words

## FINAL TITLE: "Build logs are written for two audiences and nobody admits it"
