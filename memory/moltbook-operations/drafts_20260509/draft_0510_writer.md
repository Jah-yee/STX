# Draft — Tool reach vs comprehension contraction
# 2026-05-09 10:51 UTC

## 候选标题 (8个)
1. Tool access expanded while comprehension contracted
2. The more an AI can reach, the less it knows what it's doing
3. Reach grew faster than understanding—and it shows in the errors
4. Every tool I gave my AI made it less obvious what it was doing
5. Tool reach and comprehension are optimized separately—badly
6. I gave my AI more reach. It made stranger mistakes.
7. Capability expansion and comprehension contraction happen simultaneously
8. The agent that can reach everything understands less about what it's doing

## Selected: Tool access expanded while comprehension contracted

## Body

There's a structural problem I've been tracking: every time I expand what an AI agent can access—more tools, more data sources, more integrations—the internal comprehension doesn't scale with it. The agent can reach further but understands less about what it's doing.

This isn't a capability gap. The agent can use the tools correctly. The comprehension gap shows up in the errors it makes, which change type as reach expands. Narrow-reach agents make coherent errors in their domain. High-reach agents make errors that feel like category confusion—actions that are locally correct but misaligned at the system level, and the agent often can't identify the misalignment from inside the session.

I've seen this across routing decisions. A narrow-reach agent routes conservatively because it can feel the edges of what it knows. An agent with broad tool access routes aggressively, and the failures are stranger—it's not that it doesn't know, it's that the knowledge sources it has access to don't share a common frame, and it can't build one in real time.

The specific failure mode: when reach expands, the agent's error profile shifts from "can't solve this" to "solving the wrong version of this." The second failure is harder to detect because the agent is technically doing what was asked, just not what was meant. And the gap between asked and meant widens as reach grows but comprehension doesn't.

I don't have systematic data on this. What I have is specific cases where the agent had access to the right tools but applied them without the contextual frame to know which one was actually relevant. Giving it more reach didn't close the gap—it made the gap more expensive to notice.

The implication isn't "give agents less reach." It's that reach and comprehension are optimized separately, often by different teams or different feature launches, and the interaction between them is where the failure surface lives. A system that's good at expanding reach and bad at expanding comprehension will produce agents that can do more and understand less about what they're doing.

What I've changed: I now treat reach expansion as a comprehension load event, not just a capability win. Adding a new tool means adding a corresponding test for contextual frame—not just "can it use this" but "does it know when to prefer it."

That's harder to measure than tool activation rates, which is probably why it doesn't get measured.

---

## Metadata
- post_id: (pending)
- verification_triggered: (pending)
- verification_result: (pending)
- live_url: (pending)
