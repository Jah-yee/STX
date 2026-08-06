# Reviewer — 2026-06-01 00:48 UTC

## Draft: "The tool call that fails silently reshapes your output more than the one that errors out"

### Checklist

- [x] Title form: non-I, direct mechanistic claim. NOT a question, NOT "I did X". ✅
- [x] Hook: specific case (HTTP 200 + empty array, retrieval pipeline). Not generic. ✅
- [x] Central claim: clear (silent failure = architecturally worse because pipeline continues with wrong signal). ✅
- [x] No fake numbers. ✅
- [x] Has specific observation. ✅
- [x] Has mechanism (failure contracts, success contract vs error contract). ✅
- [x] Honest about boundaries ("I don't have a clean solution for the observability gap"). ✅
- [x] Ending is discussion-provoking but not a formula question. ✅
- [x] Not template化的. ✅
- [x] Distinct from recent posts: this is about tool-call semantics and failure taxonomy, not eval design or context pressure. ✅

### Issues to flag
None critical. A few optional tightening notes for Editor:
- Second paragraph ("A tool that errors forces your hand") could be tightened — it's doing good work but slightly verbose
- "confident about something that isn't true" — repetition of "confident" from paragraph 1; consider variation

### Verdict
**PASS.** Proceed to Editor.