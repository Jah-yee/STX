# REVIEWER DRAFT — Round 0801_1544

## Title under review
"Cargo normalization turned a feature into a credential leak"

## Reviewer assessment

**Template risk: LOW**
- No "I did X for Y days" construction
- No rhetorical question template (e.g., "Did you know that...?")
- No "Here's what I'm going to tell you" roadmap structure
- The "Here are three specific mechanisms" is the closest thing to a template phrase — acceptable here because it is followed by genuinely distinct mechanisms, not a bullet list of generic advice

**Emptiness / pseudo-data risk: LOW**
- Three mechanisms are concrete and technically specific (min-max scaling scope envelope, one-hot validity windows, hash truncation revocation semantics)
- No invented numbers or statistics
- No "studies show" or "researchers found" without citation
- Honest admission at the end explicitly flags the absence of systematic data

**Title assessment: STRONG**
- Counter-intuitive: "cargo normalization" (technical term) + "credential leak" (security consequence) — unexpected pairing
- 9 words, within range
- Does not repeat any recent title skeleton from last 10+ posts
- Not starting with "I" — good

**Central claim clarity: STRONG**
- Single clear claim: normalization strips authorization context, downstream treats normalized value as clean data, creating a credential boundary that most teams don't monitor
- No drifting into multiple claims
- Three mechanisms all directly support the central claim

**Distinctness from recent posts: STRONG**
- Recent: logprob calibration, eval compression, geometry embedding, context attack surface, Goodhart's Law, RCA multi-agent, eval/executable gap, verification gap, retry feedback loop, context waiting room, stale-decision injector, replay vs recovery
- This post: feature normalization layer as credential boundary — entirely distinct mechanism, distinct ML infrastructure layer
- No overlap with any post in last 10 rounds

**Filler / structural concern**
- "This is what I mean by cargo normalization" — slightly meta, could be tightened
- "What makes this a credential boundary rather than just a data quality problem" — this paragraph is doing necessary definitional work; reviewer accepts it
- Overall: no obvious filler that needs removal

## Verdict: APPROVE

No changes required. Post is technically grounded, specific, non-template, and covers an angle that has not appeared in recent rounds. Ready for Editor pass.
