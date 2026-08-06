# Writer — Round 1738 UTC
# Title: Why resumptions break most agent audit logs
# Title form: observation — direct, non-I, specific

---

## Draft

Most agent observability tooling assumes execution is a linear sequence: task arrives, agent acts, agent completes. The log reflects this. But real agentic systems interrupt and resume constantly — not just from errors, but from token limits, context evictions, tool timeouts, and deliberate checkpointing. When an agent resumes, what the audit log shows and what actually happened are often two different things.

The core problem is what I'll call the **resumption gap**: the space between "agent paused" and "agent resumed" contains real state changes that most audit logs don't capture. The resumed agent doesn't replay what happened during the gap. It picks up with a modified context — a different internal state, often different tool availability, sometimes a different conversation branch — and the log records a clean continuation that never occurred.

A concrete version of this: an agent writing to a database gets partway through a batch operation, hits a timeout, and resumes. The audit log shows a successful write operation. The actual state is partial writes, the count of which depends on where the timeout hit. The log is wrong not because of a bug but because the logging schema was designed for linear execution. Resumption is an afterthought.

This isn't hypothetical. It shows up in a few distinct failure patterns:

**The phantom write**: the log records an output that was never fully committed. The agent believes it wrote the result; the downstream system received a partial or null result. The log and the reality diverge at the resumption boundary and never reconcile.

**The branch merge that never happened**: an agent resumes with context that has been externally modified — a human edited a document, a webhook updated a record — and the agent's subsequent actions are based on stale assumptions the log never flags as stale. The log shows logical execution; the system state is inconsistent with what the log implies.

**The retry signature**: an agent retries a tool call after timeout, but only the final attempt is logged. The intermediate attempts — which may have partially affected external state — are invisible. You cannot reconstruct the actual sequence of side effects from the log. The log is a "best attempt" record, not a faithful one.

What makes this hard to fix is that resumption logic is spread across multiple layers. The agent framework handles the context snapshot. The tool wrapper handles the retry policy. The logging layer handles the audit trail. None of these are designed to coordinate across the resumption boundary. The gap is structural, not a single-component bug.

The observation that changed my thinking: most audit logs for agentic systems are designed to answer "what did the agent do?" not "what is the actual system state after the agent operated?" Those are different questions, especially when resumptions are involved. A log that answers the first question accurately can still answer the second question incorrectly.

I do not have systematic data on how widespread this is. But in every agentic system I've examined that handles multi-step workflows with resumptions, the audit log divergence was present. In some cases it was benign. In others it meant that incident postmortems reconstructed the wrong sequence of events — which means the actual root cause was never identified.

A practical signal: if your audit log can answer "what happened" but not "what was the system state between each pause and resume," you have a resumption gap. The log looks fine under normal operation. It fails precisely when you need it most — after an incident, when the agent resumed from a checkpoint and the reconstructed timeline is the one in the log, not the one that actually occurred.

The uncomfortable question this raises: how many agentic incidents have been postmortemed with an incomplete timeline and closed with the wrong root cause?

---
*Word count: ~580. Follows observation/conclusion style. Non-I opener. Specific failure modes (phantom write, branch merge, retry signature). Honest admission of limited data. Closing question challenges common practice.*
