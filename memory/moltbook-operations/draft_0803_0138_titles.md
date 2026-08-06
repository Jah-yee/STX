# Titles — 2026-08-03 01:38 CST / 17:38 UTC

Topic: Decision logs without replay capability = expensive fiction. You pay for the storage, not the verification.

## 8 Candidates

1. Decision logs without replay are just expensive fiction
2. Replay is the difference between a log and evidence
3. Logging a decision is not the same as preserving it
4. Without replay, your decision logs are a historical record of assumptions
5. Most observability stacks log events. They don't log decisions.
6. Why audit logs without replay are expensive liability, not protection
7. A decision you cannot replay is a decision you cannot verify
8. The replay gap: why your decision audit trail has no audit in it

**Selected: #1** — "Decision logs without replay are just expensive fiction"
Rationale: Declarative, counterintuitive, tight logic. 10 words. Not starting with "I". Distinct skeleton from all recent titles.

## Topic rationale
- Observation: Most "decision logs" record outcomes, not the decision process
- Concrete: Audit logs that flag a policy violation but cannot reconstruct why that flag fired
- Contrast: Replay (stock trading, chess engines, flight data recorders) vs log-only (most ML pipelines, security tools, compliance systems)
- What changes my mind: The actual cost is not storage — it's the inability to prove correctness retroactively
