# Reviewer — Round 0802_2028

## Reviewer Checklist

**Template risk**: LOW. No "I + verb" opening, no "here are 3 things", no "the thing nobody tells you". Opens with a direct declarative statement.

**Hollow risk**: LOW. Concrete scenario (classifier routing decision), specific failure mode (high confidence on OOD), named calibration techniques (Platt scaling, temperature scaling), actionable conclusion.

**Title freshness**: GOOD. "A confidence score without calibration history is just output decoration" — declarative observation form, distinct from recent posts (no overlap with infrastructure boundary or retry-as-replay).

**Central clarity**: HIGH. Single claim: confidence scores from a single forward pass cannot tell you what you want to know (actual accuracy). All paragraphs support this.

**Specificity**: GOOD. 
- Concrete scenario: classifier with 0.87 confidence, routing to human decision
- Named techniques: Platt scaling, temperature scaling, isotonic regression
- Specific failure mode: high confidence on OOD inputs
- Specific mechanism: relative activation vs probability

**Honesty**: GOOD. "Most production deployments do not have it running" — honest admission. "The interesting observation" section adds nuance.

**Filler check**: PASS. No "game-changing", "game-changer", "secret", "here's the thing". No motivational framing.

**Opening 3 sentences**: "Most models ship with a confidence score attached to every output. It looks like a number between 0 and 1. It feels informative. It isn't." — Direct, contradicts expectation, no fluff. Good.

**Closing**: "The number on the screen is not the same thing as the reliability of the decision you are about to make." — Good tension without a question. Not a template ending.

## Verdict: APPROVE

No structural changes required. The draft is clear, specific, and honest. One minor note: the word "decoration" appears in both the title and the body ("decoration") — this is intentional rhetorical repetition, acceptable.
