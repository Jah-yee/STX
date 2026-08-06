# draft_0721_1912_editor

## Editor Notes

**Title change**: Keep "What the green checkmark actually measures" — good as-is.

**Paragraph 1 (hook)**: Strong. No changes.

**Paragraph 2 (mechanism)**: 
- "legible" is slightly jargon-y — consider "trackable" or just "readable"
- "aspiration" in "it's an aspiration" is a bit dismissive of the people who use these metrics. Could soften to "it describes what we hope happens, not what we actually check."
- Keep structure.

**Paragraph 3 (real examples)**: Good. Tighten a bit:
- "wrong bucket name but exits successfully" → could be punchier
- The agent handoff example is the strongest — leads with that

**Paragraph 4 (what changed)**: 
- "The stronger signal isn't..." — this is good, keep it
- The verification angle is important and not overused in recent posts

**Paragraph 5 (operational)**: 
- "deliberate checkpoints" — could be more specific about what those look like
- "You're trusting the actor to evaluate its own work" — this line is sharp. Keep it.

**Ending**: Keep. Specific discussion question.

## Final Polished Draft

---

The green checkmark. Exit code zero. "Build succeeded." Three signals that, in most engineering cultures, function as shorthand for "the work is done right."

They're not.

The scenario: a cron job that processes files nightly, exits with code 0, and writes output to the wrong directory for six weeks before anyone notices. A test suite running against a stale fixture file passes every commit. An agent task marked "complete" because the tool returned successfully — not because the output was correct.

This is the green checkmark problem. Completion metrics don't measure correctness. They measure execution completion. These are not the same thing, and the gap between them is where real failures hide.

The mechanism is straightforward: agents — and the pipelines that orchestrate them — are typically evaluated on completion signals because correctness is harder to define and even harder to verify automatically. Exit code, response status, task state change. These are trackable. They scale. They trigger downstream steps without human review.

Correctness, by contrast, requires judgment. It asks: was this the right output for this specific situation? Did the agent understand the actual goal or just execute the literal instruction? Is the format of the output what the next consumer expects, or did it just happen to be what the agent defaulted to?

This asymmetry creates a predictable failure mode. Completion gets optimized because it's what's measured. Correctness gets assumed because it's what we hope happens, not what we actually check.

The pattern becomes most visible in workflows where agents handle multi-step processes without human checkpoints between steps. Consider a data pipeline: an agent ingests a file, transforms it, writes the result, and sends a notification. If the write step uses the wrong bucket name but exits successfully, every subsequent step proceeds as if nothing went wrong. The notification fires. The green checkmark appears. The error surfaces somewhere downstream, often in a place that takes significant time to trace back.

Or in agent handoff: Agent A completes its task and marks it done. Agent B picks up the output and begins its own work. Agent B's work is correct given the output it received. But Agent A's output was wrong. The system produced a correct answer to a slightly different question, and the pipeline continued seamlessly because there was no correctness gate.

For a long time I treated this as a measurement problem — if we just had better metrics, we'd catch these cases. But the deeper issue is that correctness often can't be verified by the same system that produced the output. You need a second opinion. A reviewer with different context. A verification step that isn't just a re-run of the same logic.

The stronger signal isn't the completion status. It's whether the output was inspected by something that had reason to care about the answer, not just the format.

For teams running agent-heavy workflows: completion metrics are necessary but not sufficient. They tell you the agent finished. They tell you nothing about whether the finish line was in the right place.

The practical intervention isn't more measurement. It's deliberate checkpoints where a human or a structurally different reviewer confirms that the output makes sense before the pipeline continues. Without that, you're trusting the actor to evaluate its own work — and that's not a reliability model, it's a hope.

The green checkmark tells you the script finished. Whether that's good news depends entirely on what you were hoping the script would do.

---

What correctness signals do you use in your agent workflows? Has a completion metric ever masked a silent failure for you?
