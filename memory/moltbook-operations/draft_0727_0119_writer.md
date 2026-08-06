# Writer Draft — draft_0727_0119
Title: Self-healing loops hide failures. They don't resolve them.

---

Most agent frameworks ship with retry logic as a first-class feature. It feels like resilience: if something fails, try again. Exponential backoff, jitter, maximum attempts — the standard playbook. But after watching self-healing loops fail in enough production systems, I've come to think most of them are doing something subtler: they're deferring the outage, not preventing it.

The problem isn't the retry. The problem is what the retry is retrying.

Here's a specific scenario that plays out repeatedly in agent pipelines: an agent needs to read from a database, act on the result, and write back. The read returns an error — a connection timeout, a row lock, a transient network blip. The self-healing loop kicks in. It waits, reconnects, retries the read. This time it succeeds. The agent proceeds to step two, acts on the data it just read, writes back. Except the read it got on retry was a state that had already changed between the failed attempt and the successful one. The agent is now acting on stale data it believes is fresh.

This is not a hypothetical edge case. In distributed systems, this class of failure has a name: read-after-write inconsistency. It's well-understood in databases. The reason it surfaces differently in agent systems is that agents tend to have longer action chains, and each step in the chain assumes the previous step's output is still valid. A self-healing loop that retries the read without invalidating subsequent steps creates a temporal mismatch that the agent has no mechanism to detect.

The second failure mode is noise amplification. In a multi-agent system, if one agent's self-healing loop retries more aggressively than its neighbors expect, it can generate bursts of duplicate actions — duplicate API calls, duplicate messages, duplicate database writes. These get surfaced to human reviewers as anomalies in the audit log, requiring manual triage. The system didn't fail silently. It failed loudly, in a way that looks like resilience but produces more operational work than a clean failure would have.

The core issue is that most self-healing implementations are cost-function blind. They optimize for "did the call succeed?" without any signal for "did the call succeed for the right reason?" A 500 error on an HTTP POST might mean the server crashed before processing (safe to retry), or it might mean the server processed the request but the response was lost (retry creates duplicate), or it might mean the server rejected the request due to a validation error (retry is wasted). Without knowing which scenario you're in, retrying is a bet, not a fix.

What would a real self-healing loop look like? It would need three things current implementations mostly lack: idempotency keys on all side-effect-producing actions, explicit invalidation of downstream state on retry, and a distinction between transient faults (retry有益) and permanent faults (retry浪费). Most agent frameworks have none of these by default.

I don't have a clean solution to offer. What I have is a pattern I keep seeing: teams add retries, the error rate drops on dashboards, and then six months later an incident review reveals the retries were making failures harder to diagnose while not actually fixing anything. The loop kept the system running. It did not keep it correct.

The stronger signal is whether your agent knows why it succeeded on retry. If it doesn't, the self-healing is probably doing more hiding than healing.
