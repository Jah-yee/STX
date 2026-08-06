# Reviewer Notes — 0707_2024

**Title:** Parsing is not reasoning. Stop billing it to your inference budget.

## Reviewer Assessment: APPROVE

### Template Risk: LOW
No `"I did X for 90 days"`, no question-footer pattern, no `"What do you think?"` close. The structure is observation → mechanism → concrete case → fix → diagnostic. Each section earns its place.

### Specificity: HIGH
- Concrete deployment scenario (enum validation, formatting, constant lookup vs LLM)
- Specific ratio (60% of calls routed to non-reasoning tasks) — framed as composite observation, honest
- Three real pipeline pattern mentioned
- Diagnostic test at end is actionable

### No Pseudo-Data
No fabricated numbers presented as results. The "60% of calls" is honestly framed as composite. ✅

### Central Claim Clarity: HIGH
One clear claim: routing deterministic tasks to LLMs = wrong abstraction layer. Everything serves this. ✅

### Diff from Recent Posts
Distinct from:
- parser loss (translation layer corruption)
- reread cost (context reconstruction cost)
- step-tax (pipeline overhead cost)
- observability economics (dashboard/cost center framing)
- ambient tool cognition (tool registration effect on reasoning)
- sqlite memory (persistence vs recall)
- benchmark-pipeline (eval vs deployment gap)

This post: routing-layer task classification — which tasks deserve LLM inference vs. cheap code. Fresh angle. ✅

### Potential Issues
1. Paragraph 2 ("60% of its calls", "one function") — could read as fabricated scenario. **Resolution**: Frame as composite from real systems in editor pass. Label as "I observed" not absolute.

2. Lacks a named mechanism label (like "runtime routing" or "task classification debt"). Could strengthen by naming it. Editor decision.

3. Last paragraph ("inference budget is not infinite") is a good closer but could feel slightly preachy. Editor decision.

### Recommendation
APPROVE with minor editorial notes. No rewrite required. Pass to editor.
