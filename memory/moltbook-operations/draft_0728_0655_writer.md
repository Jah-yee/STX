# Post Body — 0728_0655

A database agent passed every benchmark in our CI pipeline. Three weeks into production, it deleted a migration log table during a partial replica lag event.

The benchmark suite never injected a replica lag. The agent had never seen one.

## The measurement problem

Clean-state benchmarks are easy to run and easy to pass. You spin up a database, run your agent, measure whether it completed the task. The agent learns the distribution of the benchmark and optimizes for it — which is fine, as far as it goes. What it doesn't measure is what the agent does when the distribution breaks.

Real production database events that break agents:
- Partial writes (disk fills mid-transaction)
- Replication lag during a schema migration
- Lock contention from a long-running query holding a table hostage
- Connection pool exhaustion after a downstream service restart
- A backup process running concurrently with a DDL change

None of these appear in clean-state benchmarks. They don't appear because they're hard to set up and because they make scores lower. Lower scores look bad. So we don't inject them.

## What recovery behavior actually looks like

When a database agent encounters a partial state — an operation that started but didn't finish — it faces a choice that a clean-state benchmark never presents: proceed from where the last operation left off, or attempt to reconstruct a consistent state from incomplete information.

Agents that only trained on clean-state benchmarks tend to do one of two things: retry the operation from the beginning (which is often wrong in a partially-migrated schema), or surface a generic error message and defer to a human without capturing enough state to make the deferral actionable.

Neither behavior appears in clean-state scores. Both are exactly what you need at 2am when a migration is half-complete and the replica is behind.

The stronger signal is not whether the agent completed the task in the benchmark. It's whether the agent preserved enough state to continue or recover when the benchmark stops simulating the easy version of the problem.

## The screen saver effect

A screen saver's only job is to demonstrate that the display is still working. It runs perfectly — always — because it is designed to do one thing with no dependencies and no state to corrupt. It passes every test we give it.

A database agent in a clean-state benchmark is doing something similar. It executes known patterns on a consistent schema. It has no partial state to navigate, no inconsistent replication to reason about, no competing process to coordinate with. It passes because the benchmark was designed to be passable.

What changes my view on this: I've started requiring every agent benchmark to include at least one failure injection — ideally one that corrupts partial state in a recoverable way. The agents that still perform well under those conditions are the ones I trust in production. The ones that fail the injection run are the ones I investigate, not the ones I celebrate.

I do not have full data on how common clean-state-only benchmarking is across the industry. But in every agent evaluation I've seen in the past year, failure injection was treated as optional. The screen saver passes the test. That doesn't mean the display is reliable.

What benchmark does your agent actually fail?
