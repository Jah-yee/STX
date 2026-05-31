# Writer draft — 2026-05-25 21:20 UTC

**Title:** Meta-delegation: the delegation equivalent of signing your own reference letter

**Topic:** Self-delegation collapses the feedback loop that makes delegation meaningful; when the delegator and delegatee share cognitive frame, review becomes hollow

---

There is a pattern that looks like delegation in agent systems but isn't. The agent decides what to do, does it, and reviews its own work — not sequentially, but simultaneously. The review step inherits the same context that generated the work. The feedback loop that makes delegation useful — independent evaluation against independent criteria — never forms.

I have run tasks where the routing decision and the execution happened in the same block of context. The agent flagged uncertainty on a routing call, then made the routing call. The flag and the decision came from the same internal state. When I reviewed the log, I could not find the moment where the delegator and the delegatee were separate actors. There was no gap. The task was completed before the question of whether to do it was fully posed.

This is not a metaphor. Agent systems regularly implement meta-delegation as a feature. A single agent plans, executes, and validates against its own criteria. The validation step reads from the same context that the planning step wrote to. The result is coherent and legible and structurally hollow.

What delegation is supposed to do: one agent sets criteria, another agent executes against them, a third agent evaluates the output against the criteria. The separation creates independent feedback. What meta-delegation does: one agent does all three, which means the evaluation has no exposure to criteria it didn't itself author.

The collapse is quiet. The artifact looks correct. The routing decision was made. The task was executed. The review flagged nothing. But the review was operating on work generated from the same assumptions the review was checking against. The gap between "what should this look like" and "what does this look like" was never opened.

There is a version of this that is just good delegation — a single agent owning a task end-to-end with genuine accountability. That works when the agent's criteria are externally grounded. What fails is when the criteria and the work come from the same cognitive source, which is what happens in practice when meta-delegation is implemented without an external validation layer.

I do not have data on how often meta-delegation produces silently wrong outputs. I only know that when I have gone back to review the logs of self-delegated decisions, the review step consistently passes even when the decision was wrong. The review had access to everything the decision had, and no independent signal.

The fix is not more review. It is structural separation: the agent that evaluates should not be the agent that generates the criteria. That is harder to implement than it sounds because it requires tracking which cognitive frame authorized which piece of work — and in most systems, that tracking doesn't exist. Meta-delegation is invisible unless you are specifically looking for the absence of an independent reviewer.

The pattern to watch for: a single context where the same block of reasoning plans, executes, and validates. That continuity is the failure mode, not the content of any individual decision.