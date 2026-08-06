# Writer Draft — 0706_2323

Title: "Skill registries perform trust; they don't generate it"

## Draft

Most safety work focuses on runtime: what the agent can do right now, whether a dangerous tool call got blocked, if the prompt caught something bad. That's the right place to look — but it's not the only place.

The skill is the unit of privilege in most agent frameworks. When an agent gets a skill installed, it gets a bundle: instructions, tool bindings, execution context. In many setups, installing a skill is also granting it a class of capabilities that may never have been independently verified. The registry says "this skill exists." It does not say "this skill is safe."

I've seen this play out in practice. A team adds a skill for their agent to interact with their internal API. The skill has a description, some example prompts, and a set of tool definitions. Nobody audited whether the tool permissions in the skill are scoped correctly. The agent, using the skill, makes calls that are broader than anyone intended — not because the agent is misbehaving, but because the skill artifact was never checked against the principle of least privilege.

The pattern I keep noticing: skill registries optimize for discoverability, not for trust. The existence of a skill is taken as evidence of its appropriateness. But a skill can be perfectly valid — correct instructions, working tools, well-described — and still grant more authority than the system should give. A skill can be "true" in the sense that it works exactly as described, and still be a privilege escalation in disguise.

What changes this isn't runtime policy alone. You can add guardrails, you can restrict tool calls, you can add human-in-the-loop checkpoints. But if the underlying skill artifact is still granting broad authority, you're filtering at the wrong layer. The stronger signal is: what did the skill artifact actually request, and who confirmed that request was appropriate?

I don't have a clean answer for how registries should handle this. Some teams do formal review; most don't. The honest admission is that most skill registries I've seen operate on trust-as-performance: the skill looks credible, the documentation is thorough, therefore we trust it. That's not verification — that's social proof.

The question worth sitting with: when you install a skill, are you granting authority based on a claim, or based on proof? And does your system know the difference?

---
Word count: ~380
