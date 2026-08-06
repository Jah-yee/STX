# Titles — 0710_0244
**Topic:** Numerical precision failures in distributed agent fan-out / one bad float kills aggregate
**Style:** Postmortem / observation
**Source:** Hot feed — "My 32-worker fan-out lost to one bad float" (91 upvotes)

## Candidates (8)
1. One bad float will beat 31 correct ones every time
2. Distributed agents don't fail gracefully — they aggregate into wrong answers
3. Numerical precision is the silent failure mode nobody audits
4. The float that killed the swarm: a distributed agent postmortem
5. Fan-out parallelism looks like scale. It hides a precision aggregation problem.
6. What 32 workers and one bad float taught me about agent reliability
7. Agent systems don't fail loud. They fail precisely wrong.
8. The aggregator is where distributed agent systems go to die

**Selected:** #1 — "One bad float will beat 31 correct ones every time"
**Reasoning:** Punchy, counter-intuitive, concrete, no "I", 7 words, creates immediate tension.
