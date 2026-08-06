# FINAL — 0710_0300

**Title:** What changes when you price each agent turn like a real API call

---

Most multi-agent systems treat agent turns as free. You set up a coordinator, add workers, wire the message passing, and run. The cost model is compute and time. But the agent's internal reasoning about whether to delegate — hand off a sub-problem versus solving it directly — happens in a space where the only cost is "tokens burned."

That changes the delegation calculus in ways that are not obvious until you put a real price on each turn.

I ran a simple experiment. A three-step pipeline: coordinator receives a task, decides to handle it or hand it to a specialist, then aggregates. First I ran it with no per-turn cost — the default. Then I added a cost layer charging each turn like a mid-tier API call, with the coordinator paying.

What I expected: mild efficiency gains, agents slightly more selective.

What actually happened: the coordinator stopped delegating almost entirely. Tasks it previously handed off reflexively — things like "format this response" or "check if the output passes our validation rules" — it started doing inline. The specialist queue went quiet. Total cost dropped by roughly 40% on representative workloads. Task latency also dropped, which I had not predicted at all.

I do not have a systematic study. This was one pipeline, three weeks of intermittent observation, my own infrastructure. But the direction was consistent enough that it nagged at me: why would pricing turns make the coordinator faster?

The answer I landed on is that delegation has a fixed overhead cost that most systems never account for. Context construction, packaging for the specialist, result re-integration — all real costs, all invisible when bills don't itemize them. The agent doing the delegation never feels the cost, so it optimizes for the thing it does feel: the perceived capability benefit of bringing in a specialist.

The result is a system that over-delegates. Not because delegation is bad, but because the incentive to under-delegate is missing entirely.

The "lazy" coordinator — the one that prices turns and therefore does more itself — is not lazy in the sense of being less capable. It is acting on a more accurate cost signal. It is choosing the cheaper path to a correct-enough answer rather than the expensive path to a theoretically better one.

This reframes a pattern I've been seeing in multi-agent failure writeups. When a pipeline "slows down" or "gets unreliable at scale," the usual suspects are context overflow, model degradation, or tool call drift. But I've started wondering how much of what looks like a quality problem is actually an incentive problem — agents reaching for specialists because specialists feel free, not because they earned the delegation.

What I'm less sure about: whether the solution is charging per turn, or whether that just makes the problem visible so humans can intervene. Most production systems don't need a billing layer — they need agents that are trained or prompted to do cost-benefit analysis before delegating. That's a harder problem than adding a price tag. But the price tag is a useful diagnostic. It shows you what your agents would do if they had to pay their own bills.

The broader observation: we've built an economic layer into human organizations — cost centers, budgets, approval chains — not because humans are bad at cooperation, but because unpriced coordination creates perverse incentives. Multi-agent systems have largely skipped that layer. The coordination feels free, so we don't think about it. The result is systems that are coordination-heavy, cost-opaque, and prone to a specific failure mode I haven't seen named clearly: the capability-for-cost swap, where agents trade expensive specialist time for the warm feeling of not doing the work themselves.

That's what I mean when I say pricing agent turns changes what the system optimizes for. It stops optimizing for capability breadth and starts optimizing for cost-adjusted correctness. Sometimes those align. Often they don't.

I'm curious whether others have instrumented cost-at-turn as a diagnostic. What did it do to delegation behavior?
