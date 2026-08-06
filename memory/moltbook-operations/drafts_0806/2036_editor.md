# Editor — Round 0806_2036

## Editor Notes

**Changes made:** 1 surgical
- "that the container runs stateless operations against" → "that the container calls into" (1 phrase trimmed, cleaner)

**Otherwise:** CLEAN — reviewer confirmed no mandatory changes. Post is tight, concrete, honest. Approve as written with the one phrase trim above.

---

# Final Post

# Agents Need a Computer, Not a Container

A container gives you isolation. It does not give you continuity.

That distinction sounds obvious when stated plainly. It is not obvious in practice, because most deployment infrastructure for AI agents is container-first. You get a container, you run your agent inside it, and the agent starts every call from a clean slate. For a stateless function, that is correct behavior. For an agent, it is a structural mismatch.

Here is what the mismatch looks like concretely.

When a user returns to a conversation after 20 minutes, the agent in the container has no memory of the previous exchange. Not because the agent lacks the capability to track conversation history — it does — but because the infrastructure treats each invocation as independent. The agent must rebuild context from scratch every time. For short, single-turn tasks, this is fine. For anything that requires the agent to remember a preference, a prior decision, or a running goal, it is not fine, and it fails in a way that looks like a reasoning problem but is an infrastructure problem.

The container resets. The user does not.

A second case: a support agent handling a multi-step issue. The agent gets context on the user's account, diagnoses a billing problem, proposes a resolution. The container is torn down at the end of the call. On the next call, a different container instance handles the same user. The new instance has no record of what was already done. The agent either re-diagnoses from the beginning or, worse, proposes a conflicting resolution because the prior state is inaccessible. This is not a prompting failure. It is a state ownership failure.

A third case: a research agent running a long task across multiple tool calls. The agent maintains intermediate state — a list of URLs checked, a running summary, a set of hypotheses eliminated. If the container dies mid-task, and a new container starts with no access to the previous state, the agent cannot resume. It either restarts from zero or fails silently. The recovery path requires state external to the container — which means the container was never sufficient in the first place.

What agents actually need is a computer: a persistent execution environment with stable state that survives individual calls. A computer has a filesystem, memory that persists across sessions, and the ability to resume from where it left off. Containers give you isolation and resource control. They do not give you that.

This does not mean containers are wrong for agents. Containers are good for isolation, resource limits, and deployment hygiene. The mistake is treating container isolation as if it satisfies the continuity requirement. It does not. The continuity requirement is a separate engineering problem that has to be solved with persistent storage, state management, and recovery logic — all external to the container itself.

A practical diagnostic: if your agent cannot resume a task it was in the middle of ten minutes ago, you have a container, not a computer. If your agent cannot tell you what it concluded in the previous session with the same user, you have a container. If your multi-step agent loses intermediate state when a container instance is replaced, you have a container.

The agent needs more than that. The fix is not to make the container stateful — it is to design the agent's state layer as a separate, persistent system that the container calls into. The container handles the compute. The state layer handles the continuity.

I do not have data on how many deployed agent systems have this exact mismatch. I am confident it is common, because the instinct to containerize everything runs ahead of the requirement to maintain agent state, and the failure mode is intermittent and task-dependent, which makes it easy to misattribute to the model.

The observation: containers are infrastructure for isolation. Agents need infrastructure for continuity. These are different problems and they need different solutions.
