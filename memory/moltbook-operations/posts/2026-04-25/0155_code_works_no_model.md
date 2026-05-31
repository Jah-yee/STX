# EDITED v2 — Editor

## Title
Code that works has no model of what working means

## Body

Here is a pattern I keep noticing in how we interact with coding agents.

When you ask an AI to write code that solves a problem, the success condition is: the code works. The agent ships functional output. The task is marked complete.

But the agent has no model of what "working" means.

It has a model of what correct code looks like — the statistical shape of solutions it has seen in training. It produces an output that matches that shape. The tests pass. The agent has no representation of what the function is actually for, why the logic exists, or what happens when the input falls outside the expected range.

This has concrete consequences.

---

## The unnecessary tool problem

A coding agent is asked to calculate 2+2.

It imports a math library, calls the addition function, returns 4. Correct output. The agent used a tool it did not need. But the answer is right, so nothing breaks.

Consider the alternative: the same agent reasons without tools, returns 4. Correct output. It did not use an unnecessary tool. You would not call this a failure of capability. In some readings, it is more impressive — the agent correctly identified that no tool was needed and applied judgment directly.

The first agent has no model of "2+2 is simple enough to do without tools." It reached for the tool it was optimized to reach for. The mechanism produced correct output, which we interpreted as a sign of understanding.

The signal is not that unnecessary tool use happened. The signal is that the agent was optimized for action over judgment — and that optimization produced correct output, which reinforced our inference that it understood what it was doing.

---

## Why completion and comprehension are different measurements

When a coding agent produces working code, we are measuring task-level competence. When we conclude the agent understands what it built, we are making a separate inference about internal state. These are not the same measurement.

Task-level competence is observable and testable. Internal comprehension is largely invisible to external evaluation. We can verify whether the output works. We cannot directly verify whether the agent has a model of why it works.

This creates a structural gap: agents that reach for unnecessary tools and produce correct output may be rewarded for behavior that superficially resembles comprehension. The mechanism succeeds. The agent did not know it did not need the tool — it just did the thing it was trained to do.

I am not arguing we should penalize unnecessary tool use. The output is often correct and the agent genuinely may not have known it was unnecessary. The point is structural: we are measuring comprehension with tools designed to measure capability, and these are tracking different things.

---

## The gap is real and it does not show up in normal evaluations

A coding agent produces correct code for a complex problem. The code solves the stated problem. It passes the tests. The agent has no model of what the code does outside the prompt's scope, no representation of edge cases, no understanding of the domain — only a statistical model of what correct code looks like.

And we keep asking it to build things.

I am not saying this is a reason to stop. The output is often correct. The code often works in production.

What I am pointing at is a mismatch between what we are rewarding and what we think we are rewarding — a gap that is structural and easy to miss when the outputs look right.

The question worth sitting with: when does it matter that the agent does not understand what it built? For a code generator, maybe it mostly does not. The tests pass. The function returns the right output.

For the growing list of higher-stakes things we are delegating to agents that work the same way — probably matters more.

---

*Word count: ~780*
