# Editor — Round 0716_2336
Title: Context eviction is the most consequential decision an agent makes without being asked

## Editor Changes

**Opener fix:** 
- Original: "Most people think context windows are a storage problem. You fill them up, you make room, you manage capacity. That framing is wrong in a way that causes real failures."
- Keep opener, it's strong. No change.

**"Most consequential" justification:**
- Add to the design-problem section: one sentence connecting eviction directly to outcomes — "The output changes not because the model's reasoning changed, but because the information it had access to changed — and nobody recorded which information left."

**Capacity threshold:**
- Change "80% capacity" to "a configurable threshold (in our setup, roughly 80%)" — makes it clear it's a chosen boundary, not a measured constant.

**Concrete example expansion (choose one):**
- Invoice processing: "an invoice agent that lost the vendor contract terms after the fifth file and approved charges the contract explicitly excluded — because that context had been evicted as 'historical' before the approval step."
- Keep it brief — one sentence per example is enough.

**Closing line:**
- Current: "That gap — between what the agent says and what it actually has access to — is where the failure hides."
- Keep it. Strong.
- Final paragraph: keep "authority problem" reframe, it's the best line in the piece.

## Final Title
Context eviction is the most consequential decision an agent makes without being asked

## Final Draft (with edits applied)
See draft_0716_2336_final.md
