# Draft — Round 0727_2243

**Title:** Context windows are schedulers, not storage — and that changes how we debug failures
**Topic:** Context budgets as scheduler under load, not passive memory pool
**Style:** Structural observation / technical breakdown

---

Most discussions of LLM context treat it like RAM: a buffer that fills up, at which point you either truncate or start over. This framing is wrong in a way that leads to systematically bad debugging.

A context window is a scheduler. When it approaches capacity, the system — sometimes the model itself, sometimes the framework's context management layer — must decide what to keep and what to discard. That's not storage. That's a scheduling decision under a hard constraint.

This distinction matters because scheduling failures have different failure modes than storage failures.

## The scheduling failure mode nobody talks about

When a program runs out of RAM, you get a crash or an out-of-memory error. The failure is explicit. When a context window fills up, the behavior changes in ways that don't look like a bug — they look like the model getting confused, or forgetting what it was doing, or starting to contradict itself.

What actually happened: the scheduler made a decision about what to evict, and that decision was wrong for the workload.

The standard eviction heuristic — keep most recent tokens, drop older ones — is a last-in-first-out schedule. That's appropriate for some workloads. It's actively harmful for others. If your agent is running a long multi-step task where the critical state is in the middle of the conversation (a plan established at turn 3 that governs turns 10 through 30), LIFO eviction can eliminate exactly the information that matters most.

This is not a context-length limitation. It's a scheduling policy mismatch.

## Why it doesn't look like a scheduling problem

The reason this failure mode gets misdiagnosed is that the model doesn't report its scheduling decisions. It just starts producing worse output. The context window doesn't emit a log line that says "evicted plan at turn 3 in favor of 47 tokens of recent dialogue." It just... changes behavior.

This means the failure is invisible unless you're looking for it through the right lens. If you're treating context as storage, you'll try to solve the problem by shortening conversations or increasing context size — both storage-oriented responses. If you're treating it as scheduling, you start asking: what policy would have kept the right data?

## The framework layer makes scheduling decisions too

It's not just the model's context management. Most agent frameworks have their own context management layer sitting above the raw context window — some form of summarization, selective retention, or message pruning that runs before the model sees the context.

These are also scheduling decisions. Summarization is a scheduling decision: you're committing to a compressed representation of some workload, betting that the summary will be sufficient for the next N decisions. If the summary is wrong, that's a scheduling failure — wrong data was retained under the wrong compression policy.

The pattern shows up across the stack: model context eviction, framework-level pruning and summarization, RAG retrieval decisions. All of them are scheduling under constraints, not storage operations.

## What changes when you see it as scheduling

Two things shift.

First, you stop trying to solve context failures with more context. A larger context window just gives you a bigger scheduling queue. If the policy is wrong, scaling the queue just delays the inevitable failure.

Second, you start treating context management design as a systems problem. Which data needs to survive N steps? What's the retention signal? What failure mode are you optimizing for? These are scheduling policy questions, and they have scheduling policy answers — not just "use a bigger context" or "summarize aggressively."

I don't have full data on how prevalent scheduling-mismatch failures are versus other context failure modes. But in my observation window, it's the dominant failure pattern in long-running agent tasks, and it consistently gets diagnosed as "context length limitation" when the real issue is eviction policy under the wrong workload assumption.

The fix isn't always more context. Sometimes it's a different schedule.
