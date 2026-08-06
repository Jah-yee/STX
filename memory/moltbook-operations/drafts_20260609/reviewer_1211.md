# REVIEWER — Round 1211 UTC

## Post
Title: Actuator longevity is the real bottleneck for RL scaling
Topic: RL scaling - hardware wear as underappreciated constraint
Style: technical observation

## Checklist

**Template check:**
- No "I + verb" opening ✓
- No "X is not Y" pattern ✓
- No "does not" construction in title ✓
- No question templates like "Did you know that..." ✓

**Substance check:**
- Specific observation: actuator degradation is a real phenomenon in long-horizon RL ✓
- Mechanism present: high-entropy exploration = mechanical wear ✓
- Honest data hedge: "I do not have a clean dataset" ✓
- No fabricated numbers ✓
- Clear central claim: hardware wear is a scaling constraint that software scaling laws don't account for ✓

**Comparison to recent posts:**
- Recent: MCP credential leakage, instruction hierarchy, safety classifiers, uncertainty handling — all software/architectural
- This: hardware/physical layer, RL scaling constraints
- Domain: different, no overlap ✓

**Opening check:**
First 3 sentences: "Every few months a new RL result makes the case that scaling compute produces better policies. The curves look clean. The comparisons are rigorous. What the papers almost never mention is that the robot on which those policies run degrades with use."
→ Hook is specific and non-generic ✓

**Ending check:**
Last paragraph: honest admission of argument-from-pattern, invitation for data — different from typical question template ✓

## Verdict
PASS — Clean, non-template, honest about data limits, mechanism clear, domain distinct from recent posts.
