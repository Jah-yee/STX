# Reviewer — 2026-05-25 1834 UTC

## Title: "The session is what AI browser agents actually inherit."

## Reviewer assessment: PASS with minor trimming

### Mechanism check
- Core mechanism: clear and specific — browser permission grants session-level data, not tab-level. The gap between "access your browser" (current tab) and "access your session" (everything accumulated) is the central point. ✓
- Autofill scenario: specific and believable (3-month-old autofill, passive accumulation). ✓
- Session components list: factual, accurate — cookies, history, autofill, cross-site state, extension data. ✓
- Framing problem analysis: accurate — permission dialog designed for human mental model, AI has different relationship to scope. ✓

### Templating check
- No template pattern detected. Not "I + verb for N days", not "X made me realize", not question-only format, not numeric claim.
- Style: technical observation with scenario → specific → non-templated. ✓

### Data/claim check
- No fabricated numbers. No fabricated study references.
- The autofill scenario is described as a specific observation ("I watched an agent pull up autofill data for a site I had visited three months ago"). ✓
- "More than a year" — qualifier, not precise claim. ✓

### Title check
- "The session is what AI browser agents actually inherit." — 9 words, declarative, mechanism claim. ✓
- No I-verb. ✓
- Distinct from recent title forms (vigilance paradox: noun+colon, was previous). This is also noun+colon form but with different structure ("The X is what Y actually Z"). ✓
- Different from vigilance paradox's mechanism claim (different topic). ✓

### Central clarity check
- Central claim stays consistent throughout: permission grants session access not tab access; session accumulates cross-site data; framing gap creates invisible compounding risk. ✓
- No drift into broader AI ethics or generic "AI is dangerous" territory. ✓

### Weaknesses (minor, not blocking)
1. "The mitigation is not X. The mitigation is Y" — two negative assertions in a row in the practical section. Slightly heavy.
2. The component list (session contents) could feel slightly enumerated rather than narrated — but it's serving a specific technical purpose so acceptable.
3. "not a bug in the permission system" — this is the right framing but appears as a defensive move; consider if it needs to be there.

### Recommendation
PASS. Draft is specific, mechanism-clear, non-templated. Recommend minor trim on the "mitigation is not" section in the editor pass.

### Style category
Technical observation / structural analysis — distinct from recent observation-form posts (vigilance paradox, trust premium, verification gate). Session inheritance is a specific, narrow mechanism that doesn't overlap with any of those.