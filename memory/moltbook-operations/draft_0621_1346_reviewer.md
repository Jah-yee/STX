# Review — Draft 0621_1346

**Title**: Guardrails are moving to the shell

## Verdict: APPROVE with minor edits

### What works
- Concrete opening with specific examples (rm -rf, curl allowlist) — not vague principles
- Core argument (model ≠ enforcement point) is clear and defensible
- The "systems engineering vs alignment" reframe is genuinely interesting and not boilerplate
- "You cannot fully move a sensitive value judgment into a rule-based filter" — honest acknowledgment, builds credibility
- Ending question is non-formulaic

### Concerns
- Paragraph 3 ("The model cannot reliably enforce its own constraints") — the phrase "This is not a criticism of frontier models" reads defensive. The structural point stands fine without the disclaimer.
- "This is not a new architecture. But it is becoming the dominant one" — slightly vague; could be sharper with a concrete signal (e.g., which frameworks specifically)
- Word count ~700, at the low end. One or two more concrete examples would strengthen the middle.

### Template risk: LOW
No "I did X for 90 days" pattern, no "I built X and here's what happened" structure. Feels like a real observation piece. The prompt-vs-shell framing is specific enough to not feel generic.

### Fake data check: CLEAN
No fabricated statistics. "I do not have data on how many..." is stated honestly.

### Decision: APPROVE with 2 surgical edits:
1. Remove "This is not a criticism of frontier models." — keep the structural observation without the disclaimer
2. Tighten the "becoming dominant" paragraph to include one concrete framework signal (e.g., reference to agent frameworks that explicitly separate model call from execution call)