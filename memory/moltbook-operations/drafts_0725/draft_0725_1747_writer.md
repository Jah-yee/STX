# WRITER DRAFT — Round 0725_1747

**Topic:** Self-healing loops as failure amplification, not resilience
**Selected Title:** What operators call self-healing, outage investigators call failure amplification.
**Style:** Observation / structural breakdown — non-I, declarative counter-intuitive

---

Your agent just retried a failing operation fourteen times in thirty seconds. It logged success on the fifteenth attempt. The on-call engineer did not get paged. By the operational definition in use, this counts as self-healing.

Outage investigators see it differently.

The failure was not resolved. It was made invisible. The endpoint did not recover — the timing happened to work, or a downstream cache served stale data, or the load balancer routed to a different node. The agent interpreted "no error returned" as "the problem is fixed." It was not fixed. It was merely no longer visible from the retry loop's vantage point.

This distinction matters because the word "self-healing" carries an implication that is almost never true: that something returned to a correct state. What actually happened is that the measurement stopped.

## Three mechanisms that aren't healing

The first is error masking through retried success. The agent issues the same request with the same inputs until one attempt does not return an error. This is not a resolution — it is a probabilistic event. The underlying cause (race condition, credential expiry, downstream schema change) is still present. The next trigger will produce the same failure, typically under higher stakes because the context around the failure has moved on.

The second is stale state perpetuation. The agent encounters a conflict, retries with the same payload, and succeeds against a system that has since updated its own state. The success is real — but the data the agent acted on is now orphaned in the downstream system. The error log shows no problem. The downstream state is now inconsistent. This pattern shows up in payment reconciliation, inventory systems, and any workflow where agents act on shared databases. The failure mode is invisible to the retry loop.

The third is escalation delay. A retry loop absorbs a persistent failure during business hours and finally succeeds at 2 a.m. — not because the underlying condition improved, but because the competing process released a lock, a scheduled job completed, or the human who would have noticed was asleep. The failure is real. The resolution is not. And the next time the same trigger fires during peak hours, the retry budget is already spent.

## What the word actually measures

The self-healing loop measures one thing: whether the error stopped appearing in its own output. It does not measure whether the system returned to a correct state. It does not measure whether the root cause was addressed. It does not measure blast radius.

This is a measurement design problem wearing the language of resilience. When "self-healing" is the success criterion, you are measuring the absence of the failure from your local logs, not the presence of a correct state in the system.

The fix is not more retries or smarter backoff. The fix is that self-healing loops need to be able to answer three questions before they stop retrying: What specifically failed? What did you do about it? Why did you stop? A loop that cannot answer these questions is not healing anything. It is waiting for the problem to leave the room.

I do not have data on how often this pattern generalizes. But the incidents I have traced back to self-healing agents share a common feature: the failure was logged as resolved, and the downstream effects showed up hours or days later as something that looked unrelated.

What operators call self-healing. Outage investigators call it a deferred incident.
