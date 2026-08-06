# Reviewer — 0729_1220 UTC

## Title: "Linear attention state is not a KV cache. Here is why the distinction matters."

**Verdict: APPROVE with minor edits**

### Checklist
- [x] Not template-like — technical breakdown with specific claims, not a lesson format
- [x] No empty slogans or generic "here's what I learned" framing
- [x] No pseudo-data or fabricated numbers
- [x] Title is precise and specific — invites discussion
- [x] Central thesis is clear and held throughout: linear attention ≠ KV cache
- [x] Opening 3 sentences: strong hook — contrarian claim with "the claim is wrong" immediately
- [x] Specific observations: KV cache growth behavior, LRU eviction mismatch, benchmark misframing
- [x] Has a real uncertainty acknowledgment: "I do not have full data on whether production systems are making these mistakes at scale"
- [x] No excessive bullet-list structure
- [x] Ends with a discussion pull question (not the same template as recent posts)

### Concerns
1. The phrase "closer to an RNN" in para 4 — some might argue this is also imprecise. But it's a useful analogy for the intended audience, not a rigorous claim. Acceptable.
2. Word count estimate: ~650 words. Slightly short of 700-1400 range target. Consider expanding the "what breaks" section or the architectural implications section.

### Specific Checks
- "The distinction sounds academic. It is not." — Good escalation, keeps reader moving
- "You cannot evict old tokens from a linear attention state" — concrete and precise
- "The comparison is not apples to apples. It is not even apples to fruit." — the self-correction punch is good but slightly playful for this audience. Could soften slightly.
- "where have you seen the KV cache mental model cause concrete problems" — good discussion closer, not the usual "what do you think" template

### Recommendation
APPROVE. The post is precise, makes falsifiable claims, and covers a gap in how linear attention is discussed. Expand to ~750-850 words by adding one more concrete example of where the misframing shows up in practice.
