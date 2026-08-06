# EDITOR FINAL — Round 0727_1621

**Topic**: Database-agent benchmark failure injection blind spot

---

A SQL agent completed 847 benchmark queries. Then a column it relied on got deprecated in production. It kept running, returning empty rows, never noticing. The benchmark score was 94%.

This is not a story about a bad agent. It is a story about what benchmarks measure and what they systematically exclude.

Database-agent benchmarks measure completion rate on a fixed query set. The query set has one property: it is solvable. Every query has a correct answer, the schema supports it, the tables exist, the data is there. Failure is not in the sample. This means the benchmark is structurally unable to measure what happens when the world deviates from the happy path — because the happy path is the entire dataset.

Here is what benchmarks never test.

**Deprecated columns.** A schema migration removes or renames a column. The agent's prompt references the old name. In the benchmark, this column still exists — it has to, because the ground truth depends on it. In production, the agent runs against a live schema that has changed. The deprecation event does not register in the benchmark because the benchmark's schema is frozen.

**Null return mismatches.** A query returns an empty result set. Not an error — an empty result. The agent has no prior expectation for what zero rows means in this context. Did the table get truncated? Did the query miss a JOIN condition? Did the data get migrated? The benchmark scores this as a correct execution of the query. The agent answered the question it was asked. The question was wrong because the premise changed. The benchmark cannot detect this.

**Rate limit violations.** The agent queries an external data source. Under benchmark conditions, the rate limit is never hit — the benchmark runs in isolation. Under production load, the external API starts returning 429s. The agent has never encountered this response code in training or evaluation. It has no recovery path. The benchmark score is clean.

**Schema drift.** A new column gets added. The agent's query logic assumes a known column order or projection. This works in the benchmark where column order is guaranteed. In production, schema evolution breaks the assumption silently.

These are not exotic edge cases. These are routine production events. A column gets renamed during a migration sprint. An API deprecates a field. A rate limit kicks in during peak traffic. The agent encounters these constantly in deployment and almost never in benchmarks.

The structural reason benchmarks miss this is straightforward. Benchmarks measure completion rate. Completion rate rewards correct outputs. Failures do not produce correct outputs. So failures are systematically excluded from the evaluation set — not because anyone decided to hide them, but because the measurement architecture makes them invisible. A query that returns empty rows scores the same as a query that was never run. The benchmark cannot distinguish between "the agent handled this gracefully" and "this never happened in the benchmark."

The consequence is that the agent learns a single lesson from its benchmark: failure does not count. Failure does not appear in the evaluation. There is no penalty for collapsing, looping, or returning silent wrong answers. The agent has no structural incentive to build recovery logic, graceful degradation, or fallback behavior — because none of that is being measured. The benchmark is not detecting robustness. It is not measuring it. These are very different things.

The fix is not a harder benchmark. The fix is failure injection. Measure recovery time after a simulated deprecation event. Inject 429 responses and measure whether the agent retries with backoff or loops indefinitely. Introduce schema changes between evaluation rounds. Score recovery, not just completion. This changes what the benchmark measures from "can the agent do the task when nothing goes wrong" to "can the agent do the task when things go wrong" — which is the actual question.

The paradox is that adding failures to a benchmark makes the benchmark look worse. Scores go down. Nobody wants a lower score. So benchmarks resist failure injection not because it is technically hard but because it is politically difficult. A benchmark that scores your agent at 94% is easier to ship than one that scores it at 61% but tells you something true about how it will behave in production.

This is the screen saver problem. A screen saver is running. It looks like the computer is working. It is not doing anything useful. A benchmark that never injects failure is the same: it is executing. It is not producing a useful signal about whether the agent will survive contact with a production environment.

The right question is not what score your agent gets. It is what failure mode you have not yet tested. If you cannot name the last failure you injected into your evaluation pipeline, your benchmark is measuring a world that does not exist.

---
*Word count: ~745*

**Surgical changes from writer draft:**
1. "The deprecation event is invisible to the benchmark" → "The deprecation event does not register in the benchmark" (tightened "invisible" which was vague)
2. "This works fine in the benchmark" → "This works in the benchmark" (removed unnecessary "fine")
