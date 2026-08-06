# WRITER — draft_0619_0642

## Title
Agent skills are becoming software, not just prompts.

## Body

Three years ago, "giving an agent a skill" meant writing a better system prompt. Today it means publishing a Python package with typed inputs, versioned dependencies, and a changelog. That shift is not cosmetic — it changes what reliability looks like.

When skills were prompts, the failure mode was misalignment: the agent misread the instruction, picked the wrong context, or drifted from the intended behavior. Fixing it meant rewriting the prompt, sometimes dozens of times, until it stuck. The skill lived in the model's weights and the model's context window. It was fragile by architecture.

When skills become software, the failure mode changes. Now you have import errors, version conflicts, broken type contracts, and CI failures on a skill that worked last Tuesday. The agent's behavior is still wrong, but the bug is in the build system, not the prompt. You're debugging a deployment pipeline, not a conversation.

This is a genuine trade-off, not an upgrade. More explicit structure gives you reproducibility, testability, and composability — things prompts never had. But it introduces an entirely new category of operational failure. The teams that are moving fastest into "skills as software" are also discovering that their incident rate hasn't dropped. It's migrated.

I notice this most clearly when I look at what actually breaks in production agent systems. Six months ago, most incidents traced back to prompt ambiguity or context overflow. Today, a growing fraction trace to dependency version mismatches, skill registration race conditions, or the skill registry going down. The failure mode shifted because the implementation shifted.

What changed is not the agent's capability. What changed is where the agent's capability lives. When the capability lives in a prompt, it's a model problem. When it lives in a software package, it's an infrastructure problem. Both problems are real. Neither is automatically smaller than the other.

The honest observation is that "skills as software" solves some reliability problems and creates others. If your team is moving in this direction, the question worth asking is not whether software is more reliable than prompts — it's whether you're ready to own the new class of failures that comes with it. Because those failures look like DevOps problems, not AI problems, and your AI team may not have the right instincts to debug them quickly.

That gap is where incidents live right now.