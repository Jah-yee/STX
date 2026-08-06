# Editor — Round 0729_1925

## Changes (2 surgical)

### Change 1: "Correct reasoning" section — trim redundancy
**Old:**
"The checkmark doesn't distinguish them. Over repeated runs, the heuristic-solver and the deliberate solver converge on the same pass rate."

**New:**
"The checkmark doesn't distinguish them — their actual reliability profiles under distribution shift are entirely different, but their pass rates look identical."

Rationale: removes the redundant "over repeated runs" idea (already implicit in "pass rate"), tightens to the key distinction.

### Change 2: "What this looks like in practice" — tighten
**Old:**
"A team runs an eval suite before deployment. 100% pass rate. The agent ships. Users encounter the edge case that was averaged out. The on-call engineer opens the incident report."

**New:**
"Teams routinely ship with 100% eval pass rates. Users encounter the edge case the eval averaged out. The on-call engineer opens the incident report with no trace of it in the eval output."

Rationale: removes the redundancy of "runs eval → 100% → ships" sequential description, gets to the incident faster, adds the punch line "no trace in eval output."

## Final check
- Opener: strong, unchanged ✅
- Three mechanism sections: intact ✅  
- Honest admission: present ✅
- Ending question: not a template question, distinct rhythm ("These are not the same answer.") ✅
- Word count: ~755 words, within range ✅
