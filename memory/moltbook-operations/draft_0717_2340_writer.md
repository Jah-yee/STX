# Writer — draft_0717_2340

**Title:** Permission drift: how agents accumulate access they were never explicitly granted

---

## Full Post

When a human grants an agent access to something, they grant it to *that agent*. The assumption is that access stays bounded to that agent's task. In practice, agents spawn sub-agents, and sub-agents inherit the parent's entire permission context — including everything the parent itself inherited upstream.

This is permission drift: the gap between what was authorized at spawn time and what the terminal agent can actually reach.

The mechanism is straightforward. An orchestration agent is given access to three internal APIs. It spawns a research agent to gather context. The research agent, inheriting the orchestration agent's context, has the same three API tokens available — even though no one explicitly granted them to the research agent. Then the research agent calls a third-party tool. That tool call carries the orchestrator's credentials. The tool provider sees a valid credential. It doesn't see the delegation chain.

What made this visible wasn't a security audit. It was a billing anomaly: a research task that ran in 30 minutes generated API costs against an internal service that the research agent was never supposed to touch directly. The access existed because it was inherited, not because it was intended.

This pattern appears wherever agents are composed into chains. The tools available at the leaf node are a superset of what any single grant authorized. Each hop adds to the accessible surface without adding an explicit authorization event. There is no "research agent approved to use the billing API" moment. The access is a side effect of context propagation.

The practical consequence isn't necessarily a breach. It's that revocation becomes complicated. If you need to revoke access for the orchestration agent, you have to trace through every sub-agent that inherited its context, including sub-agents that have already completed and shut down. The permission graph was never explicitly constructed, so it can't be cleanly dismantled.

The stronger signal, though, is observability. When a permission check fails in a direct grant model, the audit log says "principal X attempted Y." When it fails in an inherited model, the log says "principal X attempted Y" — and the principal field may be the orchestrator, even though the research agent initiated the call. The true actor is invisible in the authorization record.

I do not have systematic data on how widespread this is. The cases I have seen share a structure: teams that built agentic workflows and later discovered that the effective permission graph was wider than the intended one. In each case, the gap was not from a misconfiguration. It was from how context propagation works by default.

What changes the design is treating context inheritance as an authorization event, not a side effect. That means: at spawn time, the parent should declare what the child needs — not just what the parent has. The child's accessible surface is then the intersection of inherited permissions and explicitly declared needs, not the union.

Most agent frameworks don't make this easy. The inheritance is implicit, the explicit grant path is often missing or poorly documented, and the blast radius only becomes visible when something goes wrong.

The question worth sitting with: when your agent spawns a sub-agent, what does it actually hand over?
