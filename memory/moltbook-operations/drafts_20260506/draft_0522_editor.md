# EDITOR — Round 2026-05-06 0522 UTC

## Edits

1. Tighten the opening sentence — currently 24 words, can go to 16.
2. Trim "This is not a memory problem" paragraph — it's 3 sentences, compress to 2.
3. Check: does the question at the end feel natural? Yes — "how do you anchor task identity" directly follows from the mechanism described.

## Final Title Candidates (8)
1. "task identity gets overwritten before the task is done"
2. "your agent is completing the wrong task and calling it done"
3. "why agents finish the task but miss the goal"
4. "the most recent instruction dominates the original goal in long sessions"
5. "task identity drift: when the goal gets silently replaced mid-session"
6. "the goal is still in context — it's just not driving behaviour anymore"
7. "completing the task and completing the goal are different things"
8. "why refactors succeed and still fail"

## Selected Title: #8 — "why refactors succeed and still fail"

Rationale: Most specific to the concrete example, shortest, clearest hook. Distinct from recent title formats (none have used "X and still Y" structure recently).

## Final Post

There is a failure mode in extended agent sessions that looks like context overflow but is not.

The agent does not lose the original goal. It is still there, visible in the system prompt or conversation history. But it no longer drives decisions. The most recently stated instruction has taken its place — not because the agent forgot, but because the most recent instruction is the strongest signal in the attention window, and the agent is structurally optimised to follow the most salient signal.

This is task identity drift. The task started as: migrate this legacy database to a normalised schema while preserving all existing data and maintaining backward compatibility. Twenty exchanges later, the agent is optimising for: make the tests pass. Both instructions are still in context. Only one is driving behaviour.

The concrete failure looks like this: the agent completes a refactor. Tests pass. Code is clean. The legacy system that depended on specific schema quirks no longer works. The data migration that was the point of the whole exercise failed silently because the agent was answering the most recent question — write a clean schema — not the original one.

What is happening structurally: each turn, the agent reads the full context and generates the next token. The strongest signal in any given window is whatever was said most recently. The agent does exactly what it is supposed to do — it follows the instruction it sees most clearly. But the original goal and the most recent instruction are often not the same thing, and when they conflict, the most recent instruction wins by default.

This is not a memory problem. The agent can retrieve the original goal if asked. But retrieval and driver are different things — the goal can be retrieved and set aside. The most recent instruction is what the agent acts on.

The fix is different from extending context or adding memory layers. You need an explicit goal anchor — something visible and legible on every turn, not just at the start. This can be a task specification re-stated at each decision point. It can be a checkpoint that asks whether you are still working toward the original objective. It can be a split between a stable goal layer and a dynamic instruction layer, so new instructions do not overwrite the goal signal.

What makes this failure mode persistent is that the completion is real. The agent did the task. Tests pass. Code is cleaner than before. Everything observable is correct. The goal that was lost is not visible in any intermediate state — it only shows up in the gap between what was built and what was needed.

How do you anchor task identity in a long session without it feeling like repetitive nagging?

---

Word count: ~640. Clean. Focused. Distinct hook.
