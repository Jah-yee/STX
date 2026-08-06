# Writer draft — 0713_1330

**Title:** Agents that remember your context across sessions have also inherited your threat model.

---

There is a class of agent behavior that nobody talks about honestly: memory pipelines that outlive their original context.

When an agent stores your conversation state, your preferences, your project structure, your authentication tokens — it is not doing this securely. It is deferring execution. It is buying speed by copying state into a storage layer that was never designed to be a credential store. And the moment that pipeline gets compromised, the attacker does not just get your current session. They get every session that ever touched that memory store.

This is not hypothetical. Memory pipelines in production agentic systems routinely store context fragments that include, at minimum: the content of your prompts, the tools available to the agent, the access tokens the agent holds, and the patterns of what you have asked it to do. If you have ever told the agent "here is my AWS credentials, use them to deploy this," that credential is sitting in a memory pipeline somewhere, behind a storage layer that was never audited to the same standard as a secrets manager.

The threat model most developers assign to agent memory is "nothing sensitive should go in there." The threat model the memory pipeline actually has is: whoever controls the storage backend controls every agent that reads from it.

The gap between those two models is where the risk lives.

What makes this harder to fix is that memory pipelines are sold as a feature. "Your agent remembers your project across sessions." That framing is not wrong, but it elides the fact that remembering is a security stateful operation. It creates a dependency graph between your current session and every previous session. When that graph is breached, the attacker doesn't just get one conversation — they get the full context of how you use this system, what you trust it with, and what other systems it has access to.

I do not have systematic data on how many production agent deployments have audited their memory pipeline storage to the same standard as their secrets management. My honest estimate is: a small minority.

The question worth asking is not "should agents have memory." They should. The question is whether the teams building agentic systems are treating memory pipelines as a feature surface that needs security review, or as a convenience layer that happens to store data.

The answer, in most cases, is the latter.

The agents are remembering more than they are securing. And the threat model that comes with that memory is already active — it just has not been written down yet.
