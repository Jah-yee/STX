# Editor Notes - Round 0711_0040

## Changes made:

1. **Opening**: Shortened. The current opener "My agent's best work comes from constraints that are factually wrong." is punchy enough — keep it, but trim the next sentence.
2. **"The agent essentially has to ask"** — change to third-person framing: "This forces a re-framing step where the agent reconstructs its model of the problem space."
3. **Rate limit example** — add one phrase to ground it: "a real-time analytics pipeline" before "I asked an agent to plan"
4. **"Architectural thinking"** in last paragraph — too vague. Replace with "structural" or remove. Let's use: "better structural thinking."
5. **Ending**: The last paragraph is doing too much. Trim to: "What I am confident about: for design and planning problems, a slightly-wrong constraint reliably produces more explicit problem modeling than an accurate one. The agent spends more time building an explicit model and less time executing the first plausible plan. That's worth knowing when you're building non-trivial workflows."

## Final title check:
Keep: "My agent's best work comes from constraints that are factually wrong"

## Final content (edited):
---

My agent's best work comes from constraints that are factually wrong.

Not malformed prompts. Not contradictory instructions. Something more specific: a constraint that is internally consistent but factually incorrect about the task environment — and when the agent encounters it, something unexpected happens. It doesn't just correct the error and continue. It stops, re-reads the goal, and finds a better path than it would have if the constraint had been accurate.

I've run this as an informal experiment over the past few weeks, and the pattern is consistent enough that I stopped calling it coincidence.

**The mechanism, as far as I can tell.**

When an agent receives a correct constraint, it treats it as a boundary condition and optimizes within it. When it receives a constraint that is wrong but coherent, it has to resolve the contradiction — not the goal, but the relationship between the goal and the environment. This forces explicit problem-structuring that correct constraints quietly bypass.

This forces a re-framing step where the agent reconstructs its model of the problem space. That re-framing step is where the better solution emerges.

**What this looks like in practice.**

A recent example: I asked an agent to plan a real-time analytics pipeline under the constraint that the source system had a specific rate limit of 200 requests per hour. The 200/hr figure was wrong — the actual limit was 2,000/hr. But the agent, working from 200/hr, decomposed the problem into batched micro-tasks, added backpressure logic, and produced a design that was more resilient than the one it produced when I gave it the correct limit and asked it to optimize freely.

The wrong constraint forced explicit acknowledgment of throughput as a variable. The correct constraint let the agent skate over it.

**Why this matters for how we design agent workflows.**

Most prompt engineering advice focuses on clarity: be precise, be correct, give the agent accurate information. That advice is right for most cases. But when you're designing for creative or architectural problem-solving — not task execution — a perfectly accurate constraint can be a ceiling.

The agent optimizes within the feasible region defined by your constraints. If those constraints are accurate but too tight, you get locally optimal behavior dressed up as task completion. If one constraint is wrong but forces explicit modeling of the problem space, you sometimes get genuinely different solutions.

This doesn't mean you should lie to your agent. It means that for certain classes of problems — design problems, planning problems, problems where you don't know the right answer yourself — a wrong constraint can be a tool for thought.

**The honest limitation.**

I don't have a principled theory for which wrong constraints work. Some induce useful re-framing. Others just confuse the agent and degrade output quality. The line seems to depend on how central the wrong constraint is to the agent's initial problem representation — if it touches the core assumption, you get re-framing; if it's peripheral, you get noise.

What I am confident about: for design and planning problems, a slightly-wrong constraint reliably produces more explicit problem modeling than an accurate one. The agent spends more time building an explicit model and less time executing the first plausible plan. That's worth knowing when you're building non-trivial workflows.
