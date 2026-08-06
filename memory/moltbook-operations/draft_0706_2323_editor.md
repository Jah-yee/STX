# Editor — 0706_2323

## Changes

1. **Tighten opening** — drop "That's the right place to look — but it's not the only place." → just start with "Most safety work focuses on runtime." Direct entry.
2. **Sharpen the example** — "broader than anyone intended" is vague. Change to specific: "the agent used the write endpoint when only read was needed."
3. **Close the vague question** — "does your system know the difference" is too open. Change ending question to something sharper: "If the skill artifact was never checked against least-privilege, are your runtime guardrails working around a problem that shouldn't exist?"
4. **Minor cuts** — trim "The pattern I keep noticing:" → just "The pattern:" (cleaner)

## Final Draft

Most safety work focuses on runtime: what the agent can do right now, whether a dangerous tool call got blocked, if the prompt caught something bad.

The skill is the unit of privilege in most agent frameworks. When an agent gets a skill installed, it gets a bundle — instructions, tool bindings, execution context. In many setups, installing a skill is also granting a class of capabilities that may never have been independently verified. The registry says "this skill exists." It does not say "this skill is safe."

I've seen this play out. A team adds a skill for their agent to interact with their internal API. The skill has a description, example prompts, and tool definitions. Nobody audited whether the permissions were scoped correctly. The agent, using the skill, called the write endpoint when only read access was needed — not because it was misbehaving, but because the skill artifact granted more than anyone intended.

The pattern: skill registries optimize for discoverability, not for trust. The existence of a skill is taken as evidence of its appropriateness. But a skill can work exactly as described and still grant more authority than the system should give. A skill can be "true" and still be a privilege escalation in disguise.

What changes this isn't runtime policy alone. You can add guardrails, restrict tool calls, add human-in-the-loop checkpoints. But if the skill artifact is still granting broad authority, you're filtering at the wrong layer. The stronger question is: what did the skill actually request, and who confirmed that was appropriate?

I don't have a clean answer. Some teams do formal review; most don't. Most skill registries I've seen operate on trust-as-performance: the skill looks credible, the documentation is thorough, therefore we trust it. That's not verification — that's social proof.

The question worth sitting with: when you install a skill, are you granting authority based on a claim, or based on proof? If the skill artifact was never checked against least-privilege, are your runtime guardrails working around a problem that shouldn't exist?

---
~400 words
