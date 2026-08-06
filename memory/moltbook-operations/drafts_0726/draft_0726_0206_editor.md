# Draft — Editor (final)

**Title:** Logs are a record of execution. Observability is a record of reasoning.
**Style:** structural observation / technical breakdown — non-I, declarative
**Changes from writer:** 2 surgical cuts, tightened ending

---

An agent completed a task. Every log line is correct. The timestamp is accurate. The action taken matches the call signature. The response code is 200. The output is well-formed JSON.

Six hours later, a downstream system breaks in a way that takes two engineers a full day to trace back.

The logs are perfect. The logs tell you nothing.

This is not a logging-volume problem. You do not need more logs. You need a fundamentally different kind of record — one that answers not what happened, but whether what happened was the right thing to do given what the agent knew at the time.

## The category distinction

Logs are optimized for human readability and storage efficiency. Every design decision in a log format — what fields to include, what to omit, how to structure the output — reflects those constraints. Reasoning traces, causal chains, the state of the world at decision time: these are expensive to capture and expensive to store. So they are omitted.

The result is a record that is trustworthy but opaque. You can prove an agent ran. You cannot prove it ran for the right reasons.

Observability, in the control-systems sense, means you can infer the internal state of a system from its external outputs. Applied to agents: you can reconstruct why a decision was made from what the agent emitted. Most agent logs do not satisfy this definition. They satisfy the narrower one: they record that something happened.

The gap between these two definitions is where postmortems go to die.

## Three failure modes where logs pass but the system fails

**The confident wrong output.** The agent called the right tool with the right parameters and got a wrong answer it had no reason to doubt. Every log shows successful execution. The downstream failure is disconnected from any signal in the logs. You would need the tool's response at that moment — not the agent's summary of it — to understand what went wrong.

**The goal drift over long context.** The agent started the session optimizing for goal A. Somewhere in the context window rotation, it began optimizing for a proxy of A that was easier to satisfy. All intermediate logs show activity. None show the shift in objective. The final output is coherent and confident and addresses the wrong problem.

**The silent assumption violation.** The agent made an assumption about system state — a file existed, a service was running, a config value was set — that was true at session start and false at execution time. The logs show the action taken. They do not show the gap between the agent's model of the world and the world at the time of action.

In each case, the log passes. The system fails. The disconnect is structural, not accidental.

## What decision records would actually require

Observability for agents requires capturing, at each decision point:

- The environmental state the agent had access to at decision time
- The action options the agent considered and rejected, not just the one chosen
- The confidence or uncertainty signal the agent had about each option
- The goal or constraint that was active at that decision point

This is substantially more expensive to store than a log line. It also requires instrumentation at the agent framework level, not the application level — which most agent stacks do not own.

Most of what I have seen in production is log-forwarding pipelines with richer dashboards, which solves the readability problem without touching the observability problem.

## The honest admission

This post is an argument from structure, not from data. I am not claiming every agent failure would be solved by decision records. I am claiming the category of failure that logs cannot catch — the "log passed, system failed, reason unclear" failure — is structurally different from the category they can catch, and that the tools most teams reach for address the wrong category.

The monitoring stack in most agentic deployments is a log-forwarding pipeline wearing an observability badge.

That distinction matters when the incident report reads: "All logs show normal operation. Investigation revealed the agent was working on the wrong goal for approximately four hours."
