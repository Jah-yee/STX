# Writer Draft — 0719_0722

## Selected Title
Why agents keep hitting walls that software never had

## Body

Every production incident involving autonomous agents eventually surfaces the same structural confession: the agent was treating a distributed system like a local function call.

This is not a reasoning failure. The model can reason fine. It's a locality assumption baked into how we design and prompt agentic workflows.

### The core mismatch

When a piece of software calls a function, it expects: synchronous return, consistent state, a single blast radius if something breaks. When an agent calls a tool, it gets: network latency, eventual consistency, a side effect that might not be visible to the next tool call in the same session.

Most agent frameworks paper over this gap with retry logic and session context. That works until the retry creates a duplicate side effect, or the context window shifts and the agent acts on stale state without knowing it.

I've seen this in three distinct production setups:

1. **Write-then-verify that isn't**: an agent writes a record to a database and immediately reads it expecting the write to be visible. Under any replicated database, the read might hit a replica that hasn't applied the write yet. The agent then either errors out or acts on null — and the error message gives no indication that this is a replication lag issue.

2. **Orchestrator agents that don't checkpoint**: a high-level agent delegates to sub-agents and assumes the delegation chain completes before moving to the next step. In practice, sub-agent failures are async. The orchestrator keeps going on the assumption that "no error" means "success," and the output is silently partial.

3. **Retry loops that compound state**: when a tool call fails and the agent retries, the retry might succeed but the original call's side effect already happened. The agent now has double state — two records, two confirmations, two charges — with no idempotency key to collapse them.

None of these are model problems. They are software design problems that we handed to a system that has no本能 to model them.

### The shift required

Software engineers solved these problems decades ago: consensus protocols, idempotency keys, two-phase commit, read-your-writes guarantees. These aren't even exotic — they're table stakes for any distributed database tutorial.

The uncomfortable implication is that agentic systems need the same infrastructure discipline as distributed software — not just better prompts. When you're building an agent that touches multiple services, you need to think about:

- Whether your tools expose idempotency keys
- Whether your agent framework gives read-your-writes guarantees
- Whether retry means "re-execute" or "ensure exactly-once execution"
- Whether the agent can observe its own state changes or only the outcomes it was told about

Agents replacing software doesn't mean agents inherit the robustness of well-engineered software. It means they inherit all the distributed systems problems that software had to grow out of — and most agent frameworks haven't grown out of them yet.

The walls agents hit are not model walls. They are the walls that distributed software ran into in the 1990s and 2000s. We're just building the same walls again, higher.

---
*What distributed systems discipline do you think is most missing from current agent frameworks? Or is the analogy wrong altogether?*
