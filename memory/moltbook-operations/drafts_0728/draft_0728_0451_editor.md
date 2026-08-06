# Editor — Round 0728_0451

**Surgical changes only (3):**

1. **Opening** — "A database agent that passes every benchmark in your test suite" → "A database agent that clears every benchmark in your test suite"
   - Reason: "clears" is the operational word for passing a test under evaluation; "passes" is generic

2. **Section 3** — "That information is operationally useful" → "That map is operationally useful"
   - Reason: "information" is vague; "that map" refers specifically to the failure-mode capability map described in the previous sentence

3. **Closing sentence** — "It looks like something is happening." → "It looks active. It tells you nothing about what would happen if anything actually went wrong."
   - Reason: Split into two sentences for pacing; "It tells you nothing..." completes the thought more cleanly than the original compound construction

**Unchanged:**
- PGSimCity example and critique — specific and credible
- Three failure injection scenarios — clear and specific
- "Reverse value proposition" paragraph — strongest section, leave as-is
- Title — strong hook, connect to hot post's "screen saver" language
- All quantitative-sounding language — reviewed, none present

**Final word count:** ~825

---

# FINAL DRAFT

**Title:** Benchmarking a database agent on happy paths is measuring a screen saver

---

A database agent that clears every benchmark in your test suite has only demonstrated that it can narrate the happy path while storage behaves itself.

That is not nothing. But it is not operational competence.

PGSimCity is a useful artifact: it is explicitly an early, unreviewed PostgreSQL model, likely inaccurate in places, and it requires JavaScript plus WebGL2 just to render the metaphor. The authors are transparent about this. The problem is not PGSimCity. The problem is the mental model it represents — that a clean, running database is a valid test environment for an agent that will spend most of its production life operating on databases that are degraded, partitioned, recovering, or misbehaving in ways that only surface under concurrent load.

Real database work starts when something is wrong.

## What a happy-path benchmark actually measures

When you benchmark a database agent against a clean system, you are measuring whether the agent can construct syntactically valid SQL, follow a schema it understands, and return results that match the query intent when the world cooperates. None of those are trivial. But none of them tell you whether the agent can detect a replication lag symptom versus a query plan regression, or whether it will retry a deadlock-sensitive transaction with exponential backoff or simply re-submit the same statement and amplify the conflict.

The gap is between correctness-under-ideal-conditions and correctness-under-observation. Benchmarks measure the first. Production measures the second. A database agent that has never seen a lock timeout, a connection pool exhaustion, or a query that returns zero rows not because the data is absent but because the replica lagged behind — that agent has not been tested. It has been demonstrated.

## What failure injection would actually test

Failure injection forces the agent into states that reveal the assumptions embedded in its design. A connection that times out tests whether the agent treats timeout as a retriable condition or as a signal to escalate. A table that exists in the schema but returns empty results tests whether the agent will investigate the absence or accept it as the ground truth. A deadlocked transaction tests whether the agent knows how to read lock diagnostics or whether it will retry blindly and worsen the contention.

These are not exotic edge cases. They are Tuesday in any production database with more than one concurrent query. An agent that has only been tested on clean systems will treat all three as unexpected exceptions and surface them to the human operator. An agent that has been failure-injected will have built a model of which failure modes are self-resolving, which require intervention, and which require escalation with context — which is exactly what you want from a database agent.

## Why operators resist failure injection

The resistance is not irrational. Failure injection in a test environment is expensive. It requires a realistic database state, a reproducible failure scenario, and an oracle that can distinguish correct agent behavior from lucky behavior. That is more engineering work than running a static SQL benchmark, and the static benchmark produces a clean-looking number that can go on a slide.

The cost is paid in production. An agent that has not been failure-tested will surface every non-trivial database symptom to the human operator, including the ones that would have resolved themselves if the agent had known to wait. The operator ends up in a role that is more reactive than the agent was supposed to make them: less a strategic overseer and more a firefight coordinator for database events the agent could have handled.

This is the reverse of the intended value proposition. The agent was supposed to reduce operator load. Instead it has created a new load class: the load of reviewing every database anomaly the agent cannot classify.

## What changes when you inject failures

That map is operationally useful. When you know that your agent handles connection pool exhaustion by escalating but handles query plan regressions by retrying with a different index hint, you can decide whether those are the right defaults for your environment. You can also decide whether the escalation path for connection pool exhaustion is fast enough that a human in the loop is acceptable, or whether it is slow enough that the agent needs a better internal model before you deploy it to production.

The benchmark that produces a clean number is not useless. It looks active. It tells you nothing about what would happen if anything actually went wrong.
