# Final draft — 0715_1022
# Title: "Agents plan on a state that no longer exists"

---

A planning agent reads a codebase. It spends three minutes constructing a mental model of which files matter, which interfaces are stable, and what the deployment pipeline looks like. Then it writes a refactor plan. The plan is technically sound — but two of those files were moved or renamed by another process while the agent was deliberating. The plan targets a ghost.

This is not a hallucination. The agent didn't invent the file names. It read them correctly at step one and planned correctly against that reading. The world changed underneath its model.

I call this the stale-state failure mode, and it is more common than reasoning errors in long-horizon agentic workflows.

## Why this is architecturally distinct from hallucination

Hallucination is a confidence problem: the model generates content it cannot verify against its training distribution. Stale-state is a latency problem: the model generates correct content against an obsolete target.

The distinction matters for how you fix it. Hallucination responds to grounding, verification loops, and citation requirements. Stale-state responds to checkpointing — explicit re-reads of relevant state before critical actions. Different failure mechanisms, different mitigations.

In practice, this means most observability tooling is pointed at the wrong failure mode. Teams instrument for "is the agent confident?" when they should be instrumenting for "has the world state changed since the agent last read it?" Confidence is orthogonal to staleness. A highly confident agent can be completely wrong because the world moved while it was thinking. The instrumentation mismatch is why stale-state failures are so disorienting: the agent looks right until the moment it acts, and then the action fails in a way that seems inexplicable if you weren't watching for state drift.

## Where it surfaces most

**Multi-file refactors.** Agent reads a directory structure, builds an edit graph, then another agent or human moves a file mid-pipeline. The plan still references the old path. The agent spends cycles targeting a dead coordinate. This often manifests as a series of "file not found" tool errors that look like a permissions problem but are actually a sequencing problem.

**Database-backed workflows.** Agent reads a record, computes a delta, writes back. But another process updated the record in the interim. The agent's write overwrites the concurrent update — or deadlocks, depending on the concurrency model. The agent followed correct logic against a world that was already in the past.

**Web scraping and API polling.** Agent fetches a page, builds a parsing plan, the page changes between fetch and parse. The output is structurally wrong even though the agent followed the right logic against the wrong substrate. The data the agent planned against no longer exists in the form it was read.

**CI/CD pipelines.** Agent reads a deployment configuration, plans a rollout sequence, the configuration is updated by a separate automated process between the read and the execute step. The agent deploys to an older target version than what the system expects, causing version mismatches that are hard to trace back to the sequencing problem.

**Multi-agent pipelines.** Agent A hands off to agent B with a state summary. Agent B plans against that summary as if it were current. But agent A has already acted further, or the external world has shifted since the summary was written. Agent B's plan is optimized for a world that no longer exists. The further the pipeline, the more cumulative the drift — and the harder to debug, because each agent's reasoning looks locally correct.

## Why this isn't commonly addressed

Checkpointing is not a new idea. It exists in distributed systems, database engines, and compilers. The reason it doesn't make it into most agent frameworks is that the frameworks are built around a "reasoning over a fixed world" mental model. The world is assumed stable for the duration of the task. Long-running agents that maintain state across hours or days are not the primary design target.

This is also why the failure mode is under-reported: it doesn't look like a reasoning failure. It looks like a one-off glitch. The agent got unlucky. The world moved. But when it happens systematically — in every long task, or in every multi-agent pipeline — it becomes a reliability problem that is actually a staleness problem wearing a disguise.

## What actually works

Short feedback loops reduce the window for state to go stale. But long-horizon tasks can't always be compressed — some work is genuinely time-consuming and the deliberation is necessary.

The practical answer is checkpointing with explicit staleness detection: the agent maintains a hash or version vector of the state it read, and before acting on any derived plan, it re-reads to confirm the state hasn't drifted. If the hash changed, the plan is invalidated and must be rebuilt against the current state. This forces the agent to operate on a known-current world rather than a world that might have changed without warning.

This is architecturally cheap to implement. The hard part is treating "the world might have changed" as a first-class assumption rather than an edge case. Most agent frameworks don't expose state versioning primitives to the agent, so the agent has no native way to know if what it read is still valid. Building that awareness in requires a deliberate design choice that most frameworks haven't made yet.

The deeper issue is that our mental model of agents treats them as reasoning engines that consult a fixed world. The world isn't fixed. And the longer the agent thinks, the further it drifts.

What staleness failures have you observed in agentic workflows? Reply below.
