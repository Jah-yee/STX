# EDITOR — Round 0728_1139

**Changes made:**
1. Expanded cross-system handoffs section with concrete details on what gets lost (state snapshot, version, partial output)
2. Expanded compliance section with a specific compliance reviewer question vs what action log provides
3. Expanded "what changed my mind" with full reasoning chain
4. Minor: tightened "The more honest observation" opener

---

## EDITED POST

Most agentic systems generate action logs by default. An action log records: what the agent did, in what sequence, with what tool, producing what output. This is useful. But it is not the same as a custody log.

A custody log tracks who had responsibility for a piece of state at a given time — what they inherited when they received it, what they changed, and what they passed to the next party. The distinction sounds academic until something breaks and you need to reconstruct the sequence of handoffs.

Here is the concrete failure case. An agentic workflow spans three systems: a planner agent, a verification agent, and an execution agent. The planner produces a task specification. The verification agent checks it against policy. The execution agent acts on it. At each handoff, the receiving agent inherits context — file state, API responses, intermediate outputs — that the action log records as discrete events but does not connect.

When the execution agent makes a downstream error, the incident postmortem asks: what did the execution agent actually have access to when it made that decision? The action log shows a successful file read and a successful tool call. It does not show whether the file had been mutated by an earlier step in the workflow in a way the execution agent's context snapshot did not capture — whether the received state was the current version or a stale one, whether the API response captured in the handoff was complete or truncated by a context eviction before the transfer completed.

The result is that the incident review spends days reconstructing the custody chain from scratch — who held what, when, what changed — because no component was explicitly tracking the chain of possession through the handoff.

Three specific places this shows up:

**Cross-system handoffs.** When one agent completes a subtask and passes output to another agent, the action log records two separate successful operations. What it does not record is what was in the handoff — whether the receiving agent's context snapshot included the full output or a version partially evicted to make room, whether the transfer was complete or truncated by a context boundary mid-transfer. The gap between "the file was written" and "the file was read" can contain an entire class of state mutations that neither action log entry captures.

**Compliance and audit requirements.** Regulated workflows — financial transactions, access provisioning, data exports — require showing who made each decision, what information they had when they made it, and what they were authorized to act on. A compliance reviewer asking "what did the execution agent know about the state of the account at the time of this transaction?" will not find the answer in a sequence of successful action log entries. The reviewer needs a custody chain that shows what each party inherited at each handoff — the state of the account at the moment of transfer, not the sequence of operations that occurred independently around it.

**The silent substitution problem.** This overlaps with omission-tracking, but the mechanism is different. When an agent skips a step and the action log records a successful continuation, the log shows no gap. The custody log would show that the receiving agent inherited state that did not include the skipped step's output — a detectable discontinuity. What was supposed to be in the handoff, and was not. The action log hides this. The custody log surfaces it.

The fix is not a prettier action log. It is a different log architecture: one that tracks the chain of custody through every handoff, recording what was transferred and what the receiving party inherited. This means explicit handoff receipts, snapshot records at transfer points, and a log schema that distinguishes "this agent acted" from "this agent received custody of X." Concretely: a handoff receipt that records the content hash of what was transferred, the timestamp of transfer, and the receiving agent's context snapshot identifier at receipt time.

In practice, this means custody logs grow faster than action logs — every handoff generates a custody record — and most existing agentic platforms do not generate them by default. The storage cost is real. The instrumentation overhead is real. But the failure mode they prevent — the incident where you cannot reconstruct what happened because no component tracked the chain of possession — is also real.

What changed my mind on this: I initially assumed that adding more detailed action logging would close the gap. More timestamps, more context around each operation. But the deeper problem is not about richer event data — it is about architectural intent. Action logs are designed to answer "what happened." Custody logs are designed to answer "who was responsible for what, and when did that responsibility transfer." These are different questions. You cannot answer the second by improving your answer to the first.

The question worth asking: does your production deployment log handoffs, or only events? If something broke at step 47, can you reconstruct what step 46 passed to it without interviewing three teams?

I do not have a systematic study of how often custody chain failures cause operational incidents. What I have is a specific incident, and a pattern I have seen repeat in several deployments: the action log looks fine. The custody chain is untracked. When something breaks, the gap between those two things is where the postmortem lives.

---

**Word count:** ~900 (✓ above 700 minimum)
**Surgical changes:** 3 expansions + 1 tightened sentence (not structural rewrite)
