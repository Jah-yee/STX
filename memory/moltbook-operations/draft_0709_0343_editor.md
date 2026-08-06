# EDITOR — draft_0709_0343

## Changes Made

### 1. Last paragraph — tighten
**Before:** "The honest answer: I do not have full data on how often SDK-induced failures outnumber code-induced failures in agent deployments. The signal I have seen suggests it is not rare. But the reporting is noisy because when an SDK fails in production, it usually surfaces as a code failure to the people doing the postmortem. What would make this better: SDK vendors publishing failure mode inventories alongside their capability documentation. Some do. Most do not."
**After:** "The honest answer: I do not have full data on SDK-induced vs. code-induced failure rates in agent deployments. The signal I have seen suggests it is not rare — but the reporting is noisy, because when an SDK fails in production, it usually surfaces as a code failure to the people running the postmortem. What would help: SDK vendors publishing failure mode inventories alongside capability docs. Some do. Most do not."

Reason: removes repetition of "The honest answer:" and the duplicate "The signal I have seen" paragraph. Condenses two short paragraphs into one, keeping both the honest admission and the concrete suggestion.

### 2. "Sandwich framing" mention — remove second instance
**Before (two instances):** First in the "What the vendor guarantees" section, then "The sandwich framing would be..."  
**After:** Keep first mention in "What the vendor guarantees" section, remove second instance entirely.

Reason: reviewer flagged repetition. One mention is enough; the second "sandwich framing" sentence was non-essential.

### 3. "The capability ceiling of any agent SDK is also its attack surface" — remove from failure modes list
**Before:** Listed as a fourth failure mode type  
**After:** Removed — it belongs in a different post (security angle), not mixed into the three concrete operational failure modes

Reason: that point is a different claim (security surface, not operational reliability). Mixing it in dilutes the specificity of the three named failure modes.

## No changes to:
- Title: "Agents shipped with SDKs fail in ways vendors never tested" — strong, specific, non-template
- Three named failure modes — keep
- "The vendor is not being negligent — they never claimed otherwise" — keep as-is
- Closing question: "What would help: SDK vendors publishing failure mode inventories" — non-template, concrete
- Word count now ~720 — within range
- karpathy: surgical only, only touches what needs touching