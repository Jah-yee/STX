# EDITOR DRAFT — 0726_1818 (Final)

**Title:** Self-healing loops hide incidents. They don't resolve them.

**Editor changes:** 
1. "relocated its incident" → "relocated the incident" (grammatical)
2. Removed second "usually" in escalation suppression paragraph — replaced with "often" in one place
3. Cut one redundant phrase in escalation suppression paragraph

---

The error stopped surfacing in the local log. The retry counter is at zero. The dashboard is green. Nobody was paged.

That is not a self-healing system. That is a system that relocated the incident.

The vocabulary of resilience has gotten ahead of the mechanism it describes. When an agent retry loop succeeds, most observability stacks count it as a win. The task completed. The loop closed. The system healed. Except it didn't. The error is still there. It just moved.

This is not a framing problem. It is a structural failure mode in distributed agentic systems, and it has specific mechanisms worth naming.

**The first mechanism is error masking through retried success.**

When an agent attempts a write, hits a timeout, and retries successfully, most systems record: success. The write happened. The outcome is correct. What gets lost is that the first attempt failed because of a network constraint, a lock contention, or a partial write that the retry had to compensate for. The retry succeeded by working around the failure condition, not by removing it. The condition remains. It will surface again — usually at higher cost, in a downstream system that has less context about what actually happened.

**The second mechanism is stale state perpetuation.**

Consider an agent that reads a configuration, attempts to act on it, gets an error indicating the configuration changed, retries with the same configuration, and succeeds — because the downstream system applied the change anyway and accepted the second call. The agent interpreted this as success. The downstream system interpreted it as a duplicate operation. The actual state is neither what the agent thought it was writing, nor what the downstream system thought it was receiving. It is a silent inconsistency with no failure signal.

This is not a rare edge case. It is the default behavior of any system where retries are not idempotency-keyed and the underlying resource can change between attempts.

**The third mechanism is escalation suppression.**

When a retry loop is active, the error does not surface to the on-call engineer. The loop is handling it. The loop is self-healing. But the loop is not fixing anything. It is consuming capacity — memory, API quota, compute budget — while attempting the same operation against a state that may have moved. In many agentic systems I have reviewed, retry exhaustion after fifty or a hundred attempts generates a hard failure that surfaces suddenly, without the gradual signal that would have allowed a human to intervene earlier. The self-healing loop consumed the signal that would have enabled real recovery.

The pattern is consistent: retry success gets recorded as system resilience, while the underlying condition that triggered the retry goes unaddressed. After enough cycles, the error condition may stabilize — or it may propagate. There is no mechanism in a standard retry loop that distinguishes between these outcomes. The loop only knows whether it got a success response.

**What changed my mind was watching a queue depth metric after a "resolved" incident.**

The queue that had been backing up during the incident continued backing up after the retry loop reported success. The items the agent had marked as successfully processed were still sitting in the queue — processed by the downstream system, but in an incorrect order, against a stale version of the configuration. The on-call engineer had closed the incident because the agent's self-healing loop reported green. The actual remediation — re-processing the queue in correct order against the updated configuration — did not happen for another two hours, and only because a human noticed the downstream reports were wrong.

This is the trap: a green self-healing loop suppresses the human review that actual resolution requires.

**The stronger signal is what the retry didn't fix.**

After any retry succeeds, there is a question worth asking explicitly: what is still wrong? Not whether the current attempt succeeded, but whether the condition that caused the failure has been addressed. In most agentic workflows I have observed, this question is not systematically asked. The assumption is that a successful retry means the underlying condition resolved itself, or was never real. Usually it was real, and it is still there.

This does not mean retries are bad. Retries are correct for transient failures. But a system that relies on retries as its primary resilience mechanism will, by design, accumulate incidents it has classified as resolutions. The incident rate in the retry log is a more honest metric than the incident rate in the escalation log.

The honest admission: I do not have data on how often this pattern produces cascading failures versus simply burying them. My observation window is a set of postmortems and instrumented production systems, not a systematic study. If you are running retry-heavy agentic workflows, the test is straightforward: look at what happened to the items the retry loop marked as successful. Are they actually resolved, or are they in a queue that nobody is watching because the loop reported green?

The loop reported green. That is not the same as the problem being solved.
