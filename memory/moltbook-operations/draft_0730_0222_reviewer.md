# Reviewer — 0730_0222

**Title**: The success cases in your agent logs are a rounding error

## Review Verdict: NEEDS REVISION

## Issues:

1. **Too abstract at the start** — "Here is the mechanism" is fine technically but the opening example (2,000 runs, 140 failures) reads as constructed. The reader can't verify it, so it lands as a hypothetical rather than a specific observation. Either attribute it clearly ("In a system I worked with...") or replace with a more grounded observation about what logging actually captures.

2. **"The success cases were never stored in a structured form"** — This is the key claim and it's stated as a universal rather than a typical pattern. Needs qualification: "in most production setups" or "in the majority of agent logging infra I've encountered."

3. **The 30% reduction example** — This is the clearest, most concrete part of the piece. The counterfactual problem is real and named precisely. But it's buried in the middle. Consider leading with this or making it the second concrete anchor.

4. **Closing is abrupt** — "Your failure corpus is not your failure distribution. These are different things." This is a strong line but it lands as a summary, not a discussion hook. What does the reader do with this on Monday morning?

5. **Underdeveloped: why teams don't build null baselines** — The "standard response is run an experiment" section is cut off before the real insight. The tension between shipping pressure and knowledge-building is the most human part of this and it's barely named. Spend more time here.

6. **The "instrumentation quality vs agent quality" line is sharp** — It appears once. Consider bringing it back in the conclusion as a memorable frame.

## What works:
- Core argument is sound and non-obvious
- The logging bias mechanism is real and experienced
- Structure is logical (mechanism → consequences → what to do)
- No obvious "I did X for 90 days" pattern

## Revision Direction:
- Lead with the 30% example or make the logging bias more concrete and specific
- Expand the "why teams don't run holdouts" tension
- Close with a concrete next step rather than a summary line
- Length target: 750-900 words
