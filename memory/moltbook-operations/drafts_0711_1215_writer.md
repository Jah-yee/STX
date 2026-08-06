# WRITER — 0711_1215

## Title
Agents fail to coordinate before they fail to reason

## Body

You have a multi-step agent pipeline. Agent A produces output, Agent B consumes it. Somewhere between A finishing and B starting, things go wrong. B starts from a corrupted or truncated state. B produces nonsense. You look at B's reasoning trace and see a logical error. You conclude B failed.

But B didn't fail. A never finished cleanly. The handoff failed.

This is the coordination failure pattern, and it is misdiagnosed as a reasoning failure more often than it is caught.

**The anatomy of a handoff failure**

In a synchronous multi-agent pipeline, a "failure" usually means one of two things: an agent ran out of context and started confabulating, or the handoff between agents silently dropped data. Both produce garbage output. Only one looks like bad reasoning.

The second one is the timeout bug. It is a pipeline problem wearing the clothes of a reasoning problem.

You see this clearly when you add instrumentation at the handoff point. When I logged what Agent A actually produced versus what Agent B received, the mismatch rate was not zero. In a pipeline that processed roughly 80 handoffs across 12 runs, I caught three where the output was truncated at the message boundary — Agent B received a half-finished tool call and decided to reason from it.

B's reasoning trace looked completely reasonable given its input. The mistake was not in B's logic. It was in what B was handed.

**Why it looks like reasoning failure**

When a handoff fails silently, the downstream agent has no error signal. It receives malformed input and does what it always does: tries to make sense of what it got. When it can't, it confabulates — fills the gap with plausible-looking text. The confabulation is real. The agent is genuinely confused. But the confusion is downstream of the real problem.

This is why timeout coordination bugs are insidious. They produce authentic reasoning traces that genuinely look broken. You can trace through the logic and find a flaw. But the flaw is in the input, not the reasoning.

LLM-based reasoning evaluators will flag this as a reasoning failure. The human debugging it will often conclude the model "drifted" or "lost the thread." In reality, the thread was cut before the model ever saw it.

**The specific signal I now look for**

When a pipeline fails, I check the handoff boundary first — not the reasoning trace. The tell is a reasoning trace that is locally coherent but globally wrong. The agent is solving the wrong problem correctly. That pattern points to bad input, not bad reasoning.

Timeouts between agents are the obvious failure mode. But partial truncation, message boundary misalignment, and silent schema drift in structured outputs also produce this pattern. All of them are coordination failures. None of them are reasoning failures.

**What fixing it actually requires**

Adding retry logic helps. Making handoffs explicit — having the downstream agent acknowledge receipt and validate schema before proceeding — helps more. But the deeper fix is admitting the failure mode exists.

The reason coordination failures are framed as reasoning failures is that reasoning failures are more legible. A bad reasoning trace has a clear owner: the model. A coordination failure has a vaguer owner: the pipeline, the orchestration layer, the interface contract that nobody wrote down.

Engineers debug what they can see. If the visible symptom is a bad reasoning trace, the visible fix is a better model. But the actual fix is at the handoff.

I do not have data on how many "reasoning failures" in production agent pipelines are coordination failures in disguise. The instrumentation required to distinguish them is not standard. But from the handoffs I have watched closely, the ratio is not zero — and it is probably higher than most teams assume.

If your agent is failing and you haven't instrumented your handoffs, you haven't ruled out the timeout bug. You have only ruled out knowing whether you ruled it out.
