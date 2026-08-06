# Round 0731_1553 — Editor Changes

**Title**: Multi-round agent degradation is a dataset staleness problem, not a memory problem

## Editor Changes (Surgical — 2 cuts)

### Cut 1: Opener trim
**Original**: "When a multi-round agent starts failing, the instinct is to reach for more context. Give it a longer memory. Add a retrieval layer. Stuff more history into the window."
**→ "When a multi-round agent starts degrading, the instinct is to reach for more context. Longer memory. A retrieval layer. More history in the window."

*Rationale*: "starts failing" → "starts degrading" (more precise for gradual performance decline); "stuff more history" cut for wordiness; sentence fragments for rhythm.

### Cut 2: Conclusion tightening
**Original**: "If you are watching an agent get confidently worse over extended conversations, check the timestamp on its training distribution before you check its context window. The ceiling on its performance was set when the dataset was built — and if the dataset hasn't moved since, the agent won't either."
**→ "If you are watching an agent get confidently worse over extended conversations, check the timestamp on its training distribution before you check its context window. The ceiling was set when the dataset was built."

*Rationale*: Final sentence redundant with prior; cut strengthens ending punch rather than weakening it.

## No Changes Required
- Body paragraphs: clear, specific, no filler
- Fix taxonomy paragraph: useful, not decorative
- Honest admission: kept as-is
- "Confidently wrong" phrase: precise, keep

## Editor Decision: APPROVED AS EDITED
