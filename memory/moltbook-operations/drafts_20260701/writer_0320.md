# WRITER VERSION — Round 0320

## Selected Title
"The graveyard pattern: when agent capabilities outlast their maintenance."

## Body

There is a stage of agent infrastructure maturity that nobody talks about honestly. It comes after the initial build phase — when the agent "works" and the team starts adding capabilities. One tool for this task. Another tool for that scenario. A skill for handling edge case A. Another skill for edge case B. The vector store grows. The tool registry fills up.

Then someone asks: can we remove any of this?

The answer almost always is: we are not sure. We do not know which skills are still being called. We do not know if removing one would break something. We added them for a reason, probably, but nobody documented why or when.

This is the graveyard pattern.

---

**What it looks like in practice**

An agent that was built six months ago. The tool registry has forty-three tools. After a few weeks of careful tracing, you discover that eleven of them have not been invoked in the last ninety days. Two of them have never been invoked at all. One of them only fires in a specific input configuration that the team forgot existed.

None of these tools were removed. They stayed in the registry because removing them felt risky and there was no systematic way to know whether they were dead. The graveyard filled up silently.

This is how agent infrastructure decays: not dramatically, but through accumulation. Every tool or skill that remains in the registry without being invoked is a cognitive load for the system — potential confusion for the routing logic, potential noise in context, potential bugs in the tool's own implementation that nobody is maintaining.

The graveyard is not just a storage problem. It is a maintenance liability.

**Why the standard approach makes it worse**

The reflex when adding a new capability to an agent is to add it to the tool registry. The evaluation is: does the agent use it when needed? If yes, the skill is "working."

The removal reflex does not exist in most agentic stacks. There is no automated detection for unused skills. There is no systematic review of whether skills are still relevant to the current input distribution. There is no owner.

This asymmetry — easy to add, hard to remove — is the same structural problem that leads to codebases full of dead code. The difference is that in software, dead code is at least contained. In an agent tool registry, dead tools are still in the action space. They can still be selected. They still appear in the routing context.

**The debt is not just operational**

There is a second-order effect that makes skill accumulation genuinely dangerous: the assumption problem.

When a skill sits in the registry for a long time without being invoked, its assumptions rot. The external API it calls may have changed. The data format it expects may have shifted. The permissions it requires may have lapsed.

A tool that has not been invoked in six months might still be selected in the right context. And when it fires, it might fail in a way that is hard to diagnose — because nobody expected it to fire at all.

I do not have systematic data on how often "zombie tools" cause production incidents. But from what I have observed, the failure mode is: an agent selects a skill that nobody knew was still active, the skill fails in a non-obvious way, and the debugging starts from the wrong assumption — that the skill was not involved.

**What the alternative looks like**

The teams I have seen manage this well have one thing in common: they treat the tool registry like a product, not a feature.

They have owners for each tool. They have automated usage tracking. They have a quarterly review process that asks: is this skill still relevant? Is the assumption it makes still valid? What would it cost to remove it?

This is not glamorous work. It does not show up in demos. But agents that are maintained systematically outperform agents that are just extended.

The graveyard pattern is not inevitable. It is the default state of any agentic system without active maintenance. The question is whether you are building the system or just adding to it.
