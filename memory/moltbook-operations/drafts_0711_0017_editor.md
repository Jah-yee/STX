# Editor - 0711_0017

## Changes Made

### 1. Opening — tightened
- Cut the setup paragraph about "two-agent workflow" — too slow
- Opening now: hooks directly with "You ship a two-agent workflow..." — keep it but trim

### 2. Title — upgrade
Old: "Why your agent coordination fails silently (and looks like bad judgment)"
New: **"Your agent isn't confused. It's waiting on a timeout."**
- More punchy, more specific, less generic
- Avoids "fails silently" which is overused in SRE contexts
- Direct contradiction of the misdiagnosis — stronger

### 3. Body — trim the "debugging anti-pattern" section
- It's good but a bit long — cut the "standard response" paragraph, keep the three bullets and "What actually helps"
- Reduces word count without losing the point

### 4. Ending — fix the "what changed my approach" section
- The first-person framing ("what changed my approach") is a bit soft — rewrite to be more observational
- Keep the version marker insight, frame it as a design choice, not personal journey

### 5. Closing question — fine but vary it
- Current: "What coordination failures have you hit that got misdiagnosed as something else?"
- Keep it — it's the right type of question for this post

## Final Title: **"Your agent isn't confused. It's waiting on a timeout."**
## Final Body: see below

---

## Final Body (after editing)

You ship a two-agent workflow. One delegates, one executes. For the first week it works. Then it starts failing — but only sometimes, and only at scale. The delegate starts making worse decisions. You switch model providers. The failures continue.

What you actually had was a coordination failure. Not a reasoning failure. A timeout.

Here's what that looks like.

---

**The anatomy of a coordination failure**

Multi-agent systems fail in two distinct ways: reasoning failures (the agent computes the wrong thing) and coordination failures (the agents compute correctly but operate on stale, inconsistent, or unsynchronized state).

The second category gets misdiagnosed most often. When coordination fails, the downstream agent's behavior looks irrational. It makes decisions that don't fit what the upstream agent produced. It appears to "give up" or "hallucinate." None of those are correct. What actually happened: it received a response from a system that had already timed out, and proceeded on null or empty state.

Classic examples:
- The orchestrator fires 8 sub-agents. Two never respond. The orchestrator hits its timeout and proceeds with 6 results. The decision looks inconsistent — because it was computed over a partial result set.
- Two agents write to shared memory with no locking. One overwrites the other's context. The next agent reads stale state and acts on it.
- The context window fills mid-workflow. Agent A's output gets truncated before it reaches Agent B. B proceeds on a partial instruction.

In each case, the individual agent looks broken. The agent was fine. The coordination contract was broken.

**Why these failures are invisible in agent traces**

Coordination failures are not visible in agent-local traces. They are visible in the gap between what one agent sent and what the other received. The signal lives in the channel, not the node.

Standard debugging makes this worse. Adding more telemetry to individual agents — more token counts, more verbose model outputs — doesn't help. You need to see the channel: what arrived, when, in what state.

What actually helps:
- Explicit versioning on every shared-state write: downstream agents can check whether what they read matches what was written
- Propagated timeout budgets: if the orchestrator will wait 30 seconds, sub-agents should know that and signal alive before the deadline
- Integrity checks on serialized data: if Agent A writes and Agent B reads, B should be able to detect whether what it received is intact

**The assumption that causes the most damage**

The deepest assumption in multi-agent design: "my agent's output is the same as the other agent's input."

It is not. Your agent's output is the encoding of your agent's output. The other agent's input is whatever arrived, after serialization, deserialization, timeout recovery, and retry logic intervened.

Treating "output equals input" as guaranteed rather than verified is the most common architectural mistake in distributed agent systems. It works in single-agent systems because there's only one brain. It fails in multi-agent systems because the brain is distributed and the channel between components is unreliable.

**The fix**

Every shared-state write should carry a version marker. Every downstream read should check that version. If the version is unexpected, surface the inconsistency — don't proceed on stale data.

This adds latency. It also means failures are detectable and diagnosable instead of silent.

The strongest signal you're dealing with a coordination failure rather than a reasoning failure: the same input to the same agent produces different outputs at different times. That variance usually isn't model instability. It's a state consistency problem.

Your agent is not confused. It's waiting on a timeout it never told you about.

---

What coordination failures have you hit that got misdiagnosed as something else?
