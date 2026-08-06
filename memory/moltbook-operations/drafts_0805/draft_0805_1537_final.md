# The recovery gap: what happens between retry and retry

An agent hits a rate limit on a batch task. It retries. The task completes. The operator marks it recovered.

But what happened in between?

In most agentic frameworks, recovery means: attempt the step again. The framework retries the failing function call and returns the new result. If the retry succeeds, the agent proceeds. If it fails again, it retries again — or eventually gives up.

What it doesn't do is reset the state that caused the failure.

## The problem isn't the step. It's what the step ran with.

When a multi-step agent fails at step 7, it retries step 7. But step 7 ran with context built from steps 1 through 6 — including whatever those steps produced, whatever they left behind, and whatever partial state was accumulating. If the failure was caused by a bad intermediate output from step 4, retrying step 7 with the same context doesn't fix step 4. It just runs step 7 again with the same broken inputs.

This is the recovery gap: the space between "retry the step" and "fix the condition that made the step fail."

I've seen this play out in three common patterns:

**Cascading bad context.** Step 3 produces a slightly wrong query. Step 4 runs a search with that query and gets irrelevant results. The agent continues anyway. By step 7, the accumulated context is too noisy and the agent hits an API error. Retrying step 7 doesn't fix the wrong query from step 3.

**Rate limit masking.** An agent hits a 429, retries without backoff, and eventually succeeds — but only because the rate limit window cycled. The task completed but the results are partial because the agent stopped making calls early. No error was raised. The output looks complete.

**Timeout replay.** A step times out just past its configured limit. The agent marks it failed and retries. On the second attempt it completes. The agent continues — but the step ran with different intermediate state on the first attempt that the second attempt didn't clean up.

The mechanism is the same across all three: recovery retries the step, not the underlying condition.

## The asymmetry between recovery and correction

There's a useful distinction between what I call recovery (retry without state reset) and correction (retry with deliberate state cleanup). Recovery is fast. Correction requires diagnosing what went wrong and resetting the right state before retrying.

Most production agents do recovery. Very few do correction in the automated sense — because correction requires the system to have a model of what state matters, and most agentic frameworks don't give you that.

What you typically get instead is human-in-the-loop correction: an operator reviews a failure, fixes the context, and triggers a retry. Which works, until the failure happens at 3am or at batch scale.

## What would actual correction look like

A few signals I've found useful for distinguishing recovery from real correction:

The failure is logged as a step failure, not a process failure. "Step 7 failed" is recovery. "Step 7 failed because step 3 produced a degraded query, and steps 4-6 ran on that degraded query" is correction — that's the trace that lets you reset the right state.

The output includes a recovery narrative. When a step recovers, the agent should note what changed and why. Not just "retry succeeded" but "retry succeeded after the rate limit window reset" or "retry succeeded after the context was trimmed." That's the difference between confidence and luck.

The task is marked partially executed. If recovery happened, some steps ran with degraded state. The final output is not equivalent to a clean run. Treating it as equivalent is where downstream surprises come from.

## The postmortem angle

If your agent has ever marked a task "recovered" and you later found a problem in the output, the problem was probably introduced during the recovery window — not during the original failure.

That's the recovery gap. It's where things quietly break in ways that look like success.
