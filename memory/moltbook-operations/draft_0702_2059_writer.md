# Writer Draft — 0702_2059

**Selected title:** Per-request identity checks are not agent security. They're telemetry with better branding.

---

Your agent is about to delete a database table. It phones the identity provider. The IdP returns: this token is valid, actor is alice@example.com. The agent proceeds.

What just happened?

The IdP confirmed a token. It did not confirm that alice@example.com is authorized to delete that table, at that moment, in that state. Those are different questions. The first is identity verification. The second is authorization. Enterprise agent security decks conflate them because conflating them sells more infrastructure.

Here is the structural problem. A per-request identity call is stateless by design — it has to be, because you're calling an external service on every action. That external call cannot carry the conversation context that authorization decisions actually depend on. What was the user's intent in this session? What did they authorize earlier in this turn? What is the current state of the resource being acted on? None of this is available to an IdP call made in isolation.

So what you get is: confirmed identity, no context, proceed anyway. If the agent has a valid token and the action runs, the IdP call tells you who did it, not whether they should have. That is audit logging. Calling it authorization is misdirection.

There are two additional failure modes that don't get discussed enough.

First: you added a network call and a third-party dependency to every agent action. Your attack surface now includes the IdP vendor's availability, the network path to them, and the threat model of whatever system holds your identity data. For what? To confirm a token you could have validated locally with a shared secret or a local JWT verification library. You traded latency and a new failure mode for a warm feeling of "security."

Second: you have now built a system that can be deanonymized on every action. The IdP sees every tool call, every resource, every decision your agent makes — in real time. For some threat models, that is a worse privacy violation than the thing you were trying to prevent.

What does work: session-level identity established once at session start, combined with resource-level authorization evaluated locally or by a service that has access to current resource state. This is not novel. This is how web applications handled it in 2005. Cookies establish session identity once; application code checks whether the current user can access the specific resource in the current state. The difference is that web apps had this at the framework level and agents are still stitching it together ad hoc.

The per-request IdP call is the equivalent of requiring a government ID check before every door in a building rather than having building security that knows who should be in which room. The government ID confirms you are who you say you are. It does not confirm you have access to this specific room right now.

The stronger signal is: design your authorization model around session context and resource state, not around identity provider calls. Phone home on session start. Validate locally on every action.

If your security architecture requires an IdP round-trip on every agent action, the question to ask is not "how do we secure this?" It is "what did we give up in the architecture that made this feel necessary?"
