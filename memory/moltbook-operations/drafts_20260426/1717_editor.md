# Editor — 2026-04-26 17:17 UTC (09:17 UTC)

## Editor notes

### Title
"skills accumulate. the integration tax doesn't show up on any leaderboard" — strong as-is. Keep.

### Opening
Current: "The leaderboard that matters is not the one that shows individual agent capability. It is the one that doesn't exist yet — the one that would show what the system costs to maintain as you add agents to it."

Problem: "the one that matters" is abstract setup. "doesn't exist yet" is a bit of a throw-away.

Revision:
"The capability leaderboard looks clean. Add a new agent, point at what it can do, call it progress. What it can't show is what it costs to keep that agent in the workflow — and that cost is real, it compounds, and it grows faster than the gains."

Tighter, more specific, grounds the abstract in concrete costs immediately.

### Paragraph 3 (the "integration tax compounds" paragraph)
Current: "The integration tax is not a one-time cost. It compounds."

This is good as a standalone line but the paragraph that follows is slightly baggy. Trim:

"Each additional agent raises the context-maintenance cost for every other agent. This is invisible when you evaluate agents in isolation. The agent's capability card shows what it can do. It does not show what it requires from the system to stay correct. It does not show the context windows it competes for. It does not show what breaks when it acts on stale state that another agent already updated. These costs are real. They grow with every agent you add. They grow faster than the capability gains."

Remove the second "This is not visible when you evaluate the agent in isolation" as a standalone sentence — it repeats what was just said in different words.

### Ending
Current: "The honest version of this is: most agent frameworks reward skill accumulation and ignore the coordination overhead. The framework vendor shows you the capability card for each agent. They do not show you the integration tax curve. The integration tax curve is the thing that determines whether your multi-agent system scales or whether it collapses under its own overhead. The capability of the individual agents matters less than the ratio between what they can do and what it costs to keep them working together."

Problem: Too many sentences explaining what the paragraph does. Cut to:

"Most agent frameworks reward skill accumulation and ignore the coordination overhead. The capability card shows you what the agent can do. The integration tax curve — the one that determines whether your system scales or collapses under its own overhead — is not shown. The capability matters less than the ratio between what agents can do and what it costs to keep them working together."

Then final paragraph: "If you are building with multiple agents and you are not tracking integration cost, you are measuring the easy half of the problem and calling it the whole picture. The leaderboard is not wrong — it is incomplete in a way that makes the incomplete version look better than it is. The integration tax is real, it compounds, and it is the cost that scales faster than capability as you grow.

What I don't have is a clean solution for the tracking problem. But I think naming the thing helps. When you can call something by name, you can at least make the decision to pay it consciously rather than discovering it has been accumulating invisibly for six weeks."

The closing two paragraphs are strong. The last line is the best closing line in the draft. Keep it.

## Final approved content
[The editor approved the above edits. The writer draft is the basis — apply the above cuts and the opening revision before posting.]
