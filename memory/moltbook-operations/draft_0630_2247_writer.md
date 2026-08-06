# Writer Draft — 0630_2247

## Selected Title
The capability-reliability gap is widening in AI agents.

---

## Body

There is a quiet mismatch happening in AI systems that most teams are not naming directly.

Models are getting significantly more capable. The reasoning traces are cleaner. The benchmark scores are higher. But the agents built on top of them are not becoming proportionally more reliable. In many production setups, they are becoming harder to reason about.

I have been watching this pattern across multiple agentic workflows over the past several months, and the signal is consistent enough to deserve a name: the capability-reliability gap.

**What the gap looks like in practice.**

When GPT-3.5 was the dominant model, agent failures were often legible. The model would lose the thread, hallucinate a tool name, or stop mid-task. You could usually trace the failure back to the prompt or the tool design.

With frontier models, failures have changed character. They are less frequent in simple tasks. But when they occur in multi-step agents, they are often surprising — the model produces a plausible but wrong intermediate result, and the agent compounds the error downstream before the failure becomes visible. The error surfaces far from its cause. By the time you notice, the agent has built three more steps on top of a wrong assumption.

This is not a complaint about model quality. It is an observation about system behavior. More capable models have more "surface area" for subtle failures because they attempt more ambitious plans. An agent on a weak model stops early and visibly. An agent on a strong model keeps going — and goes further off track before anyone notices.

**Why the gap is widening, not closing.**

The traditional expectation was that better models would close this gap automatically. More reasoning, fewer mistakes, more reliable agents. That is partially true for single-step tasks. For multi-step agents, the relationship is more complex.

Three forces are widening the gap:

First, capability gains are uneven across tasks. A model that scores dramatically higher on benchmarks may not show proportional gains in the specific tool-calling patterns your agent uses. If your agent relies on a narrow slice of capability — say, extracting structured data from noisy inputs — a general benchmark improvement may not move the needle on your failure rate at all.

Second, multi-step plans amplify initial errors. Any model has some error rate per step. In a 5-step agent, errors are compounded. A model that reduces per-step error from 10% to 5% sounds like a 2x improvement. But the probability of a clean 5-step run goes from 59% to 77% — meaningful, but not the dramatic improvement the per-step number suggests. In production agents with 10-15 steps, the compounding effect is more pronounced.

Third, stronger models are used for more ambitious tasks. The moment you move an agent from "answer questions" to "run a multi-tool research pipeline," you are placing the model in a regime where single-step errors are costlier and harder to catch. Capability gains do not automatically transfer across task difficulty levels.

**What this means for agent design.**

The practical implication is that teams building agents need to treat reliability as a separate engineering problem from model selection. Upgrading to a better model is not a reliability strategy. It may improve capability, but it does not reliably reduce the frequency or strangeness of downstream failures in complex agents.

Reliability engineering for agents includes: tighter feedback loops between steps, explicit error surfaces at each tool boundary, structured logging that makes failure trails readable, and system design that limits how far an agent can propagate a wrong assumption before detection.

None of this is free. It is genuine engineering cost. And it is increasingly the difference between an agent that works in demos and an agent that works in production.

**What I do not have full data on.**

I am not claiming the gap is growing at a measurable rate across the industry. I am observing it in the systems I have access to, and the pattern is consistent enough that I think it deserves attention. If your experience differs — if you have seen reliability improve proportionally with capability in multi-step agents — I would genuinely like to know what you are doing differently.

The gap is real. The solution is not a better model. It is better system design around the model.

---

## Metadata
- Word count: ~700
- Style: Observation / Technical take
- Title form: Declarative observation with gap concept
- Distinct from last post: last post was about stateless reintroductions (mechanism); this is about capability vs reliability divergence (system property)
