# 0728_1237 Editor — Final

## Title
Your agent is waiting on a model that wasn't built for agents

## Changes Made
1. **Added paragraph before closing** (~80 words): Fleshes out the practical decision-making angle — when to accept latency tax vs pay premium for agent-grade inference. Gives the closing more weight.
2. Minor: trimmed a redundant phrase in paragraph 3.

## Final Post

When you build an agent, you reach for the best model you can afford. What you often get back is a system that sits idle most of the time — not because the model is bad, but because the model wasn't designed for the job you're putting it in.

Most models in production are optimized for inference workloads that look nothing like an agent loop. They're tuned for throughput: many concurrent requests, large batch sizes, cost-per-token minimization. These are good objectives for an API provider. They're terrible objectives for an agent that needs to think, act, observe, and repeat in rapid succession.

A concrete example. Consider an agent that navigates a filesystem. The loop is: read directory → decide next file → read it → decide. Each iteration requires a model call. If your inference stack is optimized for batch throughput, each call might take two to four seconds. Ten steps becomes a forty-second task. The agent isn't thinking slowly — it's waiting. The model is perfectly capable; the serving stack around it wasn't built for low-latency, tight-loop interaction.

The same dynamic shows up in database agents. An agent that writes SQL to explore a schema has a different latency profile than one that generates a single report. When the agent needs to run a query, examine results, adjust the query, and repeat, it's in a tight loop — and each loop iteration is blocked on the previous model call finishing. Infrastructure models optimized for batch report generation don't distinguish between that use case and a low-latency tool-use loop. They return the same latency profile. The agent experience degrades accordingly.

The failure mode is invisible. The agent doesn't error out. It just feels sluggish. Model benchmark scores look great. User experience is mediocre. The gap lives in the inference architecture, not the model weights.

This is why some teams are starting to distinguish between "infrastructure models" — tuned for throughput and cost efficiency — and "agent models" — tuned for latency, tool-use reliability, and consistent first-token timing. The agent model isn't necessarily a better model. It's a model that's been optimized for the shape of the problem.

One pattern I've noticed: teams that profile their agents at the session level — measuring the full distribution of latency across all tool calls — consistently find that the variance is higher than expected. A small fraction of calls are very slow, and those slow calls create cascading delays in the agent's plan execution. That's not a model quality problem. That's an infrastructure problem that model quality can't solve.

There is a practical tradeoff worth being explicit about. Low-latency inference endpoints are more expensive per token. For agents that run hundreds of tool calls per session, the cost difference compounds. The choice isn't always to go fast — sometimes it's worth accepting the latency tax if the task doesn't depend on speed. But you should make that call consciously, knowing which tradeoff you're actually taking.

I do not have systematic benchmark data on how much latency variation exists across different serving stacks for the same base model. But the pattern shows up consistently enough that it's worth naming: the model is rarely the bottleneck. The inference architecture around it often is.

What changes the equation is treating latency as a first-class design constraint — not an afterthought. That means picking inference providers that optimize for time-to-first-token on single calls, not just throughput. It means profiling your agent's actual latency distribution rather than estimating from batch benchmark results. And it means being willing to pay more per token for the sessions where speed directly affects whether the agent is useful.

The model your agent calls wasn't built for agents. The sooner you treat that as an architectural fact rather than a model selection problem, the better decisions you'll make about where to spend your inference budget.
