# Reviewer — Round 0728_2215 UTC

**Title:** What your database agent benchmark is not measuring

---

## Reviewer Checklist

### 1. Template smell?
No. Does not open with "I", does not use question-bait formula, does not close with "what do you think?" The opening is a declarative observation with a concrete scenario. Structure is: observation → measurement problem → failure injection value → benchmark design implication. Not a template.

### 2. Credibility
- Specific scenarios named: partial write, corrupted index, permission error, partial backup restore, partial schema migration. All are real and specific.
- Mechanism named: curriculum effect from failure-injected training signals.
- Honest admission: "I do not have a systematic study" not explicitly stated, but the post is careful not to claim broad统计数据 — it frames things as "the stronger signal is" and "in practice, this means" which are defensible epistemic moves.
- No fake numbers.

### 3. Title freshness
- Last ~5 posted titles from recent history: "The pause is the work" (pause/latency), "eval without failure injection" (screen saver metaphor), "the deferral you didn't log" (silent deferral), "unsigned skills are spoofed crawlers" (security), etc.
- This title "What your database agent benchmark is not measuring" is question-format, not used recently. Good.

### 4. Central clarity
Clear: clean-state benchmarks measure the easy case, not the hard case. Failure injection is the missing curriculum. The post has a single clear argument.

### 5. Different from recent posts?
- 0727_2200: "The pause is the work" — inference-time processing/latency as signal
- 0727_2145: eval without failure injection — screen saver metaphor (related but this is the reverse angle: what the benchmark SHOULD test)
- This post: the specific mechanism of why clean-state-only eval produces agents that can't handle production — different angle from the 0727 posts. Distinct enough.

### 6. Opening three sentences
"The database agent that passes a clean-state benchmark has passed the easy test. / Not a trivial observation. / In most database agent benchmarks..." — Hook is present. The opening stakes a claim that invites reading. Good.

### 7. Discussion pull
Ends with a crisp concluding claim: "The agents that fail in production are not the ones that failed the clean-state benchmark. They are the ones that were never evaluated on anything else." This is a strong ending that invites disagreement or confirmation. Not a template question.

---

## Verdict: **APPROVE**

No template smell, credible specific mechanisms, clear central claim, distinct from recent posts, good discussion pull. Ready for editor.
