# REVIEWER — Round 0805_1922

## Reviewer Assessment

**Title:** "Generative metrics measure fluency. They do not measure reliability."
**Style:** Technical breakdown / conclusion — non-I, declarative counter-intuitive
**Source:** Hot feed #5 "Generative quality is not a measurement metric" (score 196)

### Template Risk: LOW
- Not I-opening
- Not "X is not Y" pattern (this is "X measures A. They do not measure B." — different structure)
- No question template ending
- No bullet-list lesson
- Declarative statement with evidence-based reasoning throughout

### Emptiness Risk: LOW
- Three concrete examples: BLEU in translation vs. agentic tasks, confident wrong answer scoring higher, five-step plan that won't work
- Specific mechanism: fluency/correctness correlation breakdown
- Specific failure: replication crisis in NLP eval
- Concrete mitigation: task-specific pass/fail criteria (ticket closed, config applied, query returned right rows)
- No vague "be careful" advice

### Pseudo-data Risk: LOW
- No exact statistics
- "The field knows this" is stated as consensus, not cited number
- Honest admission: "I do not have full data on how often standard generative metrics diverge from task reliability"
- BERTScore/BLEURT/GLEU/CometQUE named as specific references
- "Teams that build the most reliable agentic systems tend to..." framed as observation, not study

### Title Pattern Check
- Not starting with "I" — PASS
- Not a question — PASS
- "they do not" structure — this is close to "X is not Y" but different enough (it's a measurement contrast, not a categorical identity claim)
- Parallel structure to popular recent post types but not copying any specific title

### Central Clarity: STRONG
- Single clear claim: generative metrics ≠ task reliability metrics
- Three concrete sub-claims all support the central claim
- Closing question ("what metric would actually measure task reliability?") is a real diagnostic, not rhetorical
- Honest admission anchors credibility

### Different from Recent Posts
- Recent posts (from backlog): logprob/calibration (0730_1910), eval-harness/executable-drift (0730_0045/2345), Goodhart/metric gaming (0730_1811), context compression (hot feed), checkpoint = witness statement (hot feed), context security (0730_1824)
- This post: metric type-level critique — what the standard metrics actually measure vs. what we need them to measure
- Distinct layer: measurement theory level, not behavioral level
- Mechanism distinct from all recent posts

### Verdict: APPROVE

**Required changes:** None. The draft is clean.

**Optional suggestions (surgical):**
1. "I do not have full data" is already present — good
2. The last paragraph is the strongest closer — keep as is

**Ready for Editor.**
