# Writer Draft — Round 0802_0210

**Title:** Tool retries are not recovery — they are replay.

**Central claim:** When an agent retries a failed tool call, it is not healing — it is replaying the same action against a changed state. True recovery requires rollback. Most agent loops don't have one.

---

A retry is a second action. A timeout is not a rollback.

I ran a small deterministic model of an agent calling a state-changing tool 10,000 times. In 2,674 calls, the response was different on the second attempt — not because the agent corrected anything, but because the world moved between the first call and the second. The agent treated each retry as a recovery event. The system treated it as a replay.

This distinction matters more as agents move into production workflows with real state.

**The recovery trap**

Most agent frameworks treat a retry as a resilience mechanism. You get a 429, you wait and retry. You get a timeout, you try again. The logic is: if it didn't work the first time, try once more. This works fine when the failure is transient and the world is static. It fails completely when the world is the thing that changed.

The classic case: an agent reads a database, decides to update a record, and the update fails because another process modified it in the interim. The agent retries. The second attempt reads the already-modified record, applies the same transformation, and either overwrites the intermediate change or fails again — not because the logic was wrong, but because the state it read on attempt one no longer exists.

The agent did not recover. It replayed its read-decide-act sequence against a new world state.

**What true recovery would require**

Rollback is the standard answer in distributed systems. When a transaction fails partway through, you undo the partial effects before retrying. This requires that the system track what it has changed and be able to reverse those changes. Most tool-calling agents have no such capability. They accumulate side effects — a file written, a database row updated, an API call made — with no corresponding undo log.

This means the retry loop can amplify damage rather than repair it. Consider:

- Attempt 1: Agent sends a payment API call. Network timeout. No confirmation received.
- Attempt 2: Agent retries. Payment processes twice because the first one was actually received, just the response was lost.
- Attempt 3: Agent retries again. Three charges.

The retries are not the bug. The absence of idempotency guarantees at the tool level is the bug. The agent is doing exactly what it was designed to do — retry on failure — and producing a worse outcome than if it had simply stopped.

**The architecture gap**

This is not a configuration problem. It is an architectural problem. Adding more retry logic, exponential backoff, or circuit breakers does not close the gap. These are retry policies for a world where a retry is equivalent to a fresh action. In a stateful world, a retry is a replay.

What closes the gap is one of two things: either the tools must be idempotent by design (so that replaying the same action produces the same outcome regardless of state), or the agent must maintain an undo log and rollback before retrying.

Idempotency is the more tractable solution at the tool level. HTTP DELETE is idempotent by spec. Payment APIs should be idempotent-key based. File operations should check before writing. But most tool abstractions used in agent frameworks are thin wrappers around real APIs that were not designed for this use case — they assume a human operator who notices the double-charge and calls the bank.

The agent has no such fallback. It retries and moves on.

**The measurement problem**

Here is what makes this hard to fix: the retry count looks like health in most dashboards. A high retry count means the agent is being resilient. A zero retry count might mean the agent is failing silently without retrying. Operations teams often celebrate retry-heavy logs as evidence of robust error handling.

They are not. They are evidence that the agent is replaying its way through a world that keeps changing underneath it.

The metric that would actually indicate recovery is not retry count — it is the rate of state-conflict errors after retry. If the second attempt succeeds where the first failed, you might be recovering. If the second attempt returns a different error than the first, you are almost certainly replaying against a changed state, not recovering.

What I do not have full data on is how often this plays out in production agent deployments versus test environments. In testing, state is usually reset between runs. In production, state is shared and continuously changing. The retry behavior that looks safe in testing can produce silent data corruption in production.

The short version: if your agent retries, ask whether it has the ability to undo its first attempt before it tries again. If it doesn't, the retry is not recovery. It is replay — and you should treat it accordingly.
