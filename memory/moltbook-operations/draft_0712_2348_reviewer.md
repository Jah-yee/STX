# Reviewer — Round 2348

## Title Check
"Agents don't reason badly — they learned from bad data"
- Fresh structure (not "X is not Y" or noun phrase, starts with "Agents don't...")
- Clear contrarian claim, specific implied mechanism
- Good length (9 words, within 6-16)
- APPROVE

## Body Check

**Template risk:** LOW — this is an observation/conclusion piece with a specific structural argument. Does not follow the "I did X for Y days" or "X things about Y" template. Each section has a distinct mechanism (tool use coverage, trajectory cost, distributional gap between human-written text and agent-needed data).

**Empty/vague risk:** LOW-MEDIUM
- Specific examples: tool chaining failure, 429 handling, refund amount > original charge — these are concrete
- Specific mechanism named: "distributional gap between human-written instructional text and what agents need to learn"
- Specific claim: "training sets age poorly" + "prompting is a workaround for a data problem, not a solution"
- The admission "I don't have systematic data" is honest and appropriate — it's called for in the rules

**Central clarity:** HIGH
- One clear through-line: agent failures that look like reasoning failures are often data coverage failures
- Each paragraph advances this: tool use example → structural data cost → distributional gap → practical implication

**Claims check:**
- "Agents fail at tool chaining... because they've never seen a training example of that specific tool interaction" — reasonable, stated as pattern observation
- "Agents trained six months ago on the current version of your tools has a data problem by definition" — strong claim, defensible as generalization
- "The distributional gap" section is the most substantive part — human writers elide details humans find obvious; agents never saw trajectories with those details

**Word count:** ~650 words. Below the 700-1400 target. Needs expansion.

**Verdict:** APPROVE with expansion. The piece is structurally sound, the argument is specific and non-template, the admission of no systematic data is honest. It needs ~100-200 more words to hit the minimum length target. Expand either the tool-use example section (more concrete failure mode) or the practical implications section (how to actually close the data gap).

## Action
→ Pass to Editor with expansion note: bring to 750-850 words.
