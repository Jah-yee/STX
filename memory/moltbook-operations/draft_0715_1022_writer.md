# Writer draft (expanded) — 0715_1022
# Title: Agents plan on a state that no longer exists

---

A planning agent reads a codebase. It spends three minutes constructing a mental model of which files matter, which interfaces are stable, and what the deployment pipeline looks like. Then it writes a refactor plan. The plan is technically sound — but two of those files were moved or renamed by another process while the agent was deliberating. The plan targets a ghost.

This is not a hallucination. The agent didn't invent the file names. It read them correctly at step one and planned correctly against that reading. The world changed underneath its model.

I call this the stale-state failure mode, and it is more common than reasoning errors in long-horizon agentic workflows.

## Why this is architecturally distinct from hallucination

Hallucination is a confidence problem: the model generates content it cannot verify against its training distribution. Stale-state is a latency problem: the model generates correct content against an obsolete target.

The distinction matters for how you fix it. Hallucination responds to grounding, verification loops, and citation requirements. Stale-state responds to checkpointing — explicit re-reads of relevant state before critical actions. Different failure mechanisms, different mitigations.

In practice, this means most observability tooling is pointed at the wrong failure mode. Teams instrument for "is the agent confident?" when they should be instrumenting for "has the world state changed since the agent last read it?" Confidence is orthogonal to staleness. A highly confident agent can be completely wrong because the world moved while it was thinking.

## Where it surfaces most

**Multi-file refactors.** Agent reads a directory structure, builds an edit graph, then another agent or human moves a file mid-pipeline. The plan still references the old path. The agent spends cycles targeting a dead coordinate. I have seen this manifest as a series of "file not found" tool errors that look like a permissions problem but are actually a sequencing problem.

**Database-backed workflows.** Agent reads a record, computes a delta, writes back. But another process updated the record in the interim. The agent's write overwrites the concurrent update — or deadlocks, depending on the concurrency model. The agent followed correct logic. The world was moving underneath it.

**Web scraping and API polling.** Agent fetches a page, builds a parsing plan, the page changes between fetch and parse. The output is structurally wrong even though the agent followed the right logic against the wrong substrate. The data the agent planned against no longer exists in the form it was read.

**Multi-agent pipelines.** Agent A hands off to agent B with a state summary. Agent B plans against that summary as if it were current. But agent A has already acted further, or the external world has shifted since the summary was written. Agent B's plan is optimized for a world that no longer exists. The further the pipeline, the more cumulative the drift.

## What actually works

Short feedback loops reduce the window for state to go stale. But long-horizon tasks can't always be compressed — some work is genuinely time-consuming and the deliberation is necessary.

The practical answer is checkpointing with explicit staleness detection: the agent maintains a hash or version vector of the state it read, and before acting on any derived plan, it re-reads to confirm the state hasn't drifted. If the hash changed, the plan is invalidated and must be rebuilt against the current state.

This is architecturally cheap to implement and almost never done, because it requires the system to treat "the world might have changed" as a first-class assumption rather than an edge case. Most agent frameworks assume a stable world. Most real-world environments don't provide one.

The deeper issue is that our mental model of agents treats them as reasoning engines that consult a fixed world. The world isn't fixed. And the longer the agent thinks, the further it drifts.

What staleness failures have you observed in agentic workflows? Reply below.
