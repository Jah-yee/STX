# Reviewer — Round 0000

## Title Check
"Agents pass demos, fail in production — the environment shift nobody talks about"
- Strong, specific, contrarian
- Not "X is Y" / not "I..." / not noun phrase only
- Within 6-16 words (11 words ✓)
- APPROVE

## Body Check

**Template risk:** LOW — This is a technical observation / postmortem-style piece. Does not follow recent "X is Y" or "I + verb" patterns. Each paragraph has a distinct mechanism: environment shift, entity mismatch, interaction pattern mismatch, feedback loop absence, gradual degradation.

**Empty/vague risk:** LOW
- Specific failure modes named: entity mismatch, interaction pattern mismatch, feedback loop absence
- Specific observation: "agents that worked in testing start failing in production" — not generic, grounded in pattern
- Specific mechanism: training-to-deployment distribution gap
- Honest admission: "I don't have systematic data" ✓

**Central clarity:** HIGH
- One clear thesis: production is a different distribution; agent failures are often environment shift, not agent defect
- Each paragraph advances this: pattern description → specific failure clusters → gradual degradation → honest admission → practical implication

**Word count:** ~620 words. Below 700 minimum. Needs expansion.

**Verdict:** APPROVE with expansion. The piece is structurally sound, the argument is specific, non-template, the admission is appropriate. Expand the middle section (specific failure clusters) or the practical implication section to reach ~750-900 words.

## Action
→ Pass to Editor with expansion note: bring to 750-850 words.