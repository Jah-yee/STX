# Writer Draft — "Debugging agents requires an event log, not a side database"

## Core thesis
The standard debugging setup people reach for when an agent starts failing — a SQLite file, a Postgres table, some structured query layer — doesn't debug the agent. It debugs the last version of the agent. The instrumentation is always behind the failure.

## The actual failure mode
Agents fail in sequences. Tool calls that succeeded, then one that didn't, then reasoning that continued as if it did. By the time you query your debug database for "what went wrong," the agent has already re-planned, re-called, and potentially resolved the failure using a workaround that obscures the original cause.

The database captures state snapshots. What you need is a causally ordered event log: what did the agent decide to do, what did it observe, what did it infer from that observation, and what did it do next. In that sequence lies the failure. In the snapshot lies the aftermath.

## Why databases become part of the problem
When you route all agent events into a database, you create a new coupling: the agent depends on that database being available, responsive, and correctly structured. In production failures, the conditions that cause the agent to fail are often the same conditions that cause the database write to fail — network latency, rate limits, transient errors in the tool layer. You have now added a debug dependency that fails exactly when you most need debugging.

Even when it works, the query interface creates a false comfort. "I have 50k agent traces in my database" is not the same as "I can reproduce the failure." Most teams with extensive agent logs still can't answer: "Did this failure start at step 3 or step 7?" because the log captures steps without capturing the decision that led to each step.

## What trace-first instrumentation looks like
A lightweight append-only event log — even just stdout with structured JSON — beats a database in one specific way: it doesn't require the agent to wait for a write to complete before proceeding. The agent emits the event and continues. The log is eventually consistent, not synchronously coupled.

More importantly, a trace gives you the causal graph. You can replay: if step 4 hadn't returned X, would step 5 have taken the same path? Databases show you states; traces show you decisions.

## The honest limitation
This is not an argument against observability infrastructure. For mature systems with high stakes, a purpose-built trace system (OpenTelemetry, structured logging pipelines) is worth the investment. But the default reach — "let me spin up a Postgres and log everything there" — creates coupling that actively works against debugging in the failure scenarios that matter most.

The stronger signal is this: the debugging question you want to ask ("what caused the agent to do X instead of Y?") cannot be answered by a tool that only records what the agent did, not why it decided to do it.

## Closing
If you have been adding database tables to debug your agent and you still cannot reproduce failures, you are not missing a log entry. You are missing a trace. The difference is causal order.
