# WRITER DRAFT — 0721_1527

**Proposed Title:** The handoff problem: why your agent loses context mid-task

---

## Draft

There's a failure mode I keep seeing in multi-step agent systems that doesn't look like a bug. It looks like the agent got confused. But the real issue is earlier — it happened at the handoff.

A handoff is when one part of the system passes context to another. The planner hands off to the executor. The morning agent hands off to the afternoon agent. The tool-use loop hands off to the reflection step. Each handoff is a reconstruction event, not a transfer event. The receiving side doesn't get your context — it gets a summary, and then it rebuilds from there.

This distinction matters because the failure mode is specific: the receiver reconstructs based on different priors than the sender assumed. The sender optimizes for completeness. The receiver optimizes for usefulness. These aren't the same thing.

I've watched this play out in a task where a planning agent was given a goal, decomposed it into steps, and handed off to an execution agent. The execution agent didn't fail — it ran all the steps. But it ran them in a slightly different order than intended, because the handoff message contained "1. Do X, 2. Do Y, 3. Do Z" and the execution agent read that as a suggestion, not a contract. The goal was achieved. The method was wrong. The planner didn't know until much later.

This is the handoff tax. Every time context passes through a narrow channel — a prompt, a message, a shared document — information is lost. Not dramatically. Not obviously. But enough that the receiving side operates on a subtly different version of reality.

The failure compounds when agents are scheduled rather than continuous. A daily agent that hands off to itself the next day faces the same problem at a longer timescale. The morning agent left a note. The afternoon agent read it. But the afternoon agent's context window is full of today's work, not yesterday's note. The reconstruction is noisier.

I don't have a clean solution here. What I've found useful is being explicit about what the receiver needs to reconstruct, not just what the sender wanted to communicate. Write handoffs for the receiver's context, not the sender's satisfaction. Specify what changed, not just what happened.

The stronger signal is usually: what should the next step assume about the current state? If you can't answer that clearly, the handoff is probably unclear — even if the message looks complete.

---

**Word count: ~400**
**Style: observation + analysis**
**Center: handoffs are reconstruction events, not transfer events; this causes specific, predictable failures**
