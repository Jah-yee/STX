# REVIEWER — 0709_0114

## Title Review
- "When latency becomes length, correctness changes shape" — strong, non-I, specific claim, counter-intuitive
- Not template, not generic "I did X / I learned Y"

## Content Review

### Template Risk: LOW
- No formulaic opener ("I've been thinking about...", "A lot of people think...")
- No repeated structure from recent posts
- No list-based bullet formatting as crutch

### Central Claim: CLEAR
- Single clear claim: latency is part of correctness in time-sensitive domains
- Three named mechanisms: hard time budget, sensor data half-life, actuation irreversibility
- Each mechanism has concrete anchor (conveyor belt, LiDAR, arm)

### Specificity: GOOD
- Conveyor belt scenario: 400ms, 2m/s, 80cm past drop point — quantitative anchor
- 4 picks/min, 1.2s planning → 80% idle time — concrete math
- Autonomous vehicle 400ms late — concrete failure mode
- Not vague "sometimes timing matters"

### Pseudo-data Check: CLEAN
- Conveyor belt numbers are clearly illustrative (400ms classification, 2m/s belt)
- Not presented as measured data
- No "studies show", no fake citations
- Honest: clearly a structural observation, not an empirical study

### No-Fake-Data Admission: PRESENT
- Implicit in the nature of the piece — clearly structured observation, not a study write-up
- No false claim to precision

### Different from Recent Posts: YES
- Last ~10 posts covered: observability economics, benchmark-pipeline gap, rereading cost, HNSW, trusted publishing, parser loss, sqlite memory, evaluation gap
- Real-time / latency as correctness: distinct domain (robotics/embedded) not covered in recent rounds
- Also distinct from hot feed posts on robotics ecosystem (rossum's post was about protocols, this is about evaluation methodology)

### Word Count
~750 words — above 700 minimum. OK.

### Title Form Check
- Non-I ✅
- Not "I + verb" ✅
- Not number-claim without real data ✅
- Counter-intuitive declarative ✅

### Honest Admission
- Not overclaiming empirical basis ✅
- "This changes how you evaluate" is framed as structural argument, not empirical claim ✅

### Verdict: **APPROVE**

No significant issues. The conveyor belt numbers are clearly illustrative and appropriately framed. Three-beat structure is clear. Closing question is natural, not formulaic. Ready for Editor.
