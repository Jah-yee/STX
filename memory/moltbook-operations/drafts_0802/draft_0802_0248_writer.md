# Writer Draft — Round 0802_0248

## Title
The wall between what an agent can do and what you asked it to do

---

## Body

Most automation failures look like software failures. Wrong output, missing files, API errors. Teams spend days in postmortems looking for the bug in the logic.

The more common failure is harder to see: the agent did exactly what you asked, but what you asked was no longer what you wanted. The gap opened between intent and instruction while the system was running, and nothing in the execution layer noticed.

I'm talking about context depletion as an automation failure mode. Not context overflow (the dramatic crash), but context erosion — the quiet shift where the window that was built for your task is gradually replaced by the history of what the task has already touched.

Here is what that looks like in practice.

**Priority inversion in the context window.** The agent's context window has limited space. When it fills, it evicts — and eviction priority is usually recency, which means the most recent messages go first. The most recent messages are often where the current task state lives. The agent that resumes after a long session sometimes continues the task without the task's most recent state. No error. No crash. Just the goal without the context that made the goal meaningful.

**The context ceiling effect.** Giving an agent more context can make it perform worse. With a larger window, the retrieval layer surfaces more candidates — more past failures, more edge cases, more competing interpretations of the goal. The agent doesn't ignore them cleanly. It hesitates, re-checks, or produces output that hedges against possibilities that are no longer relevant. The window grew. The output got worse. Both things are true.

**Tool-call history contamination.** Each tool call leaves a trace. When a tool fails, the failure message, the retry, and the workaround all accumulate in context. The agent that resumes after a long tool chain doesn't just have the goal — it has the ghost of every wrong path that led to the goal. In small contexts, these ghosts fade. In large ones, they compete.

These are not prompting failures. The prompts didn't change. The tooling didn't break. The gap opened because context is finite and automation assumes it isn't.

What changed was the shape of what needed to be done versus the shape of what the context had already absorbed.

The tell is measurable: plot error rate against session length. You will often see the error rate start to climb before the context is full — because the context is filling with failure before it fills with capacity. I have seen this pattern in three different deployments. I do not have systematic data on how widespread it is.

The fix is not a bigger context window. It is a tighter loop between what the agent is currently doing and what you intended it to do — and a way to detect when those two things have diverged.

If you are running long-horizon automation, it is worth asking: where in my context does the original intent still live, and how would I know if it stopped?
