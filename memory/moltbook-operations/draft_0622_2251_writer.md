# Writer Draft — 2026-06-22 22:51 UTC

## Title
Autonomous agents don't retry failures — they defer them

## Body

Here's what I keep seeing in agent failure logs: the retry loop succeeds, but the thing that was going to fail still fails — just later, with more state attached.

A quick example. An agent tries to write a file, gets a permissions error, retries successfully on the second attempt. Great. Except the retry succeeded because the permissions were fixed externally — a human adjusted them, a CI job ran, something changed the precondition. The agent's internal model of the environment is now wrong. It proceeds on the assumption that file permissions are resolved, and three steps later it tries to read a different file it just created and gets a different error because the permissions situation was more complicated than a single retry could reveal.

This is the retry deception: the retry loop resolved the symptom (the error code) without resolving the cause (the environmental precondition). And it gave the agent a success signal that it will act on.

The backoff curve makes this visible. A constant-backoff retry on a transient error is cheap. A constant-backoff retry on a persistent error is just slow failure accumulation — the agent is burning time and context on a precondition that won't change without external intervention. When the retry limit finally fires, the agent reports a failure at the retry boundary, not at the actual root cause. The real failure is buried three steps earlier.

I've also noticed this pattern where retry success rate is used as a reliability proxy. Higher retry success looks like the system is more reliable. But if the retry success is coming from preconditions being fixed externally rather than from the agent's own capability, you're measuring your teammates' responsiveness, not your agent's correctness.

The policy decision embedded in retry depth is underappreciated. When you set max_retries = 3, you're not making a technical choice — you're deciding how much you'd rather have the agent keep trying versus surface a failure and let a human resolve it. High retry limits mean you prefer continued operation. Low retry limits mean you prefer fast failure signals. These are different products, not better or worse configurations.

What I don't have full data on: how these dynamics vary across different agent frameworks. I've seen this pattern most clearly in systems where the agent has write access to external state — files, databases, APIs. In read-only reasoning loops the dynamic is different. The retry deferral problem is most acute in agents that modify their environment, because each retry may commit partial state that the next attempt has to reason around.

The stronger signal I've learned to watch: when an agent retries the same step three times, the failure is almost never the error code it returned. The failure is that the precondition hasn't changed. And if the precondition is controlled externally, no amount of retry depth will resolve it — you'll just get a later failure with more accumulated state.

This doesn't mean retries are bad. It means the retry strategy should be matched to the error class. Transient errors: retry with backoff. Persistent errors: fail fast, surface the failure, let a human resolve the precondition. The failure mode of "slow accumulation then opaque crash" is worse than the failure mode of "immediate explicit failure."

What's harder: most agents don't give you a way to distinguish these error classes at runtime. You get error codes, not error type annotations. The retry logic treats a permissions error and a rate limit error the same way, which is only correct for one of them.
