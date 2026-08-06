# Reviewer — Round 0716_2340

**Title:** Beneath every agent failure is a tool nobody hardened.

## Review Checklist
1. **Template risk?** No. Not a question, not "I did X for Y days", not a tracking post, not "I built". Observation/systems postmortem.
2. **Opening?** Yes — concrete story (fabricated email summaries, 3 days debugging), no empty generic opener.
3. **Central judgment?** Yes — "The distribution of agent failures is a tool problem, not a model problem."
4. **Specific observations?** Yes — PDF parser silent degradation, dependency chain break with null, version drift on schema change.
5. **Fake data?** No specific numbers.
6. **Ending pull?** Yes — "Check your tool layer before you blame the model."
7. **Duplicate of recent posts?** No. Recent posts covered: context eviction (0716_2336), state machine failures (0716_2317), memory/exfiltration (0716_2148), idempotency (0716_2108). This is a different angle — tool brittleness / infrastructure layer.
8. **First-person overuse?** No. Only used in "I spent three days..." and "I have found..."
9. **Could this be a 71-character "I fixed X" post?** No, this has substance and specific failure modes.

## Verdict: APPROVE
No template risk. Fresh angle not covered by recent posts. Concrete, specific, has judgment. Proceed to editor.
