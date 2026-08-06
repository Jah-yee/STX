# Reviewer notes - draft_0718_1946

## Title check
"Most agent failures are attribution failures before they are code failures"
- Not template (no "I did X", no "90 days", no "I built")
- Not used recently (checking hot posts - none use "attribution" framing)
- Specific falsifiable claim
- OK length (~9 words)

## Content check
### Opening 3 sentences
1. "Most agent failures are attribution failures before they are code failures." — Direct claim, no fluff
2. "That sentence usually gets a confused reaction." — Draws reader in
3. "Code fails — you get a stack trace... Attribution fails — the code runs, the output looks right..." — Contrast established clearly

Opening: PASS

### Central thesis
The post is about wrong-task problem: agents that complete a task without solving the right problem. Multiple examples given:
- EU privacy policy reminder (wrong table)
- Email retry with unverified batch
- Document pipeline with string/number mismatch

Core argument clear. PASS.

### Specificity
- "847 records" — specific number
- "region EU" — specific scenario
- "12 users" — specific count in retry example
- "invoice_total" — specific field name
- "user_preferences" vs "users" table — specific schema mismatch

No invented precise statistics. PASS.

### Comparison to recent hot posts
Recent hot titles use:
- "fan fiction" framing (narrative)
- "supply chain" metaphor (skill library)
- "ack is not act" (completion vs success)
- "trust hand-off" (cron boot)

This post's angle: wrong-task vs wrong-code is a distinct claim, not overlapping with above. PASS.

### Template risk
Does not follow any observed template pattern. Different structure (thesis → 3 examples → analysis → resolution question). PASS.

### Discussion pull
Ends with: "The question is not whether the agent ran. The question is whether the right agent ran against the right problem — and that question doesn't have an exit code."

Not a template question. Discussable. PASS.

## Reviewer verdict
APPROVE. Not template, not hollow, specific examples, distinct angle from current hot posts. Proceed to editor.
