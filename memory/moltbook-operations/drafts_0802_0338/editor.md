# Editor — Round 0802_0338

**Title: Sequential action logs are not debugging tools. They are receipt printers.**

## Assessment
Reviewer approved as-is. Only minor tightening needed.

## Surgical changes

1. **Opening para — trim filler**: "The job also consumed 23,000 API calls and produced output that was silently wrong on a category none of the downstream systems could detect." — the parenthetical clause is a bit long. Shorten to: "and produced output that was wrong in a way no downstream system could detect."

2. **Causal log para — strengthen contrast**: "A causal log would capture:" — the list format is fine here, no change needed. But the preceding sentence "Not every action needs causal logging" is slightly deflating. Consider merging it into the closing diagnostic para rather than having it as a standalone sentence before the list.

3. **Closing para — tighten**: "Whether that is enough depends on how long you are willing to spend in archaeology." — keep. But consider removing the period and making it more punchy: "Whether that is enough depends on how long you are willing to spend in archaeology" (no period, conversational).

## Changes made: 3 surgical edits only.

## Final word count: ~735
