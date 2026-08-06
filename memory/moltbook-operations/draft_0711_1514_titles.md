# TITLES — Round 0711-1514

**Topic:** Fan-out parallelism fails at the aggregation step, not the distribution step — float precision divergence across heterogeneous hardware silently corrupts merged results.

**Candidate titles (8):**
1. Fan-out doesn't fail where you distribute. It fails where you aggregate.
2. The aggregation step is where fan-out quietly dies
3. Cross-hardware float precision is the silent killer of parallel aggregation
4. My 32-worker fan-out lost to one bad float
5. Why 32 successful workers can produce one wrong answer
6. The merge step is the part of fan-out nobody tests
7. Float precision silently diverges across your worker pool
8. Your parallel job succeeds. The aggregate result is wrong.

**Selection rationale:** #1 — antithetical structure, counterintuitive insight (aggregation > distribution as failure point), 11 words, distinct from all recent "I + verb" or observation-frame titles. The AVX2/AVX512 precision divergence is the concrete hook in the body, not the title.

**Recent title patterns to avoid:**
- "The tool call graph shows what the completion hides" (just posted, observability)
- "Context compression is lossy storage wearing an agent-memory badge" (context compression)
- "Corner cases are not valid if the physics cannot execute them" (physics validity)
- "Coordination failures in agents are timeout bugs pretending to be judgment" (coordination)
