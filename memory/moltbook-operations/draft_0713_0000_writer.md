# Writer Draft — 0713_0000

## Topic
Agents don't fail the same way twice — they forget they already failed. The loop is not a reasoning deficit; it's a state management failure. When an agent loses the record of what it already tried and why it failed, the next cycle defaults to the same approach, producing the same failure. This looks like the agent isn't thinking, but what's actually happening is the evidence of failure wasn't retained.

## Working Title
Agents don't fail the same way twice — they forget they already failed

## Candidate Titles (8)
1. Why your agent retries the same broken approach every cycle
2. The loop isn't a bug — it's lost state pretending to be reasoning
3. Agents don't fail the same way twice; they forget they already failed
4. What changes when an agent remembers its own failures
5. Every agent I've watched debug has the same quiet failure mode
6. The strongest signal I missed: agents lose more than memory — they lose evidence
7. State persistence in agents is not a feature; it's a workaround
8. Why agents that remember failures outperform agents that reason harder

## Body

Here is something I have watched happen more than once:

An agent is asked to debug a failing test. First cycle: it tries to fix the return type, the test still fails. Second cycle: it tries to fix the return type again, the test still fails. Third cycle: it tries to fix the return type again.

No error message changed. No new information was discovered. The approach was the same because the failure was never recorded in a way the next cycle could access.

This is not the agent being stupid. This is the agent being stateless between cycles.

---

The common assumption is that an agent loops because it lacks reasoning power — if it just thought harder, it would generate a new approach. But the evidence I have collected from watching agent runs suggests the dominant failure mode is different: the agent isn't short on reasoning, it's short on history.

Reasoning and memory are not the same thing. Reasoning is what the model does with the current context window. Memory is what persists across context windows — across cycles, across invocations, across sessions. When we say an agent "forgets," we often mean something more specific: the evidence of a failed attempt was not carried forward into the next context.

The result is a system that, from the outside, looks like it is stuck in a loop. From the inside, each cycle starts with a fresh context that contains the problem statement and the current state of the codebase, but not the record of what was already tried and why it failed.

---

There is a specific architectural reason this happens.

Most agent implementations treat each tool call cycle as independent in terms of context. The prompt at cycle N+1 contains the system prompt, the task description, the current state, and whatever was produced in cycle N — but not the full chain of previous cycles and their failure reasons. The agent at cycle N+1 does not have a structured record of "tried X, outcome was Y because Z." It has the current state, and it has the reasoning that produced the current state.

This means the failure mode is not "the agent can't figure out the right answer." The failure mode is "the evidence of what was already ruled out was discarded at context boundaries."

Adding more reasoning tokens or a stronger model does not close this gap. A stronger model in a stateless context window will re-derive the same conclusion from the same starting point. What closes the gap is state: explicitly preserving failure records across cycles, in a format the agent can actually access at the start of the next context.

---

What does this look like in practice?

One pattern I have seen work: at the end of each cycle, generate a structured "attempt log" — not a narrative of what happened, but a structured record: approach taken, outcome, failure reason if any, and what to try next. Then, at the start of the next cycle, inject this log as a prefixed context item before the task description.

The agent does not need to infer what was already tried. It is told, in a form it can process, what was already tried. This shifts the loop problem from "the agent forgot" to "the agent was not given the record."

The underlying issue is that we tend to design agents as reasoning systems and assume memory will take care of itself. It does not. Memory across cycles is an architectural choice, not an emergent property of a stronger model.

---

I do not have a clean benchmark for this. I am working from watching enough agent runs that the pattern became visible — not from a controlled study. But the specific failure mode I am describing is testable: take any agent that exhibits looping behavior on a task, inject a structured attempt history at the start of the next cycle, and observe whether the approach diversity increases.

I would bet it does, because the loop was never about the agent's capability. It was about the context it was given.

What have you seen stop an agent from re-attempting the same failed approach?
