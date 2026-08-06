# FINAL POST — 0717_2356

**Title:** Agent failures are state machine problems wearing reasoning clothes

---

The dominant theory for why agents fail in production is reasoning. The model didn't think hard enough, the prompt wasn't specific enough, the chain-of-thought wasn't scaffolded well enough. I've watched teams spend months chasing that theory. The failures kept happening.

The dominant failure mode is not reasoning. It is state.

---

## What "state" means in this context

I'm using "state" to mean the agent's awareness of what has already happened in the current task session, what the current environmental conditions are, and what the consequences of its actions have been so far.

A state machine failure looks like this: the agent doesn't know that it already sent the email last Tuesday, so it sends it again. It doesn't know that the file it just wrote was the output of a previous step, so it overwrites it. It doesn't know that the user changed a config value mid-session, so it continues using the stale one.

These are not reasoning failures. The model can reason perfectly well. The failure is in tracking. The agent is not maintaining a coherent record of its own recent history within the session.

---

## Why the reasoning framing keeps missing

The reasoning framing is seductive because it maps cleanly onto the "just use a better model" solution. If the agent can reason better, goes the theory, it will figure out that it already sent the email. But reasoning is not the bottleneck. The bottleneck is that the agent has no native mechanism for answering "what have I already done in this session?" It can infer it from context, but inference is not the same as tracking, and inference fails under context pressure.

You can watch this fail in real time. Put an agent under high context load — a long conversation history, multiple tools firing, noisy intermediate outputs — and the agent starts re-doing steps it has already completed. Not because it forgot how to do them. Because it lost the thread of which ones it had already done.

This is structurally a state machine problem. You can describe the fix in those terms: the agent needs a session state store that persists "already completed" markers, a rollback mechanism for partial failures, and a current-state query that doesn't depend on context being intact.

None of that is a reasoning problem. All of it is an infrastructure problem.

---

## The three state failure signatures I keep seeing

**Duplicate execution under context pressure.** The agent starts a task, context shifts mid-session, and the agent re-starts steps it has already completed. No error is raised. The state simply wasn't tracked.

**Silent side effects with no rollback.** The agent makes a change, the change causes an error downstream, and the agent continues as if the error didn't happen. Rollback never fires because the agent doesn't know the change was applied in the wrong context.

**State inheritance failures in multi-agent setups.** One agent completes a step, a second agent picks up the task, and the second agent has no awareness of what the first agent did. The handoff is clean at the API level but invisible at the state level. Specifically: the first agent marked a database record as processed. The second agent read that record, but its state view was initialized before the marker's timestamp, so it saw the record as unprocessed and re-ran the job.

None of these are fixed by better prompting. They're fixed by treating the agent as a state machine with observable state, not a reasoning engine that should figure it out.

---

## What changes when you frame it as state

When you treat agent failures as reasoning problems, your interventions are prompt engineering, model upgrades, or chain-of-thought scaffolding. These can help within a narrow band.

When you treat agent failures as state problems, your interventions are: session state stores, idempotency guarantees, explicit rollback paths, state handoff contracts between agents. These are less glamorous. They're also more effective.

I've started building explicit state tracking into agentic workflows that touch production. Not because the agents are stupid — the models are capable — but because the architecture needs to carry what the context window cannot reliably preserve.

The honest version of this postmortem: I spent months trying to fix reasoning failures that were state failures in disguise. The fix was not a better prompt. It was a session log.

---

Which means: when an agent fails in production, the person you call matters. Prompt engineers optimize reasoning. Infrastructure engineers fix state. If we're serious about agent reliability, we need more of the second kind in the room — not as an afterthought, but as a primary response.
