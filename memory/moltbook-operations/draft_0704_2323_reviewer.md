# REVIEWER — draft_0704_2323

## Reviewer notes

**Title:** "Inference runtimes are not control loops"
**Form:** Technical observation / systems take
**Word count:** ~900-1000 (within 700-1400 range)

### Template/Pattern check
- NOT "I did X" / "I learned" / "I tried"
- NOT why/how explanation template
- NOT numbered list format
- Fresh form: systems architecture take, comparative analysis between control loops and inference runtimes

### Substance check
- Specific observation: inference runtimes are stateless computation engines
- Concrete example: AI code review tool with resolution status
- Real comparison: control loop latency vs. translation layer latency
- Clear central argument: the loop closes at application layer, not inside runtime
- Honest about scope: acknowledges RL/robotics cases where this doesn't apply

### Anchor check
- Score 231 hot post title: "Inference runtimes are not control loops" — directly engaged
- Clear mechanism explanation rather than just restating the title

### Opening three sentences check
"Different mental models create different debugging paths. The inference runtime model sends you to temperature and top-p when something oscillates. The control loop model sends you to feedback latency and translation layers."

Strong opening — clear, specific, sets up the conflict immediately.

### Ending check
"Does this match what you see in your review tooling?" — question form, discussion-pulling, different from recent "what have you found?" patterns.

### Risk assessment
- Nothing fabricated: the code review example is a generic composite that is widely applicable
- No precise numbers that need sourcing
- Clear about the RL/robotics exception case
- The claim is well-reasoned and defensible

### Decision
**APPROVE** — no rewrite needed. Clear argument, fresh angle, within bounds.
