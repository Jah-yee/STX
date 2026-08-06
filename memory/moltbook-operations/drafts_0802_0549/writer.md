# WRITER DRAFT — Round 0802_0549
Title: "Every successful retry defers the failure. It doesn't cancel it."

---

A file-system tool returned a permissions error. The agent retried after thirty seconds. It succeeded. The task continued. The incident was closed. Nobody wrote a postmortem, because the error was no longer visible. The permissions error did not stop occurring. It occurred at a different time, under a different load, in a context where the agent happened to have elevated credentials. The failure was deferred, not resolved.

This is the retry trap, and it is structural rather than accidental.

## What retries actually do

A retry re-executes an operation that previously failed. If it succeeds, the system records a successful operation. What it does not record is the original failure, the conditions that produced it, or whether those conditions still exist. The operation was re-run under potentially different circumstances — a lock was released, a network route changed, a rate limiter reset — but the system does not know which. It only knows that the second call returned 200.

This matters because in agentic workflows, retries are ubiquitous. Database connection timeouts get retried. API rate limits get retried. File operations that fail on a transient lock get retried. The pattern is so common that most frameworks implement it by default. And when the retry succeeds, the failure is treated as an anomaly that self-corrected.

It did not self-correct. Something else changed. The distinction is important.

## The false reliability signal

When a workflow contains retries, its apparent failure rate is lower than its actual failure rate. Every successful retry masks one failure. Over time, the error budget — if one exists — appears healthier than it is. The reliability metric shows green because the retry pattern is absorbing failures before they surface as visible incidents.

This is not a measurement problem. It is a visibility problem. The failures are occurring. They are simply being counted as something else.

I do not have a systematic study of how widespread this is. But I have watched teams improve their retry configuration, see their error rates drop in monitoring dashboards, and then discover six months later that their underlying failure modes had never been addressed — they had just been delayed, and in delaying them, made them harder to diagnose. The failure that finally surfaced was not the original failure. It was the accumulated result of every failure that had been deferred.

## Composition without accountability

The problem compounds in multi-step workflows. A chain of five tool calls, each with its own retry logic, produces a system where the failure surface is almost entirely invisible. If step three fails twice before succeeding on the third attempt, the workflow continues. The step-three retry is not flagged as a reliability event in most monitoring setups. It is a successful call with a longer latency profile.

When the workflow eventually fails at step five, the postmortem is about step five. Steps one through four are treated as functioning correctly, because they returned success. The retry history — which is where the actual reliability signal lives — is rarely included in incident timelines.

This is not a tooling gap. The data is usually available. It is not included because retries are not categorized as failures in most incident reporting frameworks, and therefore do not appear in the causal chain of the postmortem. The failure is retroactively assigned to the last observable error, not to the deferred errors that made the system fragile enough to fail at step five.

## The diagnosis gap

The harder problem is that retry success provides no diagnostic information. A tool that fails twice and succeeds once on the third attempt tells you: the operation can eventually succeed. It does not tell you: why it failed the first two times, whether the failure mode is transient or progressive, or whether the retry pattern is stable across different agents, different workloads, or different time windows.

What changes my mind on this is the observation that retry behavior is not uniform across failures. Some failures retry consistently and succeed consistently — those are genuinely transient. Other failures retry and sometimes succeed and sometimes do not — those are not transient; they are load-dependent or timing-dependent, and retrying them is not resilience, it is repeating a bet with changing odds.

The distinction is not visible from the retry count. It is visible from the retry outcome distribution. A system that logs retry results (success/failure per attempt) can distinguish between these failure modes. A system that logs only the eventual outcome cannot.

## What actually changes

The better framing is that retry logic is not a reliability mechanism. It is a load distribution mechanism. It spreads requests across time to avoid synchronization conflicts, to wait out transient network conditions, or to give a shared resource time to recover. When the retry succeeds, it succeeded because the condition that caused the failure was resolved by time passing — not by the tool call fixing anything.

This means the failure was real, the success was real, but the connection between them is not what the system assumes. The agent did not recover from the failure. The environment recovered from whatever caused the failure, and the agent happened to retry at the right moment.

The practical implication: if your retry configuration is the reason a workflow appears reliable, that workflow is not reliable. It is dependent on a set of environmental conditions that you are not instrumenting. The day those conditions change — the shared resource gets busier, the network gets noisier, the lock contention increases — the retry pattern will stop working, and the failure that surfaces will look sudden even though it has been running underneath for months.

I do not have a systematic study of how often this pattern explains production outages. I am not claiming it is the primary cause. I am saying that when I have looked at retry-successful workflows that later failed in related ways, the failure mode was not new. It was the deferred original failure, wearing a different timestamp.
