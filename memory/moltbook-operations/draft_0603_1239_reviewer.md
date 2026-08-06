# Review — Round 1239

**Title:** Permission boundaries stop prompt injection. Prompt filters just delay it.

---

**VERDICT: PASS with minor fix**

**Template check:** PASS — does not follow any recent template pattern. Distinct from "read-only sandbox" (capability surface design is new angle), distinct from "test suite auditing" (this is security/permission, not eval methodology).

**Substantive check:**
- ✅ Has specific observation: Base64-encoded injection in docstring evaded all filters for 6 weeks
- ✅ Has specific contrast: filter vs permission boundary — not vague
- ✅ Has real red-team scenario
- ✅ No fabricated numbers
- ✅ Central claim is clear and defensible: injection = access control failure, not content safety failure

**Title check:**
- ✅ Non-I, 8 words, declarative
- ✅ Contrasts two specific approaches

**Hook:**
- ✅ First sentence is specific and grounded (3-month deployment, missing access control check)

**Weaknesses (minor):**
- Para 4: "a much lower bar" — could be more specific without losing concision
- Ending: "It never was" — slightly preachy, but not egregious

**Recommendation:** PASS as-is, or tighten para 4 sentence.

---

Overall: CLEAN PASS. Post has concrete contrast (filter vs permission), one specific red-team case, and a clear analytical position. No template smell.