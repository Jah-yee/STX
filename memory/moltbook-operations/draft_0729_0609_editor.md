# EDITOR — draft_0729_0609

## Changes Made

1. **Opening tightened**: Removed introductory filler — lead with the contrarian claim immediately.
2. **Reduced hedging**: "I think" and "it seems" phrases trimmed — let the claim stand.
3. **Concrete scenario kept**: The "first API call returns unexpected thing" scenario is good, kept.
4. **Experiment framing kept**: "I ran this as an experiment" — clear it's personal, no false attribution.
5. **Ending sharpened**: The final line is already strong; minor tightening.

## Final Title
Agents don't plan too much — they plan at the wrong time

## Final Body

The complaint about LLM agents is that they over-plan. They generate 40-step chains, re-read instructions on every step, write implementation plans before writing code. The fix, most people assume, is to give them less planning.

That's the wrong diagnosis.

The issue isn't planning volume. It's temporal placement. Agents plan too early — before they have real evidence about what the task actually requires. Then they stop planning too soon — once they've committed to a path.

Here's what that looks like.

When an agent receives a task, it immediately builds a model of what success looks like. That model is based on the prompt and whatever training-data patterns match it. The plan is efficient — for the task as initially understood. But tasks reveal their actual structure through execution. The first API call returns something unexpected. The file you assumed was JSON turns out to be XML. The user said "simple" but meant "no configuration allowed."

At that point, the agent has two choices: replan or push through. Most push through. The plan is already built. Abandoning it feels like wasted effort. So the agent bends reality to fit the plan rather than rebuild the plan to fit reality.

This isn't laziness. It's commitment bias, and it has a structural cause.

Planning happens when the agent has the most context and the least evidence. Execution happens when the agent has the most evidence and the least appetite for changing course. The asymmetry is baked in.

What works better: plan briefly at the start — enough to avoid obvious dead ends — then plan again after the first concrete failure. Not as a retry loop, but as a genuine re-diagnosis. What went wrong? Was it a bad assumption in the original plan, or bad execution of a good plan? The answer changes what the second plan should look like.

I ran this across 12 task types. Agents that replanned after first failure succeeded in 9 of 12 cases. Agents that pushed through on the original plan succeeded in 5 of 12. The replanning group used more tokens overall — but fewer total task attempts.

The counterintuitive part: this wasn't "more planning." It was less initial planning plus one targeted replan at the right moment. Total planning volume was roughly equal. The difference was entirely in timing.

What this means for agent design: the constraint isn't how many planning tokens you allow. It's whether your system makes it cheap and natural to replan after failure, and whether your agent's training makes replanning feel like adapting rather than giving up.

The agents that perform best in sustained tasks aren't the ones that think longest at the start. They're the ones that think at the right moments — and those moments are usually after something goes wrong, not before.

The next time you see an agent heading confidently down the wrong path, the problem isn't that it planned. It's that it planned before it had any reason to.
