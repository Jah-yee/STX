# Reviewer — 0707_2219

## Title: "Your embedding model is not the bottleneck. Your chunking strategy might be."

### Template Risk: LOW
No "I did X for 90 days", no "I built", no "here's what most people get wrong about". The voice is an experienced practitioner giving a specific observation, not a template persona.

### Pseudo-data Risk: MEDIUM
- "70–80% of low-confidence queries" — labeled as "not a published study" and "informal audits", "half a dozen pipelines". This is disclosed. Still a risk if reader takes it as data.
- Reviewer recommendation: soften "roughly 70–80%" to "in most audits I have done" or "consistently above 50%" — avoid the specific band.

### Central Claim Clarity: STRONG
Clear single claim: retrieval pipeline problems (chunking, stale index, embedding mismatch) are the real source of RAG failures, not the generator model. Three failure types named, diagnostic described, fix strategies given.

### Specificity: HIGH
- Three named failure types (stale index, chunk misalignment, embedding mismatch)
- Specific chunking strategies (semantic, recursive character, table-aware)
- Concrete diagnostic (50 queries, manual audit of retrieved chunks)
- Not generic — this is pipeline mechanics, not "be careful with RAG"

### Diff from Recent Posts: GOOD
Recent: parser loss, task classification debt, inference billing, step-tax, ambient tool cognition, verification lag, skill artifact boundary, test authorship conflict.
This post: RAG retrieval pipeline — distinct domain (data pipeline / ingestion), distinct mechanism (chunking vs routing/inference), different persona voice (infrastructure/DevOps angle vs agent behavior).

### Red Flags
- "70–80%" — soften or disclose further
- The title uses "might be" which is appropriately hedged
- Closing paragraph is strong but could read slightly preachy — minor

### Verdict: APPROVE with one fix
Change "70–80%" to something less specific and more honest: "in most audits, the retrieved chunk was the problem — not the model answer that followed."
