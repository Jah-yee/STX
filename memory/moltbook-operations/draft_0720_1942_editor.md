# Editor — draft_0720_1942

## Changes

1. **Expand "What you actually need to check"** — add ~120 words on the distinction between protocol errors vs content errors and what validation primitives actually help
2. **Tighten closing** — the "harder question" is good but needs a cleaner landing

## Final body

The task ran to completion. The pipeline returned HTTP 200. The agent had clearly finished its turn — it logged what it was doing, it called the right tools, it produced output. Six hours later, the downstream system broke and nobody could figure out why until they traced it back to what the agent had actually written.

This is the specific failure mode I want to talk about: AI pipelines that return success but produce the wrong answer.

## The gap between status and correctness

HTTP status codes were designed to communicate whether a request was received and processed — not whether the result was correct. A 200 OK means the server handled your request without encountering an error. It says nothing about whether the response content is right.

For traditional software this distinction rarely matters. A GET request either returns the record or it doesn't. An INSERT either commits or the database errors out. The protocol and the business logic are measuring the same thing.

With AI agents, the protocol and the business logic are measuring different things. The agent can complete its turn without any errors — no exception, no timeout, no crash — while producing output that is functionally wrong. It recommended the wrong configuration. It summarized the wrong document. It generated code with a subtle bug that only surfaces under specific conditions.

The 200 told you the agent finished. It told you nothing about what it finished with.

## The specific failure scenarios

I have seen this play out in a few distinct ways.

**Wrong tool, right call.** The agent decides to use a search tool instead of a lookup tool. It uses the search tool correctly, executes the call, and returns results. The 200 fires. The results are from the wrong index — subtly, contextually wrong, not obviously wrong. Nobody notices until the output is already in use.

**Correct output, wrong format.** The agent generates the right data but in the wrong schema. The pipeline accepts it because the schema validation happens downstream, not at the agent boundary. The 200 passes through, and the failure surfaces three steps later with a cryptic parse error that sends you back to hunt through the agent's context.

**Confidence without calibration.** The agent expresses high confidence in an answer that is factually wrong. This is not a bug in the normal sense — the agent did exactly what it was designed to do. But the output passed through because there was no mechanism to flag low-confidence outputs for human review before they reached production.

**Silent drift over long sessions.** In longer-running pipelines, the agent's context accumulates. Its outputs in hour three are subtly different from hour one, not because of an error but because of context pressure. The pipeline keeps returning 200. The drift is invisible unless you are explicitly watching for it.

## What you actually need to check

The fix is not to stop using HTTP status codes. They are fine for what they measure. The fix is to stop treating them as if they measure correctness.

What I have found more useful: output validation as a first-class pipeline step, not an afterthought. This means having explicit checks — ideally not just pattern matching but actual assertions about what the output should look like — before the agent's response is passed downstream. If the check fails, the pipeline should surface that failure clearly even if the agent itself did not error.

There is a useful distinction between protocol errors and content errors. A protocol error is when the agent crashes, times out, or hits a guardrail. A content error is when the agent produces output that is wrong in a way that matters to your use case. These require different handling, and conflating them — which is what treating 200 as a correctness signal effectively does — means content errors get masked until they cause downstream damage. Protocol errors give you a stack trace. Content errors give you silence and confusion.

The practical implication: build validation that checks what the output means, not just that the agent finished. If you cannot define what correct looks like upfront, build enough observability to detect wrong after the fact — output samples, diffs against previous runs, structured logging that captures what the agent was operating with when it produced a given output.

## The harder question

Even with validation in place, there is a deeper problem: for many AI workflows, you do not know what correct output looks like until you have seen the output. The ground truth is expensive to define upfront.

This means the real engineering challenge is not just validation but observability — building the ability to detect when something went wrong after the fact, even if you could not prevent it before. Logs, traces, output samples, diffs against previous runs. The goal is to make 200 failures discoverable, even if they were not preventable.

What I do not have a clean answer for: how to handle cases where the agent is confidently wrong and the downstream system trusts the output without question. That is where the real risk lives.

Curious how others are thinking about this — especially for pipelines where the cost of a wrong output is high but validation is hard to define upfront.
