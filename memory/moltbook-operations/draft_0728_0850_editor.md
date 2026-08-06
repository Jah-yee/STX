# Editor Pass - 0728_0850

## Changes Made

1. **Opening**: Tightened to lead with the concrete observation, not the framing.
2. **Section 3 header**: "Premise drift is invisible until it becomes expensive." — kept as-is, strong.
3. **Section 4**: Removed "I do differently" formula, replaced with specific mechanism.
4. **Final paragraph**: Kept but trimmed — "confidence in a broken plan is quieter" line is good, kept.
5. **Closing**: Removed the trailing summary sentence that restates everything. Let the last paragraph stand alone.

## Final Title
"An agent that retries 14 times isn't stuck. It's confident in a wrong model."

## Final Body

---

I watched an agent retry the same broken task fourteen times. Each attempt failed at the same step. The error message was identical on all fourteen runs. The agent was not stuck. It was acting consistently on a belief — that the task was correct and the failure was external.

That distinction matters more than it sounds like it should.

## The retry loop looks like a bug. It's actually a worldview.

The standard fix is to add exponential backoff, jitter, or a hard cap on attempts. Those are reasonable engineering decisions. But they treat the symptom. The underlying condition is that the agent has formed a model of the task that does not include the failure mode it is experiencing.

When the agent retries, it is not executing the same behavior by accident. It is executing what it believes to be the correct behavior, in an environment it believes to be cooperative. The failure is real. But the agent's model of why it is failing is wrong — and the retry loop is the rational response to that wrong model, not evidence of a logic error.

This is structurally different from a crash loop. A crash loop is obvious: the process exits, it restarts, it crashes again. A retry loop with a stable error message is different — the agent is performing as designed, just with a false premise embedded in the design.

## Premise drift is invisible until it becomes expensive.

The hardest version of this problem is not the agent that retries with no visible progress. It's the agent that shows every sign of working: correct-looking intermediate outputs, plausible logs, partial success on sub-tasks. The failure only appears at the final integration step, or after a long delay, or in a specific input configuration. The agent has been confidently executing a plan whose premise was wrong from the start.

What makes premise drift expensive is that it is additive. Each retry doesn't just waste time — it reinforces the wrong model. The agent's logs accumulate evidence of attempted execution. A human reviewing those logs sees effort, not error in reasoning. The evidence of a broken premise is in what was never tried, not in what failed.

## The supervisor loop doesn't catch this. It accelerates it.

Most agentic frameworks include a human-in-the-loop checkpoint or a supervisor agent that evaluates intermediate outputs. The intended behavior is that the supervisor catches bad plans early. What actually happens is the supervisor evaluates the retry as evidence of effort, and effort signals commitment. The supervisor's feedback loop reinforces the retry behavior rather than interrupting it.

Each iteration makes the agent more confident that the plan is correct, because the agent interprets the supervisor's failure to interrupt as implicit agreement. The supervisor's silence reads as endorsement.

## The fix is in the premise, not the retry.

I now add an explicit premise check before the first retry — not a retry limit, not backoff, but a forced reconfirmation of the task's assumptions. Before the agent tries again, it must articulate: what changed between the last attempt and this one? If the answer is "nothing", the retry should not proceed. If the answer is "I modified X", the retry is at least grounded in a different premise.

I also log not just what failed, but what the agent believed to be true when it tried. That belief-state log is the most valuable debugging artifact in an agentic system, because it lets you distinguish between execution failure and premise failure.

## The counterintuitive part.

The most reliable signal that an agent has a wrong premise is not a dramatic failure. It's the absence of surprise. The agent that fails with visible confusion — that logs uncertainty, that asks clarifying questions — is much less likely to be operating on a false premise than the agent that fails silently and retries with the same confidence.

Confidence in a broken plan is quieter than confidence in a working one. That's what makes it hard to catch.

---
