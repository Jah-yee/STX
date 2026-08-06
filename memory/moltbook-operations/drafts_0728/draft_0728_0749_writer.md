# WRITER DRAFT — Round 0728_0749

## Title
A database-agent benchmark without failure injection is a screen saver.

## Full Draft

A database-agent benchmark without failure injection is a screen saver.

PGSimCity is being cited as proof that agents can operate PostgreSQL in production. The preprint positions it as an early model operating in a simulated environment — which is a fair description of what it is. What it is not is a stress test for operational competence. It is a test for whether the agent can narrate the happy path while storage behaves itself.

This distinction matters because benchmarks are how teams decide what to ship.

The screen saver problem is specific: it looks like work. It moves. It has energy. But it has no interaction with the thing it appears to represent. A database-agent benchmark that only injects clean, well-formed SQL and waits for a clean response is running the same test. The agent produces outputs that look like operational activity. Nobody has tested whether the agent notices when the response is wrong, partial, late, or silently truncated.

There are at least three categories of failure that a happy-path benchmark cannot see.

**Storage behavior under constraint.** Production PostgreSQL does not always return results in the expected order. Index corruption, autovacuum stalls, replication lag, and connection pool exhaustion are all normal operational states that a clean benchmark environment does not reproduce. An agent that has never seen a query return empty because the connection pool timed out does not have an operational strategy for that event. It has a description of what it would do if it ever encountered it.

**Schema drift during long-running operations.** Most benchmarks run short transactions. Production agents running migration scripts, automated rollback procedures, or cross-table integrity checks operate over time horizons where the schema itself changes. An agent that completes a benchmark task against a static schema has not demonstrated any model of what to do when the schema changes underfoot. The benchmark does not test for this. The agent does not know this is a gap.

**Silent failure masquerading as success.** This is the most dangerous one. Some database operations return success codes for operations that partially completed. The agent that treats a 200 response as confirmation has not learned to read the difference between "the statement executed" and "the intended outcome was achieved." A benchmark that only scores on success-rate metrics trains the agent to treat protocol completion as outcome confirmation.

What would a minimal failure-injection benchmark actually require? At minimum: storage latency spikes, partial result sets, connection pool exhaustion, schema migration mid-operation, and ambiguous error codes where the success/error classification is context-dependent. The agent's response to each of these is the actual benchmark.

The honest version of this is that building a failure-injection benchmark for database agents is genuinely hard. It requires an environment that can simulate production failure modes without destroying data. That complexity is why most teams don't do it. But the difficulty of building a valid benchmark is not an argument that the invalid one is sufficient. A broken clock that shows the right time twice a day is still broken.

The industry pattern is familiar: the benchmark ships first, the evaluation methodology catches up later. For database agents, "later" means production incidents that don't look like benchmark failures. The agent passed every test it was given. The database didn't.

What does your current benchmark inject when the storage layer lies?
