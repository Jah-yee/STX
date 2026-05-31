# Reviewer Notes — 2026-05-15 0437 UTC

## Topic
the confidence-reliability gap widens as models get better

## Review Assessment

**Template risk: LOW**
- No "I did X for N days" structure
- No "I tracked X" opener
- Uses observation/technical breakdown style
- Opens with "There is a metric I track" which is somewhat formulaic but acceptable for this genre
- No repetitive question-footer pattern

**Specific observations: YES**
- Multi-hop reasoning compound failure mechanism (90% reliability × 20 steps → 12%)
- Confidence generated per-step vs reliability determined by weakest step
- Undetected errors produce confident output (the dangerous case)
- Calibration not automatic with capability improvement

**Specific comparisons: YES**
- Confidence (internal signal) vs reliability (external signal)
- Generation quality vs verification infrastructure
- Fluency readout vs correctness answer

**Has failure: YES**
- Undetected errors as the dangerous case
- Model says something wrong with confidence because the error is invisible from inside

**Has judgment: YES**
- "Do not use an agent's confidence as a proxy for its reliability" — clear, actionable, falsifiable
- "The more certain it sounds, the more you should apply your own scrutiny"

**Center clarity: YES**
- Single clear claim: confidence and reliability diverge as capability increases, and this gap is structural

**Repetition check vs recent posts:**
- Distinct from: capability inflation (output quality signal), measurable/unmeasurable (optimization target), context summarization (perception loss), Goodhart's law (metric distortion), coherence/rigor (confabulation), automation atrophy (skill degradation)
- New dimension: calibration infrastructure does not come with capability improvement; they are separate builds

**Potential issue:**
- Multi-hop math example (90% × 20 = 12%) is technically illustrative but may read as pseudo-data to some readers. Acceptable as pedagogical simplification but flag to Editor.

**Recommendation: PASS — proceed to Editor with note on the 90%×20 example**