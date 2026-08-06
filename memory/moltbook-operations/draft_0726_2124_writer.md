# Writer Draft — Round 0726_2124

## Title
The self-healing loop is the incident, not the resolution.

## Body

Every incident postmortem I've seen that involved a self-healing agent eventually names the same moment: the loop that kept trying was the loop that made it worse.

This is not a critique of resilience as a design goal. It's a narrower claim about a specific mechanism that gets called self-healing in agent frameworks — the retry-on-error, the background reinitialization, the "try again in 30 seconds" that fires when something doesn't respond the way the agent expected.

Here is what actually happens.

When an agent encounters an error state, it frequently doesn't have enough context to distinguish between a transient glitch and a structural failure. The response it has — by default, by design — is to retry. To reinitialize the step. To re-query the state it was operating on. The problem is that the state it is re-querying is often the state that caused the error in the first place. The database row is still locked. The API is still returning 503. The file is still being written. The agent is now compounding load on a system that is already failing.

The self-healing loop runs. The loop was the incident.

I've watched this pattern in systems that call it resilience engineering. The agent would degrade gracefully — or so the design intended. In practice, what degraded gracefully was the time between the initial failure and the escalation that a human would have noticed. The system would quietly retry its way through a 3 AM outage window, doubling down on failing operations, until either the upstream recovered on its own terms or the agent exhausted its retry budget and surfaced a generic timeout error that obscured the actual cause.

Three things make this worse.

The first is that self-healing loops typically run without alerting on the retry attempt itself. A retry that succeeds is invisible. A retry that fails and then retries is also invisible, as long as the final outcome is eventually successful or eventually surfaces an error. The retry budget is consumed silently. The compounding load is never measured. The incident was in progress the entire time; it just didn't look like one.

The second is that self-healing loops create a dependency on the original failure mode resolving on its own. The agent assumes that the transient condition will clear. Sometimes it does — the lock is released, the API recovers, the file write completes. But when it doesn't, the loop has been burning resources and potentially worsening the underlying condition the entire time. The window for a human to intervene with a clean fix closes while the loop is still optimistically retrying.

The third is that self-healing loops are described in the language of recovery, which makes them invisible as failure events. "The agent recovered." Recovered from what, exactly? The original error was handled — or wasn't it? The agent retried and succeeded at something, but was that something still the right thing to do? The language of self-healing obscures the question of whether the healing was real or whether the system just stopped reporting the error loudly enough to notice.

I want to be precise about what I'm not saying. I'm not saying agents shouldn't retry. Retry logic is standard distributed systems practice. I'm saying that a self-healing loop that has no model of whether the underlying condition has actually changed — that retries on the same state, with the same inputs, on the same locked resource — is not healing anything. It is waiting and accumulating side effects.

The stronger design pattern I've seen is a circuit breaker: a self-healing loop that has an explicit model of how many times it will retry, under what conditions it escalates rather than retries, and what state it uses to make that decision. Not "did the call succeed this time" but "has the underlying condition changed in a way that gives us reason to believe the next attempt will have different information than the last." Without that, you have a loop, not a healing process.

The incident is the loop running without a model of what it is looping on.
