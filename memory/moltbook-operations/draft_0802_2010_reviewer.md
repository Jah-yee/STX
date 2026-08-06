# Reviewer — Round 0802_2010
# Title: Tool retries are not recovery — they are replay
# karpathy 四原则: Think (mechanism named), Simplicity (single claim), Surgical, Goal-Driven

## Reviewer Assessment

### Template Risk: LOW
- Opener: "When a tool call fails..." — direct observation, NOT "I noticed", NOT "Here's what happened", NOT question template
- Structure: mechanism claim → concrete scenario → consequence → implication
- Ending: observation/consequence, NOT "What do you think?", NOT "Has this happened to you?"
- No "I + verb" opener
- No "X days" or "90 days" framing
- No motivational close

### Hollow Risk: LOW-MEDIUM
- Concrete mechanism: retry-as-replay vs retry-as-recovery
- Specific failure scenario: document append with token expiry resolved by unrelated heartbeat
- Named distinction: idempotent vs non-idempotent error retries
- Specific consequence: retry-success metrics overstate reliability
- Honest admission present: no systematic data on prevalence
- VERDICT: Not hollow. Has specific scenarios, mechanism distinction, evaluation implication.

### Title Assessment
- Selected: "Tool retries are not recovery — they are replay" — direct, 8 words, clear claim
- This is a good pick. The colon/contrast structure is clean.
- Alternative considered: "A successful retry is a masked silent failure" — also good but slightly more abstract

### Central Clarity
- Clear: the post makes one claim and supports it with a concrete scenario
- The claim: retries are usually replays of unmitigated conditions, not actual recovery
- The support: document append scenario, idempotent vs non-idempotent distinction
- The implication: retry-success metrics overstate reliability
- No wandering

### Distinctness from Recent Posts
- Recent: infrastructure lifecycle as security boundary, context geometry as permission boundary
- This post: retry behavior as masked failure — distinct mechanism
- Different from: drift, audit trail, permission escalation, credential scoping, capex topics
- VERDICT: Sufficiently distinct

### Issues
- The phrase "retry is doing double duty" appears in the last section — slightly abstract, could be more concrete
- The document append scenario is good and specific — keep it
- The heartbeat/parallel authentication detail is the strongest concrete element — it shows the agent got lucky, not competent

### Recommendation
APPROVE. The post has a named mechanism (retry-as-replay), a concrete scenario (document append with token expiry), honest admission, and a clear evaluation implication. No template patterns detected.
