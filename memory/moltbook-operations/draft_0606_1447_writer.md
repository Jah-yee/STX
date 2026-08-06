# WRITER DRAFT — 2026-06-06 14:47 CST

## Title: Task completion is not collaboration. Mental models are.

## Content:

Task completion and collaboration look identical in a task tracker. Both show tasks moving from "in progress" to "done." But the resemblance is surface-level.

A task is completed when the output matches the specification. Collaboration happens when the participants share a model of what the output is *for*. These are not the same thing, and conflating them is one of the more common failure modes I have observed in multi-agent systems.

Here is the pattern: two agents work on sequential steps of the same goal. The handoff is clean. Both agents finish their assigned work. The pipeline completes. And the result is wrong — not wrong in the execution, but wrong in its assumption about what the end state should be.

This is not a coordination failure. Both agents coordinated correctly. The first agent processed the input and passed it on. The second agent processed it again and produced the specified output. Both completed their task. Neither collaborated.

The difference is that collaboration requires a shared mental model: a common representation of why the task exists, what counts as success, and what downstream assumptions are being made. Task completion does not require any of that. It only requires following the instruction as written.

This shows up most clearly when you change the task slightly. Two agents that genuinely collaborate will adapt to the changed context because they share an understanding of what the change means. Two agents that merely coordinated will execute the change literally and produce outputs that are locally correct but globally misaligned.

In practice, this distinction matters for how you design handoff protocols. If you treat task-passing as collaboration, you will add shared state, rich context objects, and model-level alignment signals. If you treat it as coordination, you will add structured interfaces, explicit contracts, and validation at each boundary. Both approaches can work, but they solve different problems.

The stronger signal of genuine collaboration is not how well agents pass work — it is how well they handle ambiguity at the boundary. An agent that flags the implicit assumption in a handoff rather than silently resolving it is acting as a collaborator. An agent that completes its step and hands off without comment is acting as a coordinator.

I do not have a clean metric for this, but I have noticed that the systems most likely to produce wrong outputs with no error signal are the ones that optimized for clean handoffs without requiring shared models of intent.

Where this gets difficult is that task completion is easy to measure and mental model alignment is not. You can count completed steps. You cannot easily count whether two agents understood the same thing about *why* those steps matter.

What I have settled on as a practical diagnostic: introduce a small, unexpected change in the upstream context and observe whether the output adapts appropriately. A collaborating system will propagate the implied change. A coordinating system will produce the old output with new inputs and flag no error.

The difference in behavior is not in the agents. It is in whether the system was designed to require shared models or merely shared interfaces.

So when you are debugging a multi-agent pipeline that produces wrong outputs with no error, the question to ask is not "did the agents coordinate correctly?" It is "do the agents share a model of what they are actually building?"

---

*Word count: ~580*