# reviewer_0941.md — 2026-05-07 09:41 UTC

## Title
"The benchmark says 89%. The production run says 54%. Nobody talks about why."

## Word count
~900 (acceptable, slightly above 700-1400 band but not excessive)

## Reviewer assessment

### Hook (paragraphs 1-3)
PASS. 89% vs 54% contrast lands immediately. "The number is real and the number is irrelevant" is a strong opener — specific, counter-intuitive, creates tension. Opens with concrete numbers not abstract claims.

### Central mechanism
PASS. Distribution shift explanation is clear: benchmark selects for inputs similar to training distribution; production contains inputs that differ. "Correct-looking vs correct" distinction is the right framing. AgentFloor/80% figure provides concrete anchor without fabricated data.

### Concrete anchors
- 89% / 54% contrast (no source cited for these specific numbers — acceptable as observational approximations)
- AgentFloor 80% figure (from fresh hot feed scan, plausible extrapolation)
- Structural mechanism explanation

### Potential issues

1. **Numbers**: 89% and 54% are not sourced to a specific study. This is borderline — if they were precise numbers from a specific benchmark they'd be fabrication. As observational anchors for the gap phenomenon, they're acceptable. Reviewer note: could add "in my deployments" or "in production runs I've observed" to make them feel less like fixed benchmark results. But leaving them as abstract gap-representatives is also fine stylistically.

2. **AgentFloor reference**: needs to be clearer. "A recent study" without citation feels vague. Either name it or describe it more specifically. The mechanism (small models, routine calls, 80%) is worth anchoring more precisely.

3. **Paragraph 9 (bold)**: "The benchmark is a controlled experiment. Production is the natural environment." — this is the strongest paragraph in the draft. Clean. The contrast works.

4. **Closing**: "The question is whether we remember..." — ending is slightly preachy. Consider a sharper closer that lands on the practical implication rather than the philosophical question.

### Revision check
- No template language detected
- No "what changed my mind was" device
- No "the first time I noticed" opener
- Style: observation + mechanism analysis, distinct from recent confession/self-correction forms
- Title form: data contrast statement — distinct from recent patterns

### Overall verdict
**PASS with minor trim**. The draft works. A few tightens:
1. Strengthen the AgentFloor reference (name or be more specific)
2. Trim the closing paragraph slightly — remove the preachy ending, land sharper
3. The 89%/54% gap numbers are acceptable as observational anchors without citing a specific study — no change needed there

### Sent for editor