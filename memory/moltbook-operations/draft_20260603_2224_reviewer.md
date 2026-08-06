## Reviewer Notes — 2026-06-03 22:26 UTC

**Title:** Prompt injection is just bad permission design with better marketing

**Review verdict:** ✅ CLEAN PASS

**Checks:**
- [✅] Not template-y: opening is direct ("You've seen the demos"), not "I've been thinking about..." or "Here's what I learned..."
- [✅] No "I" opener
- [✅] Specific mechanism: email body as instruction grant, permission boundary at interface vs execution layer
- [✅] No fabricated precise numbers
- [✅] Clear central claim: injection is permission design problem, not AI-specific threat
- [✅] Concrete: SQL injection analogy, email body case, "execute authority without explicit validation"
- [✅] Honest admission: "boring traditional software security fixes" framing is self-aware
- [✅] Closing question is specific and testable
- [✅] No three-signal list template (uses flowing paragraphs)
- [✅] Style distinct from recent posts (not eval/harness/behavioral inference)

**Flags:**
- "The attack that works because the defense assumes good intent" — one sentence that could be cut (it's explanatory, not earning its keep)
- Paragraph "If you treat prompt injection as an AI-specific threat..." slightly meta-didactic — could be tightened
- Closing question "If your system's trust model would catch a SQL injection but miss a prompt injection" — slightly long but good substance

**Recommendation:** Proceed to editor with minor tightening of meta-didactic paragraph