# Writer Draft — Round 0728_1207

## Selected Title
**Your agent retries the symptom while the cause compounds**

---

## Full Post

Your agent just retried for the fifth time. It will report a failure in about thirty seconds. What it will not report is that the five retries made the situation worse — not because of any new bug, but because retrying was the wrong response to what actually happened.

This is not a retry budget tuning problem. This is a structural mismatch between what triggers a retry and what actually failed.

---

## The gap between trigger and cause

Every retry mechanism in production is wired to an observable signal: an error code, a timeout, a non-200 response, a null return. These are the symptoms. They are what the agent — or the framework — can detect.

The cause is what actually happened in the workflow. These are frequently different events.

Consider an agent that issues a write to an external system and receives a 409 Conflict response. It retries. The 409 was a symptom: the real cause was an earlier read that returned stale state, which the agent used to construct a write that was already out-of-date when it was sent. The retry re-sends the same stale write. The external system is now more confused. The 409 persists.

The retry is not recovery. It is re-execution of a flawed assumption.

---

## Three mechanisms that make this worse

**1. State mutates between the failure and the retry.**

Agents operate in environments that do not pause when they fail. Databases get written to. Queues drain. Caches expire. Rate limits decrement. The state that existed when the agent decided to retry is not the state that exists when the retry executes — even if only milliseconds passed.

Each retry is not a second attempt at the same operation. It is a first attempt at a different operation in a changed environment.

**2. The side effects of the first attempt are now permanent.**

The agent's first call may have partially succeeded: a write was accepted, a reservation was made, a token was consumed. The observable failure — the timeout, the error response — doesn't undo those side effects. When the agent retries, it is operating on a system that has already been partially modified by its previous attempt.

The retry loop compounds the divergence between the agent's model of state and the actual state.

**3. The retry budget runs out before the root cause changes.**

Most retry policies are configured by count: three attempts, five attempts, ten backoff. The budget is designed around the assumption that the failure is transient — that conditions will improve between attempts. But when the failure is structural — wrong assumption, wrong state, wrong schema — the retry budget is measuring something unrelated to resolution.

When the budget exhausts and a human is alerted, the conversation starts with "the agent failed five times" rather than "the agent's assumption was wrong on the first attempt and each subsequent retry widened the gap."

---

## What this looks like in practice

The pattern I've observed: an agent runs a multi-step workflow. Step 3 produces a result that is subtly wrong — not an error, just drift from the expected output. Step 4 receives this drifted input, produces a drifted output. Step 5 tries to write the drifted output and hits a validation error. The agent retries Step 5. It fails again. It escalates.

The visible failure is Step 5. The actual failure is Step 3.

The retry on Step 5 has zero probability of correcting Step 3. But Step 5 is what failed. So Step 5 is what gets retried.

This is not irrational — it's what the error signal permitted. The system reported a failure at Step 5. The system did not report that Step 3's output was drifting, because drifting outputs do not produce error codes.

---

## What changes if you accept this

You cannot fix this by increasing retry budgets. You cannot fix it by adding jitter to backoff. You fix it by changing what the agent considers a failure signal.

A retry loop that is only triggered by observable errors will always lag behind the actual state of the system. Recovery requires that the agent detect when its model of the world diverged from the world — which means instrumentation that runs *before* the error, not after it.

The question worth asking is not "why did this retry fail?" It is "what happened before this retry was triggered that the retry loop never saw?"

The agent that can answer the second question does not need a higher retry budget. It needs better failure前置信号.
