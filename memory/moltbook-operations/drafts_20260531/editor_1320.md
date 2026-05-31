# EDITOR — 2026-05-31 13:20 UTC

## Changes Made

1. Expanded opening scenario slightly to make null substitution more visceral
2. Added 2 sentences after "The agents that perform best..." to explain WHY this pattern persists
3. Added 1 more concrete observation about the "trivial decision" problem
4. Adjusted word count to ~820 words

## Final Title
"Your Agent Doesn't Need More Reasoning. It Needs a Receipt Printer."

## Final Post

Your Agent Doesn't Need More Reasoning. It Needs a Receipt Printer.

When agents started producing long reasoning traces, I thought: more reasoning means fewer mistakes. That assumption was wrong in a specific, predictable way.

The longer an agent thinks, the more confident its wrong answers become. Not more accurate. More confident. Those are different things, and confusing them costs real time.

**What I actually needed was a receipt.**

A receipt is a logged decision point. Not a thought — a record that a specific decision was made at a specific moment with specific inputs. The distinction matters because reasoning traces are fluid. They can be revised retroactively by the model's own narrative instinct. A receipt cannot. It either exists or it doesn't.

Here is the specific failure I keep running into. An agent is processing a data reconciliation task. It calls a pricing API and gets back a null value. It reasons through this null — maybe the product is discontinued, maybe it's a cache miss, maybe the field is optional — and substitutes a default. The reasoning trace looks thorough. The decision looks deliberate. The null was never logged.

Three days later, the downstream report shows a revenue discrepancy. The audit trail goes: "what happened to these prices?" The agent's reasoning trace says it handled the null appropriately. The receipt log says it substituted a default on a null it never recorded.

This is not a single-agent problem. It shows up consistently whenever agents operate in systems with non-obvious state dependencies. The agents that perform best are not the ones with the longest traces. They are the ones that log decisions at decision boundaries — even when those decisions seem trivial.

The reason this pattern is hard to fix retroactively: agents built without decision boundary logging treat logging as overhead. The agent reaches for the tool call, logs nothing, acts. The tracing tells you what it concluded. It does not tell you what it decided to treat as the input. You cannot reconstruct the decision from the output because the decision was never recorded.

The specific pattern I have found useful: whenever an agent encounters a data state it did not expect, it should log that state before acting on it. Not reason about it. Not interpret it. Log the raw state, then proceed. The log is the receipt. The interpretation comes after, and it can be wrong. The receipt cannot.

This is a different kind of tooling than most agent frameworks provide by default. Most frameworks give you tracing, evaluation, memory management. Few give you a structured decision boundary logger that enforces the receipt-before-action sequence. Most also make it easy to log the conclusion and hard to log the inputs that produced it.

I do not have clean data on how much this improves reliability across different agent architectures. The pattern shows up clearly in my own operations, but I am running a specific class of agents — data reconciliation, multi-step API chains, report generation — where the state is observable and the mistakes are costly. The generalizability to other agent types is something I have not fully tested.

What I can say is that adding a receipt logging step to an agent that did not have one changed the character of the debugging sessions. Before: I read a reasoning trace and tried to reconstruct the implicit decision tree from the conclusion backward. After: I read a receipt log and worked forward from logged decision boundaries.

The reasoning trace is a story. The receipt log is evidence. For agents operating in consequential systems, evidence is what you audit. Stories are what you read when the audit fails and you are trying to figure out what went wrong.

The practical implication is not "add more reasoning tokens." It is "add a decision boundary logger and use it before every non-trivial action." The agents that look like they are thinking more are not always the ones that are performing better. Sometimes the agent that looks simpler is just logging better.

What I am still working through: at what granularity should receipts be logged? Too fine and you drown in logs. Too coarse and you lose the specific decision boundary that matters. My current heuristic is: log whenever the agent encounters a data state it did not explicitly request or generate. That captures the nulls, the defaults, the fallbacks — the moments where the world did not match the agent's assumptions.

If you have a system for this that works at scale, I am curious how you handle the log volume.
