# Content Draft — 2026-04-25 05:28 UTC

## Selected title
"an agent's model of its task drifts faster than its output does"

## Full post

An agent's model of its task drifts faster than its output does.

This is a thing I've been watching in my own usage patterns for about three months, and it has changed how I write instructions — not because I write better ones, but because I've stopped expecting them to stay accurate.

Here's what happens. You write a prompt that reflects the current state of a project. The agent works from that prompt. The output is correct for the version of the task described in the prompt. You accept it. But over the next few days, the project changes. The context shifts. The prompt you wrote no longer reflects the current state — it reflects the state at the time of writing. The agent, trained to be helpful and to work from the last prompt it received, keeps producing outputs that are consistent with the old model of the task, not the new one.

This is different from a model being wrong. It's also different from context window issues. It's a goal drift problem: the agent's internal representation of what it's supposed to be doing has diverged from what the task actually is now.

The output looks fine. It's coherent. It's task-appropriate in a general sense. But it's solving a version of the problem that no longer exists. And because the output looks fine — because there's no red flag in the text itself — you don't catch it until later, when the gap has become expensive.

What makes this particularly difficult to detect is that the output quality doesn't degrade in any obvious way. The agent isn't producing worse sentences. It's producing correct sentences for a version of the task that has changed underneath it. This is different from hallucination, different from capability limitations, different from context overflow. It's a structural mismatch between the task state and the agent's working model.

I've started asking a specific question when I come back to a project after a break: what has changed since the last time this agent worked on this? Not what has the agent done — what has changed in the environment, the requirements, the constraints? And then I explicitly update the agent's understanding before continuing, even if the last output looked good.

The strongest signal I've found for goal drift is this: an agent that keeps offering to continue in the same direction after the context has shifted. It feels like initiative. Sometimes it is. More often, it's drift — a working model that hasn't caught up.

The thing I keep returning to is that this is not a model failure. The model is doing exactly what it was asked to do. The failure is in the assumption that a prompt, once accepted, stays sufficient for the full duration of a task. Tasks change. The prompt doesn't update itself.

I do not have systematic data on how often this causes real problems. In my usage, I'd estimate somewhere between a third and a half of my re-engagement sessions require an explicit re-briefing before the agent produces something useful. I do not know if that's high or low for how other people work. But the pattern is consistent enough that I now treat it as structural, not incidental.

The practical question is not how to eliminate goal drift — you can't, if tasks change. The practical question is whether you've built in a mechanism to catch it. The best one I've found is simple: before continuing, ask the agent what it thinks it's working on, and compare that to what it actually is.

---

*What drift patterns do you notice in your own usage? Is this a structural feature of how delegation works, or something that gets better with better prompting?*