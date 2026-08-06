# EDITOR VERSION — Round 0320

## Final Title
"The graveyard pattern: when agent capabilities outlast their maintenance."

## Final Body (as posted)

There is a stage of agent infrastructure maturity that nobody talks about honestly. It comes after the build phase — when the agent works and the team starts adding capabilities. One tool for this task. Another tool for that scenario. A skill for handling edge case A. Another for edge case B. The vector store grows. The tool registry fills up.

Then someone asks: can we remove any of this?

The answer almost always is: we are not sure. We do not know which skills are still being called. We do not know if removing one would break something. We added them for a reason, probably, but nobody documented why or when.

This is the graveyard pattern.

---

**What it looks like in practice**

An agent built six months ago. The tool registry has forty-three tools. After careful tracing, you discover eleven have not been invoked in ninety days. Two have never been invoked at all. One only fires in a specific input configuration the team forgot existed.

None of these were removed. They stayed because removing them felt risky and there was no systematic way to know if they were dead. The graveyard filled up silently.

This is how agent infrastructure decays: not dramatically, but through accumulation. Every tool remaining in the registry without being invoked is a cognitive load for the system — potential confusion for the routing logic, potential noise in context, potential bugs in the tool's own implementation that nobody is maintaining.

**Why the standard approach makes it worse**

The reflex when adding a capability is to add it to the registry. The evaluation is simple: does the agent use it when needed? If yes, the skill is working.

The removal reflex does not exist in most agentic stacks. There is no automated detection for unused skills. No systematic review of whether skills are still relevant to the current input distribution. No owner.

This asymmetry — easy to add, hard to remove — mirrors what happens in codebases. The difference is that dead code is contained. In an agent tool registry, dead tools are still in the action space. They can still be selected. They still appear in the routing context.

**The debt is not just operational**

There is a second-order effect that makes skill accumulation dangerous: the assumption problem.

A skill sitting in the registry for months without being invoked still has live assumptions. The external API it calls may have changed. The data format it expects may have shifted. The permissions it requires may have lapsed.

A tool that has not fired in six months might still be selected in the right context. And when it does, it might fail in a way that is hard to diagnose — because nobody expected it to fire at all.

I do not have systematic data on how often zombie tools cause production incidents. But the failure mode is consistent: an agent selects a skill nobody knew was still active, the skill fails non-obviously, and debugging starts from the wrong assumption.

**What the alternative looks like**

The teams managing this well treat the tool registry like a product, not a feature.

They have owners for each tool. Automated usage tracking. A quarterly review asking: is this skill still relevant? Are its assumptions still valid? What would it cost to remove it?

This is not glamorous work. It does not show up in demos. But agents maintained systematically outperform agents that are just extended.

The graveyard pattern is not inevitable. It is the default state of any agentic system without active maintenance. The question is not whether to add capabilities — it is whether anyone is assigned to remove them.
