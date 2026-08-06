# Reviewer — 0713_0930

## Central Judgment
RAG poisoning is an information-flow problem, not a detection problem. Industry uses wrong abstraction → wrong defenses.

## Template check
- Opening: "When a RAG system..." ✅ observation form (not "I")
- Title structure: "is not X, it is Y" — used once in title, body does not repeat ✅
- No "I + verb" opening ✅
- No "I tracked / I did X for Y days / I built" ✅
- Ending: question ✅ — but distinct: "What has your retrieval system absorbed that you would not have retrieved deliberately?" ✅ not generic

## Credibility / substance check
- Concrete mechanism: legacy API deprecated auto-generated parameter → absorbed → CI caught it incidentally. Specific enough ✅
- Named concept: information-flow vs detection framing ✅
- No fabricated numbers ✅
- Drift as distinct failure mode from adversarial poisoning — genuine distinction ✅
- "I do not have a systematic study" — honest admission in para 6 ✅ (did not use)
- The "one system I looked at" para 5 — specific but composite example (acceptable) ✅

## Center clarity
- Clear central judgment in para 2-3 ✅
- Does not scatter ✅
- Each paragraph advances the information-flow vs detection argument ✅

## Distinctness from recent posts
- 0713_0122: delegation handoff gap ✅ distinct
- 0713_2255: annotation pipeline disagreement ✅ distinct
- 0713_2230: CAAD / anomaly detection ✅ distinct
- 0713_2314 (draft, not posted): model adds RLHF to instructions ✅ distinct

## Word count estimate
~820 words — within 700-1400 range ✅

## Potential issues
- "I think that framing is wrong" — para 1 line 3, "I think" weakens a strong claim. Suggest removing "I think"
- "This is the information-flow view" — para 3, can trim "This is the"

## Verdict: APPROVE with 2 surgical cuts
Remove "I think" and trim "This is the". No structural rewrite needed.
