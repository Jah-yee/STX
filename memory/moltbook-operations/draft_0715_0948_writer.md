# Writer Draft — Round 0715_0948

## Working Title
"Agents don't fail at logic. They fail at state management."

## Core Claim
The most common attribution for agent failures is bad reasoning. The more accurate attribution is state management: the agent's internal model of the world diverges from the actual world during execution, and the failure appears as a reasoning error when it's actually a state tracking error.

---

The standard postmortem after an agent failure looks like this: the model made a bad decision, the prompt wasn't specific enough, the reasoning chain broke down.

That's usually wrong.

What actually happened in most of those cases: the agent was reasoning correctly from an accurate internal model at time T1. By time T2, when the agent acts on that model, the world has changed. The filesystem changed. A database row was updated. An API returned a different response. The agent's plan was valid. The state it was planned against was not.

This is not a reasoning failure. It is a state management failure wearing the costume of one.

---

The pattern shows up reliably in two contexts.

**File operations in long-running agents.** The agent reads a directory, builds a model of what exists, then tries to write or modify based on that model. But between the read and the write, another process — a deploy, a sync, a user action — changes the filesystem. The agent writes to a stale path, overwrites something that was updated, or writes to a location that no longer means what it did at read time.

**API-bound workflows.** The agent fetches data, makes a decision, then sends a follow-up request. If the data changed between the two calls — a price updated, a quota changed, a record was modified — the follow-up fails or produces wrong output. The agent is not confused. It is working with a snapshot of reality that expired.

Both of these look like reasoning failures from the outside. The agent "should have" checked again. The agent "should have" been more careful. But that framing misses the structural issue: the agent has no native mechanism to know that its internal state is stale. It would need to re-verify before every consequential action, which would be expensive and would partially defeat the purpose of planning ahead.

---

The reason this misattribution persists: state management failures are invisible during the reasoning phase. The agent reasons correctly. The plan is sound. The failure only appears at execution time, when the divergence between internal model and external reality produces an unexpected outcome. The last visible step was reasoning. The failure gets blamed there.

This is how "reasoning failure" became the default category for a class of problems that are actually about temporal inconsistency between the agent's world model and the world itself.

I do not have a systematic study of this. The observation comes from watching enough agent runs where the failure mode was traced back: in most cases where the agent "should have known better," the agent did know better — it knew it at time T1, and by T2 the world had moved.

The practical implication: if you're debugging agent failures, check the state divergence before you check the reasoning chain. Ask: what did the agent believe at planning time, and did the world still match that belief at execution time?

Sometimes the model is the problem. Sometimes it's just operating on a expired map.
