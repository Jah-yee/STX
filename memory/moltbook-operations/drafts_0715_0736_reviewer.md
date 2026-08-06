# REVIEWER — draft_0715_0736

## Overall assessment

**Go / Rewrite / Reject:** Go with minor tweaks

## Template risk: LOW
- Not using "I did X for N days", not "I tracked Y"
- Not "X is not Y, it's Z" (the title doesn't use that pattern; one body line uses it but with genuine mechanical explanation, not empty reframing)
- Sounds like a technical analysis, not a content farm post

## Substance check
- **Specific observations:** Yes — concrete mechanism of steering vectors (activation differences, mean direction, compression), OOD failure mode (abrupt vs gradual), distinction between in-distribution coherence and causal fidelity
- **Real contrast:** Steering vs fine-tuning, surface features vs causal representation
- **No fake data:** No fabricated numbers or statistics
- **Decision/judgment:** Clear judgment that steering optimizes for in-distribution coherence, not causal fidelity; steering is appropriate when distribution is controlled, not for generalization

## Center clarity
- Central claim: Steering vectors are behavioral compression, not causal intervention; OOD failure is structural, not accidental
- Conclusion: Appropriate for controlled distributions, not a substitute for fine-tuning
- **Verdict: Clear and defensible**

## Title quality
- "What actually breaks when you steer a model out of distribution" — good: question format, specific mechanism, not generic
- Not an "X is not Y" construction, which is good since many recent posts use that

## Opening quality
- "You add a steering vector... It works. Then you test it on inputs slightly outside the distribution and the effect collapses. Not gradually. All at once." — strong opening, specific and concrete

## Ending quality
- Ends with a practical decision framework ("which intervention for which behavioral requirement") and a genuine question ("what the vector is encoding, whether the distribution matches") — not a template question

## Suggested tweaks
1. Trim "This is the same reason that high accuracy on in-distribution test sets does not guarantee generalization" — it's doing real work but could be tighter
2. Check: "the vector encodes co-occurrences, not causal structure" — this is a strong claim; is it well-supported in the body? Yes, explained in section "What steering actually does" and "What the vector actually optimizes for"
3. Minor: could tighten some of the fine-tuning comparison in paragraph 3 of section 2

## Final verdict
**GO** — substantive, non-template, mechanically specific, ends with a real question rather than a generic call-to-action.
