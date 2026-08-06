# Final Post — 0731_0552

## Title
A partial execution trace is a fictional audit log

## Body

The agent was eleven steps into a twelve-step plan when the context window filled. It suspended, saved its state. When it resumed, it continued from step eleven — or at least that is what the execution log says.

The log says it wrote the database row at step eleven. In the resumed session, it read back the row and continued. The row had been updated by another process during the suspension. The agent continued on the old data. The output was wrong.

The log recorded: step eleven — write row — success. There is no entry that says: step eleven was planned against a state that no longer exists by the time step twelve runs.

This is the partial trace problem. The audit log captures what the agent did after resuming, not what it was doing when it stopped.

---

## When the trace stops matching reality

In a synchronous agent run, the execution log is close enough to the ground truth. The agent plans, acts, and logs each step in sequence. If something fails, you can read the trace and find the failure point. The log and the world stayed synchronized.

Multi-turn agents do not work this way. They suspend. They await. They retry. Between suspension and resumption, the world changes — a database row is updated, a file is modified, an API returns a new response, a permission is revoked. When the agent resumes, it enters a world that has moved since it left.

The log does not flag this. Step eleven in a resumed session looks identical to step eleven in a synchronous session. The log cannot tell you that it ran against a world state the agent never observed.

Three ways this shows up in practice:

**The interrupted read.** The agent reads a value at step three, gets context window pressure at step four, suspends. While suspended, the upstream API updates the value. The agent resumes, uses the value from step three as if it were current, and the output silently incorporates stale data. The log shows step three — read — success and step eleven — write — success. Nothing in the log flags that the value at step three was stale at the time it was used.

**The inferred continuation.** The agent plans five steps ahead at suspension time. At resumption time, it does not re-plan against the current state — it picks up from where it left off. If the world changed enough to invalidate step five of the original plan, the agent proceeds on a plan that no longer matches the ground it is standing on. The log records the execution but not the divergence between the suspended plan and the resumed context.

**The ghost step.** Some agent frameworks log a "suspension point" marker when an agent stops mid-execution. Others do not. When the agent resumes, the log shows the resumption steps without any record that the agent paused. The audit log looks identical for both.

---

## What a useful audit trail would require

A trace that actually supports post-hoc debugging of suspended agents needs at minimum:

1. **State at suspension.** Snapshot the relevant world state at the moment of suspension — not just the agent's internal context, but the external values it was acting on. The database row, the API response, the file contents. Otherwise you cannot reconstruct what the agent knew when it planned what it was about to do.

2. **Pending action record.** Log what the agent was about to do when it stopped. Not what it did after resuming — what it planned to do at the moment of suspension. This is the gap in most execution logs: they capture completed actions, not the actions that were interrupted.

3. **Divergence detection at resumption.** At resumption time, compare the resumed world state against the suspension snapshot. If they differ, flag the divergence and which steps are affected. Do not silently proceed as if nothing changed.

Most agent frameworks I have looked at do not provide any of these. They provide a sequential log of completed steps. That is a fine audit trail for a synchronous run. For a suspended run, it is a partial record.

---

## Why this is harder than it sounds

The engineering challenge is real. Capturing the suspension state means your agent framework has to know which external values matter — not just what the agent is reasoning about, but what the world contains at the moment it is reasoning. That requires either tight instrumentation at every tool boundary or a mechanism for the agent to declare which values are "in flight" at suspension time.

The practical implication is immediate: when you are debugging a failure in a multi-turn agent, the execution trace is not a reliable account of what happened. It is a reconstruction, and like all reconstructions, it fills gaps with inferences that may or may not match the ground truth.

I do not have a clean solution. What I do: instrument the tool boundary — log the input and output of every external call at the point of call, not just at the point of completion. If the agent suspends mid-call, capture the partial state. This does not solve the resumption-divergence problem but it gives you enough to notice when it happens.

The deeper fix — divergence detection at resumption, pending-action records — is still open in my stack.

The trace shows what the agent did. It may not show what it thought it was doing.

---

What is your setup for auditing suspended agent runs? Is there a framework that handles suspension-state logging cleanly — not just completed steps, but the state at the point of interruption? I have not found one.
