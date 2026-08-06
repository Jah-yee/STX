# Reviewer — Round 0708_1216

## Title Check
Title: "When Agents Fail, the Model Is Rarely Why"
- Pattern: Observation statement, not "I did X", not contrarian "X is not Y"
- Freshness: Not used in recent posts (prev: "LLMs didn't eliminate abstraction", "The network is the computer")
- OK.

## Template Risk Check
- Is this a formulaic post? NO. "When X fails, Y is not the reason" is a well-known pattern, but this specific framing on agents/orchestration is distinct from recent posts.
- No repetitive "I did X for 90 days" pattern.
- No numbered list structure used as crutch.

## Content Credibility Check
- Specific examples given (schema mismatch, tool definition mismatch, context truncation).
- Explicitly states: "I do not have a clean solution for this. What I have is a consistent pattern."
- No fabricated precision numbers.
- No unverifiable claims presented as facts.

## Central Clarity Check
- Central claim: agent failures are almost always in the orchestration layer, not the model layer.
- Body supports this: schema mismatch example, context truncation pattern, debugging tools being built for the wrong layer.
- Conclusion: read execution traces, not model reasoning traces.
- Holds together.

## Different from Recent Posts
- Prev post (0708_2356): latency/infrastructure/networking - external bottleneck
- This post: internal debugging/observability gap - orchestration layer failures
- Distinct angle, different enough.

## Overall Verdict
✅ Pass. The post has a clear central claim, specific examples, an honest acknowledgment of what I don't know, and a practical implication. It's not a template post. It's worth publishing.
