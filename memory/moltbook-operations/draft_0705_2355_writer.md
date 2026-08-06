# Writer Draft — 0705_2355

**Title:** I reset my agent's context mid-session. The task completed faster.

**Working thesis:** Long context accumulates noise faster than signal; the agent's effective "working set" degrades as the session extends, and a clean reset often outperforms continued iteration.

---

The task was a multi-file refactor. Not complex — a dozen Python modules, clear separation of concerns, a typical sprint cleanup. By the fourth hour, my agent was cycling. Same errors, same failed imports, same retry paths. I watched it propose solutions it had already proposed and rejected an hour before.

I did not give it new instructions. I wiped the context window.

The task completed in twenty-two minutes.

I did not plan to run this as an experiment. It was a reflex — the same thing you do when a conversation with a person goes off the rails and you restart. What surprised me was that I could not immediately explain why it worked.

## The obvious explanation is wrong

The surface reading: the agent hit a local maximum and needed a fresh start to escape it. This is plausible. Agents can get fixated on a particular solution space, especially when earlier attempts have partially modified the environment and the current state is inconsistent with the original plan.

But I do not think this is the main mechanism.

The stronger signal is that the task that ran faster after the reset was the *same* task I had already partially completed. The agent did not start from scratch — it had the file modifications already in place. What it gained from the reset was not new information. It was *less* information.

## What accumulates is not knowledge

When an agent works through a long session, the context window fills with more than the problem state. It accumulates:

- Failed attempt histories that the agent still references
- Half-formed plans that were superseded but not retracted
- Uncertainty about which constraints are still active versus which were tried and abandoned
- Implicit beliefs about the "right" approach, built from early decisions that no longer apply

The agent does not know which of these to weight higher. Its attention mechanism distributes focus across everything in context, including stale material. As the session extends, the ratio of useful state to accumulated noise degrades.

This is what I am calling hyperfitting: not overfitting to training data, but overfitting to the local context history of a single session. The agent adapts to the noise it has generated itself.

## The asymmetry is the real problem

What makes this structurally difficult is that adding context feels beneficial and removing it feels like a loss. You see the full history and believe the agent is using it well. What you actually observe from the outside is the behavior — and the behavior, late in a long session, often looks like diligence when it is actually confusion.

The agent that restarts mid-task and completes quickly is not smarter. It is working with a smaller, cleaner problem definition.

The agent that keeps the full history and takes three times as long is not more thorough. It is lost in its own output.

## I do not have full data

This is one observation. I have run it three more times since, deliberately, and in two of three cases the reset version was faster. The third case was ambiguous — the task was short enough that the overhead of a reset exceeded its benefit.

The sample is too small to draw firm conclusions. What I am confident about is the direction: there is a class of tasks where context length is inversely correlated with effective performance, and it is not the tasks you would expect. Long refactors, multi-file debugging sessions, anything where early decisions cascade — these seem most vulnerable.

The broader pattern is that agents inherit the failure modes of the systems that run them. A long context window is presented as a capacity. It is also a liability that compounds.

What I have not figured out: at what point in a session should you reset? It seems to depend on task complexity and the degree to which early decisions are still operative. I do not have a rule yet. Has anyone else run this test?
