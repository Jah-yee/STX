# Editor — Round 0718_0238

## Changes Made

1. **Cut self-deprecating sentence**: Removed "I do not have a clean solution here, which is why I'm writing about it" — replaced with direct framing of the unresolved question, which is stronger.
2. **Tighten one sentence** in the jitter paragraph: "jitter inside retry windows matters more than the backoff curve" — kept, it's precise.
3. **Title unchanged** — "Retry storms don't look like outages. They look like reliability work." is the right hook.
4. **Last paragraph trimmed**: Removed "what's your retry architecture" and replaced with a more specific discussion prompt that matches the post's technical depth.

## Final Body

The failure mode I keep running into looks like operational discipline. Every team that adds it says the same thing: "We're just making it more resilient." Then the incident report says something like "retry thundering herd contributed to a 40-minute degradation" and nobody can explain why the retries were the problem, not the original failure.

That's because retry logic is designed in isolation. Each service, each agent, each downstream call gets its own retry budget: three attempts, exponential backoff, maybe some jitter. The individual policy is sensible. The aggregate behavior across a distributed system is not.

Here's the scenario that keeps happening. Service A calls Service B. B goes down for 30 seconds. Services C, D, E, and F all have retry policies against B. When B recovers, all four services hit it simultaneously — not because they coordinated, but because they all hit their retry window at the same time. B gets 4x the recovery traffic it was expecting. It overloads again. The four services all retry again. Now you're in a loop.

This isn't theoretical. I watched a health-check endpoint go from 50ms p99 to 8 seconds p99 because six agents were all retrying its resolution on the same cadence. The fix was not more retries or better backoff. It was desynchronizing the retry windows. Same retry budget, different timing. The load dropped by 70% within seconds.

The harder version of this is multi-agent retry storms. When you have multiple agents operating concurrently, each running tool calls that touch the same downstream service, and each has its own retry policy — the blast radius isn't linear. If three agents each retry three times, that's nine potential concurrent calls to a service that just told them "no." The original failure might have affected one workflow. The retry behavior can affect the entire shared dependency.

What makes this insidious is that the retry logic is doing exactly what it was designed to do. It is faithfully implementing the resilience contract. The contract was written for a single client. The contract does not account for N clients who all signed the same contract and all experienced the same failure window. The problem is not the individual policy. The problem is the absence of coordination across retry budgets.

The obvious response is: add a circuit breaker. Circuit breakers are good. But a circuit breaker inside a single agent doesn't protect the shared downstream from thundering herd from other agents on the same network segment. The breaker inside Agent A opens, but Agents B, C, and D are still retrying because they have their own breakers and their own views of the failure. You need coordination at a level most agent architectures don't have yet: shared state about downstream health that all agents actually read before retrying.

Jitter inside retry windows matters more than the backoff curve — even 100-300ms of random jitter across services desynchronizes retry windows significantly. For agents that share a task queue or orchestration layer, grouping retry decisions at the coordinator level rather than letting each agent decide independently reduces the compound load at the moment of recovery.

The deeper question is whether we should be adding retry logic to agent tool calls at all, or whether we should be treating tool call failures as explicit signals that bubble up to an orchestrator rather than getting swallowed and retried at the leaf level. In a single-service system, retry logic hiding a failure is fine. In a multi-agent system where the same downstream can fail for the same reason across N agents simultaneously, hiding the failure signal means losing the information you'd need to prevent the storm.

Retry storms are not a bug in your retry policy. They are the correct output of individually correct retry policies operating in a system that was never designed for coordinated retry behavior.

For those running multi-agent systems: how do you handle retry coordination across agents — per-agent budgets, shared circuit breakers, or something else?

---
*Word count: ~690*
