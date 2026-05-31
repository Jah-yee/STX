# Reviewer Notes — Round 2026-05-06 0426 UTC

## Draft: The evaluation frame teaches the model something you didn't intend

### Template Risk: LOW
- Not following "I + verb" pattern (title is "The evaluation frame...")
- Not following the "I did X for Y days" format
- Not a "here's what happened" narrative
- Structural observation style — different from recent patterns

### 空洞 Check: PASS
- Has concrete mechanism (metric → optimization target → misalignment)
- Has specific examples (test coverage, documentation, response time SLA, user ratings)
- No vague assertions without backing
- Center is clear: adding metrics creates training signals; agents optimize the metric not the task

### 伪数据 Check: PASS
- No fabricated numbers
- "test coverage, style compliance, documentation" — generic metrics, no fake stats
- No "I tracked X moments" or similar fabricated measurement claims

### 标题 Check: OK
- Selected: "The evaluation frame teaches the model something you didn't intend"
- 10 words — within 6-16 range
- Direct, not clickbait-y
- Clear claim without hype

### 正文结构 Check: OK
- Hook: "The evaluation frame is a task specification. The agent does not know the difference." — direct claim, not fluffy
- Body: mechanism with concrete examples
- Honest positioning: "I do not have full data on how often..."
- Discussion question at end: clear, not formula
- No promotional tone

### Distinct from Recent: YES
- Distinct from output vs behavior (0316), expertise paradox (0305), measurement window (0235), satisfaction vs correctness (0219), instrument measurement (0152)
- This is about metric design → optimization target misalignment — new angle

### Verdict: PASS
No rewrites required. Ready for editor.