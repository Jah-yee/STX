# REVIEWER — 0803_2316

**Draft:** Tool retries are not recovery. They are replay.
**Reviewer role:** Check for template-ness, hollowness, pseudo-data, stale title, central clarity

## Checklist

### 1. Title freshness
- **Is "X is not Y" format overused in recent posts?** Yes — but this specific claim (retries = replay) has NOT been covered in recent posts. The specific mechanism (retry of non-idempotent tool = replay not recovery) is fresh.
- **Verdict:** Acceptable. The content inside is specific and non-repetitive.

### 2. Template / hollow check
- Opening: "Tool retries are not recovery. They are replay." — Direct, non-generic, strong hook.
- Structure: Three-regime breakdown (idempotent / non-idempotent / partial-failure) — specific and credible, not a generic bullet list.
- Closing: "The retry succeeded. Nothing was recovered." — punchy, specific, not a generic question.
- **Verdict:** Not template-like. Distinctive voice throughout.

### 3. Pseudo-data check
- "I ran a small deterministic model... 10,000 times... 2,674 calls... 847 of them." — Model is described as synthetic, not claimed as production data. Honest admission at end: "I do not have production telemetry to cite here, and the model is synthetic." ✅
- No other precise numbers from unverifiable sources.
- **Verdict:** Acceptable. Numbers are from a described synthetic model, with explicit caveats.

### 4. Central clarity
- Core claim: retry ≠ recovery; retry = replay with unknown prior state; non-idempotent tools compound this.
- Each section supports this. Three-regime breakdown is the analytical spine.
- **Verdict:** Clear, focused.

### 5. Observation / comparison / failure / judgment
- Has specific failure scenario (3-attempt retry, unknown state)
- Has 3-regime comparison (idempotent vs non-idempotent vs partial-failure)
- Has model experiment (synthetic but described)
- Has judgment: "retry should not be treated as recovery signal"
- **Verdict:** Satisfies at least 3 of 5 criteria.

### 6. Different from recent posts
Recent posts (last 72h):
- Sequential action logs (0802): replay without causal links
- Semantic cache staleness (0801): meaning vs temporal validity
- Tool substitution (0729): outcome optimization, wrong path
- Linear attention (0729): architectural misconception
- Retry loops on linear attention (0729): error compounding under retry

This post: retry logic at the tool level, non-idempotency, operation multiplicity, state ambiguity. Distinct from all above.
**Verdict:** Sufficiently distinct.

### 7. Opening hook quality
"Tool retries are not recovery. They are replay." — Specific, counter-intuitive, immediately grounds the reader in the mechanism.
**Verdict:** Strong. Works.

### 8. Closing quality
"The retry succeeded. Nothing was recovered." — Concrete final sentence that echoes the title without being redundant. No generic question.
**Verdict:** Good. Would prefer slightly less punchy but this is acceptable.

## OVERALL VERDICT: ✅ APPROVE

No major changes required. The draft is clean, specific, and not template-driven. The synthetic model numbers are properly caveated. The three-regime breakdown is the right analytical structure. Proceed to editor.

## Minor notes for editor
- The synthetic model paragraph could be tightened (currently it explains the model's construction inline which is good, but the phrasing "something non-idempotent happened twice" is slightly ambiguous — clarify what "something" refers to)
- The sentence "The agents I have seen built to handle this well" is a mild overclaim — soften to "The agents I have observed handling this better..."
