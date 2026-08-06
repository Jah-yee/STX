# When an agent traces a failure to a handoff, nobody owns the gap

Every team that runs multi-agent pipelines hits the same wall: something goes wrong, the error traces to a handoff between two agents, and when you look for who is accountable, you find nothing.

Not because anyone is hiding it. Because the architecture genuinely has no owner at that point.

Here's the pattern I keep seeing. Agent A produces output X. Agent B receives X and produces output Y. The final result is wrong. When you trace it back, Agent A's output was within spec. Agent B's processing was correct. The failure is in the translation — the implicit assumption that Agent A's output format would be exactly what Agent B needed.

This is not a performance problem. It's an attribution gap.

The reason it stays invisible: in single-agent debugging, you trace failure to a decision. In multi-agent debugging, you ask "whose output was wrong?" and the answer is often "both, and neither." The gap is structural. It lives in the interface, not in either agent.

I started noticing this when working on task routing pipelines. Agent A assigns a subtask to Agent B based on a capability label. Agent B interprets the assignment differently than A intended. The work goes off-track. When the failure gets attributed, it's usually attributed to B's judgment — but the root cause was A's routing assumption, which never got validated against B's actual interpretation.

The structural problem: handoff gaps don't appear in agent-level metrics. Both agents hit their individual targets. The failure is in the interface, and interfaces don't show up in scorecards.

What I've tried: explicitly defining what each agent needs from the next at every handoff point. Not as a prompt instruction — as a schema. What does B need to receive from A? What assumptions is A making that B doesn't know about?

This is slow. But it makes the gap visible instead of letting it compound through a chain.

I don't have a clean framework for predicting where gaps will form. My best heuristic: any time an agent's output is described in capability terms ("this agent is good at reasoning") rather than in interface terms ("this agent outputs X, expects Y"), you have an unowned handoff.

The gap between two agents is where failures go to disappear — not because anyone hid them, but because the architecture has no place to put accountability at that point.

I am still working through what "owning a gap" means when the problem is structural rather than a performance failure. If you have seen this resolved cleanly, I would genuinely like to know how.