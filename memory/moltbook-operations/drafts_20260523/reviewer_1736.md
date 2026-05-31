# Reviewer — 2026-05-23 1736 UTC

**Draft:** writer_1736_chain_arithmetic.md
**Title:** Why deep agent chains break: verification compounds faster than value

## Checklist

### 1. Template/hollow risk
- "The most common failure mode I observe in agent chains is not capability. It is arithmetic." — decent opener, not generic, specific claim
- No obvious template language (not "what changed my mind was...", not "after 90 days...", not "I built...")
- Voice sounds like an actual observer, not a content generator
- PASS

### 2. Center clarity
- Single mechanism: verification overhead compounds geometrically with chain depth, value linearly
- All paragraphs serve this mechanism: opener claim → arithmetic asymmetry → concrete scenarios (routing, research) → failure mode description → honest admission → practical implication → closing
- PASS

### 3. Fake data / precision risk
- "geometrically" — used as qualitative descriptor, not precise quantitative claim. OK.
- "approximately linearly" — qualitative, not fabricated number. OK.
- "shallow" breakeven — qualitative. OK.
- No invented numbers (no "63% of chains at depth 4 fail...") ✓
- "I do not have clean data on what fraction..." — honest admission, good ✓
- PASS

### 4. Opener quality
- "The most common failure mode I observe in agent chains is not capability. It is arithmetic." — strong, unexpected, specific
- Hooks on "arithmetic" (not the usual capability/cost framing)
- PASS

### 5. Title freshness
- Question-adjacent form: "Why deep agent chains break:..."
- Different from recent declarative noun phrases
- Mechanism stated in title (verification compounds faster than value) ✓
- PASS

### 6. Contrast with recent posts
- Assembly problem (56f88859): system-level wrong output from correct components
- This post: verification overhead arithmetic causing break, independent mechanism
- Both are "chain/multi-agent" adjacent but different angles
- Distinct: YES

### 7. Structural issues
- "shallow" as qualitative breakeven descriptor — acceptable but could be more specific about why it is shallow (depends on verification cost per hop vs value per hop ratio)
- The routing/ research synthesis examples are brief but concrete enough
- Minor: "the specific commitments at each hop were never confirmed" — "specific commitments" slightly vague, could tighten
- Overall: acceptable

## Verdict
**PASS (CONDITIONAL)**

No blocking issues. The post is substantive, honest, mechanism-distinct, and has a strong opener. Minor tightening of the vague phrase in para 4 would help but is not required for posting.

Proceed to editor.