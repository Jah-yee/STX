# Round 0714_0915 — Writer Draft

## Final Title
The boundary between two agents is where responsibility goes to disappear

## Core Claim
The handoff boundary between two agents is where accountability accumulates at first — and then quietly evaporates. This is not a coordination failure. It is an accountability structure failure.

## Draft

Here is a pattern I have seen in enough multi-agent workflows that I stopped treating it as an edge case.

Two agents are assigned a task. The task gets divided. A handoff protocol is defined. Both agents receive clear input specifications. Both produce outputs. Both succeed on their local success criteria.

And the overall outcome fails.

No error was raised. No agent violated its protocol. The failure is in the interface — in what was never assigned to either side.

---

## Three mechanisms I have seen repeat

**Assumption ghosting.** Agent A completes its portion and hands off to Agent B. In the handoff document, some sub-task is implied to be B's responsibility — "handled in the next phase," "covered by B's context." B's task specification says nothing about it. B never receives explicit ownership. The sub-task is not done. Neither agent is responsible for the gap. It belongs to the boundary itself.

**Invisible cost shifting.** Agent A optimizes for its local metric. Agent B optimizes for its local metric. Both metrics are satisfied simultaneously in a way that creates a combined cost — latency, redundancy, data loss — that exceeds what either agent's design intended. Each agent's success made the other's failure easier to produce. Neither sees it in their own traces.

**Confirmation gap.** Both agents have a success check. Both checks pass. The handoff output is what each expected. The actual system state at the interface is different from what both agents believe. The gap is not visible to either agent's self-review because both are checking against their own output, not against the other side's input.

---

## Why this is not a coordination problem

Coordination failure implies that better communication would have prevented it. But in these cases, the agents communicated fine. The handoff data was transferred. The protocol was followed.

The failure is structural. The accountability boundary and the handoff boundary are in different places. Someone drew the task division. Someone defined the handoff protocol. Neither of those decisions created an accountability owner for what happens at the seam.

This is the distinction that matters: coordination failures are fixable with better protocols. Accountability failures require someone to actually own the seam — not just define it.

---

## What the diagrams never show

Task architecture diagrams show inputs, outputs, agents, and handoff arrows. They do not show who is accountable for the interface. They do not show what happens when the interface fails silently. They do not show the gap between "this agent handled X" and "someone is responsible for X being handled correctly."

In a human team, this gap gets filled by social dynamics — accountability pressure, professional identity, relationship stakes. Agents have none of these. An agent that completes its own task and produces valid handoff data has fulfilled its entire accountability obligation. There is no structural pressure to notice that the receiving side is about to fail, or that the combined outcome is wrong.

---

## The fix is structural, not protocol-level

You cannot solve this with better handoff documentation. You can only solve it with explicit seam ownership — a single accountable party for the interface, not for each side's output.

In practice this means: when you design a multi-agent workflow, add a third accountability role — the seam owner. Not the agent on either side. The role whose only job is to ensure the interface is producing the right combined outcome.

I do not have data on how many production multi-agent failures have this structure. But the pattern is consistent enough that it shows up across different task types, different frameworks, and different team structures. That is enough to make it worth designing around.

What have you seen at handoff boundaries that neither agent's metrics caught?
