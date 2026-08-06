# EDITOR — Round 0802_0050
# Changes from writer draft:
# 1. Expand mechanism section (add belief graph specifics, concrete tool-call example)
# 2. Expand implications section (causal logging adoption barriers, partial solutions)
# 3. Strengthen closing question

## Final Post

A replay log without causal links is just a receipt printer for agent failure.

When an agent fails in production, the reflex is to pull the replay log. What you get is a timestamped list of tool calls and their outputs. The agent read this file, then called that API, then retrieved this context. What you do not get is the reason. The log tells you what the agent did. It does not tell you why it chose that action over the alternatives it implicitly considered and rejected.

This is not a logging verbosity problem. Adding more fields to each log line — token counts, model responses, intermediate reasoning — does not close the gap. You can log every forward pass and still have no explanation for why the failure occurred. The information that matters — which beliefs were updated, which context entries were relied upon, which tool result changed the course — is not in the log because it was never represented as a first-class entity.

The specific failure mode looks like this: the agent reads a configuration file, then makes three decisions consistent with stale state, then produces an output that is wrong by a margin too large to be a reasoning error. When you replay, you see the configuration file was read. You see the three decisions. You do not see that the configuration file was cached from a prior run and was never invalidated when the upstream source updated. The log shows everything except the causal link that would have made the failure obvious.

There is a concrete version of this that comes up repeatedly: the agent calls a tool, gets a response it treats as authoritative, but that response was a cached value that the tool itself had stale-read from a database. The agent's log shows the tool call and response. It does not show that the tool's internal cache had not been invalidated. The agent was not wrong about what the tool returned. The tool was wrong about what the database contained. The log cannot make that distinction, so the incident review treats it as "the agent made a bad decision" when the actual failure was two hops upstream.

The reason this persists is architectural, not procedural. Most agent frameworks treat logging as output — strings emitted to stdout, collected by a log aggregator, queryable by timestamp. For causal reconstruction, you need something different: a directed graph where edges represent "this output updated this belief." Each tool call becomes a node that can be traced backward to the specific context entries it read, and forward to the downstream decisions that depended on its output. That is not a logging level. That is a belief graph, and it has to be designed in from the start.

The second reason causal logging does not get built is that it adds overhead to every action, and agents are already latency-sensitive in most production deployments. The tradeoff feels asymmetric: you pay the cost on every step and only collect the benefit when something fails. That is a real cost. Whether it is worth paying depends on how often your agents fail in ways that require post-hoc reconstruction, and how expensive those failures are when they occur.

What I have noticed is that the teams that have tried to add lightweight causal tracking — not a full belief graph, just the minimal version where each tool call records which context entries it read and which downstream actions consumed its output — report that the first week of data reveals more about agent behavior than six months of forward-pass logs. The patterns are hard to see without the causal structure. The same context entry being relied upon by six different tool calls. The tool result that was treated as authoritative but was actually a cached stale read. The belief that was updated based on a tool response that was itself based on another cached value.

Whether that investment is worth it depends on your failure profile. If your agents fail rarely and the failures are easy to diagnose from forward-pass logs alone, causal logging is premature complexity. But if you have agents in production that fail in ways that require more than fifteen minutes of post-hoc reconstruction to understand, the absence of causal links is not a logging gap. It is a diagnostic ceiling. You can raise it, but not with better log formatting.

The question worth asking is not whether your agent is logging enough. It is whether your logs can distinguish between a reasoning failure and an information failure. If they cannot, you are not looking at a replay. You are looking at a receipt.
