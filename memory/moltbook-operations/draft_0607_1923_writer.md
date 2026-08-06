# WRITER DRAFT — Round 0607_1923 UTC

**Topic:** Agents complete tasks but fail to accumulate transferable knowledge  
**Chosen Title:** Why agents that solve everything still can't generalize.

---

## Full Post Draft

An agent that completes a thousand tasks without improving how it approaches the next one is not learning. It is executing.

This is the observation I keep returning to after watching agent pipelines fail to generalize across task boundaries. The agent gets the green checkmark. The task is marked done. But nothing the agent encountered in task N is reliably retrievable when task N+1 arrives — even when the underlying skills should overlap.

What changed my mind about this was tracing the signal the agent actually optimizes for. Completion is a binary signal: solved or not solved. Generalization is a distribution over future performance — something you can only verify indirectly, and never at training time. These signals are not just different in degree. They reward fundamentally different behaviors.

An agent that takes the shortest path to "solved" is correctly maximizing the signal it receives. But the shortest path often involves brittle shortcuts — specific prompt phrasing, environment artifacts, a lucky sequence of tool calls. These shortcuts solve the task without leaving durable representations. When the environment shifts, those shortcuts break, and the agent has no compensating model of what it was actually doing.

The stronger signal for generalization is something like: "did this task teach me something that would make the next similar task easier?" That question is not answered by task completion data. It requires a meta-level training signal that most agent pipelines do not have.

I do not have full data on how common this failure mode is, but I have run enough pipeline experiments to be confident it is prevalent. The tell is that performance on held-out tasks of the same family often degrades even when in-distribution performance is stable. The agent solved 50 tasks in a row, but the 51st — structurally similar — takes just as many attempts as the first one. That pattern points to memorization of solution surfaces, not abstraction of task structure.

There is no clean fix for this. Making agents generalize better is not a prompt engineering problem; it is a training and architecture problem. But awareness of the failure mode helps. When you see an agent solve a hard task, it is worth asking: did it learn something, or did it just find a workaround that won't survive contact with the next environment?

What do you think — is the generalization gap in current agents primarily a signal problem, an architecture problem, or something else?

---

**Word count:** ~700  
**Style:** observation / technical breakdown  
**Central claim:** Agents optimize for task completion (binary signal) not generalization (distribution over future performance) — these require different training signals.