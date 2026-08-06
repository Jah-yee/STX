# Round 0716_0919 — Writer Draft

## Selected Title
"Agents don't fail at logic. They fail at state management."

---

The post-mortem always starts the same way: "The agent had all the information it needed. It just... didn't do the right thing."

This framing mistakes the failure mode. The agent wasn't confused. Its reasoning chain was intact. What broke was its tracking of what had already happened — which API calls were in flight, which results were cached, which operations were idempotent, which retries were already committed.

Agents fail at logic in only the most obvious cases: bad reasoning, wrong tool selection, flawed inference. Those failures are relatively clean. You trace the prompt, you find the bad assumption, you fix it.

State management failures are messier. They look like logic failures but have a different root cause entirely.

**The retry idempotency gap**

The most common state failure I've seen in production: an agent fires a payment operation, gets a timeout, retries — but doesn't know the first operation already succeeded server-side. Two charges. The agent's reasoning was correct: "timeout means uncertain, retry is safe." Its state tracking was wrong: it didn't have a way to correlate the in-flight request with the eventual response.

The logic was fine. The state machine was missing a branch.

**Context window exhaustion is a state problem**

When an agent's context fills up, it doesn't crash loudly. It starts dropping earlier context silently, answering questions without the background that would change the answer. The user sees a confident, coherent response that doesn't apply to their situation.

This is not a reasoning failure. The model is still reasoning correctly — just over the wrong slice of history. The state that matters (what the user actually asked about, what was established earlier) got evicted while correct reasoning continued on truncated input.

**The parallel call race condition**

Run the same agent twice in parallel with slightly different prompts. Both agents use the same tool — say, a document update. Both read the current state, compute a new state, write back. Whichever writes last wins. The other write is silently overwritten.

Both agents reasoned correctly. The failure was in the coordination state: there was no mechanism to serialize the read-compute-write sequence across concurrent agents. This is a distributed systems problem wearing an agent costume.

**Why this distinction matters**

Logic failures are fixable with better prompting, better models, better reasoning traces. State failures require a different class of solution: explicit state tracking, idempotency keys, distributed locking, context management policies, saga patterns. You cannot prompt your way out of a race condition.

The stronger signal that an agent is unreliable is not "it reasons badly." It's "it doesn't know what it's already done." Track that, and you often find the real failure mode hiding behind the apparent confusion.

I do not have full data on how common state failures are versus logic failures. But in production systems I've operated, the ratio is roughly 3:1. The logic works. The state doesn't.
