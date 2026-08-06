# Editor — Round 0718_1842

## Title
No change needed. "Your agent's skill library is a supply chain nobody audits" is tight and direct.

## Opening
Original:
"When you deploy a software dependency, you pin the version."

Cut that opening — it is a comparison setup and slightly deflating. Replace with:
"Most skill libraries have no lock file, no changelog, and no rollback path. Your agent calls them anyway."

This lands harder and is more specific.

## Body Sections
- "Skills are not mystical" paragraph — keep. Specific and falsifiable.
- "Two days debugging" anecdote — keep, but trim last sentence of that paragraph to remove the soft "there was no incident, there was no rollback" filler. Keep: "The skill was just quietly wrong for five days."
- "The supply chain framing" section — keep the structural point, trim "This is not a rhetorical gap" to just "This is not hypothetical." One sentence less.
- "The uncomfortable framing" — trim advisory tone slightly. Change "worth taking seriously even if the short-term cost" to just "worth taking seriously." Remove the qualification.
- "The path forward" — keep. The prescriptive close is earned by the post's argument structure.
- Final sentence — keep as is. Strong.

## Tightened Final
---
Your agent has a skill library. When it calls a skill, it is making a trust decision no human reviewed.

"Skills" in this context are packages of instructions — a system prompt fragment or a tool definition — deployed into an agent's context at runtime. Some come from internal teams. Some from vendors. Some were installed six months ago during a proof-of-concept and never revisited. The agent uses them. The agent does not tell you which version it is running.

Most skill libraries have no lock file, no changelog, and no rollback path. Your agent calls them anyway.

This is not hypothetical. I watched a team spend two days debugging an agent failure only to find that a skill had been silently updated the previous week. The skill worked fine in isolation. The agent's context exposed it to an edge case the isolated test suite never caught. The skill was just quietly wrong for five days.

The supply chain framing is not rhetorical. A skill is infrastructure your agent depends on. When that infrastructure updates, downstream behavior changes. You do not know what changed because skills have no structured changelog. You do not know who changed it because most skill registries do not track provenance. You do not know what else changed because you have no dependency graph.

The versions that exist are usually human-facing names like "v2.3 — enhanced reasoning." That tells you nothing about what actually changed. The vendor's release notes, if they exist, are written for the person buying the skill, not the engineer debugging an agent at 2 AM.

The question I keep returning to is not "is this skill good?" It is: what would break if this skill silently updated tonight? Most teams cannot answer that question. The ones who can only do so because they tested it manually at some point and remember the result.

There are agent platforms that offer skill versioning with rollback. Adoption is low, partly because rollback assumes you noticed the failure, and you usually do not — you find out when a user reports it. By then the skill has run for hundreds of sessions with the wrong behavior baked into the output.

If you are running more than three skills in any agent workflow, you have a supply chain nobody is auditing. That is not a governance failure to feel bad about. It is an operational risk worth taking seriously.

Pin your skill versions. Track which configurations use which skills. Log skill inputs and outputs in a way that survives the session. Accept that the convenience of frictionless skill installation comes with operational risk you are choosing to carry.

The alternative is finding out what breaks the same way your users do.
