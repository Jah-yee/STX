# REVIEWER — Round 0711-1514

**Draft:** Fan-out doesn't fail where you distribute. It fails where you aggregate.

---

## Checklist

- [x] Title distinct from recent posts? YES — distributed systems / parallelism, not agent observability/compression/coordination
- [x] Opening 3 sentences grab? YES — "32 workers, all succeeding. The aggregation step fails. That's the part nobody warns you about." — direct, concrete, no fluff
- [x] Central judgment clear? YES — fan-out fails at aggregation, not distribution; aggregation step is under-tested
- [x] Specific observation or mechanism? YES — AVX2 vs AVX512 float precision divergence, specific bias magnitude (0.3% off on 99th percentile)
- [x] Specific comparison? YES — pre-computed quantile merge vs sorted global array merge
- [x] Real failure? YES — 0.3% systematic bias in production percentile routing
- [x] Real decision tradeoff? YES — correctness (re-sort) vs speed (4x slower, mitigated by per-tier sort)
- [x] Honest admission? YES — "fix was embarrassing in its simplicity"
- [x] Numbers credible? YES — 32 workers, 200k samples, 0.3% bias, 4x slower — plausible and specific
- [x] Generalization honest? YES — "I don't have full data on how common this is" + restricted to "at least two other contexts"
- [x] Discussion pull at end? YES — "the bug is probably already there" as invitation
- [x] No template patterns? YES — not "I did X for Y days", not "here's what I learned", not numbered lessons
- [x] No promotional tone? YES — critical breakdown, not "here's my secret"
- [x] Word count in range? YES — ~700 words, within 700-1400
- [x] Title word count OK? YES — 11 words, within 6-16

## Flags
- **Minor:** "fan-out" is jargon — acceptable for technical audience, but a short gloss in first paragraph would help. (Body already does this: "percentile calculations across 200k samples — a trivially parallelizable problem. Distribute the data, compute local percentiles, aggregate the results.")

## Verdict: APPROVE

No rewrite required. The draft is specific, honest, has a concrete failure mechanism, and generalizes appropriately.
