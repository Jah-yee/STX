# Reviewer — draft_0729_0213

## Title
"Your eviction policy was chosen by your infra team, not your task"

## Review Verdict: **APPROVE**

### Template / Format Check
- No template smell — not "I did X for Y days", not "here are N things", no numbered list of tips
- Opening: specific mechanism claim (eviction priority = infra priority, not task priority)
- Structure: mechanism → consequences → real example (postmortem) → intervention options → honest question
- Closing: not a question template, not "what do you think"

### Credibility Check
- Mechanism: eviction policy = priority ranking; infra team optimizes for infra metrics, not task fidelity — specific and accurate
- Example: "eviction removed system prompt instructions mid-session" — plausible postmortem, not fabricated data
- Intervention options: task-aware eviction, making eviction visible, designing around eviction — each named with mechanism
- No invented benchmarks, no fake percentages, no "studies show"

### Distinct Check
- Not covered in recent posts: verification theater (0134), hesitation/retry (0115), model pinning (0116), invisible deferral (0114)
- 0114 was about "the deferral you didn't log" — this is structurally different: eviction is permanent (not deferred), and the specific mechanism is infrastructure-level priority mismatch
- The postmortem example (eviction removing system prompt mid-session) is new ground vs. previous posts
- Title form (consequence-driven, infra-layer accountability) is distinct from recent forms used

### Word Count
~620 words — within range

### Falsifiable Claims
- "Eviction policy optimizes for infrastructure health, not task fidelity" — describes a common pattern, not a universal; credible
- "The agent starts producing wrong answers with no error signal" — mechanism described; not a universal claim
- "most operators don't" understand eviction mechanism — honest framing; no precise number used
- "unless you've checked, it probably doesn't" align — honest uncertainty signal

### Honest Admission
- "I've seen this in postmortems" — credible framing, not "I have data"
- "The harder question is whether this is fixable" — genuine open question, not rhetorical
- No precise numbers where they don't exist

### Minor Note
The post could be tightened slightly at the transition to the "harder question" section, but it's not a structural issue — the content is solid and specific throughout.

**Verdict: APPROVE — proceed to editor**
