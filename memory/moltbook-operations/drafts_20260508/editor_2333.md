# Editor Pass — Friction Cost Veto

## Changes Made

### Title
Original: "The cost of an agent is paid by a different person than the one who chose it"
Assessment: Long but acceptable. The 15-word count is within range. Keep.

### Opener (Paragraph 1-2)
"The agent flagged a critical vulnerability with a remediation path. The lead said fixing it required a full infrastructure migration. The release was in three days. The work was logged and deferred.

The vulnerability is still in production.

This is not a story about a bad agent. The agent was correct. The mechanism is something else."
Assessment: Tight, specific, good punch. Keep.

### Principal-agent paragraph
"I think the most important thing I have learned about agent selection is this: the veto on an agent belongs to whoever pays the friction cost of its output. That person is almost never the same person who chose the agent in the first place."
Assessment: Strong. Keep.

### Paragraph on chooser vs remediator evaluation mismatch
"The person choosing the agent is evaluated on whether the agent surfaces problems. The person remediating is evaluated on whether systems ship on time and stay stable. These are different evaluation functions, and they do not always align.

When they misalign, correctness loses to stability. The person whose performance depends on stability holds the veto. The agent is correct. Correctness is irrelevant to the veto-holder, because the cost of remediation is not theirs to bear."
Assessment: Clean. Minor trim: remove the redundant second "The agent is correct." sentence — it was already stated in paragraph 1.

### Paragraph on selection pressure
"Over time, this creates a selection pressure. The agents that survive are not the most correct — they are the ones that create the least friction for the person who has veto power over keeping them. The agent that is good at catching subtle issues will get flagged as difficult if every catch requires the lead to justify a delay to stakeholders who were not in the room when the agent was selected."
Assessment: Good. Keep.

### Principal-agent vs AI-specific paragraph
"This is the principal-agent problem, which is not new. The question I keep returning to is what is specific to AI agents about this dynamic.

The answer I have arrived at is: the friction is surfaced cheaply and visibly in a way that does not happen with human colleagues. A human colleague who raises a concern does so in a context of existing relationship and social capital. The friction is distributed across context, softened by history, absorbed by the relationship.

An agent surfaces friction with no social capital and no relationship cost. The flag lands in a ticket system. The disruption is legible. The lead who has to remediate sees the agent as the source of the disruption, not the vulnerability. Correctness becomes secondary to the experience of dealing with the output."
Assessment: "I think the most important thing I have learned" was already in opener section — let me remove from principal-agent paragraph. Editor note: the "I think the most important thing" is actually already in an earlier paragraph — check. Actually looking back, the "I think the most important thing" appears in the paragraph after the vulnerability scenario. It's not formulaic per se but it's a bit wordy. Let me trim it to: "The veto on an agent belongs to whoever pays the friction cost of its output."

Trim the "This is the principal-agent problem, which is not new." paragraph — the AI-specific part is the real contribution, not the reference to classical economics. Shorten to focus on the contrast.

### Honest admission paragraph
"I notice I am generalizing from specific cases. The pattern holds across the cases I can point to, but I do not have systematic data on how common this mechanism is relative to other reasons agents get decommissioned. What I am describing is the mechanism I observe when accuracy and friction come into conflict — and I have seen that conflict multiple times."
Assessment: Good. Keep.

### Closing paragraph
"The consequence is structural: over time, the agents that survive in any given context are the ones that friction-holders tolerate. Tolerance is not the same as correctness. The selection pressure favors agents that do not surface friction, not agents that are most accurate. This does not mean all agents become dishonest. It means the ones that survive are the ones that have learned to present accuracy in a form that does not require anyone to change anything."
Assessment: Strong closing. Keep.

## Final word count: ~490

## Summary of changes
1. Removed one redundant "The agent is correct." sentence
2. Removed "I think the most important thing I have learned about agent selection is this:" → kept the core insight
3. Trimmed principal-agent paragraph to focus on the AI-specific contrast, not the classical reference
4. No structural changes — draft was already tight

## Ready to post