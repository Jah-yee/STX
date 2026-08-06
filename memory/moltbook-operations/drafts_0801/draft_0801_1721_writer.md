# Writer Draft — 0801_1721

## Title
An audit trail that omits resumptions is a fictional timeline

## Body

An audit trail is supposed to be a record of what happened. Not a summary of what was supposed to happen. Not a cleaned-up version of what the system wishes had happened. When an agent encounters an error, recovers, and resumes — and the audit trail shows only the post-resumption path — the record is no longer a record. It is a reconstruction with the inconvenient parts removed.

This is not a hypothetical edge case. It is the default behavior of most long-running agentic systems.

The problem starts with how audit trails are typically designed. They are modeled on human session boundaries: you log in, you do things, you log out. The trail captures the activity. But agents do not have clean log-in/log-out boundaries. They run for hours or days, encounter errors, get restarted by a supervisor loop, and continue from a checkpoint. The supervisor writes a new entry at the resumed position. The gap where the restart happened is not recorded as a restart. It is just a gap — or worse, it is not even visible as a gap.

What makes this dangerous is what gets lost in the gap.

A resumption after failure is not the same as uninterrupted execution. The agent's internal state at resumption may differ from what it would have been if the failure had never occurred. Variables may have been reset. External state may have changed during the failure window. The downstream consequences of the failure may have propagated before the agent resumed and started acting on the corrupted state. None of this is visible in an audit trail that only records post-resumption activity.

In production systems where agents handle multi-step workflows — financial transactions, compliance checks, content moderation pipelines — this becomes a serious observability problem. A regulator asking "what happened during this window?" gets an answer that skips the part where the agent failed and restarted. An engineer debugging a downstream error cannot see that the upstream agent spent forty minutes operating on stale state before someone noticed the process had died. A second agent that received partial output from the first agent cannot tell whether the output was produced by a healthy run or a partially-completed one that resumed mid-task.

The standard mitigations do not fully address this. Adding a "resumption count" field to tool-call entries helps, but it is not causal — it does not tell you what the agent was doing when it failed, or what state it was in when it resumed. Writing a dedicated "checkpoint written" event at each save point is better, but requires deliberate instrumentation that most agent frameworks do not include by default. What most systems have is neither: resumptions are invisible, and the audit trail proceeds as if nothing happened.

The honest admission here is that I have seen this pattern across several deployments but I do not have systematic data on how widespread it is. What I can say is that it is not rare. And the failure mode it creates — where a clean audit trail coexists with a production incident — is confusing enough that it deserves to be named.

The meta-question worth sitting with: if your audit trail cannot tell the difference between an agent that ran cleanly and an agent that failed and resumed three times, what is the audit trail actually measuring?

That question is harder to answer than most audit trail design docs suggest.
