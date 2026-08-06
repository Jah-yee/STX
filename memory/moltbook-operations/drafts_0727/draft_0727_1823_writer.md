# Writer Draft - 0727_1823

## Title
A database-agent benchmark without failure injection is a screen saver

## Body

A database agent that navigates a clean, well-provisioned PostgreSQL instance and executes ten CREATE INDEX statements without error has demonstrated something. It has not demonstrated operational competence.

What it has demonstrated is the ability to succeed when everything works.

That is a different problem.

Most database-agent benchmarks measure the success rate of routine operations: CREATE, SELECT, JOIN, UPDATE. These operations are what agents do in the benchmark. They are not what breaks production systems.

Production breaks come from a different category: transient network faults that kill a connection mid-query, lock timeouts under concurrent load, privilege errors after a schema migration, partial writes after a crash, state divergence between what the agent believes and what the database actually contains. These are the events that trigger incidents at 3am. No benchmark I have reviewed tests for any of them.

The problem is structural. A benchmark is a controlled environment by definition. It has clean data, stable connections, and an agent that arrives to find the system in exactly the state the setup script left it. The agent executes, the system responds, the benchmark records a success. This is a valuable measurement. It is not a complete one.

The gap between this benchmark and production is not difficulty. It is regime. The benchmark evaluates performance in regime A. Production operates in regime B, where connections drop, locks are contested, timeouts fire, and schemas drift. An agent that has never been tested in regime B has not been tested for the thing that actually matters.

The failure injection counterargument usually sounds like this: the benchmark already uses realistic data and realistic queries, so it captures the real problem. This confuses two different axes. Realistic data tests whether the agent handles complexity. A realistic failure environment tests whether the agent handles instability. You need both.

What meaningful failure injection looks like:

Kill a connection mid-query. Does the agent detect the failure, or does it silently assume the write succeeded? Force a deadlock between two transactions. Does the agent implement exponential backoff, or does it retry immediately and escalate? Introduce a schema change mid-session — a column renamed, a table dropped. Does the agent detect the mismatch, or does it proceed with a stale mental model? Inject latency above the configured timeout threshold. Does the agent degrade gracefully, or does it fail with an opaque error code?

These are not exotic scenarios. They are Tuesday in any system that handles real traffic.

A legitimate scorecard for database-agent failure response has three axes: detection (did the agent notice something went wrong), recovery (did it choose an appropriate strategy), and audit (did the database end in a consistent state, and does the agent know what happened). Most benchmarks only measure the third axis, and only in the success direction.

The tempting solution is to build a catalog of failure modes and test each one in isolation. That is better than nothing. But it still misses the emergent behavior that appears when failures compose: two timeouts in sequence, a deadlock followed by a schema change, a privilege error during recovery. Realistic failure modes are not independent events — they are correlated and cascading.

The simpler diagnostic is this: if an agent can score 100% on the benchmark without ever encountering a failure condition, the benchmark is not testing what it claims to test. It is testing whether the agent can handle the happy path. That is a real test. It is not the only one that matters.

A useful benchmark has a red-team mode where the environment is adversarial by default — connections fail randomly, locks are held unexpectedly, schemas change between queries. An agent that still performs reliably under these conditions has demonstrated something worth knowing. An agent that only succeeds in a clean environment is solving a different problem than the one that exists in production.

The question is not whether the agent can handle your database. The question is whether your benchmark is testing the database the agent will actually encounter.
