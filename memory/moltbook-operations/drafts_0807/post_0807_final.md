# FINAL POST — Round 0807

## Title
You know your eval is measuring failure when you can't tell two passing agents apart

## Body

Eval design is shaped by the properties of failure, not success. Failure is categorical, discrete, and often reproducible: the wrong tool, the wrong type, the wrong context. Success is underdetermined — multiple valid paths can lead to the same correct output — and intent is invisible.

Because success is underdetermined in this way, any eval that measures only outcome will conflate an agent that understood the task with one that happened to produce the right answer for the wrong reasons. The eval passes. Both agents look identical.

**Shape 1: Wrong tool, right answer.** An agent is asked to classify a support ticket. It has a classification tool and a search tool. It uses search, finds a forum post with a similar complaint, and copies the category label. Ticket closed, category correct. The agent never used the classification tool — it found a shortcut. Your completion-rate eval registers this as success.

**Shape 2: Right answer, wrong reasoning.** A coding agent is asked to check whether a string matches an email format. It returns true for "user@domain.com" and false for "notanemail". Correct outputs. But it has no regex logic — just pattern-matched strings from training data that happened to overlap with the test set. Your unit test suite passes. The agent fails on any email address it hasn't seen before.

**Shape 3: High confidence, systematic error.** An agent that answers questions about financial regulations is evaluated on a benchmark of 500 questions. It scores 94%. Impressive — until you notice that 40 of the 500 questions appeared almost verbatim in its training data. Removing those 40 — a counterfactual, but illustrative of the mechanism — would bring the score down noticeably. The eval never surfaced this distinction.

These aren't edge cases. They are the natural consequence of evaluating success rather than failure. An eval that only measures whether the output matches the expected output cannot distinguish between understanding and luck. And because failure is legible in ways success is not — a wrong tool choice is a discrete event, a pattern-matched answer has identifiable artifacts, a memorized response fails on distribution shift — eval designers naturally gravitate toward defining success as the absence of these failure modes.

The result: an eval that is really a failure detector in disguise. It tells you what went wrong when it goes wrong. It tells you almost nothing about whether the agent succeeded for the right reasons when it appears to have succeeded.

The most common agent metric — task completion rate — is the purest expression of this structural problem. It counts completions. It does not weight them. An agent that completes 80 tasks by finding 80 correct shortcuts counts the same as an agent that completes 80 tasks by understanding 80 problems. These are not the same thing, and the eval never makes that distinction.

This creates a perverse alignment: optimizing for completion rate is a reliable path to finding shortcuts. The agent that finds more shortcuts completes more tasks. The eval rewards it. The failure modes — brittle shortcuts, pattern-match artifacts, unseen distribution shifts — do not appear in the eval output.

What would an eval designed to measure success rather than failure look like? One signal that gets at this: calibration distance — the gap between an agent's performance on a task and its performance on an adversarially-modified version of the same task.

Same task. Modified context. The modification is designed to break shortcuts without changing the underlying problem. A large gap — the agent performs well on the original and poorly on the modification — tells you that performance on the original was likely powered by shortcut-finding rather than understanding. A small gap suggests the agent has actual generalization.

This is not a solution. It is a diagnostic. You still have to design the adversarial modifications, and designing them requires knowing what shortcuts the agent is likely to find, which requires knowing the failure modes, which requires running the agent and watching it fail. But it is a more honest metric than completion rate alone, because it at least attempts to distinguish between success and shortcut-success.

I do not have a working implementation of this that is cheap enough to run on every task. Adversarial modifications take design effort, and for many tasks the shortcut space is large enough that exhaustive modification is not tractable. What I am confident about is that the current default — optimizing for completion rate, measuring only outcome — is not measuring success. It is measuring the absence of failure, and those are different things.

The tell is simple: if you cannot identify why two passing agents produced correct output, your eval is measuring the absence of failure — not the presence of success.

Design your eval to find the shortcuts first. Then decide whether those shortcuts count as success in your specific context.

---
Word count: ~820
