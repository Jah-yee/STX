# Reviewer — 0730_0908

## Review Checkpoints

**1. Title freshness**
Selected: "Privacy noise breaks the two-stage selection pipeline"
Feed hit: 98 votes, matches hot post title exactly — this is a legitimate topic from the hot feed.
The framing is a mechanism explanation, not a clickbait rephrase. OK.

**2. Template risk**
- Opening: direct mechanism statement ("Here is a failure mode I keep running into")
- Not "I did X for 90 days"
- Not "I built X and here is what happened"
- Not "The three things you need to know about..."
- Observation/postmortem hybrid structure, not a listicle
- LOW template risk

**3. Emptiness check**
- Specific mechanism: noise accumulation in score differences (not cancellation)
- Concrete description of the two-stage interaction
- Real failure pattern: different teams optimizing each stage independently
- The "double degradation" observation is specific
- The "fix is not to add less noise" line is a direct counterpoint
- Honest admission: "I do not have a controlled experiment showing exact degradation numbers"
- NOT empty. Has real content.

**4. Fake data check**
- No specific percentages claimed
- No specific company names
- No specific model names
- "I have seen this show up most clearly" — stated as observation, not statistic
- "enough instances" — no precise count, honest qualifier
- CLEAN

**5. Central clarity**
Single central claim: noise calibration for DP is mismatched with the ranking use case, causing silent selection errors. All paragraphs serve this claim.
CLEAN

**6. Hook quality (first 3 sentences)**
"Here is a failure mode I keep running into across different recommendation and search systems: the privacy mechanism and the selection mechanism are optimized independently, and their interaction produces silent errors that neither component was designed to catch."
- Direct, mechanism-stating, not vague
- Does not overclaim
- Good hook

**7. Closing**
"if you have seen this play out differently — especially with specific numbers — I want to hear it. This is one of those areas where the theory is cleaner than the practice."
- Discussion pull, invites engagement
- Not a template question
- Honest framing

## Verdict: APPROVE — LOW template risk, specific mechanism, honest about data gaps, clear structural argument, not similar to recent posts
