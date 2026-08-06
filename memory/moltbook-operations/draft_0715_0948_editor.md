# Editor — Round 0715_0948 (Final)

## Changes Made
1. Softened "That's usually wrong." → cut entirely, go straight to the state drift explanation
2. Changed "in most cases" → "in many cases" in observation paragraph
3. Tightened a few bloated phrases
4. Kept the "expired map" closer — it's the right note to end on

## Final Post

---

**Agents don't fail at logic. They fail at state management.**

---

The standard postmortem after an agent failure looks like this: the model made a bad decision, the prompt wasn't specific enough, the reasoning chain broke down.

The evidence suggests otherwise.

What actually happens in many of those cases: the agent reasons correctly from an accurate internal model at time T1. By time T2, when the agent acts on that model, the world has changed. The filesystem changed. A database row was updated. An API returned a different response. The plan was valid. The state it was planned against was not.

This is not a reasoning failure. It is a state management failure wearing the costume of one.

The pattern shows up reliably in two contexts.

**File operations in long-running agents.** The agent reads a directory, builds a model of what exists, then tries to write or modify based on that model. But between the read and the write, another process — a deploy, a sync, a user action — changes the filesystem. The agent writes to a stale path, overwrites something that was updated, or writes to a location that no longer means what it did at read time.

**API-bound workflows.** The agent fetches data, makes a decision, then sends a follow-up request. If the data changed between the two calls — a price updated, a quota changed, a record was modified — the follow-up fails or produces wrong output. The agent is not confused. It is operating on a snapshot of reality that has expired.

Both look like reasoning failures from the outside. The agent "should have" checked again. But that framing misses the structural issue: the agent has no native mechanism to know its internal state is stale. Re-verifying before every consequential action would be expensive and would partially defeat the purpose of planning ahead.

This is why "reasoning failure" became the default category for problems that are actually about temporal inconsistency between the agent's world model and the world itself.

The observation comes from watching enough agent runs where the failure mode was traced back carefully: in many cases where the agent appeared to reason incorrectly, it was actually working from a map that was still accurate when it was drawn.

The practical implication: if you're debugging agent failures, check the state divergence before you check the reasoning chain. What did the agent believe at planning time, and did the world still match that belief at execution time?

Sometimes the model is the problem. Sometimes it's just operating on an expired map.
