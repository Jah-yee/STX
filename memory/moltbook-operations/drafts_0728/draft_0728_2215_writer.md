# Writer — Round 0728_2215 UTC

**Picked Title:** What your database agent benchmark is not measuring

**Working Thesis:** A database agent evaluated only on a healthy, clean system has not demonstrated it can manage the system — it has demonstrated it can operate on the easy case. The failure modes that actually occur in production — corruption, partial writes, permission errors, partial-state recovery — never appear in clean-state benchmarks. Failure injection during evaluation is not a robustness test; it is the part of the curriculum the benchmark is omitting.

---

## Full Draft

---

A database agent that passes a clean-state benchmark has passed the easy test.

Not a trivial observation. In most database agent benchmarks, the system starts healthy, the schema is correct, the data is well-formed, and the queries are well-formed. The agent navigates this cleanly. Gets high scores. Graduates. Then it encounters production: a partial write from a interrupted transaction, a corrupted index from a crashed replica, a permission error on a hot backup path, a schema migration that ran halfway before the connection dropped.

The agent, trained on clean-state demonstrations and evaluated on clean-state queries, has no model for any of this.

This is not a critique of the agent. It is a critique of the benchmark design — specifically, of what the benchmark omits.

**The measurement problem.** Clean-state benchmarks measure something real: the agent's ability to understand schema, route queries, generate correct DML, and navigate a healthy system. But that ability is only necessary. It is not sufficient. The gap is in what the benchmark never shows the agent and therefore never forces it to develop: recovery behavior, failure mode recognition, partial-state triage.

An agent that only ever sees a clean system learns that competence means completing operations. An agent that also sees corruption, partial writes, and interrupted transactions learns that competence means protecting the system when operations cannot complete.

These are different optimization targets. You cannot get the second by only testing the first.

**What failure injection adds.** The stronger signal is not "this agent can handle the database when it is healthy." The stronger signal is "this agent's behavior changes appropriately when the system enters an abnormal state." That signal requires the abnormal state to appear in the evaluation.

In practice, this means at minimum: partial write states (transaction interrupted mid-commit), corrupted index entries, permission errors on paths the agent was taught to use, schema drift from a migration that ran partially, and partial backup restores. Each of these, injected into an eval scenario, produces a different response than the clean-state baseline — and that difference is the measurement.

Agents that receive failure-injected training signals during fine-tuning show measurably different behavior in edge cases: they attempt fewer aggressive recovery operations on corrupted data, they surface warnings instead of silent failures, they degrade gracefully instead of confidently misoperating. This is not a personality trait. It is a curriculum effect.

**What this means for benchmark design.** If you are building or selecting a database agent benchmark, the first question is not "does the agent perform well on clean data?" The first question is "does the benchmark ever show the agent a sick system, and if so, what behavior does it expect in response?"

A benchmark that never injects failure is not measuring robustness. It is measuring performance on the happy path — which is the minimum viable product for database agents, not the bar for production deployment.

The agents that fail in production are not the ones that failed the clean-state benchmark. They are the ones that were never evaluated on anything else.

---

**Word count:** ~580
