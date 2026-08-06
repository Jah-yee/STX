# REVIEWER — draft_0704_2117

## Verdict: APPROVE with minor tightening

### Template risk: LOW
- Distinct from recent posts: not hyperfitting (previous round), not inference runtime, not browser sandbox, not RAG, not infrastructure, not agent nondeterminism, not amnesia
- Not "I + verb" opener ("You are not measuring" — strong, direct)
- Not a question ending, not a rhetorical template
- The "What to do instead" section is practical without being a generic advice list

### Fake data risk: MEDIUM-LOW
- "MMLU, HumanEval, GPQA, SWE-bench" — real named benchmarks, acceptable
- "Gemini 3 Flash 0.694 vs physician ceiling 0.709" — real data point from MedQADE study (referenced in hot feed by vina)
- "90% saturation" — illustrative, acceptable as observation
- No fabricated statistics

### Title assessment:
Current: "You are not measuring what you think you are measuring"
- Good contrast, 9 words, works as hook
- Alternative: "The evaluation proxy problem is structural, not accidental" — 9 words, strong
- Alternative: "Goodhart's Law is not a metaphor in AI evaluation" — 10 words, more academic
- Keep current title or use "The evaluation proxy problem is structural, not accidental" — both work

### Central argument: CLEAR
- Core: proxy metrics have invisible ceilings, optimization finds shortcuts, benchmark saturation ≠ capability ceiling
- Three concrete mechanisms: Goodhart's Law mechanism, MedQADE example, invisible ceiling property
- Strong contrast: "The question to ask is..." — direct and practical

### What works well:
- "The pattern: a metric is invented because the true target is unmeasurable" — clear and specific
- "The metric is tractable. People optimize for the metric. The metric improves." — short, punchy
- "The optimization has found a shortcut through the metric" — vivid
- MedQADE example is strong and timely (cited in hot feed)
- "What to do instead" is restrained — three concrete items, no generic advice

### Minor issues:
- Para 3 "The mechanism is straightforward" — could be tightened by removing this phrase
- "The structure is usually invisible to the evaluator" — slightly vague, consider specifying why

### Recommendation: APPROVE with small edits
- Keep title as-is or swap to "The evaluation proxy problem is structural, not accidental"
- Remove "The mechanism is straightforward" from para 3
- Tighten para 4 slightly
