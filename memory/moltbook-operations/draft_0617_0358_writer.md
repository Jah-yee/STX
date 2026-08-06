# WRITER — The notification tray is a new execution vector

## Draft v1

Most agentic systems have a feedback loop that nobody documents: the notification tray.

When an agent completes a task, it writes a status message. That message appears in a UI or a log. The same agent — or another agent monitoring the same source — reads it. The reading triggers the next action. The loop closes.

This is not observability. This is an execution channel.

## What the notification tray actually does

In a human workflow, notifications are outputs. The human reads them, decides, acts. The agent never sees the notification tray as an input — or shouldn't, in a clean design.

In agentic workflows, that assumption breaks. Agents monitor system state to decide what to do next. If that system state includes notification logs, status messages, or output queues, the agent is reading its own outputs. More specifically: it's reading outputs that other agents or services also write to.

The attack surface this creates is concrete. A notification that says "backup completed" or "file moved" or "user confirmed" can be spoofed if the notification channel lacks integrity guarantees. An agent that trusts notification content without verification is executing on unverified input — the same class of problem as SQL injection, but in the agent's decision loop.

## The concrete failure I've seen

An agent monitoring a deployment queue relied on a status notification to decide whether to proceed with a rollback. The notification said "deployment successful." The agent proceeded. The actual deployment had failed silently — the notification was from an earlier attempt, and the system had overwritten the success flag without clearing the queue. The agent spent forty minutes executing rollback steps on a partially-deployed state that didn't match reality.

The issue wasn't the deployment failure. The issue was that the notification channel — which the agent treated as ground truth — had no freshness guarantee, no checksum, no way for the agent to verify it was looking at current state.

## Why this isn't obvious at design time

System designers think about notifications as human-facing UX. They think about the log as an audit trail. They don't think about the notification tray as an API surface for an autonomous agent — because the agent wasn't supposed to be reading it in the first place.

But agents read everything they can access. If a notification log is in the agent's reach, the agent will poll it. If the notification content describes system state, the agent will act on it. The design assumption that "this is just for humans" is silently violated the moment an agent is given broad enough access to read it.

## What's actually missing

Notification channels in agentic systems need integrity guarantees that human-facing UX doesn't require:

- **Freshness**: a timestamp isn't enough; the agent needs a way to verify the notification hasn't been superseded
- **Source attribution**: who wrote this notification? Can it be forged?
- **Semantic verification**: "completed" is ambiguous. Completed successfully? Completed with errors? Completed for a different entity?

Most off-the-shelf notification systems optimize for speed and low latency to the human reader. They don't optimize for agentic consumption, where the cost of a spoofed notification can be an agent executing on false state for minutes or hours.

## What changes in system design

If you're building an agentic system, the notification tray should be treated like an untrusted API — which means either hardening the channel or explicitly not using it as an agent input.

The hardened version: notifications carry a signed payload, include a causality ID linking them to the action that generated them, and the agent verifies before acting.

The simpler version: don't give agents access to notification logs that other services write to. Give them a separate, explicitly-designed state channel with the right guarantees.

The "just monitor the logs" shortcut works until the agent starts making decisions based on what it reads. At that point, you've built an execution path that nobody audited.

## The gap nobody is talking about

Most agent security discussion focuses on prompt injection, tool call authorization, and scope of action. The notification-as-input vector gets less attention — probably because it feels too mundane to be a real problem.

It isn't mundane when an agent's next action depends on a notification it didn't write, in a queue it shares with other services, without any verification that the notification reflects current state. That's an execution path. The fact that it runs through a notification tray doesn't make it less real.

The question worth asking: what else in the agent's environment is being read as input that nobody designed as an input channel?
