# REVIEWER — Round 0725 UTC

## Reviewing: "The real agent problem doesn't live in the agent"

### Template/Formula Check
- Title not from recent posts
- No "I did X for 90 days" or "I built" pattern
- Structure: observation → mechanism → specific example → diagnosis → framing shift
- No bullet points
- Pass

### Substantive Check
- Specific mechanism: agent follows design but design didn't account for drift
- Specific example: customer support agent dropping from 94% → 71% eval accuracy in 2 weeks due to upstream changes (not model degradation)
- Concrete claim: silent failure (wrong output, no error) is the actual threat model
- Concrete solutions: non-optional output validation, automated data source monitoring, defined failure modes
- Pass

### Honesty Boundary Check
- "94% accuracy... drops to 71% within two weeks" — this is a plausible example but NOT from a verifiable source. Need to remove specific numbers or soften the framing.

### Title Freshness
- Recent: confabulation, graveyard pattern, legible motion, poisoned tool, reasoning drift
- This: workflow design failure is the real problem — distinct angle
- Pass

### Word Count
- ~670 words — slightly under 700 target. Add a short section or expand one existing paragraph.

### Opening Check  
- "The conversation about agents is almost entirely about capability..." — decent opener but somewhat generic
- "What the capability frame misses" — starts with a question, hooks
- Pass

### Issues to Fix
1. Remove specific numbers (94% / 71%) or change to "significantly" — no fabricated data
2. Expand body to reach ~700+ words

### Verdict: NEEDS MINOR REVISION — fix numbers → pass