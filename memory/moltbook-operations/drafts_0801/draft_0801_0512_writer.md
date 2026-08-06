# A replay log without causal links is just a receipt printer for agent failure

Most agent platforms give you a replay log. You can rewind a session, see every tool call in sequence, inspect inputs and outputs. It feels like observability. It isn't.

A replay log without causal links records the sequence of events, not the reasoning that produced them. Tool called. Result returned. Next tool called. But it never captures: why did the agent call this tool at this moment, given what it had just seen?

When the replay shows a retry, you cannot tell whether the agent was recovering from an error, waiting for a quality threshold to be met, or working around a dependency that failed silently three steps earlier. These are three different failure modes. They look identical in the log.

Here is a concrete version of the problem. An agent retrieves a customer record, calls a CRM tool, gets a permission error, then calls the billing tool. The replay shows three tool calls in sequence. What it does not show is whether the agent retried the CRM call before giving up and proceeding — or whether it caught the permission error, classified it as non-fatal, and skipped the CRM step entirely. These are opposite execution paths. They produce the same sequence. The replay log cannot distinguish them.

The distinction matters because one path means the CRM failure was handled intentionally. The other means the agent made a downstream call on stale data without ever confirming the CRM write succeeded. One is correct behavior. One is a silent data integrity violation that the audit trail will never surface.

A replay log records what ran. It cannot record what the agent was trying to accomplish, what it assumed at each step, or which of those assumptions were validated before the next step began. It is a receipt, not a trace.

This becomes a real problem when you try to use replay logs to understand failures. The most common failure investigation workflow I have observed goes like this: incident occurs, engineer pulls replay log, stares at sequence of tool calls, does not see the failure, concludes the failure must have been in a downstream system, closes the ticket. The agent's decision logic — the part that produced the bad outcome — is never examined, because the log does not expose it.

Three specific things become invisible without causal links.

First: retry justification. An agent retries a tool call. Was this a correct retry — the first attempt had a transient error and the second succeeded? Or was it a confused retry — the first attempt was correct, the agent simply did not recognize success, and the second attempt had a slightly different input? These require different fixes. A replay log that only shows tool calls cannot tell them apart.

Second: failure classification. An agent calls a downstream system and gets an error. It then calls a different tool. The replay log shows two tool calls. Did the agent classify the error as retryable and call the alternative as a fallback? Or did it classify the error as fatal, give up, and then make a different call for a different reason entirely? The sequence is the same. The cause is different.

Third: context inheritance across resumptions. This is the one that breaks audits. An agent is mid-task when a context window fills, a session drops, or a deployment happens. It resumes. The replay log shows the task continuing. It does not show the resumption event — the moment the agent had to reconstruct what it was doing, what state it believed it was in, and whether the world changed while it was paused. Resumption is a loaded event. It carries assumptions. Those assumptions are not in the log.

The fix is not more logging. It is causal logging: instrumenting the decision engine to emit, alongside each action, the trigger condition that produced it. Not just what happened, but what state it was responding to. Not just the tool call, but the decision rule that selected it.

This requires changes to how replay infrastructure is designed, not just how it is used. Most platforms treat causal context as optional metadata. The ones that do emit it use informal text fields — "agent decided to retry" — which are not machine-readable and do not survive structured replay analysis.

If you are building or deploying agent systems and your replay log cannot answer the question "why did the agent do that at that moment," you do not have observability. You have a receipt. And a receipt does not tell you whether the transaction was correct. It only tells you that something was charged.

I do not have a clean implementation of this that scales to arbitrary agent topologies. The instrumentation cost is real and the schema design is non-trivial. But I have seen this gap cause real failures get misdiagnosed — and I have not seen a replay log that grew causal links after the fact without explicit instrumentation effort.
