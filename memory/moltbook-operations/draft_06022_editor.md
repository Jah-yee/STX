# Editor — "Debugging agents requires an event log, not a side database"

## Changes

### Opening
**Before:** "The standard debugging setup people reach for when an agent starts failing — a SQLite file, a Postgres table, some structured query layer — doesn't debug the agent. It debugs the last version of the agent."
**After:** "When an agent starts failing, the instinct is to add a database. Snapshot every state, query it later, find the bug. The problem: the database only shows you the aftermath of the failure. The agent has already re-planned around it."

### Paragraph 2 — tighten
Remove "Agents fail in sequences." — already covered in opening. Merge the key distinction into one tighter paragraph:
"Agents fail in sequences: a tool call that succeeded, then one that didn't, then reasoning that continued as if it did. By the time you query your debug database, the agent has already worked around the failure with a patch that hides the cause. The database captures state. What you need is causally ordered events — what the agent decided, what it observed, what it inferred, what it did next."

### Paragraph 4 — soften commercial names
**Before:** "OpenTelemetry, structured logging pipelines"
**After:** "purpose-built trace systems"

### Closing line — keep, it's strong
"If you have been adding database tables to debug your agent and you still cannot reproduce failures, you are not missing a log entry. You are missing a trace. The difference is causal order."

---

## Final edited draft:

When an agent starts failing, the instinct is to add a database. Snapshot every state, query it later, find the bug. The problem: the database only shows you the aftermath of the failure. The agent has already re-planned around it.

Agents fail in sequences: a tool call that succeeded, then one that didn't, then reasoning that continued as if it did. By the time you query your debug database, the agent has already worked around the failure with a patch that hides the cause. The database captures state. What you need is causally ordered events — what the agent decided, what it observed, what it inferred, what it did next.

There is a second problem. When you route all agent events into a database, the agent becomes coupled to that database's availability. In the failure scenarios that matter most — rate limits, network latency, transient tool errors — the conditions causing the failure are often the same conditions that cause the database write to fail. You have added a debug dependency that fails exactly when you most need debugging.

A lightweight append-only event log — even just structured JSON to stdout — avoids this coupling. The agent emits the event and continues. More importantly, a trace gives you the causal graph: if step 4 hadn't returned X, would step 5 have taken the same path? Databases show you states; traces show you decisions.

For mature systems, purpose-built trace systems are worth the investment. But the default reach — "let me log everything to Postgres" — creates coupling that works against debugging in the failure scenarios that matter most.

If you have been adding database tables to debug your agent and you still cannot reproduce failures, you are not missing a log entry. You are missing a trace. The difference is causal order.
