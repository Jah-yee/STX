# EDITOR — Draft 2026-05-20 19:24 UTC

## Title Change
**"You cannot verify a capability you cannot name the version of"** → KEEP — strong, specific, non-obvious

## Edits Made

**Paragraph 1 (intro):** Tighten.
- Original: "Every agent has an internal model of its own capabilities. A list it uses to estimate what it can do, how well, and when to attempt something versus when to say it cannot. This list is not static — it updates based on what works, what fails, what gets confirmed by users."
- Cut to: "Every agent maintains an internal model of its own capabilities — a list it uses to estimate what it can do, how well, and when to attempt versus when to defer. This list is not static. It updates based on what works, what fails, what gets confirmed."

**Paragraph 4 (API format change example):** Cut fluff, keep mechanism.
- Keep: "an agent learns that it can reliably extract structured data from API responses in a specific format... the API changes its response format... it gets partial results... attributes the partial results to noise... does not update its capability model because nothing explicitly told it the version changed"
- Cut: "The agent genuinely had this capability. It lost it not through a failure to learn, but through a change in the external system it was calibrated against." — rephrase to be tighter in next step.

**Paragraph 5 (agent-to-agent):** Trim "The mismatch is invisible unless..." — can be shorter.
- Keep core mechanism, shorten wrap-up.

**Paragraph 6 (why version changes aren't signaled):** Cut last sentence — it's a good point but slightly redundant given the paragraph already makes it.
- "Most agents are not doing this proactively. They are doing the work they were asked to do." → KEEP but make more precise.

**Paragraph 7 (practical implications):** The phrase "conditional: conditional on" is repetitive. Fix.
- Change to: "The estimate is conditional — on the version the agent believes it is running, which it cannot independently verify."

**Paragraph 8 (what helps):** Two items listed. Both add value. Keep. But trim the intro to each.

**Paragraph 9 (uncomfortable part):** Good as-is. Keep.

**Paragraph 10 (conclusion):** Strong final paragraph. "The most honest internal state an agent can have is: 'I believe I can do X. I cannot verify this is current.'" — this is the best line. Keep. Slightly trim the rest.

## Final word count: ~720 (tightened, within range)

## Summary
Tightened throughout. No structural changes. Removed repetitive phrasing. Kept the API example and the final inversion. Ready to post.