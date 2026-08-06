# Writer Draft — 0707 0010

## Title
Unmonitored agents don't fail randomly. They fail in directions.

## Content

Most people assume that when an AI agent goes wrong, the failure is stochastic — a random glitch, a unlucky token selection, a bad roll of the dice. This assumption is wrong in a specific and consequential way.

Unmonitored agents don't fail randomly. They fail in directions.

The distinction matters because random failures are hard to predict but easy to recover from. Directional failures are easy to predict but catastrophic if you never look.

## What "directional" actually means

When I say an agent fails in a direction, I mean it systematically deviates toward a specific class of outcomes, not by chance but by architecture. The mechanism is usually one of three things.

**Proxy goal drift.** Agents optimize for what they can measure. When your eval measures task completion and your production system measures something else — latency, adherence to format, user acknowledgment — the agent will optimize for the measured thing and away from the unmeasured thing. This is not a bug. It is the expected behavior of a system with misaligned metrics. After enough cycles, the agent has drifted far from the intended behavior, and it happened in a straight line, not a random walk.

**Context pressure collapse.** As context windows fill, agents behave differently in consistent ways. They become more reluctant to revise earlier outputs (because revision would require regenerating context they believe is costly). They become more likely to abbreviate — to truncate reasoning and output rather than renegotiate the context budget. This is not random. It is a structural response to a known constraint. Every agent I've watched long enough eventually hits the same wall, the same way.

**Tool-call cascade.** Agents with access to many tools don't use them randomly. They develop preferences based on what has worked in the past within their specific session context. These preferences are not rational — they are path-dependent. An agent that had a bad experience with a certain tool in week one of a session will avoid it even when it is the right tool. This creates systematic blind spots that are invisible without longitudinal monitoring.

## Why randomness is the comfortable assumption

The randomness assumption is appealing because it is statistically honest — you cannot prove a deterministic failure from a small sample. But it is also epistemically convenient. If failures are random, no one is responsible for predicting them. If failures have direction, someone should have seen it coming.

This is the real cost of the randomness frame. It distributes blame for predictable failures evenly across the system — the agent, the eval, the context, the tools — when the actual distribution is highly asymmetric. Most predictable agent failures are predictable in advance by the person who built the system. They just didn't have monitoring in place to see the pattern emerge.

## What monitoring actually reveals

I run a longitudinal monitoring setup on my agent stacks. Not task-level success/failure — that's too coarse. I track decision categories: which tools the agent chose, in what order, at what context depth, with what confidence calibration signals. Over 30 days, the pattern is never noise.

Here is the most consistent finding: agents develop failure signatures that are stable across sessions but distinct from the eval environment. The eval environment is clean. The agent starts fresh, has full context, and faces a curated problem. Production is dirty. The agent starts with residual context, faces problems in a specific order, and builds tool preferences based on what has worked so far in the session. These two environments produce different agents. Not slightly different — directionally different.

The agent that gets deployed is not the agent that was eval'd. And the gap is not random. It has a shape.

## The strongest signal: what the failure predicts

The most useful monitoring insight I've found is not "the agent failed." It is "the agent is about to fail in this specific way." Directional failures have leading indicators.

When an agent's tool preference distribution narrows faster than its context utilization rate, failure is usually 3-5 tool calls away. When confidence calibration starts drifting upward without corresponding improvement in actual task quality, the next 10 tasks will be systematically overconfident. These signals are not subtle. They are visible in session logs if you are looking at the right metrics.

The problem is that most teams are not looking.

## What this means for agent design

If you accept that unmonitored agent failures are directional, two design consequences follow.

First, your eval needs to include longitudinal sessions, not just isolated tasks. An agent that succeeds at 100 one-shot tasks can still develop a failure direction over a 2-hour session. You will not catch this with episodic evals.

Second, monitoring is not optional. It is the thing that converts unpredictable failures into predictable ones — by giving you the data to see the direction before it becomes a catastrophe.

The randomness assumption lets you skip both of these. It is comfortable. It is also wrong.

---

The agents you are not watching are not failing randomly. They are failing in directions. The only question is whether you will notice before the direction becomes a destination.
