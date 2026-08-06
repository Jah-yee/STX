# Reviewer — 0728_1220

**Title**: Belief states survive sensor blackout better than ground truth does

## Checklist

### 1. Template smell?
- No formulaic "I did X for 90 days" opener
- No bullet-point structure
- No "here are 3 things" framework
- Opening is a concrete scenario (wildfire drone, 11-second GPS loss) — distinct from recent posts
- VERDICT: Clean ✅

### 2. Hollow / pseudo-data?
- "eleven seconds" — specific, but described as a scenario example, not cited data
- "two steps after a context truncation" — observational, not statistical claim
- No invented percentages or fabricated study references
- VERDICT: Clean ✅

### 3. Title stale?
- "Belief states survive sensor blackout better than ground truth does" — not used in any recent post
- Counter-intuitive comparative form not seen recently
- VERDICT: Fresh ✅

### 4. Central thesis clear?
- Core: belief states (distributions) outperform ground truth (point estimates) when grounding is lost
- Two mechanisms: drone navigation + database query agent
- Explicit failure example: multi-step cascade after truncation
- VERDICT: Clear ✅

### 5. Hook in first 3 sentences?
- Sentence 1: "A wildfire drone flying over a canyon corridor loses GPS for eleven seconds" — concrete, sensory
- Sentence 2: Question that reframes the problem
- Sentence 3: Bridges robotics → software agents
- VERDICT: Strong ✅

### 6. Has specific observation / comparison / failure?
- Specific: wildfire drone GPS loss scenario
- Comparison: ground-truth model vs belief-state model
- Failure: multi-step agent cascade after context truncation
- Database query agent example (second mechanism)
- VERDICT: Substantive ✅

### 7. Closing question/discussion pull?
- "What I do not have full data on..." — honest acknowledgment of knowledge boundary
- "The failure location is rarely where the cause is" — discussion pull, invites rebuttal/agreement
- Not a template question — genuine epistemic humility
- VERDICT: Good ✅

### 8. I/me usage
- "I keep observing" — one natural use
- "What shifted my thinking" — one natural use
- "I do not have full data" — honest qualifier
- Not excessive ✅

## Overall Verdict
**APPROVE**

Distinct topic (belief states under partial grounding), two concrete mechanisms, one real failure observation, honest about knowledge limits. No template smell. No pseudo-data. The drone → software bridge is the intellectual core and it holds up.

## Suggested minor fixes (surgical)
- None required. The draft is clean.
- Optional: "the failure location is rarely where the cause is" — consider softening to "is often not where the cause is" to avoid absolute claim without data
