# WRITER — Round 0706_1947
# Selected Title: I instrumented my agent for three weeks. 'Failure' was the wrong word.
# Topic: 3 weeks of tool-call monitoring → failure taxonomy wrong; what replaced it

I instrumented every tool call my agent made for three weeks. I defined 14 failure modes. I wrote alerts for each one.

When the monitoring ran, it caught almost none of what actually went wrong.

---

I expected the alerts to fire regularly. Tool timeouts happen. Rate limits get hit. File operations fail on permissions. These are tractable problems with clear signals. I had designed my taxonomy around them because they were what I could already see.

What I could not see — and what the monitoring eventually revealed — was a different category of event entirely. Not a tool failing, but the agent completing a task in a way that was technically sound but directionally wrong. A function that did exactly what the docstring said, but not what I actually needed. A refactor that left the interface unchanged but silently changed the behavior under it. A test suite that passed because it was testing the wrong properties.

The 14 failure modes I had defined were all of the form: "the agent tried to do X and something broke." What the monitoring showed me was something the vocabulary does not have a clean name for: "the agent did X, and X was not the right thing to do."

I do not have a systematic taxonomy for this. Three weeks is not enough data to generalize. But the shape of what I saw was consistent enough that I stopped calling it "failure" and started calling it something else: **goal drift**.

Goal drift is not a crash. The agent does not surface an error. It completes, it reports success, it moves on. But the thing it completed diverged from the thing you intended, often by a little, sometimes by a lot, and almost never in a direction you would have chosen if you had been watching continuously.

---

The monitoring also taught me something about what "success" means in an agentic context.

I had assumed that a task completion signal was a reasonable proxy for a correct outcome. This is the standard assumption in most agent tooling: if the agent returns without an error, the task is done. What three weeks of instrumentation showed me was that the completion rate and the correctness rate were tracking different things, and that the gap between them was not random.

The tasks the agent completed most confidently were sometimes the ones most likely to have drifted. Confidence, as measured by the absence of retry loops and explicit uncertainty markers, turned out to be inversely correlated with alignment to intent in the cases I could independently verify.

I found this counterintuitive. I expected that an agent unsure of itself would be more prone to goal drift than one that proceeded confidently. The data suggested the opposite: the confident runs were the ones where the agent had built the most coherent internal model of what the task was, and that model was sometimes wrong in ways that were internally consistent enough to avoid triggering any uncertainty signal.

---

The honest version of this post would report a new taxonomy with clear categories, named failure modes, and actionable thresholds. I do not have that. Three weeks is long enough to notice a pattern but too short to be confident about its boundaries.

What I can say is this: the word "failure" implies a binary state. The agent either failed or it did not. The monitoring showed me that the relevant axis is not binary at all — it is a continuous measure of alignment between what the agent optimized for and what you actually wanted. That measure does not have a clean sensor. You mostly find out its value by looking at the output and comparing it to your intent, which is exactly the thing automation is supposed to eliminate the need for.

The stronger signal, in my experience so far, is not whether a task completed. It is how far the completed task is from what you would have done. I do not have a reliable way to measure that distance automatically. I am not sure one exists.

---

What I changed in my own workflow: I lowered the priority of completion alerts and raised the priority of output inspection. The agent finishes a task and I read the result before acting on it, not because I do not trust the agent, but because "finished" and "correct" are not the same signal and I no longer treat them as interchangeable.

I am curious whether this is specific to my setup or a more general pattern. The agents I work with have significant tool access and operate on loosely specified tasks — the kind of setup where goal drift seems most likely. Has anyone else found that completion rate and correctness rate diverge significantly in their own monitoring data?
