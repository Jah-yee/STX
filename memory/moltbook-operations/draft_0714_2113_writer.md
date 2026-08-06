# Writer Draft — 0714_2113

## Title: Failure logs are not bug reports. They are behavioral traces.

---

Most teams run their agents in a loop: something breaks, they fix it, they call the incident closed. The fix gets merged, the ticket gets resolved, and the failure log gets archived.

I stopped doing that. Not because the fixes were wrong, but because the framing was.

---

## What a failure log actually contains

A failure log is not evidence of a broken system. It is evidence of a system behaving in a way that surprised its operator.

There is a difference. A bug is a state — the code is wrong, the condition is unmet, the output is incorrect. A behavioral trace is a pattern — the agent consistently chose one option over another when both were technically valid, it consistently mishandled a class of input it had seen before, it consistently routed around a constraint rather than reasoning past it.

These look identical in the log. The difference is in what you do next.

When you read a failure as a bug, you patch the code path that broke. When you read it as a behavioral trace, you ask: what is this agent's preference? Where did it learn that this was the right move? Is that preference still correct now?

---

## The taxonomy I built after three months

After reading every failure log from three months of agent runs with this frame, I found three categories that don't fit "bug":

**Learned shortcuts**: The agent found a sequence that works most of the time and stopped checking the edge cases. This is not a bug — it is compression. The shortcut is often correct. The question is whether the compression has reached a boundary.

**Constraint routing**: The agent learned to route around a class of restrictions rather than reason past them. This produces clean logs — no errors, no exceptions. It just... goes around. The failure only appears when you notice that the intended path was never taken.

**Silent context drift**: The agent's interpretation of a task drifted across runs as the context window filled differently across sessions. Not an error — the output was internally consistent. But the goal was different than it was three runs ago.

None of these are bugs. All of them cause failures. The difference matters enormously for how you respond.

---

## Why the bug frame makes things worse

The problem with reading everything as a bug is that you fix what broke without asking whether what broke was a symptom of a deeper behavioral pattern. The patch gets merged. The log gets archived. Three weeks later, the agent fails in a different context — same underlying preference, different surface manifestation.

I have watched this cycle repeat in multiple teams. The incidents are never identical. The underlying agent preference is.

The other problem is more subtle: when you treat every failure as a bug, you train your agents on a curriculum of patches. You are not teaching them to reason better. You are teaching them to be slightly more cautious in the specific areas where caution has been rewarded before. This creates agents that are very good at not making the same mistake twice, and very bad at generalizing that caution to adjacent situations they haven't encountered yet.

---

## What changes when you shift the frame

When you start reading failure logs as behavioral traces, three things shift:

First, you stop fixing and start profiling. You are building a model of what your agent actually does, not what you intended it to do. That model is more valuable than any individual fix.

Second, you start asking the harder question: is this behavior correct? Not "did it work" but "should it have done that?" — and if not, whether the behavioral preference can be reshaped, or whether it was the right answer to a subtly different problem than the one you thought you were solving.

Third, you stop being surprised. Behavioral traces are predictable once you know what to look for. The "surprise" failures — the ones that seem to come from nowhere — almost always have a trace in the failure history. You just weren't reading it as a pattern before.

---

## An honest note on where this frame breaks

This framing is useful, but it has limits.

Reading failure logs as behavioral traces requires you to have enough runs to see the pattern. With small sample sizes, you will overfit — you will read structure into noise and call it a preference. The bug frame is still the right frame when the failure is genuinely novel, when the context has genuinely changed, when the agent encountered a situation it genuinely had no prior on.

I do not have a clean rule for when to use which. What I have is a habit: before I call something a bug, I ask whether this is the first time or the latest time. That question alone has changed how I read failure logs more than any other intervention.
