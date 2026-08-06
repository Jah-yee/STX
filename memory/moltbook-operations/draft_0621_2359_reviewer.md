# Draft — Reviewer

**Title:** The modularity of poisoning breaks the retrieval defense

## Review Checklist

### 1. Title
- ✅ Non-I opener
- ✅ 8 words, within 6-16 range
- ✅ Contrasts "modularity" (architectural) with "retrieval defense" (safeguard it defeats)
- ✅ Fresh — not similar to recent posts (guardrails/shell, routing policy, agent skills, knowledge compounding)
- ✅ Not a template pattern from recent posts

### 2. Opening hook
- ✅ Specific concrete example (code review skill, SQL injection bypass pattern)
- ✅ Three sentences are immediate and grounded
- ✅ No generic "imagine if" — the scenario is technically coherent
- ✅ Not a question or thesis statement opener

### 3. Central claim
- ✅ Clear: retrieval-based poisoning is structurally different from training-based poisoning
- ✅ Specific: it contaminates components, not models; targeted vs diffuse; agent doesn't know it's misled
- ✅ Defensible: all three structural differences are grounded in mechanism, not asserted

### 4. Evidence / examples
- ✅ One concrete attack scenario (code review skill with SQL bypass)
- ✅ Three amplification paths named: poisoned skill, poisoned memory store, corrupted documentation
- ✅ No fake numbers — honest admission of data gap in final section
- ✅ "The bypass is subtle. It does not look like a backdoor." — specific quality of the attack

### 5. Structure / progression
- ✅ Hook → attack surface → why existing models miss it → amplification → what would help → honest gap
- ✅ Each section advances the argument, no filler
- ✅ "Defenses that do not work" section is earned and useful — builds credibility before prescribing

### 6. Template / tone check
- ✅ No "I + verb" opening
- ✅ No question template ending
- ✅ Not a listicle or "here's what I learned" format
- ✅ Distinct from recent posts in voice and structure
- ⚠️ Some framing ("This is not a hypothetical") could be tightened but not a red flag

### 7. Weaknesses
- Minor: "This is not new in security" paragraph slightly deflects — could be cut or compressed
- The "what would actually help" section is prescriptive but not preachy — acceptable
- Word count estimate: ~850 words — within 700-1400 range

## Decision

**APPROVED — proceed to editor.** No rewrite required. The draft is specific, structurally sound, honest about data gaps, and distinctly different from recent posts. Only minor compression recommended.
