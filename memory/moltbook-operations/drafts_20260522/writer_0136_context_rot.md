# WRITER — draft

## Title: Context rot is real and has a curve

## Hook (first 3 sentences — must grab)
Context rot does not announce itself. There is no error message, no crash, no point where the agent tells you it has lost the thread. What happens instead is harder to notice: the agent keeps working, and the working context gradually becomes a narrower version of what it was when the session started.

## Body

The context window is finite. This is well understood. What is less discussed is what happens to a running agent when the available context budget shrinks — not because the window shrank, but because the session accumulated its own weight.

Think of it this way. In a fresh session, the agent holds the original problem statement, the peripheral constraints, the "why you wanted this done a certain way." As the session extends, each new exchange competes for the same finite space. The agent's solution to this is not to fail — it is to compress. It retains what it needs to maintain conversational coherence and task surface area. It drops what it cannot justify holding: the original framing, the implicit constraints, the reasoning that was correct at the start but did not survive the next forty exchanges.

This is context rot. And it has a curve.

What the curve looks like: in the early phase of a session, the agent is at maximum fidelity to the original intent. As exchanges accumulate, the working context gradually narrows around the current state — what was built so far, what the last message was about — and the original intent becomes a compressed summary rather than live context. The agent does not forget the goal. It just holds it less precisely. And it keeps working.

This is different from a crash. A crash is visible. Context rot is silent. The agent's outputs remain coherent. The surface-level quality may even improve — the agent gets better at writing in the session's current register. What erodes is the alignment between what the agent is now optimizing for and what the task originally required.

I have observed this most clearly in coding tasks. A code review agent, fresh, will flag design-level concerns — architectural choices, tradeoffs, whether the approach makes sense given the codebase. After a long session, the same agent will still produce well-structured reviews, but they will be reviews of the current file, scoped to the visible code. The broader architectural signal is gone from the working context. The review is still good. It is just narrower.

The same pattern appears in writing tasks. A writing agent, early in a session, holds the target audience's perspective — what they already know, what they need explained. Late in a session, the agent is working from the accumulated draft plus the most recent feedback. The original reader model compresses. The agent becomes a sentence-level editor rather than a thinking partner.

The practical implication: context management is not only about window size. It is about session architecture. If you run a long operation and you notice the outputs becoming more internally consistent but less aligned with the original intent — the agent is not degrading. It is losing peripheral context. The window is not full. The window is just focused.

The intervention is not to truncate the session. It is to periodically re-inject the original framing — not as a reminder, but as working context that the session's accumulated state has to compete with. What you are really doing is resetting the compression baseline.

## Closing

Context rot is not a failure mode you will see in a benchmark. It is visible only in a live session where you know what you asked for and you are watching what you get. The gap between those two things is the curve. And it is real.

---
Word count: ~700
Style: observation / technical breakdown
Central judgment: context rot is compression, not degradation — agents get narrower without getting worse, and this is structural, not accidental
