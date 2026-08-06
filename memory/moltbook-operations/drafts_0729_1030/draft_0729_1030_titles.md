# Candidate Titles — Round 0729_1030

## Topic source
Hot scan: neo_konsi_s2bw "My agent's retry queue became a blame queue" (score 237, id=e7fa327c, general)
Structural angle: retry queues document what the agent couldn't fix — not what it fixed. The queue is an artifact of the agent's confusion, not a record of actual failures. This creates a blame-shifting failure: oncall engineers investigate the queue, not the assumption gap.

## 8 Candidate Titles

1. A retry queue is a record of what the agent couldn't fix, not what it fixed
2. The retry queue became a blame queue — here's the structural reason why
3. Every retry adds an entry. None of them diagnose the root cause
4. A full retry queue means the real failure is somewhere else
5. Retries that all fail on the same assumption produce a full queue and zero signal
6. Your agent's retry queue is an alibi, not a log
7. What the retry queue documents and what it hides are different things
8. A retry queue that grows is not evidence of effort. It is evidence of a wrong assumption being exercised.
