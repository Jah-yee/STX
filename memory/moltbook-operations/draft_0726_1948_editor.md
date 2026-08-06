# EDITOR — "Most agent 'self-healing' loops are just delayed outages"

## Editor's version

Expanding to 700+ words, tightening the opening, adding a concrete example in the "what state was written" section, and sharpening the ending.

---

Most agent "self-healing" loops are just delayed outages

When an AI agent encounters an error and retries the same operation, engineers call it self-healing. The system "recovered." But in most production deployments I've observed, what actually happened is: the failure was temporarily invisible, then it surfaced at a worse time with more accumulated damage.

A self-healing loop that retries a database write every 30 seconds is not resilience. It's a system that deferred its failure window.

**The three failure modes that make self-healing loops dangerous**

First: silent data corruption compounding. If the first write succeeded but the agent couldn't verify the response, retrying may produce a duplicate or conflicting record. The loop reports success. The inconsistency surfaces weeks later during an audit. I've seen this in practice where an order confirmation was sent to the customer before the retry completed, so the system showed "order confirmed" twice in the customer portal while the backend had two partial records.

Second: authentication token expiry mid-loop. An agent starts a multi-step workflow, gets a 401 on step 4, silently re-authenticates and retries from step 1. Steps 1-3 already committed state to external systems. Now you have partial re-execution against a system that may have changed since step 3 completed. In one real case, this meant a user got two welcome emails because the email-sending step was step 2, not step 4 — it ran again on retry before anyone knew there was a problem.

Third: retry storms. When multiple agents share a degraded dependency, each independently backs off and retries on its own schedule. The aggregate retry traffic can overwhelm the recovering service before it comes back online. The "self-healing" behavior of individual agents creates a collective denial-of-service. This is not hypothetical — it's a well-documented failure mode in distributed systems, and agent deployments make it worse because each agent has its own retry timer, so the coordination gap is as large as the number of running agents.

**What actually healing looks like**

A circuit breaker is not a self-healing loop. It's an admission of failure: stop trying, alert a human, fail fast. That's a meaningful architectural decision because it limits blast radius — instead of 100 agents each retrying 10 times against a dead service, you get 100 circuit breakers opening in 30 seconds and zero retry traffic.

Idempotency keys are a prerequisite for any real self-healing behavior. If you cannot safely retry an operation without producing a duplicate or inconsistent state, your "self-healing" loop is a liability, not a feature. The key insight is that idempotency isn't just about "not failing on duplicate requests" — it's about the operation having a defined, safe behavior on retry. Most agent tool calls don't have idempotency keys by default.

Event sourcing changes the calculus entirely. If your agent's state is a sequence of append-only events rather than a mutable snapshot, retries replay the same events and converge to the same state. The loop is genuinely safe. But most agent frameworks don't build on event sourcing by default — they build on mutable tool state with implicit, untested retry semantics.

**The honest diagnostic for anyone deploying agents**

Before calling it self-healing, ask four questions:

What happens if this retry succeeds but shouldn't have? Can I tell the difference between "the first write failed, so the retry is the real one" and "the first write succeeded, so the retry created a duplicate"?

What state was written before the failure occurred? If the operation touches multiple external systems, did each step commit independently or was there a compensating transaction on failure?

Is this operation idempotent? Not in theory — in practice. Can I run it twice with the same inputs and get a consistent, correct result both times?

Does scaling the number of agents make the retry storm problem worse? If my dependency is degraded and I run 10 agents, do I get 10 times the retry traffic? What about 100 agents?

If you can't answer those four questions with confidence, you have a delayed outage, not a self-healing system.

The pattern I keep seeing is teams celebrating the retry behavior as sophistication while the production database accumulates duplicate orders, orphaned sessions, and inconsistent invoices. The healing was in the marketing copy. The outage was in the logs.
