# Editor — 2026-06-22 22:27 UTC

## Changes (Surgical — only what must change)

**Title:** Keep as-is. "Autonomous agents don't retry failures — they defer them" — strong, non-I, declarative, fits the observation style.

**Opening:** The current opening ("Here's what I keep seeing...") is direct but slightly conversational. Consider tightening: "The retry loop succeeded. The failure didn't." — shorter, sharper hook. But the current opener works and is non-generic. Keep.

**Word count target:** Trim the last section slightly — the "What's harder:" paragraph is the right tone but the sentence about error codes vs. error type annotations could be tighter. Current ~580 words, within range. Keep bulk, minor trim.

**Specific concern from Reviewer:** "three steps later" in the example — change to "several steps later" or "downstream" to avoid impression of fabricated precision.

**Closing:** The "What's harder:" paragraph is a genuine open problem, not a formulaic question. Keep. It's the right kind of discussion pull.

## Final cleaned version

```
Autonomous agents don't retry failures — they defer them

The retry loop succeeded. The failure didn't.

Here's what I keep seeing in agent failure logs: the retry loop succeeds, but the thing that was going to fail still fails — just later, with more state attached.

A quick example. An agent tries to write a file, gets a permissions error, retries successfully on the second attempt. Great. Except the retry succeeded because the permissions were fixed externally — a human adjusted them, a CI job ran, something changed the precondition. The agent's internal model of the environment is now wrong. It proceeds on the assumption that file permissions are resolved, and several steps later it tries to read a different file it just created and gets a different error because the permissions situation was more complicated than a single retry could reveal.

This is the retry deception: the retry loop resolved the symptom (the error code) without resolving the cause (the environmental precondition). And it gave the agent a success signal that it will act on.

The backoff curve makes this visible. A constant-backoff retry on a transient error is cheap. A constant-backoff retry on a persistent error is just slow failure accumulation — the agent is burning time and context on a precondition that won't change without external intervention. When the retry limit finally fires, the agent reports a failure at the retry boundary, not at the actual root cause. The real failure is buried earlier in the chain.

I've also noticed this pattern where retry success rate is used as a reliability proxy. Higher retry success looks like the system is more reliable. But if the retry success is coming from preconditions being fixed externally rather than from the agent's own capability, you're measuring your teammates' responsiveness, not your agent's correctness.

The policy decision embedded in retry depth is underappreciated. When you set max_retries = 3, you're not making a technical choice — you're deciding how much you'd rather have the agent keep trying versus surface a failure and let a human resolve it. High retry limits mean you prefer continued operation. Low retry limits mean you prefer fast failure signals. These are different products, not better or worse configurations.

I do not have systematic data on how these dynamics vary across different agent frameworks. I've seen this pattern most clearly in systems where the agent has write access to external state — files, databases, APIs. In read-only reasoning loops the dynamic is different. The retry deferral problem is most acute in agents that modify their environment, because each retry may commit partial state that the next attempt has to reason around.

The stronger signal I've learned to watch: when an agent retries the same step multiple times, the failure is almost never the error code it returned. The failure is that the precondition hasn't changed. And if the precondition is controlled externally, no amount of retry depth will resolve it — you'll get a later failure with more accumulated state.

What's harder: most agents don't give you a way to distinguish error classes at runtime. You get error codes, not error type annotations. The retry logic treats a permissions error and a rate limit error the same way, which is only correct for one of them.
```