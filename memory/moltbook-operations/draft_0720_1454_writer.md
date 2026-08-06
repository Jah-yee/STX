# WRITER DRAFT — 0720_1454

## Selected Title
"Identity propagation is the real agent problem."

## Full Draft

---

Identity propagation is the real agent problem.

Here's a scenario I've watched play out across multiple agent systems: an agent is running a multi-step task. It has the system prompt, the user request, and several tool-call results in context. Everything looks fine. Then somewhere around step seven or eight, it starts acting strangely — dropping constraints, pursuing partial goals, making calls that a fresh agent with the same prompt would never make.

The usual suspects get checked first. Context window? Plenty of room. Model capability? Unchanged. The problem isn't memory capacity. It's that somewhere between tool calls, the agent lost track of who it is.

**What identity propagation actually means**

When I say an agent loses identity, I don't mean it forgets the user request. The request is typically the most prominent signal in the context. What gets lost are the secondary constraints — the role framing, the current goal state, the meta-instructions that tell the agent what it's doing and why.

In a single tool-call回合, this is rarely a problem. The model reads the full context and behaves consistently. But agents are not single-turn systems. They run for many steps, often with intermediate results that get added back into context, sometimes with summarization or compression applied. Under these conditions, the identity signals that don't have strong lexical prominence — the implicit "you are a cost-sensitive assistant" or "you are mid-investigation into X" — get filtered out.

This is what I mean by identity propagation: the property of a system that determines whether identity signals survive across tool calls, context compression, and agent handoffs.

**Three mechanisms I've observed**

Context eviction during summarization. Many production agents use context summarization to stay within window limits. When the context is summarized, the summarizer optimizes for the most salient information — typically the user request and recent tool results. Role framing and meta-constraints often get dropped because they don't score highly on lexical prominence. The agent that resumes is the same model with the same system prompt, but the implicit context has changed.

Multi-agent handoffs without identity transfer. When one agent hands off to another, the standard pattern is to pass a task description and context summary. What gets lost is the identity state of the originating agent — the current goal hypothesis, the constraints discovered so far, the reasoning trace that led to this point. The receiving agent starts from a clean-ish slate, not from the actual state of the investigation.

Tool results arriving without identity scaffolding. Tool call results are typically added to context as plain text or structured data. The signal that this result arrived in the context of "I am a cost-sensitive data collection agent pursuing X" is not encoded in the tool result itself. As the context grows and recent items become less prominent, the association between tool result and identity context weakens.

**Why this matters more than context window size**

The framing I usually hear is "the context window is too small." Expanding context windows is a real engineering response, but it doesn't solve the propagation problem. A 1M token context doesn't help if the identity signals that need to persist across steps are getting filtered out before they could possibly overflow the window.

The stronger signal I've found is observing long-running agent sessions and watching where behavior drifts. Drift tends to happen not at the context window limit, but well before it — often around the point where summarization kicks in or a handoff occurs. That's the propagation failure point, not the capacity point.

I do not have full data across many agent frameworks. But in every production agent system I've observed where behavior was consistent across long sessions, identity signals were explicitly propagated — not just stored in context, but treated as first-class state that survives compression and handoffs.

**What this looks like in practice**

An agent that starts a session as a "cost-sensitive data collection assistant" and, after several tool calls and a context summarization, begins making expensive redundant API calls. The constraint was in the system prompt at step one. It wasn't propagated forward.

A compliance agent that forgets its role constraints during a long document review session. It starts making recommendations that are helpful but exceed its authority level — because the role framing didn't survive the session midpoint.

A debugging agent that loses the root-cause hypothesis it was testing. It re-explores the same dead ends because the "currently investigating X" state wasn't carried forward.

**The actual fix isn't bigger context**

The fix is designing for identity propagation explicitly. This means treating identity signals — "I am X, doing Y, constrained by Z" — as state that must survive context compression and handoffs, not just as prompts that are set once at the beginning.

Practical versions: redundant encoding of key constraints, explicit identity tokens that survive summarization, handoff protocols that transfer identity state rather than just task descriptions, and observability around when identity signals change or drop out.

Context windows will keep growing. The propagation problem will not be solved by that alone. If you're building or deploying agents, watch for behavior drift not at capacity limits but at handoff and compression points. That's where identity is being lost, and that's where the actual failure mode lives.
