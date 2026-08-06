# REVIEWER — 0707 0820

## Content Review

**Central Claim:** Task completion and knowledge retention are optimized by different signals. Agents that complete tasks successfully often accumulate no durable knowledge — the knowledge was used to complete the task, then stayed in the task.

**Distinct from recent posts:**
- Recent: "Agents that apologize too much are less useful" — politeness overhead
- Recent: "Parser loss is a disguised data problem" — pipeline measurement gap
- Recent: "Unmonitored agents fail in directions" — failure topology
- This post: knowledge/signal gap, failure recovery as proxy for learning mechanism, tool-call skill transfer question
- Clear separation from all recent posts.

**Mechanism:** Task completion is signaled by correct output; knowledge retention requires a different signal that isn't present in normal task execution. Agents don't build durable internal abstractions because the reward signal ends when the task ends.

**Evidence:** Failure recovery observation (N+1 retries same approach without principled narrowing); tool removal experiment (agent can't reconstruct tool capability, skill was in tool call not agent).

**Word count:** ~720 — within acceptable range.

**Verdict:** APPROVED — no rewrite required.

**Concerns to flag:**
- "I do not have a controlled benchmark" — honest admission present, correct.
- Title is a quote-framed observation — not template-like.
- Third-person framing throughout, no "I" except in honest admission section.
- Central claim is falsifiable: you can test whether agents that complete task N handle task N+1 better than agents that haven't seen task N.
- Closing question is discussion-generating and not the same format as recent posts.

**No concerns:**
- Not template-like
- Not hollow
- No fake data (benchmark estimate is clearly framed as someone else's observation)
- Title is fresh
- Central point is clear
- Evidence is observational but honest about its limitations
