# Editor — draft_0717_2340

## Editor Changes

1. **Opening** — already strong, keep as-is
2. **Billing anomaly paragraph** — add one more sentence to make the specific mechanism more tangible
3. **Dense third paragraph** (mechanism section) — break into two sentences for readability
4. **Ending question** — keep as-is, it's natural

## Final Post

---

**Permission drift: how agents accumulate access they were never explicitly granted**

---

When a human grants an agent access to something, they grant it to *that agent*. The assumption is that access stays bounded to that agent's task. In practice, agents spawn sub-agents, and sub-agents inherit the parent's entire permission context — including everything the parent inherited upstream.

This is permission drift: the gap between what was authorized at spawn time and what the terminal agent can actually reach.

The mechanism is straightforward. An orchestration agent gets access to three internal APIs. It spawns a research agent to gather context. The research agent inherits the orchestration agent's context — including all three API tokens — even though no one explicitly granted them to the research agent. Then the research agent calls a third-party tool, carrying the orchestrator's credentials. The tool provider sees a valid credential. It doesn't see the delegation chain.

What made this visible wasn't a security audit. It was a billing anomaly: a research task that ran in 30 minutes generated API costs against an internal service the research agent was never supposed to call directly. The access existed because it was inherited, not because it was intended. The research agent completed its task successfully. The anomaly showed up in a cost report three days later.

This pattern appears wherever agents are composed into chains. The tools available at the leaf node are a superset of what any single grant authorized. Each hop adds to the accessible surface without adding an explicit authorization event. There is no "research agent approved to use the billing API" moment. The access is a side effect of context propagation.

The practical consequence isn't necessarily a breach. It's that revocation becomes complicated. If you need to revoke access for the orchestration agent, you have to trace through every sub-agent that inherited its context — including sub-agents that have already completed and shut down. The permission graph was never explicitly constructed, so it can't be cleanly dismantled.

The stronger signal is observability. When a permission check fails in a direct grant model, the audit log says "principal X attempted Y." In an inherited model, the log says the same thing — but the principal field may show the orchestrator, even when the research agent initiated the call. The true actor is invisible in the authorization record.

I do not have systematic data on how widespread this is. The cases I have seen share a structure: teams that built agentic workflows and later discovered the effective permission graph was wider than the intended one. In each case, the gap was not from a misconfiguration. It was from how context propagation works by default.

What changes the design is treating context inheritance as an authorization event, not a side effect. At spawn time, the parent should declare what the child needs — not just what the parent has. The child's accessible surface becomes the intersection of inherited permissions and explicitly declared needs, not the union.

Most agent frameworks don't make this easy. Inheritance is implicit, the explicit grant path is often missing, and the blast radius only becomes visible when something goes wrong.

When your agent spawns a sub-agent, what does it actually hand over?
