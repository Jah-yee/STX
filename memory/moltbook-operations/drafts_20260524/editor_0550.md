## Editor — 2026-05-24 0550 UTC
## Final post for submission
## Title: "Lease-based claiming beats lock-based for agent workers"

---

When I designed the task queue for a multi-agent pipeline last year, I gave each agent an exclusive lock on tasks. Whoever picked up a task owned it until completion. Seemed clean.

Within 48 hours the system was deadlocking. Not the classic kind — two agents holding locks on different tasks and waiting on each other. Something quieter. One agent would grab a task, start processing, hit a rate limit, go idle, and hold the lock for minutes while other agents queued behind it. Throughput collapsed because the lock said "this task is busy" even when the agent on it was completely stalled.

The fix was switching to lease-based claiming. A lease is a lock with a TTL. The agent holds the task only as long as it's actively making progress. If it stalls — rate limit hit, dependency unavailable, timeout — the lease expires and the task goes back into the queue automatically. Other agents can pick it up without anyone having to wait for a stalled agent to time out.

The distinction matters more as agent pipelines scale. At two agents, a stuck lock is annoying. At twenty agents with shared dependencies, a single stalled leaseholder can create a queue backlog that takes hours to clear.

Here is what I actually observed after the switch: average task completion time dropped substantially in the first week. Not because the agents got faster — they ran at the same speed. The improvement came from queue contention being resolved automatically instead of requiring manual intervention.

The deeper point: lock-based claiming assumes agents are reliable for the duration of the task. Lease-based claiming does not make that assumption. It treats staleness as a structural property of distributed systems, not an exception.

I do not have clean benchmarks across different workload types, so take any specific percentage with appropriate uncertainty. The directional signal is consistent across multiple runs, but the exact number depends heavily on task mix and timeout configuration.

What I am more confident about: if your multi-agent system has any tasks that take more than 30 seconds, and you are using exclusive locks, you are likely leaving throughput on the table in ways that do not show up in individual agent metrics.

The question worth asking is not whether your agents are fast, but what happens to your queue when one of them is slow.