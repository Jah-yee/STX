# Reviewer — Round 0704_1852

**Draft:** draft_0704_1852_writer.md
**Title:** The retrieval model is not your RAG system. The language model is.

## Reviewer Verdict: APPROVE

### Hook Check (first 3 sentences)
"The retrieval model is not your RAG system. The language model is." — Direct, specific, sets up a category correction. Works. No vague opener.

### Template Risk: LOW
- No "I tried X for N days"
- No "I did X and then Y"
- No "Here's what I learned" closing template
- Voice is analytical throughout
- Style: technical breakdown / industry critique

### Center Clarity: STRONG
One central claim: RAG systems are two models trained separately with different objectives, concatenated at inference time. The retrieval stack optimizes precision; the LM's actual performance is the real metric. The informal test adds a concrete data point.

### Specificity Check
- "Decision boundary" framing — precise
- Informal test with two models — concrete observation (not fabricated numbers)
- Two working directions (active retrieval, end-to-end) — specific enough to be useful
- "Concatenated at inference time" — sharp phrasing, not vague

### Weaknesses
- Section 3 ("What the retrieval model is actually doing") could be trimmed — it rephrases the same insight as section 2, slightly redundant
- Ending could be punchier — currently tails off into "everything else is the interface to it" which is fine but not the sharpest possible landing
- Minor: "BM25, dense passage retrieval, cross-encoders, re-rankers" — some readers may not know all of these; acceptable for this audience

### Title Check
"The retrieval model is not your RAG system. The language model is." — Strong. Clear, structural, avoids all recent patterns. Good selection from the 8 candidates.

### Diff from Recent Posts
- 0704_1838: Infrastructure-as-researcher (infra trend)
- 0704_1824: Nondeterminism in agents (infra/cognition)
- 0704_1800: Agent amnesia experiment (cognition/process)
- 0704_1852: RAG retrieval vs policy problem (systems/architecture) — distinct from all three

### Verdict
APPROVE. Proceed to Editor with minor trim recommendation on section 3.
