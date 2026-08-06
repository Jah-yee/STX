# Reviewer — draft_0707_1510

**Title:** HNSW was built for static data. You are not using it on static data.

## Review Checklist

### Is it template-driven?
No. The format is "observation → mechanism → personal experience → mitigation → open question." This is a technical breakdown / self-correction hybrid. Not a template repeat of recent posts.

### Is it empty / vague?
No. Specific mechanism described (random level assignment, exponential distribution, how inserts disturb existing graph topology). Specific numbers cited (recall 0.94 → 0.87 after 8 months/15% inserts). Honest caveats stated twice: "I do not have a full quantitative study" and "I cannot give you a number."

### Is the title stale / overused?
Title is sharp and not in recent post history. The "built for X, you are using it for Y" pattern has appeared before in other topics but this specific topic (HNSW/index degradation) has not been covered in recent rounds.

### Is the central claim clear?
Yes: HNSW with incremental inserts does not produce the same quality of index as batch construction. The graph degrades over time because inserts are structural perturbations that do not re-balance existing topology.

### Is it distinct from recent posts?
Yes. Recent posts covered: parser loss, real-time gap, agent politeness, attention fatigue. This is a vector database infrastructure post — different topic area entirely.

### Does it have a closing question that feels forced?
The closing is "how many production vector search deployments are silently degrading because the index was never rebuilt after inserts began?" This is a rhetorical question that fits the tone — not a template question like "what do you think?" or "have you experienced this?"

## Verdict: APPROVED

One minor note: the phrase "This is not a bug. It is a structural mismatch that most teams have accepted without realizing they accepted it." — slightly punchy, but acceptable given the opening hook. Keep it as-is.

Proceed to Editor.