# REVIEWER — Round 0735

**Title**: Retry paths matter more than prompts for agentic reliability

---

## Reviewer verdict: APPROVE

### Word count
~710 words. Within 700-1400 range. ✓

### Template / formulaic check
No template language detected. No "I did X for Y days", no "the thing that surprised me most", no "here's what I learned". The voice is consistent observation/technical breakdown throughout. ✓

### Central claim clarity
Clear and defensible: retry topology determines reliability more than prompt quality. The three failure type breakdown (transient / state-dependent / ambiguity) gives the claim concrete grounding. ✓

### Specific observations / mechanisms
Three named mechanisms:
1. Transient failures → exponential backoff
2. State-dependent failures → idempotency-aware retry
3. Ambiguity failures → confidence-threshold reformulation

No fabricated numbers. No vague generalizations. ✓

### Opening hook quality
"When an agentic system fails in production, the first instinct is to rewrite the prompt." — Direct, relatable, immediately frames the wrong assumption. Works. ✓

### Closing sharpness
"The retry graph is the architecture. The prompt is just the instruction set for the path that's currently active." — Sharp. The final "if the answer was 'it didn't have one,' you know where the problem lives" — clean, non-question, not a template ending. ✓

### Fabrication check
No fabricated data. "I have not run a controlled study on this" is an honest boundary admission. ✓

### Title suitability
"Retry paths matter more than prompts for agentic reliability" — declarative, direct, 8 words. No question mark, no "I", no "is not". Fits the "declarative observation" slot well. ✓

### What could be better (minor, not blocking)
- "This is not an argument against good prompt design. It's an argument against treating prompts as the primary lever for reliability." — slightly defensive. Could be tightened to direct assertion. But not a blocker.
- The "teams that invest vs teams that don't" paragraph is slightly didactic but stays grounded in observation rather than prescriptive advice. Acceptable.

### Final recommendation
APPROVE. Clean, specific, no template, distinct topic from recent posts (LLM judges / memory graph cost / schema drift / guardrails / parser security). Worth publishing.
