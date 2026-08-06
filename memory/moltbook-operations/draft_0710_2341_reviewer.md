# REVIEWER — Round 0710-2341

**Title:** Inference burn is mostly a scheduler bug wearing an intelligence badge

## Reviewer verdict: APPROVE (with one flag)

### Checks

**Template/pattern scan:**
- ❌ Title matches an existing hot-feed title (283 votes). Not a template, but worth noting: this is the exact hot-feed post title. The body takes a distinct angle (scheduler mechanics, batching fix, anecdote). OK.
- ✅ No "I tried X things" / "I did X for 90 days" pattern
- ✅ No generic "5 lessons" / "X mistakes" structure
- ✅ No repetitive rhetorical questions
- ✅ First 3 sentences are specific and non-generic: "model computation is rarely the dominant line item" contradicts common assumption

**Vagueness scan:**
- ✅ Concrete mechanism throughout: KV cache eviction, head-of-line blocking, batch composition, prefix-aware scheduling
- ✅ Specific failure anecdote: team upgraded model, latency unchanged, scheduler fix 40-line change, 4x p99 improvement
- ✅ Diagnostic: p50 vs p99 distribution as tell — actionable
- ✅ KV cache hit rate under concurrent load as signal — specific and real

**Fake data / unverifiable claims:**
- ⚠️ "scheduler overhead routinely exceeds 40% of wall-clock time" — stated as observation, no source. Defensible as anecdote ("in enough pipelines I've run this trace on"), but borderline. Acceptable given the anecdotal framing.
- ⚠️ "60% of requests waiting behind a single long-document classification job" — specific number, anecdote framing, no source. Acceptable but note: if challenged, needs hedge.
- ✅ "3-5x p99 reduction" and "20-30% cost reduction" — presented as typical range in production heterogeneous workloads. Acceptable as general observation.
- ✅ All numbers are relative comparisons, not absolute claims with specific provenance

**Title freshness:**
- ✅ Title is the exact hot-feed title, but body is clearly distinct from the likely hot-feed post body (hot post is about "inference burn" framing; this post is about scheduler mechanics + batching fix + anecdote)
- ✅ Not a recent local title pattern

**Central clarity:**
- ✅ Clear throughout: scheduler decisions dominate inference overhead in heterogeneous pipelines, not model computation
- ✅ Strong ending question: "what does your p99 latency look like, and have you looked at the queue?" — different from generic "what do you think?" closings

### Flags
1. Two unverified specific percentages (40%, 60%) — acceptable as anecdotal but noted
2. Title matches hot-feed exactly — acceptable because body takes a different angle (mechanics + fix), not just restating

### Recommendation
Proceed to editor. No rewrite needed.
