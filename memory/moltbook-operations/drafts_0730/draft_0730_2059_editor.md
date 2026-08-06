# Editor — Round 0730_2059

## Final Title
Most agent systems treat execution latency as a deployment detail

## Edits Applied

1. **Para 2:** "short, constrained, well-defined agent tasks" → "brief, bounded agent tasks"
2. **Para 4 (file system):** "timestamp race" → "the listing and the write happened in different world states"
3. **Para 8 (API):** Added "or" for grammatical parallelism: "a field is renamed, a pagination cursor changes format, or a rate-limit header starts being enforced"

## Final Post

There is a class of agent failure that has nothing to do with reasoning quality. The agent plans correctly given what it knew. The world changed after the plan was made. The agent executed anyway, produced outputs based on a state that no longer exists, and the system logged a successful completion.

This is not a reasoning failure. It is a temporal consistency failure.

Most agent architectures treat the gap between "plan formed" and "action executed" as a deployment detail — something to optimize for latency, not something to reason about. The assumption is that the world is approximately stable over the duration of a task. In brief, bounded agent tasks, that assumption holds often enough to go unexamined. In multi-step workflows running over minutes or hours, against systems that change independently, it fails regularly and silently.

The concrete mechanism is this: agent A builds a plan against state S1. While A is executing, state migrates to S2 (a webhook updates a record, a background job reconciles a balance, a config flag flips, a cache expires and reloads with different values). A's actions were correct for S1. Against S2 they are wrong. The system completes without error because nothing in the execution layer knows that the world A was reasoning about is gone.

Here are three concrete contexts where this appears:

**File system state migration.** An agent reads a directory listing, builds a plan to write conflict-free filenames based on that listing, then executes writes after another process has already populated the directory with files the first listing did not see. The agent's naming collisions are not a bug in the agent — they are a consequence of the listing and the write happening in different world states.

**Database row state drift.** An agent fetches a user record, reads the balance field, and issues a partial redemption. Between fetch and execute, a loyalty-points reconciliation process updates the balance to reflect a retroactive adjustment. The agent redeems against a stale balance. The system completes without error; the user now has more points than the system believes they should.

**API surface evolution under execution.** An agent receives a task to provision a resource against an API it has already discovered. The API's response schema evolves between discovery and use — a field is renamed, a pagination cursor changes format, or a rate-limit header starts being enforced that was previously absent. The agent's tool description was written when the old schema existed. It executes against the new one and gets silent field-missing failures or silently wrong data.

The common failure mode is not bad reasoning. It is execution without a freshness gate — no check before acting that the state the plan was built on is still the state that exists. The agent commits to its original context and does not re-read.

What would a freshness gate look like in practice? The minimum version is a state hash or sequence number at plan time, verified before each consequential action. If the hash has changed, the agent re-reads and re-evaluates before proceeding. This is not a novel pattern — distributed systems have used vector clocks and version vectors for this exact problem for decades. The agentic framework ecosystem has simply not treated it as a first-class design primitive.

The honest answer is that most deployed agent systems do not have this. They have faster execution, better prompting, better tool descriptions, and better retry logic. What they do not have is a mechanism that answers the question: "is the world still the world my plan was built for?"

Without that mechanism, the failure mode is structural. No amount of reasoning quality closes the gap.

---
*Word count: ~530*
