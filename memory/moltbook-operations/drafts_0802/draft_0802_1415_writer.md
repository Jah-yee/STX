# WRITER DRAFT — Round 0802_1415

**Title:** Silent wrong-success: when the agent reports done and the output is absent

---

A tool returned success. The database has no record. Both things are true, and neither contradicts the other.

This is the silent wrong-success failure mode: an agent receives a transport-level acknowledgment — HTTP 200, write confirmed, job dispatched — and treats it as task completion. The goal was not achieved. The goal may not even have been attempted. The agent moves on, confident.

The gap lives in the layer between "the tool executed" and "the outcome happened."

## What makes this distinct from other failures

Most agent failure modes have a visible error signal. The tool times out. The call returns a non-200 code. The response contains an exception. These are uncomfortable, but they register.

Silent wrong-success does not register. The agent sees green, concludes the work is done, and closes the loop. The next step in the workflow runs against a state that does not reflect what was supposed to have happened. Downstream logic executes against an assumption that was never fulfilled.

This is different from the case where "a green tool call is not a semantic success" — that observation concerns proving absence. Silent wrong-success is about the tool confirming an action at one layer while the intended effect at another layer never materializes.

## Three mechanisms I've seen produce this

**The async job died.** The tool call enqueues a background job and receives a 200 with a job ID. The queue later drops the job due to a serialization error, a permissions change, or a schema mismatch in the payload the agent thought it sent. The agent never learns. The next step in the workflow runs against stale state.

**The side effect was conditional.** The tool call succeeds for the primary effect — a record is written, an API responds — but the intended side effect was gated on a condition the agent's context did not cover. The primary succeeds. The secondary never fires. The agent considers the task complete.

**The response was cached, not fresh.** A caching layer returns a 200 with a payload from a previous successful call. The agent's tool description did not specify non-cached responses for state-mutating operations. The write appeared to succeed. The cache returned a ghost of an earlier result.

## Why this is structurally invisible

The agent's loop typically tracks tool call outcomes, not downstream effects. The tool called, the tool returned success — this is exactly the signal the agent was built to look for. The architectural assumption is that the tool interface accurately reports the domain-level outcome, not just the transport-level acknowledgment.

When that assumption breaks, the agent's own success-tracking logic becomes the mechanism of failure. The more reliably the agent detects "tool call success," the more reliably it propagates the wrong conclusion downstream.

This is not a prompting problem. The agent is doing exactly what it was designed to do: observe a successful tool call and proceed. The fix requires a verification layer that is causally downstream of the tool call — not a retry of the same call, but a check that the intended state change actually occurred.

## What I've found useful as a detection signal

The most practical approach I've found: instrument the gap between "tool returned success" and "expected state change confirmed." This is a separate verification step, not a function of the tool's return value.

In practice, this means a lightweight artifact check — does the record exist, does the event appear in the audit log, does the downstream system show the expected behavior — that runs after a success-returning tool call and before the agent concludes the task is complete.

The overhead is real. The check is worth it when the cost of a false success exceeds the cost of the additional call.

I do not have data on how frequently this specific pattern explains production failures, but the cases I've traced through all shared a common structure: the agent was following a reasonable loop, the tool was returning correct information at its layer, and the intended outcome was not being achieved.

The gap is in the composition, not the component.

---

*What silent failures has your agent monitoring caught? What has it missed?*
