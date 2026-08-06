# Writer Draft

## Title: Coding agents lack the social intelligence to stack

---

Coding agents lack the social intelligence to stack.

When two agents work on the same codebase, the failure mode is not a logic conflict. It is a social one. One agent does not know what the other agent has already decided, so it re-decides it, or contradicts it, or defers to a stale version of it. The bug is not in the code. It is in the coordination protocol — or the absence of one.

This is different from the typical multi-agent failure narrative. Most discussions focus on capability: can each agent do the task? But the harder problem is: can they maintain shared context, recognize conflicting assumptions, and repair breakdowns without an external human signal?

Here is what that failure looks like in practice.

Agent A modifies a function signature. Agent B, running in parallel, updates call sites based on the old signature. Both agents produce clean outputs. The CI passes because Agent B's changes are tested against a test suite that was also written under the old signature. No error surfaces. The regression is silent.

Or: Agent A opens a pull request. Agent B reviews it using criteria it cannot articulate — not because it lacks capability, but because the criteria are distributed across implicit precedent rather than written policy. The review is not wrong. It is just calibrated to a different codebase than the one that was actually submitted.

These are not prompting failures. The agents are not misaligned in intent. They are misaligned in social context — what the group has already established, what is currently contested, what was decided in a thread that was never read.

The mechanism is structural. Agents are good at individual reasoning under a given context window. They are not designed to track what other agents in the system have committed to, what the current state of contested ground is, or when to defer rather than assert. That is a social intelligence function, not a logical one.

The practical consequence: teams adding a second coding agent often see performance degrade before it improves. The first agent had exclusive access to the codebase's social context — the PR history, the review comments, the decisions that were made and then silently reversed. A second agent operating independently has to reconstruct that context from artifacts, or it operates without it.

What makes this hard to fix is that the failure mode looks technical. The symptom is a merge conflict, a broken test, a regression. The cause is a coordination gap that no test suite is designed to catch.

I do not have a clean solution for this. What I have observed is that teams who succeed at multi-agent code operations invest in explicit coordination infrastructure: shared state for decisions, not just shared context for code. The agent that can read a decision log and reason about it is more useful than the agent that can write more code faster.

The question worth asking is not how fast your agents are, but how they handle it when they disagree.
