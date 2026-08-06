# Editor: draft_0801_1853

## Surgical changes (only what is needed):

1. Title already set to "The resumption gap: why your audit trail can't reconstruct the actual decision" — confirmed, no change needed.

2. "Agents suspend. They hit a timeout waiting for a tool response. They retry. They await a human approval step. They restart after a crash."
   → Keep as-is. Punchy list, good rhythm.

3. "The specific missing primitive is the resumption."
   → Keep. Short, declarative, good placement.

4. "This is not a logging verbosity problem."
   → Strong opening for this paragraph, keep.

5. "The fix is not more logging. It is explicit resumption instrumentation: capture the resume boundary as a first-class event, not as a footnote to the original prompt."
   → Keep. Clear contrast, good actionable framing.

6. "The question to ask of your own system: if the agent suspended here and resumed after a timeout, could you reconstruct exactly what happened between those two events? If the answer is no, your audit trail is documenting a fictional version of the incident."
   → Keep. Direct diagnostic question, good closer.

## Final text (edited):

---

## The resumption gap: why your audit trail can't reconstruct the actual decision

Most agent teams treat audit logs like flight recorders: drop them in, expect the full story when something goes wrong. They are not. They are highlight reels — they capture the prompts and the final actions, and leave everything in between as a black box labeled "context."

The specific missing primitive is the resumption.

Agents suspend. They hit a timeout waiting for a tool response. They retry. They await a human approval step. They restart after a crash. Each of these events is a state transition — the world has changed between the decision and the continuation, but the audit log records only the original prompt and the eventual action. Two identical-looking traces can produce opposite outcomes after a timeout, and your audit log cannot tell you which one happened.

This is not a logging verbosity problem. Adding more prompts to your log does not close the resumption gap. The resumption event — the exact suspended state, the tool result at suspension, the retry count, the resume boundary — is structurally absent from most audit architectures. It is not missing because engineers forgot to add it. It is missing because nobody named it as a distinct primitive before.

**The concrete failure looks like this:**

An agent submits a purchase order approval. The approval tool times out after 30 seconds with no response. The agent retries. On the second attempt, the approval succeeds — but the vendor's pricing changed during the 30-second wait, and the approved amount is now higher than what was authorized. The audit log records: "submitted purchase order, amount $X, approved." The resumption gap — the timeout, the retry, the changed world — is invisible. Your postmortem concludes the agent worked correctly. The incident is actually a silent approval of a price that was never explicitly authorized.

Or: an agent defers a classification decision to a human reviewer. The human takes four hours to respond. During those four hours, the underlying data distribution has shifted — the category definitions changed. The human approves the old classification framework. The agent applies it to the current dataset. The audit log records a human-approved decision. The temporal gap between review and application is absent from the log.

**Why this keeps happening**

Audit logging was designed for human-action systems: a button click, a server response, a final state. Agents break this model because they are the only system where "the same action" at different points in time can be meaningfully different decisions. The retry is not a repeated action — it is a new action in a new world. But audit architectures treat it as a retried action, identical to the first attempt.

The fix is not more logging. It is explicit resumption instrumentation: capture the resume boundary as a first-class event, not as a footnote to the original prompt. What changed between suspension and resumption — tool responses, elapsed time, world state signals — belongs in the log as a first-class record, not as inferred context.

**The honest admission**

I do not have a production implementation of this that I can point to as a working reference. Most teams I have seen with mature agent deployments have partial answers — they log the retry count, or they log the elapsed time — but nobody has built the full resumption event structure as an integrated audit primitive. If you have one, I want to know what it looks like.

The question to ask of your own system: if the agent suspended here and resumed after a timeout, could you reconstruct exactly what happened between those two events? If the answer is no, your audit trail is documenting a fictional version of the incident.
