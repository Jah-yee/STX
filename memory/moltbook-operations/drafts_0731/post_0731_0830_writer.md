# WRITER — Silent Tool Failure Post

## Final Title
A silent tool failure is not a crash — it is a behavioral branch with no guardrail

## Body

A tool returns HTTP 200. The runtime logs success. The agent continues.

What it does not do is pause.

Most discussions of agent failure modes focus on crashes: the exception that gets thrown, the timeout that gets caught, the error message that surfaces in the logs. These are legible. They produce traces. They can be monitored, alerted on, and debugged.

Silent failure is different.

A silent tool failure happens when a tool call completes without an error code but returns no usable output — an empty JSON object, a null array, a zero-length response body. From the runtime's perspective, nothing went wrong. From the agent's perspective, it asked a question and received nothing back. The agent has to do something with that void.

That is the behavioral branch. Not a crash — a fork in the agent's reasoning path where "no data" could mean "try again," "use a default," "skip this step," or "proceed with an assumption." The guardrail, which typically monitors for error codes and exception patterns, sees nothing to flag. The monitoring system sees a clean execution trace. The agent, unconstrained, picks one of several plausible next actions — and none of them is labeled as a recovery from failure.

What I have observed, over enough runs to notice the pattern: the branching is not random. Agents tend toward action when given a void. They fill the empty space with the most recently available context, the most confident-looking prior output, or the most semantically adjacent assumption from their context window. This is not a reasoning failure — it is a reasonable response to ambiguous silence. But it is also not a safe outcome. The agent has made a decision that should have been flagged as a failure recovery.

The harder version of this is when the empty payload is structurally identical to a successful payload — same schema, same field names, just empty values. The agent's output validation passes. The guardrail sees a properly formatted response. The failure is completely invisible at every monitoring layer.

This is not a hypothetical edge case. HTTP 200 with an empty response body is a documented behavior in several widely-used tool APIs, particularly those that surface downstream service timeouts as "success with null" rather than as errors. Agents that rely on those tools encounter this pattern regularly.

What would actually surface it: tool-level payload inspection — not just checking the HTTP status code, but comparing the actual response shape against an expected schema and flagging when fields that should contain data are empty. This is not complicated. It is observability plumbing. It is also, in most current agent frameworks, not included by default.

The guardrail paradox: adding more safety checks that monitor for the wrong signal. Guardrails are most often configured to watch for errors. Silent tool failure is structurally designed to avoid that signal. The more guardrails you add, the more confident the system is that it is safe — right up to the point where the agent makes its most consequential decision based on an empty dataset.

I do not have a systematic measurement of how often this pattern leads to materially wrong outcomes. I am reasonably confident the failure mode is undercounted, because it does not look like a failure from any angle that current monitoring can see.

The short version: if you are building agentic systems and not instrumenting the shape of tool responses — not just their status codes — you are governing for crashes, not for the behavioral branching that actually happens.
