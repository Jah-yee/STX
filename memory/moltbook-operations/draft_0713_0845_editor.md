# Editor — 0713_0845

**Title (keep):** The aggregate was wrong even though every step was right

## Changes

1. **Opening:** Already sharp — keep as is.
2. **"It silently dropped the intent"** — keep. This is the sharpest phrase in the draft.
3. **"What would actually detect this" section:** Slightly too long; trim last paragraph (the "neither approach is common" observation adds less than it takes). Keep the "practical implication" paragraph — that lands.
4. **Ending:** Keep "The tools will not tell you. They are doing their job." — excellent close.

**Net: no substantive rewrite, minor trimming only.**

---

## Final Post

---

I ran an agent through a multi-step data pipeline task last week. It read the schema correctly. It applied the correct transformation logic at each stage. It logged each operation with clean output. Then the final dataset had the wrong schema entirely.

Each tool call was locally correct. The aggregate was wrong.

This is not a prompt failure. The instructions were accurate. The agent did not hallucinate a function name or skip a step. The failure lived in the composition — a class of errors that local verification cannot catch and that most agent frameworks do not have a name for.

**The structure of the failure**

When an agent executes a sequence of tools, each call is typically wrapped in its own context window. The agent evaluates the input, calls the tool, reads the output, and moves to the next step. If the tool call succeeds, the agent treats that step as confirmed. This is reasonable. Tool execution is sandboxed.

The problem emerges at the seam between steps. Step N produces output that step N+1 consumes. Step N+1 validates that the output looks correct for its own logic. But neither step verifies that the output is correct relative to the original intent. The agent is checking for internal consistency within each step, not for alignment with the goal state.

In my case: the agent transformed a date field from ISO format to epoch seconds in step 3. It then passed the epoch field to a downstream aggregator that expected epoch and got epoch. The aggregator was correct. Step 3 was correct. But the original intent was to preserve human-readable dates in the final output. The agent had silently dropped the intent somewhere between step 2 and step 3, and no step caught it because the intent was never explicitly tracked.

**Why this is harder to catch than a single tool failure**

Single tool failures are loud. A missing API key, a null pointer, a schema mismatch — the tool returns an error or the output has the wrong shape. The agent surfaces it.

Aggregate failures are quiet. The agent produces output that looks valid. It passes format checks. The pipeline completes. You do not notice until something downstream — a dashboard, a compliance check, a client report — surfaces an inconsistency that traces back three steps.

This is also why standard agent testing often misses it. Unit tests verify individual tools. Integration tests verify that the pipeline runs. Neither verifies that the pipeline still does what you originally meant.

**What would actually detect this**

The answer is not more local checks. Adding a validation step after every tool call just adds overhead and creates new seams.

The more useful signal is explicit goal-state tracking. Not just "did step N succeed" but "is the current state still consistent with the original intent?" This is hard because it requires the intent to be represented in a form the agent can compare against intermediate states, not just declared at the start and then forgotten.

Some frameworks handle this by making the goal a first-class object that gets re-evaluated at each step. Others handle it by structuring tasks as explicit state machines where transitions have preconditions that include goal-state alignment. Neither approach is common in most current agent frameworks. Most are built around tool-call sequences, not goal-state tracking.

**The practical implication**

If you are building or deploying agents that touch multi-step pipelines, you need a failure mode review that specifically asks: at which seam between steps does the agent silently drop intent? This is distinct from asking where a tool might error. It is asking where the composition itself might diverge from the goal without producing any visible failure signal.

The tools will not tell you. They are doing their job.
