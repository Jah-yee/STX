# Writer Draft — "Observability is not intent reconstruction"

## Post

Observability is not intent reconstruction.

This sounds like a vocabulary dispute. It is not. It is a structural gap that explains why teams with mature agent observability still get surprised by failures they cannot explain after the fact.

Here is the distinction. Observability tells you what the agent did: which tools it called, what it read, what it output. Intent reconstruction would tell you whether what the agent read was still valid by the time the output was produced. The first is a log. The second is a validity check. Most agent observability stacks are very good at the first and structurally incapable of the second.

---

## What gets instrumented

Agent observability has improved significantly over the past year. Most production systems now capture tool call traces, context window utilization, model outputs, and latency breakdowns. You can replay what the agent did step by step.

What you cannot see, in most systems, is whether the state the agent read at step N was the same state that existed at step N+1. The gap between read and act is unobserved — not because teams do not care, but because it requires instrumenting the substrate, not the agent.

The substrate is the state layer: databases, queues, caches, third-party APIs, shared file systems. The agent is the process that reads from and writes to the substrate. Standard observability for agents does not include consistency checks at substrate boundaries.

This is not a monitoring problem you can solve with better tracing. Tracing tells you the agent read X. It does not tell you whether X was still true when the agent acted on X. These sound similar. They are not.

---

## The read-write gap

Here is the concrete failure mode. An agent reads a resource value, computes an action based on that value, and writes the result. Between the read and the write, the resource changes — either because another process wrote to it, because it is a time-sensitive API with its own refresh rate, or because the agent's own prior write has not yet propagated.

The agent produces an output that is locally correct — it correctly processed X — but globally wrong — it should have processed Y, because X had already become Y by action time.

Your observability stack shows: read(X), compute(action), write(result). Everything looks fine. The failure is invisible in the trace because the trace records events, not state validity.

This is not a hypothetical edge case. In any system with concurrent access — which is most production systems — this happens constantly at some rate. In stable test environments it rarely happens, which is why it does not show up in benchmarks.

---

## Why intent reconstruction is harder than logging

You cannot reconstruct intent from a trace because intent requires knowing what the world looked like at each decision point — not just what the agent saw, but whether what the agent saw was still the current state.

To do this, you need one of two things. Either you need replayable state — the ability to freeze the world at each read and validate whether the read value matches the committed state at the time of the corresponding write. Or you need explicit consistency checks at read-act boundaries: re-read the critical value immediately before the irreversible action, and fail explicitly if it changed.

Neither of these is standard in agent frameworks. They are standard in distributed systems — optimistic locking, read-your-writes consistency, version vectors — but that literature has not been widely absorbed into the agent tooling ecosystem.

The result is that most agent observability is a very detailed record of what happened, with no mechanism to determine whether what happened was still correct when it happened.

---

## The practical consequence

When you run a post-mortem on an agent failure and you have full observability traces, you can usually reconstruct what the agent did. You cannot usually reconstruct whether the agent's decision was valid given the state it was acting on, because that would require state-level instrumentation you probably do not have.

This shifts every post-mortem toward "the agent made a wrong decision" rather than "the state the agent was acting on had changed since the read." The first is a model problem. The second is a substrate problem. They have different fixes. Observability that cannot distinguish between them will keep pointing you at the wrong root cause.

The stronger signal for this gap is not in the agent trace. It is in the delta between what the agent read and what the substrate shows as the authoritative value at the time of the action. If that delta is non-zero, the failure was not in the reasoning — it was in the gap between read and write.

Getting that delta into your observability stack is not a model upgrade. It is a substrate instrumentation problem.
