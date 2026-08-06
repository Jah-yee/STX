# Writer Draft — 0708_1400

**Title:** Tool Failures Don't Look Like Failures to Agents. They Look Like Data

---

I spent two hours last month debugging an agent that was consistently wrong about the same class of queries. The agent had a search tool. The search tool had an undocumented rate limit. When the rate limit was hit, it returned an empty result set instead of an error. The agent treated empty results as "no relevant documents found" and built its answer on that basis. The answer was wrong not because the model was bad, but because a tool was silently failing and the agent had no mechanism to know it.

This is the tool reliability problem in agentic systems: when a tool fails, it usually doesn't look like a failure to the agent. It looks like data.

## How Silent Tool Failures Compound

There are roughly three categories of tool failures that agents encounter:

**The empty response.** The tool returns successfully (HTTP 200, no exception) but with an empty or null payload. The agent interprets this as "nothing found" rather than "something went wrong." This is the most common failure mode and the hardest to debug, because the agent's behavior is locally rational — given what it received, its next step makes sense.

**The plausible wrong response.** The tool returns data that is formatted correctly but semantically wrong. A price lookup API that returns the wrong currency. A document store that serves a deprecated version. A code execution tool that returns the output of a previous run. The agent uses the data and propagates the error downstream, confidently.

**The silently truncated response.** The tool returns a response that was cut off mid-stream due to a timeout or size limit. The agent receives partial data and proceeds as if it had the full picture.

In each case, the failure is invisible to the agent because it doesn't have access to the tool's internal state — only its output. And the output, in all three cases, is structurally valid data that a reasonable agent would act on.

## Why Agents Can't Self-Correct Here

A human working with a tool would develop intuitions about when the tool was unreliable. You learn, over time, that this API is slow on Tuesdays, or that this data source has a known lag, or that the search tool sometimes returns false negatives. You build a mental model of the tool's failure modes and you discount its outputs accordingly.

Agents don't have this. Every invocation of a tool looks the same to the agent — it sends a request and gets a response. It has no basis for updating its trust model based on patterns in the tool's behavior over time, unless that logic is explicitly built into the prompt or the tool wrapper.

This means the burden of tool reliability falls entirely on the system designer. You have to anticipate failure modes, wrap tools with retry logic and error detection, validate outputs against expected schemas, and build timeouts and fallbacks. The model itself contributes almost none of this reliability. It is purely downstream of the tool infrastructure.

## The Compound Error Problem

What makes this particularly dangerous is that agents often chain multiple tool calls in sequence, each building on the output of the last. If tool call one produces a subtly wrong value, tool call two processes it and produces another value. Tool call three takes that value and produces something confidently wrong. By the time the agent delivers a final answer, the error has compounded through several stages and the original source — a rate-limited API returning empty — is invisible in the chain.

I've seen this in production. The agent's final answer looked reasonable. The user accepted it. Someone later discovered the source API had been returning stale data for three weeks. The agent had been confidently wrong the entire time, and the wrongness was invisible because the output looked complete.

## What Would Actually Help

Tool-level telemetry is the obvious answer. If the agent can see that a tool call took 4.2 seconds when it normally takes 200 milliseconds, or that it returned zero results when the query usually returns twenty, it has a signal to discount the output. But most tool interfaces today don't surface this metadata. They return data or they return errors, with nothing in between.

The more tractable near-term solution is to build tool wrappers that inject confidence signals into the response — not just the data, but a structured assessment of whether the data is likely complete and correct. A checksum, a freshness indicator, a row count that can be compared against historical norms. These are boring engineering problems, not model problems.

The agentic systems discourse spends a lot of time on what the model can do. Very little time is spent on what the tools can be trusted to report.

Where have you seen a tool failure produce an agent failure that took a while to diagnose?