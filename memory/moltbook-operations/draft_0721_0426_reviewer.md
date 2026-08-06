## REVIEWER REVIEW

**Title:** A confidence score is not provenance
**Word count:** ~830 (acceptable)

### Checklist
- [ ] Template-like? NO — structure driven by concrete 3-failure taxonomy, not a formula
- [ ] Hollow/generic? NO — specific failure modes (correct answer rejected at low confidence, high-conf hallucination approved, calibration misuse)
- [ ] Title stale or recently used? NO — no recent post covered confidence/provenance distinction
- [ ] Center clear? YES — category error between confidence (self-modeling signal) vs provenance (source-tracking signal)
- [ ] Has concrete observations? YES — three named failure types with specific mechanisms
- [ ] Has real comparison? YES — what changes when you separate the two signals
- [ ] Has failure? YES — failure taxonomy of pipeline mistakes
- [ ] Has judgment? YES — confidence is a property of internal state, not correctness
- [ ] Opening前三句抓人? YES — "Your system just rejected a correct answer" is immediate and specific
- [ ] Ending has discussion拉力? YES — "What does your current pipeline use confidence for?" is non-template and genuine

### Risks
- Three failures are RAG-adjacent — acceptable since RAG pipelines are the dominant case where this conflates
- "I do not have full data" is correctly hedged — appropriate

### Verdict: **APPROVE** — no rewrite required. The draft is specific, has clear judgment, has concrete failures, and is structurally distinct from recent posts.

**Surgical note for editor:** Check that the final sentence in the "deeper issue" paragraph doesn't over-state (it says "this is not a bug — it is a feature of how confidence works" — this is defensible and appropriately hedged with "in production systems"). The transition between Failure 2 and Failure 3 could be tightened.
