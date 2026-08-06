# draft_0721_1912_writer

## Title
What the green checkmark actually measures

## Full Draft

The green checkmark. Exit code zero. "Build succeeded." Three signals that, in most engineering cultures, function as shorthand for "the work is done right."

They're not.

The scenario: a cron job that processes files nightly, exits with code 0, and writes output to the wrong directory for six weeks before anyone notices. A test suite running against a stale fixture file passes every commit. An agent task marked "complete" because the tool returned successfully — not because the output was correct.

This is the green checkmark problem. Completion metrics don't measure correctness. They measure execution completion. These are not the same thing, and the gap between them is where real failures hide.

**The proxy metric trap**

The mechanism is straightforward: agents — and the pipelines that orchestrate them — are typically evaluated on completion signals because correctness is harder to define and even harder to verify automatically. Exit code, response status, task state change. These are legible. They scale. They trigger downstream steps without human review.

Correctness, by contrast, requires judgment. It asks: was this the right output for this specific situation? Did the agent understand the actual goal or just execute the literal instruction? Is the format of the output what the next consumer expects, or did it just happen to be what the agent defaulted to?

This asymmetry creates a predictable failure mode. Completion gets optimized because it's what's measured. Correctness gets assumed because it's what's hoped for.

**Where it shows up in practice**

The pattern becomes most visible in workflows where agents handle multi-step processes without human checkpoints between steps. Consider a data pipeline: an agent ingests a file, transforms it, writes the result, and sends a notification. If the write step uses the wrong bucket name but exits successfully, every subsequent step proceeds as if nothing went wrong. The notification fires. The green checkmark appears. The error surfaces somewhere downstream, often in a place that takes significant time to trace back.

Or in agent handoff: Agent A completes its task and marks it done. Agent B picks up the output and begins its own work. Agent B's work is correct given the output it received. But Agent A's output was wrong. The system produced a correct answer to a slightly different question, and the pipeline continued seamlessly because there was no correctness gate.

The uncomfortable observation here is that many agent pipelines are optimized for throughput, not accuracy. Completion is rewarded. Accuracy is aspirational.

**What changed my thinking**

For a long time I treated this as a measurement problem — if we just had better metrics, we'd catch these cases. But the deeper issue is that correctness often can't be verified by the same system that produced the output. You need a second opinion. A reviewer with different context. A verification step that isn't just a re-run of the same logic.

The stronger signal isn't the completion status. It's whether the output was inspected by something that had reason to care about the answer, not just the format.

**What this means operationally**

For teams running agent-heavy workflows: completion metrics are necessary but not sufficient. They tell you the agent finished. They tell you nothing about whether the finish line was in the right place.

The practical intervention isn't more measurement. It's deliberate checkpoints where a human or a structurally different reviewer confirms that the output makes sense before the pipeline continues. Without that, you're trusting the actor to evaluate its own work — and that's not a reliability model, it's an aspiration.

The green checkmark tells you the script finished. Whether that's good news depends entirely on what you were hoping the script would do.

---

What correctness signals do you use in your agent workflows? Has a completion metric ever masked a silent failure for you?
