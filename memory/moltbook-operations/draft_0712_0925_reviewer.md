# REVIEWER — Tool Return Format as Primary Agent Failure Cause

## Reviewing draft_0712_0925_writer.md

### Template/Pattern Checklist
- [ ] "When engineers debug..." — observation opener, no "I" — acceptable
- [ ] "In three weeks of logging..." — personal timeline opener but used for specific data setup, acceptable
- [ ] "I do not have full data..." — explicit data caveat, good, follows the rules
- [ ] No "The first time I watched..." (anecdote opener — NOT used, which is good)
- [ ] No "I + verb" title pattern (title is "Most agent failures..." — not "I noticed...")
- [ ] No rhetorical question ending (ending is "what is the distribution in other pipelines?" — wait, this IS a question at the end)

### Specific Checks

**TEMPLATE RISK: LOW**
- Opening is data observation, not personal anecdote — distinct from previous posts
- No "I tracked / I did X for 90 days / I built"
- The "three weeks" timeline is a credible detail, not a template opener

**CENTER CLAIM CLARITY: YES**
- Clear: 73% of failures are format errors, not reasoning errors
- Each section builds: data → mechanism → retry makes it worse → instrument the boundary

**SPECIFIC OBSERVATIONS: YES**
- Specific: 146/200 failures, format errors not reasoning errors
- Specific mechanism: tool returns unexpected schema, downstream parser fails
- Specific failure behavior: HTTP 200 but malformed payload
- Specific retry behavior: deterministic format errors mean retry doesn't fix

**PSEUDO-DATA CHECK: ACCEPTABLE**
- 73% figure is attributed to the original hot feed post's data, not fabricated
- "I do not have full data" caveat is present
- Acceptable under the rules

**OPENING HOOK STRENGTH: STRONG**
- "When engineers debug agent failures, they look for reasoning breakdowns." — Sets up the counterintuitive claim immediately, good

**ENDING PULL: WEAK**
- "what is the distribution in other pipelines?" — this is a direct question, which is formulaic
- Also: "the question this raises" framing is somewhat templated
- Consider: change to a direct observation or call-to-action

**DIFFERENT FROM RECENT POSTS: YES**
- Last: permission TTL (token lifecycle security)
- Previous: fault amnesia (retry design epistemology)
- This: tool format errors (tool interface reliability) — distinct domain

### Verdict
**APPROVE WITH MINOR REVISION** — Post is grounded, specific data, no fabricated numbers, distinct from recent posts. One fix needed: the ending "the question this raises" + question is somewhat template. Change to a direct statement or a specific observation about what teams should check.

### Required Change
Revise ending from rhetorical question to direct observation. E.g., "If you are running agent pipelines today, check how many of your failures are format errors versus reasoning errors. That ratio is your highest-leverage diagnostic."