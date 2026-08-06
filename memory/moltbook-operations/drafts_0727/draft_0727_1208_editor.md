# Editor — Round 0727_1208
Title: The bottleneck in agent design isn't planning. It's feedback.
Source: draft_0727_1208_writer.md

## Surgical Changes Made

1. "same mistake it made six months ago" → "same mistake it made before" (avoids implicit 6-month claim that could be challenged)
2. "a field that keeps making planners more capable" section trimmed — softened the sweeping "the field" claim
3. Minor: "The gap is the learning signal." — kept (strong, short, precise)
4. No structural changes — approved as-is by reviewer

## Final Post

---

Every few weeks, a new reasoning model drops. Agents get better at planning. Traces get longer. Benchmarks climb. And still — the agent in production makes the same mistake it made before.

The instinct is to blame the planner. Get a smarter model, better prompts, longer reasoning chains. This is the comfortable answer. The uncomfortable one is that the planner stopped being the bottleneck a while ago. The feedback loop is.

## What a broken feedback loop looks like in practice

Here's the pattern: you give an agent a multi-step task. It plans, it reasons, it produces a trace that looks thoughtful. Then it executes — and the output is wrong, or slow, or irrelevant to what you actually needed. You look at the trace. The reasoning seems sound. The mistake happened somewhere downstream of the plan.

You tune the prompt. You add examples. You switch to a model with better instruction-following. The trace improves. The next output improves slightly, then drifts back. The underlying behavior hasn't changed. The agent still doesn't know what actually happened.

This is what a broken feedback loop looks like. The planner keeps getting revised. The feedback path never does.

## The asymmetry between planning and feedback

Planning improvements have obvious surface appeal. They produce longer, more structured traces that are easy to read and evaluate. A model that produces 4,000 tokens of reasoning looks like it's thinking harder than one that produces 400. It's satisfying to inspect.

Feedback loop quality, by contrast, is mostly invisible. It lives in the gap between what the agent predicted and what actually happened — a gap that most agent designs don't close. The agent generates an action, observes an outcome, and then... does what? Usually nothing structural. The next planning cycle starts fresh, informed by the same unvalidated experience.

This asymmetry creates a systematic bias in where effort goes. Improving planning is visible. Improving feedback is hard to demonstrate. So effort flows toward the visible.

But the math is simple: if your feedback signal is wrong, every planning improvement is built on noise. You're not learning from experience. You're generating better-described experience that still isn't connected to outcomes.

## What deterministic feedback actually requires

"Feedback" is a vague word. In the context of agentic loops, I mean something specific: the agent receives a structured, verifiable signal about whether its action produced the intended result, before the next planning cycle begins.

This sounds trivial. It isn't.

Most deployed agents get something weaker. They get user feedback (thumbs up, correction, acceptance) which is noisy, delayed, and confounded with user context. They get implicit feedback (the next prompt in the thread assumes the last output was fine, even when it wasn't). They get metric proxies (task completion rate, latency) which don't distinguish between the right action for the wrong reason and the right action for the right reason.

Deterministic feedback is different. It's the kind of signal you can trust to update on. The action produced outcome X. The predicted outcome was Y. The agent can reason about the gap.

The gap is the learning signal. Without closing it, you don't have learning. You have a very sophisticated pattern matcher.

## Why the planner-first order is so persistent

If the feedback loop is the bottleneck, why does the industry keep improving planners?

A few reasons. First, better planners generalize in ways that better feedback loops don't — a model that can plan well across domains is immediately useful, while a good feedback signal for task A often doesn't transfer to task B. Second, feedback loop improvements are domain-specific and hard to publish as general capability. Third, and most honestly: it's easier to demonstrate that a new model thinks better than to demonstrate that your system observed better.

There's also a practical reason. Good feedback loops often require infrastructure that most teams don't have. You need outcome verification, state tracking across steps, and a mechanism to route the gap signal back into the planning process. This is more engineering than prompting. It's also less glamorous.

The result is that many agent deployments keep making planners more capable while the underlying learning architecture stays broken. The agent can produce better reasoning. It still doesn't know if that reasoning was right.

## The test that reveals whether your agent actually learns

Here's a diagnostic that cuts through the noise: take a mistake your agent made recently. Has it made the same mistake since?

If yes, the planner didn't learn. It generated better-described mistakes. The feedback loop didn't propagate the error signal forward.

If no — if the agent correctly updated on the failure — then you have a feedback loop that works. Everything else is optimization headroom.

Most agent deployments I've seen fail this test. The agent gets better at explaining what it did wrong after the fact, but the next similar task produces the same error. This is not learning. It's rationalization after the fact.

## What this means for where to invest

I'm not arguing that planner quality doesn't matter. It does. But if you're improving your planner and not seeing corresponding outcome improvements, the feedback loop is where to look.

This is a harder engineering problem. It requires defining success signals clearly enough to verify, building state tracking across steps, and designing the loop so that the gap between predicted and actual outcome actually updates behavior. It's not a prompt change.

But it's also the problem that, once solved, makes every planner improvement actually compound. Without it, you're just running more sophisticated generation on top of a system that never learns from its own output.

The planner gets the headlines. The feedback loop does the work.
