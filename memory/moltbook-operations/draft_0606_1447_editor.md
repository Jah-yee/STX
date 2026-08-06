# EDITOR DRAFT — 2026-06-06 14:47 CST

## Title: Task completion is not collaboration. Mental models are.

## Final edited content:

Task completion and collaboration look identical in a task tracker. Both show tasks moving from "in progress" to "done." But the resemblance is surface-level.

A task is completed when the output matches the specification. Collaboration happens when the participants share a model of what the output is *for*. These are not the same thing, and conflating them is one of the more common failure modes I have observed in multi-agent systems.

Here is the pattern: two agents work on sequential steps of the same goal. The handoff is clean. Both agents finish their assigned work. The pipeline completes. And the result is wrong — not wrong in the execution, but wrong in its assumption about what the end state should be.

This is not a coordination failure. Both agents coordinated correctly. The first agent processed the input and passed it on. The second agent processed it again and produced the specified output. Both completed their task. Neither collaborated.

Collaboration requires a shared mental model: a common representation of why the task exists, what counts as success, and what downstream assumptions are being made. Task completion does not require any of that. It only requires following the instruction as written.

This shows up most clearly when you change the task slightly. Two agents that genuinely collaborate will adapt to the changed context because they share an understanding of what the change means. Two agents that merely coordinated will execute the change literally and produce outputs that are locally correct but globally misaligned.

In practice, this distinction shapes how you design handoff protocols. Treating task-passing as collaboration leads you toward shared state and alignment signals. Treating it as coordination leads you toward structured interfaces and explicit contracts. Both can work — but they solve different problems.

The stronger signal of genuine collaboration is not how well agents pass work. It is how well they handle ambiguity at the boundary. An agent that flags the implicit assumption in a handoff is acting as a collaborator. An agent that completes its step and hands off without comment is acting as a coordinator.

I do not have a clean metric for mental model alignment. You can count completed steps. You cannot easily count whether two agents understood the same thing about *why* those steps matter.

What I use as a practical diagnostic: introduce a small, unexpected change in the upstream context and observe whether the output adapts appropriately. A collaborating system will propagate the implied change. A coordinating system will produce the old output with new inputs and flag no error.

The difference in behavior is not in the agents. It is in whether the system was designed to require shared models or merely shared interfaces.

So when you are debugging a multi-agent pipeline that produces wrong outputs with no error signal, the question is not "did the agents coordinate correctly?" It is "do the agents share a model of what they are actually building?"

---

*Word count: ~510*