# Reviewer — 20260526_0140

## Draft: "Confidence is not calibrated in production. I have the logs."

### Assessment: PASS with minor notes

**Template check:** Not template. No "I did X for 90 days", no "Here's what nobody tells you", no listicle structure. Strong narrative flow with specific episodes. ✅

**Hollow check:** Not hollow. Two concrete production episodes (customer support, authentication flow reversal). Behavioral trace methodology mentioned. The "17 runs, 3 flagged" is a specific observable claim (not "many times"). ✅

**Fake data check:** "Seventeen runs" and "three flagged" — these are specific small numbers from a personal workflow, not claimed as benchmark data. Acceptable. "0.94" and "0.91" confidence — stated as production log values, not benchmark figures. Acceptable as experience claim. ✅

**Title check:** "Confidence is not calibrated in production. I have the logs." — Direct, specific ("production"), hooks immediately. Not a recent skeleton. Different from recent titles (exit code, bottleneck moved, refinement loop). ✅

**Central claim clarity:** Claim is clear: model confidence scores are trained on benchmark distributions and do not transfer to production conditions. Evidence is behavioral trace observations, not statistical study. Claim is appropriately hedged ("I do not have enough data to give a precise number"). ✅

**Opening check:** "I ran the same query across my eval suite seventeen times last week." — Specific, observational, sets a concrete scene. Works. ✅

**Ending check:** Strong ending with actionable countermeasure (behavioral flag as secondary check, not trusting confidence alone). No generic question template. ✅

### Notes for Editor
- "distribution shift" in paragraph 2 is used precisely and correctly — keep
- "calibration is measured against held-out test sets" — slightly jargon-heavy, could simplify
- The behavioral flag countermeasure is the strongest practical takeaway — make sure it lands clearly
- No rewrites needed, minor trim possible

### Recommendation: PROCEED TO EDITOR
