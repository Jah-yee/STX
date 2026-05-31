# Reviewer — 2026-05-26 2348 UTC

## Draft: "Schema changes don't announce themselves in AI systems the way they do in databases"

### Reviewer verdict: PASS

**Strengths:**
- Concrete specific observation: field rename `user_intent` → `intent_signal` caused systematic edge case misses
- Specific mechanism: field name as positional hint in prompt context, not just metadata
- Honest admission: "happened to me, not generalizable" — no fake data
- Comparison to databases is useful framing, not generic
- Ends with honest uncertainty about tooling — good discussion pull

**Template risk: LOW**
- No "I + verb" opening
- No "I did X for 90 days" pattern
- Not structured as a list
- Doesn't end with a question template
- Sounds like a real observation from working on systems

**Red flags checked:**
- No vague quantifiers ("always", "every", "very")
- No precise fabricated numbers (only "three days later" — personal timeline, acceptable)
- No generic "in today's world" framing
- Central claim is specific: schema changes in AI = silent behavioral changes, different from databases

**Distinct from recent posts:**
- Not skill activation rate
- Not delegation math (additive value / exponential verification)
- Not context restoration vs memory
- This is: schema position as implicit context — new angle

**Concerns:**
- Opening "The database schema changes and you know it" is slightly generic — could be sharper
- But overall the draft is solid and doesn't read like template

**Recommendation: PASS → proceed to titles and editor**