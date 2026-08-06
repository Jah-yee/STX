# 0728_1237 Reviewer Notes

## Draft: "Your agent is waiting on a model that wasn't built for agents"

### Template Check
- NOT template-generated. Distinct opening ("When you build an agent, you reach for the best model") — not a stock opener.
- No "I + verb" title opener — title is "Your agent..."
- No question mark, no number-led structure
- PASS

### Content Check
- Concrete mechanisms: filesystem navigation agent (1), database query agent (2) — two distinct domains
- Specific failure mode: latency tax compounding per tool call — quantifiable in principle
- Central thesis: infrastructure models are optimized for throughput, not agent loop latency — clear and defensible
- Honest admission: "I do not have systematic benchmark data" — appropriate, not apologetic
- No pseudo-data or inflated claims

### Structural Check
- Opening: grabs attention with counterintuitive framing (best model + idle time = surprising)
- Two concrete mechanisms (filesystem, DB query)
- Technical nuance: batch throughput vs single-call latency — meaningful distinction
- Closing: actionable framing (treat latency as architectural constraint, not model selection problem)

### Title Check
- Selected: "Your agent is waiting on a model that wasn't built for agents" — 9 words, direct, counterintuitive
- Previous titles in recent rounds used: observation sentences, question forms, "X vs Y" comparisons, declarative conclusions
- This is a "your X is doing Y" pattern — distinct from recent templates
- PASS

### Word Count
~662 words — slightly below 700-minimum target. Recommend adding 1 short para (50-80 words) before the closing to flesh out the actionable recommendation section.

### Verdict: APPROVE with minor expansion
