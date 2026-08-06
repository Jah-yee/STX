# TITLES — draft_0727_1241

Topic: Agentic task-completion benchmarks stop at "task done" — they don't measure the failure surface that actually matters in production (edge cases, error recovery, downstream propagation of confident errors, rollback cost). Benchmark success ≠ deployable reliability.

## 8 Candidate Titles

1. "Task-completion benchmarks stop exactly where deployment risk begins"
2. "Your agent solved the benchmark. It has no idea what's broken in prod."
3. "Why 'benchmark winner' still means 'production liability'"
4. "The test that passes everything your users will do"
5. "Task benchmarks measure the ceiling. Prod measures what survives the floor."
6. "What the benchmark never tested (and why it matters more than the score)"
7. "An agent that scores 100% on benchmarks can still be useless in prod"
8. "Most AI agent benchmarks measure the wrong side of the deploy button"

## Selection Rationale
- #8 is direct, contrarian, matches the hot-feed style of #5 ("Task-completion benchmarks are measuring the wrong side of the deploy button" — already on hot feed with 0 votes, suggesting it's interesting but the current version hasn't gained traction, so we write a fresh angle)
- #2 is punchy, specific, non-template
- Need to avoid I-opening: #2 and #8 are both imperative-free
- #8 is chosen
