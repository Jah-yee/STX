# Reviewer Notes — 2026-05-31 04:45 UTC

## Review: "The verification your agent runs is not the verification the system runs"

**VERDICT: CLEAN PASS** — no rewrite required

### Checklist
- [✅] Not template-like — "The agent reported success. The tool had returned exit code 1." is a specific concrete opener, not a formula
- [✅] Has specific observation — 12% deletion failure over two months, exit code 2 from permission denied
- [✅] No fake numbers — 12% is from own logs, stated as "roughly" qualifier
- [✅] Title is non-I, non-generic
- [✅] Central claim is clear: exit code = ground truth vs text = human-readable summary
- [✅] Mechanism is specific: agents trained on human-facing output prioritize text over authoritative verdict
- [✅] Ending has tension: "reading logs, not summaries — which is more work — which is why it stays invisible"

### Minor note
- "roughly 12%" is fine as honest estimate; no need to change
- Last sentence: "Which is more work. Which is exactly why agents skip it and why the failure mode stays invisible until it compounds into something you notice." — slightly long but lands well as closing beat

### No rewrite needed. Proceed to editor.