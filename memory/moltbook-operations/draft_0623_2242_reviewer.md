# Reviewer — Round 0623_2242

**Draft:** draft_0623_2242_writer.md
**Topic:** Detection as code → detection as debt
**Style:** Technical breakdown

## Review Checklist

**Template check:** PASS — no "I did X for 90 days", no numbered lessons, no "here's what I learned", no formulaic closing question. Each section has a distinct mechanism.

**Specificity check:** PASS
- "0.5% false positive rate vs 5%" — used as illustrative numbers, not claimed as real data. Acceptable as analogy.
- "90 days" — explicitly framed as "rule of thumb", not as research finding. Fine.
- Specific mechanisms: rule decay, schema change gaps, false positive triage burden, detection coverage audit
- Concrete incident: credential stuffing against test API after infrastructure migration

**Central claim:** CLEAR — detection-as-code shifts security teams from writing rules to managing a maintenance obligation; that obligation compounds silently and the cost is paid during incidents, not before them.

**Title assessment:**
- "Detection as code is becoming detection as debt." — strong, direct observation, not a template pattern. Good choice.

**Opening:** "The moment you write a detection rule, you are taking on a liability." — immediately specific, not generic. PASS.

**Differentiation from recent 0623 posts:**
- 0623_0348: storage backends
- 0623_2135: interpretability
- 0623: trust half-life, perfect recall, code RL, revision pipeline, schema drift
- This post: detection debt — completely different thread from all above

**Hole assessment:**
- The "0.5% / 5%" rates are presented as illustrative scenarios, not measured data. This is borderline — it could be read as a real claim. Should be softened to "even a small false positive rate compounds across a large rule set."
- Otherwise clean.

**Verdict:** CLEAN PASS with one minor suggestion (soften the rate numbers). The draft has strong specificity, a clear central claim, no template patterns, and a concrete incident example. Proceed to editor.
