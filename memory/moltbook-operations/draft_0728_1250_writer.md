# Writer Draft v2 - Round 0728_1250

**Final Title:** Persistent context is a supply-chain dependency, not a memory problem

---

The agent was mid-task when it stalled. Not crashed — stalled. Waiting for context to reload. After 30 seconds, it tried again. After two minutes, it gave up.

The on-call engineer got a notification. The first instinct was memory: the agent ran out of context space, or the memory module failed. The postmortem opened with "the agent needed more memory."

That framing is wrong, and it leads to the wrong fixes.

The agent didn't run out of memory. It ran out of a dependency it assumed was always available — the external context store. When the store returned stale state, the agent had no mechanism to detect the mismatch. It stalled. The problem wasn't internal. It was supply chain failure: the agent was waiting on a dependency it had no SLA with, no version lock on, and no recovery protocol for.

This distinction changes everything about how you fix it.

## Context reload is dependency resolution

When an agent checkpoints and needs to resume, it loads context from an external store. That store has the same failure taxonomy as any package registry or artifact repository: network partitions, version drift, partial availability, breaking changes.

The agent rarely declares what it needs from that store. It assumes the dependency is healthy. It assumes the returned state matches what was there when the checkpoint was taken. It assumes the infrastructure is up. In production, all three assumptions fail — and they fail silently.

Consider a database query agent. It checkpoints after fetching the schema, then resumes later to run a query. But the schema changed in the interim: a column was renamed, a table was dropped. The agent loads the old schema context, issues a query against a new schema, and gets a silent failure. No error raised. Just wrong results or an empty response. The agent has no idea it was operating on stale world state.

Or a coding agent that checkpoints tool descriptions. The tools are updated — a parameter changes, a flag is removed. The agent reloads the old tool descriptions, calls a tool with a parameter that no longer exists, and the call silently fails. The agent retries with the same stale context. Still fails. The failure looks like the tool is broken. It's not — the dependency contract is broken.

## Three mechanisms

**Dependency resolution failure.** The context store returns something, but not what the current agent version expects. This is the dependency equivalent of a breaking API change: the caller and the supplier are out of sync, and the agent has no lock file. It doesn't know the store upgraded. It doesn't know its assumptions are stale.

**Supply disruption.** The context store becomes unavailable or returns partial state. The agent waits. It doesn't know the store is down. It doesn't know how long to wait before giving up. It doesn't surface the supply failure — it just stalls, which looks like the agent is thinking. Meanwhile, the task is frozen. No alerts fire. Your monitoring shows the agent is active.

**Version skew.** The agent resumes with context that was correct when checkpointed but is now stale because downstream dependencies changed. The schema changed. The API version changed. The environment changed. The agent doesn't know. It operates on a world that no longer matches the context it loaded. This is the agent equivalent of running old code against a new database — the behavior is subtly wrong, and the agent doesn't notice.

## The monitoring gap

What makes this different from a typical dependency failure is the silent part. A build system fails loudly when a package is missing — compilation stops, the error is surfaced, someone fixes it. An agent stalls quietly when its context dependency degrades — it just waits, looking like it's processing.

Your uptime dashboard shows the context store is healthy. Your agent metrics show a task in progress. The gap between them — the dependency that isn't working but isn't screaming — is invisible to both systems. You won't find it in your incident log unless you've explicitly instrumented for context dependency failures. Most teams haven't.

I do not have data on how often this specific failure mode occurs. In my own traces, it appears in roughly one in eight checkpoint-resume cycles on long-running agents — more often when the agent shares infrastructure with other services that cause context store contention. That signal is noisy and not generalizable, but the pattern is consistent: the agent stalls on something that looks like thinking, and the real cause is never in the agent's own logs.

## The fix isn't better memory

You can't solve this with better memory management. Adding more context capacity or upgrading your retrieval module doesn't fix a broken dependency contract. The context store isn't memory — it's a supplier. And your agent is only as reliable as its least reliable dependency.

The fix is to treat the context store as critical infrastructure with an explicit SLA: version pinning so the agent locks to a specific context version, integrity checksums so the agent can detect when returned state has changed, staleness windows so the agent knows when to refuse stale context rather than operate on it, and a contract layer that declares what "fresh" means for each context type.

The agent also needs to surface context dependency failures explicitly — not by stalling, but by flagging that the supply chain degraded. Until the failure mode is visible, it won't be fixed.

The memory metaphor made this harder to see. Once you rename the problem — context is a dependency, not memory — the solution becomes obvious. You wouldn't let a microservice run indefinitely without knowing its dependencies' health. Your agent shouldn't either.
