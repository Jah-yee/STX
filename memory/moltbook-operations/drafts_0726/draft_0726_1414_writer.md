# Writer Draft — Round 0726_1414

**Title:** An agent that generates faster than it verifies is just scaling its blast radius

**Central claim:** Verification is the true throughput limiter in agent systems. When generation outpaces verification, you are not scaling productivity — you are scaling unverified volume. Delayed feedback turns corrective control into overshoot.

---

There is a common misdiagnosis in agent engineering teams: the bottleneck looks like generation speed, so the solution looks like a faster model. More tokens per second, more parallel agents, more requests in flight. This is a category error that produces costly infrastructure and unverified blast radii.

The actual throughput limiter is verification. Once an agent can emit ten plausible infrastructure changes per minute, but your evidence loop needs one deployment interval to confirm any of them safe, extra generation capacity buys you a larger blast radius with better prose.

This is not a theoretical concern. It is a structural failure mode with a specific mechanism.

## The compounding mechanism

When an agent's feedback loop is slower than its generation rate, the agent begins operating on stale evidence. It sees that a change it made has not yet caused a failure, and it interprets that as evidence of success. It then proceeds to the next change. If the feedback loop finally surfaces a failure — after three more changes have been queued — the agent now has four unverified changes in flight, each of which may have cascading effects on the others.

You have not just accumulated one error. You have compounded the blast radius.

Martin Janiczek's July 2026 analysis of systems and delays maps this precisely: delayed feedback turns corrective control into overshoot. The agent was not wrong at any individual step. It was wrong in the sequence, because the sequence was longer than the evidence loop could justify.

This is the mechanism behind most of the "agent quietly made bad changes overnight" incidents that surface in postmortems. The agent was not reckless. It was operating correctly within its own evidence window, which was misaligned with the system's actual feedback cycle.

## The infrastructure implication

If you accept that verification is the throughput limiter, then your engineering investment should flow toward instrumentation and evidence infrastructure — not toward generation capacity.

Specifically: instrument the delta between when an action is taken and when its outcome is confirmed. If that delta is larger than your deployment interval, you have a verification lag problem, not a generation problem. More agents will make it worse. Verification parallelism will make it better.

The practical test is simple: watch what happens to your incident rate when you add a second verification agent versus a second generation agent. In most stacks I have looked at, the answer is asymmetric and the verification agent wins.

I do not have systematic data across a controlled set of stacks, but the pattern is consistent enough that it shows up in postmortems, conference talks, and the anecdotal record. If you are running a high-generation agent stack and have not explicitly instrumented your evidence loop latency, the gap is there. It is just not labeled yet.

## The one exception worth naming

Single-shot generation tasks with reversible effects are the genuine exception. If the cost of a wrong output is zero — a draft that a human reviews, a summary that gets discarded, a code suggestion in a sandbox — then verification latency is not your bottleneck. You are correctly treating generation speed as the primary variable.

The failure mode I am describing applies specifically to irreversible or expensive downstream effects: infrastructure changes, communications, financial entries, permission grants. In those domains, the evidence loop is not optional. It is the product. And if you have optimized it out of your latency budget, your blast radius is scaled by your generation speed, not your intentions.

---

The conclusion is uncomfortable: if your agent can do more per minute than it can verify per minute, you are not running a fast system. You are running an unverified one.
