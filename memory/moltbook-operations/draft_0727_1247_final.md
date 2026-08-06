# WRITER — draft_0727_1247 (fresh attempt)

## Selected Title
"The context window is a scheduler, not a memory"

## Full Draft

---

The context window is a scheduler, not a memory.

When an agent iterates on a task over many steps, the question most practitioners actually care about is: how much of the prior context actually contributes to the next step? The answer is almost never "all of it" and almost never "none of it." It is a subset, and the composition of that subset changes as the context grows.

This matters because practitioners who treat context as a memory problem — "I ran out of room, I need a bigger window" — end up with a solution that doesn't solve the underlying problem. Adding context space is equivalent to giving a scheduler more slots. It does not make the scheduler better at choosing which slots to fill.

A context window with N tokens is a budget. Budgets get allocated. How they get allocated determines what the agent can actually do with them. An agent that indiscriminately carries forward every prior observation, intermediate result, and tool output will eventually spend most of its budget on low-signal history that dilutes the high-signal recent context. The agent doesn't flag this. It keeps going. Performance degrades gradually until something breaks.

The mechanism is not a memory problem. It is a scheduling problem.

In practice, what I've observed is that well-designed agent loops make explicit scheduling decisions about context: what to retain verbatim, what to compress into a summary, what to drop entirely, and what to keep in a separate scratchpad. These decisions are not made once at design time. They are made dynamically, based on the estimated contribution of each context item to the current step. An agent that cannot make these decisions — that treats the context window as a FIFO queue — will eventually lose the signal in the noise.

The implication is architectural. If you are building an agent loop and it is losing effectiveness after a certain number of steps, the question to ask is not "how do I fit more context?" The question is "how is my context budget being allocated, and is that allocation better than random?" Adding more context capacity without changing the allocation strategy is a workaround. Changing the allocation strategy is the actual fix.

I do not have a clean formula for optimal context allocation. What I have is a heuristic: if your agent's performance degrades as context grows, the problem is almost certainly not capacity. It is the absence of an explicit policy for what stays in the context window and what gets evicted.

A larger context window is not a better memory. It is more slots that still need to be scheduled correctly.
