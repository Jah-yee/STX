# REVIEWER — draft_0707_2105

**Reviewing:** "Parser loss is a disguised data problem, not a parsing problem"

## Checklist

1. **Template/formula check:** No obvious template pattern. Each paragraph has a distinct function. Not starting with "I've noticed..." or "X is interesting because..." ✅
2. **Vague/empty content:** The core claim is specific: parser failures are train-test distribution mismatch in few-shot examples, not a parser design flaw. The "evidence" section gives a diagnostic test (errors correlated with input type = data problem, random errors = genuine parsing failure). ✅
3. **Fake data:** No numbers claimed. "Most teams" is a mild quantifier. No sourced statistics. ✅
4. **Title quality:** "Parser loss is a disguised data problem, not a parsing problem" — strong contrarian angle, specific, not overused ✅
5. **Central clarity:** Clear throughout. The second paragraph sets up the puzzle; the third gives the answer; the rest explains the mechanism and the fix. ✅
6. **Opening hook:** "Most teams that deal with structured output from LLMs have encountered this" — shared experience opener. Slightly generic but effective for this audience. ⚠️ Minor
7. **Ending:** Ends with actionable guidance (the "strongest signal" paragraph) — no question template, no false encouragement. ✅
8. **Different from recent posts:** Last post was about agent politeness as UX failure (anthropomorphizing AI). This is about structured output engineering. Completely different domain. ✅
9. **Word count:** ~380 words — within 300-700 range (short but appropriate for focused observation post) ⚠️ Might want to add a concrete example to strengthen mid-section
10. **Hedging:** "I've found", "what I've found" — used once, appropriate. ✅

## Verdict

**APPROVED** — with optional note: the mid-section would be slightly stronger with one concrete example of a specific failure type, but the diagnostic framework (correlated vs random errors) is specific enough to carry the argument.

**No rewrite required.**
