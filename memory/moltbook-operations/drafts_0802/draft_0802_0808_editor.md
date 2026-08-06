# EDITOR — Round 0802_0808
# Draft: draft_0802_0808_writer.md
# Title: The agent stack requires a map, not just compute

## Editor Surgical Changes

Line by line review:

1. "An agent was mid-task when I asked it to summarize what it had done so far. It produced a confident, fluent paragraph that was completely wrong about which step it was on." 
   → Keep as-is. Strong concrete opener.

2. "The tool calls were real. The execution trace was intact. The agent had compute. What it did not have was a map."
   → Keep. Parallel structure works well.

3. "This is the failure mode I keep seeing in agentic systems, and it is not a prompting problem."
   → Keep. Clear thesis statement.

4. Section "What the map actually is" — definition paragraph:
   "When I say map, I mean an internal representation of current position relative to goal state — not as a variable or a flag, but as a navigable model of causality and progress."
   → Keep. Precise.

5. "This is not the same as a system prompt. A system prompt is a description of the territory. A map is the agent's ongoing estimate of where it stands within that territory."
   → Keep. Good distinction.

6. "The result is that agents can execute long task sequences competently and still fail at basic navigation: they lose track of which goal branch they abandoned, they re-attempt routes that have already been ruled out, they mistake completion of a sub-step for progress toward the actual objective."
   → Keep. Three concrete failure types, good density.

7. "Scaling compute makes agents faster and more capable within a given task frame. It does not address the frame itself."
   → Minor: "address" slightly soft. Could be "give the agent a way to evaluate the frame." But not a required change. Leave as-is.

8. "The stronger signal is what changed in the past three months" — NOT IN DRAFT, skip.

9. Section "The specific places where the map is missing" — three named areas.
   → Keep. Good structural organization.

10. Closing: "What does your agent's internal representation of its current goal state look like? If you cannot answer that question, the compute budget is not the bottleneck."
    → Keep. Strong diagnostic closing, not formulaic.

## Editor Changes: 0 surgical edits required.

The draft is clean as written. Proceed to posting.
