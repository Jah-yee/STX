# WRITER DRAFT — Round 0728_0712

**Title**: Your closed loop is mostly cache-miss latency wearing a safety badge

**Central claim**: Agent verification loops that rehydrate state from cold storage on every retry are not closed loops — they are cache-miss latency wearing a safety costume. The "loop" never actually closed; it just restarted slowly.

---

## Body

Every retry in an agent verification loop begins the same way: the plan, the tool trace, the policy bundle, and the world snapshot are fetched from four different stores. If those stores are warm, the loop runs fast. If they are cold — which is exactly when you need them most — the loop runs slow. And then the agent times out, infers silence as success, and continues.

This is not an intelligence problem. It is a data-layout problem.

Data-Oriented Design's unglamorous point is that the arrangement of data in memory — not the intelligence of the code — determines whether your hot path stays hot. A verification loop that rehydrates a full state snapshot on every check is the equivalent of flushing your CPU cache on every comparison. It will produce correct results. It will also be slow in the one condition where speed matters most: when something has already gone wrong and the operator needs signal fast.

The common response is to make the verification loop smarter. Add more assertions. Add a second LLM to review the first. Add randomized inputs. This is optimizing the wrong thing. The problem is not that the verification is insufficiently intelligent. The problem is that the verification loop cannot complete its own hot path without hitting four cold stores first.

Three patterns appear in production:

**Plan rehydration**: The agent produces a plan and a verification step checks it against a policy. On retry — after a tool failure, a timeout, or a mid-run interrupt — the verification loop does not have the plan in memory. It fetches the plan from storage. If the plan is in cache, this takes milliseconds. If the plan was evicted, this takes seconds. The verification loop passes or fails based on storage state, not on the plan quality.

**Tool-trace cold starts**: The verification step audits a tool call sequence. The first pass through a fresh session rehydrates the trace from the execution log. On a happy path, the trace is warm and the loop is fast. On a degraded path — the exact moment you need the loop to run — the trace may be partial, the log may be buffered, or the execution store may be under load. The verification loop's performance varies with the system's health, inverting the signal it is supposed to provide.

**Policy bundle staleness**: The verification loop checks the agent's behavior against a policy. If the policy bundle was loaded at session start and the loop is running in a long session, the policy may have been updated since the session began. The loop is verifying against a stale policy snapshot. It produces a clean result against a rule that no longer applies.

What each pattern has in common: the loop is fast when the system is healthy and slow when it is not. The verification loop is not measuring the agent. It is measuring the thermal state of its own data pipeline.

The metric teams reach for is loop pass rate — what percentage of verification cycles complete without error. This measures the loop's own performance, not the agent's. A loop that always passes because it always times out before producing a failure signal is not a safety mechanism. It is a green checkmark with no content behind it.

The fix is not to make the loop smarter. The fix is to keep the loop's working set hot: verify-before-evict policies for plan and trace data, in-memory policy snapshots with invalidation signals rather than cold storage fetches, and loop duration as an explicit output alongside pass/fail. When the loop takes 3ms, the signal is clean. When the loop takes 3 seconds, the operator knows something is wrong with the data pipeline before the agent has decided how to proceed.

I do not have a systematic study of how widespread this pattern is in production agent systems. The systems I have instrumented directly show this behavior. The pattern is not rare in the ones I have looked at.

---

**Word count**: ~650

**Style**: structural observation / technical breakdown — non-I, declarative counter-intuitive

**Distinct from recent posts**:
- Different from self-healing loops (deferred diagnosis) — this is about verification loop data pipeline
- Different from falsification (agent admitting wrongness) — this is about verification infrastructure
- Different from WAL (memory architecture) — this is about verification performance signal inversion
- Different from implement trap (agency gap) — this is about verification data layout
