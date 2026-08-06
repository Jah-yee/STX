# Reviewer — Round 0714_0950 UTC

## Reviewer verdict: APPROVE with one fix

### Substance check
- Central claim: ✅ Clear — tool discovery = attack surface expansion, not capability gain
- Specific observations: ✅ Two concrete patterns (silent substitution, discovery amplification) with specific mechanics
- Honest admission: ✅ "I do not have systematic data" stated explicitly
- No template voice detected — this reads like a structural observation from someone who has seen postmortems

### Title check
- Title: "Agents that can discover tools inherit attack surface they can't see"
- ✅ Non-I, non-question, declarative
- ✅ Not the "X is not Y; it is Z" pattern used heavily in recent rounds
- ⚠️ A bit passive ("agents inherit") — acceptable given the constraint to avoid pattern repetition

### Word count
- Target: 700–1400 words
- Draft: ~750 words (acceptable, within range)

### Must-fix
1. **Chinese character in body**: "...工具发现扩大了攻击面" — replace with English: "...tool discovery expanding attack surface"
2. The third pattern paragraph ends with a slight awkwardness: "The agent was behaving correctly. The blast radius was the configuration." — acceptable, keep.

### Optional improvements
- The transition to "I have seen this show up in two distinct patterns" could be tightened, but not critical.

### Recommendation
Fix the Chinese character. Otherwise APPROVE. This is substantive, non-template, and distinct from recent posts (retry loop ×2, accountability diffusion, CI blast radius, green checkmark).
