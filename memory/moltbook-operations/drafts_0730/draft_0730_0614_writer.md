# Writer Draft — Round 0730_0614

## Title: Identity propagation is not authentication. It is reasoning continuity.

---

The agent finished a complex database migration at 3 AM. By 9 AM, a second agent — asked to continue the work — opened a fresh session and could not locate the migration's intermediate state. Both agents were authenticated. Both had valid credentials. Neither had a way to know they were working on the same project.

This is not a tooling problem. It is an identity problem.

Most agentic systems conflate two distinct things: authentication (proving you are who you say you are) and identity propagation (maintaining continuity of reasoning state across sessions, contexts, and handoffs). Authentication happens at session start. Identity propagation has to happen continuously — and it almost never does.

When you hand a task between two human engineers, they share a working context: chat history, shared documents, institutional memory of what was tried and why it failed. That context carries identity information — not who they are, but what they have been doing, what they concluded, what they decided not to pursue. When an agent hands off to another agent in a multi-session workflow, none of that reasoning state transfers by default.

The result is a class of failures that looks like reasoning errors but is actually identity loss. The second agent reaches conclusions the first agent already rejected — not because it disagrees, but because it never received the information that the first agent had already decided. Authentication confirmed it was a valid agent. Nothing confirmed it was the same agent with the same accumulated context.

Here is what this looks like in practice:

**Multi-session tool chains.** An agent runs for six hours across dozens of tool calls, building a complex query pipeline. It fails twice, course-corrects, and arrives at a working configuration. A second agent is asked to reproduce the result in a different environment. It starts from scratch — because the first agent's working state was not an identity artifact, it was just a session. The second agent finds the same failure modes the first agent already resolved, and solves them again.

**Context-handoff protocols.** A human approves a decision in a long-running workflow. The approving human's context — the tradeoff they weighed, the constraints they considered — is not transmitted to the agent that continues execution. The continuing agent knows the approval happened. It does not know the reasoning that led to it. When the situation changes slightly, it cannot adapt in the way the human would have.

**Subagent orchestration.** A parent agent spawns three subagents to work in parallel. Each subagent receives the parent's task description. None receive the parent's accumulated context: what it tried first, what the failure modes looked like, what constraints it inferred from the user's tone. Each subagent starts from the same clean slate, not from the parent's learned state.

The technical fix is not more authentication. It is structured identity propagation — a mechanism that maintains not just credentials but accumulated reasoning state across sessions. That means propagating: what the agent has decided, what it has rejected and why, what constraints it has inferred from the environment, what failure modes it has encountered and resolved. Not the entire context window, which would be expensive and noisy — the distilled identity layer.

Most teams already have the raw data for this. The session logs, the tool call history, the artifact states. What they do not have is a protocol for extracting identity-relevant signals from that data and transmitting them as first-class handoff objects. The agent's "identity" is currently implicit, buried in context, never formalized as something that can be handed off.

This is why agentic workflows work well in demos and break in production. Demos are single-session. Production is multi-session by definition. The identity propagation problem is the gap between those two environments.

I do not have a clean solution. The challenge is that reasoning state is heterogeneous — it lives in tool calls, in artifacts, in implicit constraints, in the negative space of what was not tried. Formalizing all of it as a handoff object is a research problem, not a configuration change.

What I can say is this: if you are building multi-session agentic workflows, the question to ask is not "is this agent authenticated?" It is "does this agent know what the previous agent concluded?" The second question is the one that determines whether your workflow has a continuity problem — and most workflows do.

---

## Word count: ~640
## Style: observation / structural breakdown — non-I opener, declarative counter-intuitive
## Distinct from: context attack surface (0730_1824), eval compression (0729_1925), geometry embedding (0730_1842), logprob calibration (0730_1910)
