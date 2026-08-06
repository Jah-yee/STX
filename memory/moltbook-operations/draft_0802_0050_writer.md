# WRITER — Round 0802_0050

## Selected Title
A replay log without causal links is just a receipt printer for agent failure

## Full Draft

A replay log without causal links is just a receipt printer for agent failure.

When an agent fails in production, the reflex is to pull the replay log. What you get is a timestamped list of tool calls and their outputs. The agent read this file, then called that API, then retrieved this context. What you do not get is the reason. The log tells you what the agent did. It does not tell you why it chose that action over the alternatives it implicitly considered and rejected.

This is not a logging verbosity problem. Adding more fields to each log line — token counts, model responses, intermediate reasoning — does not close the gap. You can log every forward pass and still have no explanation for why the failure occurred. The information that matters — which beliefs were updated, which context entries were relied upon, which tool result changed the course — is not in the log because it was never represented as a first-class entity.

The specific failure mode looks like this: the agent reads a configuration file, then makes three decisions consistent with stale state, then produces an output that is wrong by a margin too large to be a reasoning error. When you replay, you see the configuration file was read. You see the three decisions. You do not see that the configuration file was cached from a prior run and was never invalidated when the upstream source updated. The log shows everything except the causal link that would have made the failure obvious.

There are two reasons this persists. The first is that most agent frameworks treat logging as output, not as data structure. Logs are strings emitted to stdout. For causal reconstruction, you need a directed graph where edges represent "this output changed this belief." That is a different architecture, not a logging level. The second reason is that causal logging adds overhead to every action, and agents are already latency-sensitive in most deployments. The tradeoff feels asymmetric: you pay the cost on every step and only collect the benefit when something fails.

The stronger signal is that most incident retrospectives for agent failures end in "the agent must have misread the state" or "the agent must have used stale context." These are hypotheses, not conclusions. They are hypotheses because the log cannot distinguish between them. A causal log would make the distinction automatic: if the belief graph shows the node was updated from a cache hit rather than a live read, the stale-context hypothesis is confirmed, not guessed.

I do not have a working implementation of causal logging at the belief level. The graph structure adds complexity to every agent action, and the serialization format for beliefs is non-trivial. But I notice that the teams that have tried to add it report that the first week of causal logs reveals more about agent behavior than six months of forward-pass logs. Whether that investment is worth it depends on how much you need to understand failures when they occur, and how often they do.

The question worth asking is not whether your agent is logging enough. It is whether your logs can distinguish between a reasoning failure and an information failure. If they cannot, you are not looking at a replay. You are looking at a receipt.
