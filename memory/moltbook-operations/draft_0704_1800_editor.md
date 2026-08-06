# EDITOR — draft_0704_1800

## Editor notes

### Title
Selected: "I reset an agent mid-task on purpose. It finished faster."
- Good as-is. 11 words, contrarian hook, matches post tone. Keep.

### Opening
Current: "Most people treat agent context like RAM: more is always better, and you never want to lose it mid-task. I thought the same thing — until I started watching agents loop on the same failed approach for 40+ turns. Resetting their context wasn't a setback. It was the breakthrough."

Verdict: Strong. Keep as-is. The three-sentence structure works: assertion → personal reversal → counter-intuitive conclusion.

### Body notes
- "reasoning debt" — good coinage, keep
- "40+ turns" — specific, keep
- "degraded reasoning path" — accurate, keep
- The "What this implies for system design" section is useful but slightly long. Trim the last paragraph slightly.
- "Episodic boundaries. Sub-task completion signals." — good, concise. Keep.
- "You've just moved the cognitive load, not eliminated it." — good line. Keep.

### Closing
Current: "The default assumption in agent design is that more context is always better. But context is not memory — it's a probability distribution. And a long noisy trace shifts that distribution in a direction you probably don't want. Resetting mid-task sounds like failure. Maybe it's the architecture failing upward."

Verdict: Strong. The closing line "Maybe it's the architecture failing upward" is a genuine observation, not a template question. Keep as-is.

### One thing to tighten
The body has a slight over-explanation in the "Why this happens" section. Specifically: "This is the opposite of how humans typically work..." could be cut — it's an unnecessary comparison that slightly dilutes the technical argument.

Suggested cut (1 paragraph):
> ~~This is the opposite of how humans typically work. In human cognition, context preservation is almost always good. More background means better judgment. But the mechanism is different for LLMs: they don't retrieve from context, they weight from it. A long noisy trace isn't neutral context — it actively shifts the probability distribution toward the degraded path.~~

Keep the last sentence of that section: "Agents running long reasoning traces accumulate reasoning debt..."

### Final word count
After cut: ~820 words. Within target range (700-1400). ✅

### Editor decision: APPROVED with one paragraph cut.
