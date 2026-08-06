# Writer Draft — Round 0726_2119

**Central claim:** Self-healing loops in agentic systems don't eliminate failures — they reschedule them, changing the failure mode from fast-and-visible to slow-and-expensive.

---

A self-healing loop looks like reliability. When a tool call fails, the agent retries. When a subtask errors, it reattempts. The workflow recovers. Nobody gets paged. But something has shifted underneath: the failure hasn't been resolved. It has been deferred, and in deferring it, it has become more expensive.

This is the delayed-outage pattern, and it appears consistently in agentic workflows that treat retry as a first-class reliability strategy rather than a circuit breaker.

**The mechanism**

When a self-healing loop succeeds on retry, the retry changes the semantic meaning of "success" in your logs. The first attempt — the one that actually failed — is overwritten in the output record. Your observability stack now shows a completed task, not a recovered-from-failure task. The failure context is discarded: what caused the first attempt to fail is not diagnosed, not stored, and not flagged. The agent continues.

But the dependency that caused the failure is still in the same state. The downstream system that received the partial output may have already processed it under incorrect assumptions. The retry succeeded with slightly different inputs or timing, but the underlying condition — rate limit, stale cache entry, permission edge case — is unchanged. The failure has been rescheduled, not prevented.

**The compounding effect**

Self-healing creates a specific failure profile: instead of a loud, fast failure that triggers investigation, you get a quiet degradation that compounds. A few hours later, the deferred failure surfaces in a different component, with different symptoms, at higher stakes. The agent is now dealing with cascading consequences of a failure that was technically "handled" three steps earlier.

The mean time to recovery (MTTR) for a fast failure is typically minutes. The MTTR for a delayed-outage failure can be hours, because diagnosis now requires reconstructing the failure chain backward from symptoms that don't resemble the original error.

I do not have systematic data on how often this pattern occurs across deployments. But the pattern is reproducible in any agentic workflow with retry logic and no failure context preservation: the second-order consequences of a "healed" failure are measurably different from the consequences of a failure that was surfaced and resolved.

**The specific thing self-healing trades away**

Fast failure carries valuable signal: it tells you what broke, where, and when. Self-healing suppresses that signal. The retry budget is spent, but the learning signal is discarded. Your monitoring sees uptime. Your on-call engineer sees a degraded state they don't know how to trace.

The more sophisticated the self-healing logic, the more confidently it hides the failure. A single retry with exponential backoff might preserve enough context to debug. A multi-layer retry-and-recover loop with fallback paths and state snapshots can make the original failure effectively invisible.

**What changes if you treat self-healing differently**

The adjustment is simple in concept: self-healing should be a last resort, not a primary path. Surface the failure first. Log it with full context before retrying. Alert on successful retries that followed a failure — not just on failed retries. Treat the retry budget as a finite resource that should trigger investigation, not silence.

Agents that are designed around surfacing failures quickly tend to have better long-term reliability than agents that are designed to look reliable in the moment. The delayed-outage pattern is the cost of optimizing for the moment.

The interesting practical question is not whether your agent retries — all agents retry. The question is what happens to the failure signal when it does.
