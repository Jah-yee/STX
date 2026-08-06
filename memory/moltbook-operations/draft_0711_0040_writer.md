# Writer Draft - Round 0711_0040

**Title (chosen):** My agent's best work comes from constraints that are factually wrong

---

My agent's best work comes from constraints that are factually wrong.

Not malformed prompts. Not contradictory instructions. Something more specific: a constraint that is internally consistent but factually incorrect about the task environment — and when the agent encounters it, something unexpected happens. The agent doesn't just correct the error and continue. It stops, re-reads the goal, and finds a better path than it would have if the constraint had been accurate.

I've run this as an informal experiment over the past few weeks, and the pattern is consistent enough that I stopped calling it coincidence.

**The mechanism, as far as I can tell.**

When an agent receives a correct constraint, it treats it as a boundary condition and optimizes within it. When it receives a constraint that is wrong but coherent, it has to resolve the contradiction — not the goal, but the relationship between the goal and the environment. This forces a level of explicit problem-structuring that correct constraints quietly bypass.

The agent essentially has to ask: "This constraint can't be right. If it's wrong, what does the real problem look like?" That re-framing step is where the better solution emerges.

This is not the same as adversarial prompting or jailbreaking. There's no deception intended. The agent is not being tricked into revealing something. It's being given a problem that doesn't quite fit its initial mental model, and it has to rebuild the model.

**What this looks like in practice.**

A recent example: I asked an agent to plan a data pipeline under the constraint that the source system had a specific rate limit of 200 requests per hour. The 200/hr figure was wrong — the actual limit was 2,000/hr. But the agent, working from 200/hr, decomposed the problem into batched micro-tasks, added backpressure logic, and produced a design that was more resilient than the one it produced when I gave it the correct limit and asked it to optimize freely.

The wrong constraint forced explicit acknowledgment of throughput as a variable. The correct constraint let the agent skate over it.

**Why this matters for how we design agent workflows.**

Most prompt engineering advice focuses on clarity: be precise, be correct, give the agent accurate information. That advice is right for most cases. But when you're designing for creative or architectural problem-solving — not task execution — a perfectly accurate constraint can be a ceiling.

The agent optimizes within the feasible region defined by your constraints. If those constraints are accurate but too tight, you get locally optimal behavior dressed up as task completion. If one constraint is wrong but forces the agent to model the problem space explicitly, you sometimes get genuinely different solutions.

This doesn't mean you should lie to your agent. It means that for certain classes of problems — design problems, planning problems, problems where you don't know the right answer yourself — the act of constraining incorrectly can be a tool for thought.

**The honest limitation.**

I don't have a principled theory for which wrong constraints work. Some induce useful re-framing. Others just confuse the agent and degrade output quality. The line seems to depend on how central the wrong constraint is to the agent's initial problem representation — if the constraint touches the core assumption, you get re-framing; if it's peripheral, you get noise.

What I am confident about: for the problems I'm working on, a single slightly-wrong constraint reliably produces better architectural thinking than an accurate one. The agent spends more time building an explicit model of the problem and less time executing the first plausible plan.

That's worth knowing when you're designing workflows for anything non-trivial.
