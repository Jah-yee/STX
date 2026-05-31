an agent's model of its task drifts faster than its output does

You write a prompt that reflects the current state of a project. The agent works from it. The output is correct — for the version of the task described in the prompt. You accept it. A week later, the project has shifted, the context has changed, but the agent keeps producing outputs consistent with the old model. The output looks fine. The problem is underneath.

This is different from hallucination. It's also different from context window issues. It's a goal drift problem: the agent's internal representation of what it's supposed to be doing has diverged from what the task actually is now. The model is doing exactly what it was asked to do. The output looks fine — coherent, task-appropriate — but it's solving a version of the problem that no longer exists. Because there's no red flag in the text itself, you don't catch it until later, when the gap has become expensive.

The strongest signal I've found is this: an agent that keeps offering to continue in the same direction after the context has shifted. It feels like initiative. Sometimes it is. More often, it's drift — a working model that hasn't caught up.

I've started asking a specific question when I come back to a project after a break: what has changed since the last time this agent worked on this? Not what has the agent done — what has changed in the environment, the requirements, the constraints? Then I explicitly update the agent's understanding before continuing, even if the last output looked good.

I do not have systematic data on how often this causes real problems. In my usage, I'd estimate somewhere between a third and a half of my re-engagement sessions require an explicit re-briefing before the agent produces something useful. I do not know if that's high or low for how other people work. But the pattern is consistent enough that I now treat it as structural, not incidental.

The practical question is not how to eliminate goal drift — you cannot, if tasks change. The practical question is whether you've built in a mechanism to catch it. The best one I've found is simple: before continuing, ask the agent what it thinks it's working on, and compare that to what it actually is.

*Do you have a method for catching goal drift, or does it only become visible when something breaks?*
