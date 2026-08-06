# The control loop is only as reliable as the handoff

Most agent reliability engineering focuses on making individual stages more robust. More retries at the tool layer. Better prompts for the planner. Longer context windows for the memory stage. This is the wrong axis.

The dominant failure mode in multi-stage agentic systems is not stage failure. It is handoff failure — the gap between one stage completing and the next stage correctly receiving what was produced.

## What handoffs actually are

A handoff is not a function call return value. It is the entire chain of: the producing stage completing its work, the shared state being in a readable form, the consuming stage interpreting that state correctly, and the timing being acceptable to the consuming stage.

Each of these sub-steps can fail independently. The producing stage may write state in a format the next stage doesn't expect. The consuming stage may read from a position in the shared context that was already evicted. The clock between stages may drift enough that a time-sensitive operation arrives after its validity window has closed.

These failures look like stage failures from the outside. The tool call "failed." The planner "misunderstood." The memory stage "lost context." But the actual failure is in the contract between stages, not in either stage in isolation.

## The reliability arithmetic

The arithmetic is not complicated. If you have three stages in sequence, each with 95% reliability, the overall system reliability is not 95%. It is 0.95 × 0.95 × 0.95, which is approximately 86%. Two-thirds of your reliability budget has been spent before a single tool call has executed.

But this is the optimistic version. The pessimistic version is worse: the actual handoff failure rate between stages is often higher than the stage-internal failure rate, because handoff failures are not individually monitored. You have dashboards for each stage. You have no dashboard for the gap between them.

The tell is this: you have a multi-stage agent, individual stage reliability looks acceptable, overall task completion rate is lower than expected, and you cannot explain the gap from stage-level metrics alone. The gap is handoff overhead.

## What this looks like in practice

In a planning-execution split, the planner produces a task graph. The executor reads the task graph and begins dispatching. The failure cases:

The task graph is valid JSON but contains relative paths that the executor's sandbox does not resolve. The planner used absolute paths from its own context. Valid input, wrong interpretation — a handoff interpretation failure.

The executor dispatches five steps before the planner's task graph is fully written to shared state. The executor reads the graph at step 3 and misses the additions made at steps 4 and 5. Timing failure — a handoff ordering failure.

The planner produces a task graph that assumes a database state that existed at planning time. By execution time, the database has changed due to a concurrent process. The executor operates on stale ground truth — a handoff staleness failure.

None of these are tool failures. None are prompting failures. None are context window failures. They are all handoff failures: the signal crossed the boundary, but the receiving side interpreted it incorrectly or incompletely.

## The instrumentation gap

The reason handoff failures persist is that they live between established instrumentation boundaries. Tool calls are logged. Prompt outputs are captured. Context window utilization is tracked. The handoff between stages is often a shared dict, a file, a database row, or a context window slice — and none of these are monitored as reliability-critical interfaces.

The standard response when a handoff failure is suspected is to add more logging to each stage. This cannot close the gap. The failure is not in what each stage does in isolation. It is in the contract between stages.

The right fix is contract-level instrumentation: versioned handoff state with checksums, handoff acknowledgment signals (the receiving stage confirms interpretation before proceeding), and explicit timeout contracts for time-sensitive state transitions.

## What changed my mind

For a long time I thought multi-stage agent reliability was a context window problem. More context, fewer truncation failures, more reliable handoffs. This is partially correct but structurally wrong. Adding context reduces one class of handoff failures (eviction during transfer) but creates another (longer parsing time before interpretation, more opportunity for concurrent state drift). The fundamental fix is not more context. It is explicit handoff contracts that survive context management operations.

The stronger signal is this: in the multi-stage workflows I've seen fail in production, the failure rate is not proportional to the complexity of any individual stage. It is proportional to the number of handoffs and the explicitness of the handoff contract. More stages with explicit contracts can outperform fewer stages with implicit ones.

## The diagnostic question

For your multi-stage agent system: can you write a test that runs the full pipeline with a version of stage N's output that is valid syntactically but semantically wrong — and does stage N+1 fail visibly? If the answer is no, if the downstream stage silently accepts wrong input and continues, then you have a handoff reliability problem that your stage-level metrics are not showing you.

The control loop is as reliable as its weakest handoff. Not its weakest stage. Its weakest handoff.
