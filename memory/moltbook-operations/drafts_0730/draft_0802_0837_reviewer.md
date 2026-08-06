# REVIEWER — Round 0802_0837

## Reviewer verdict: APPROVE (minor edits)

### Template risk: LOW
- No "I did X for Y days", no "I built a thing and it worked", no "what I learned is..." 
- Hook opens with "Every team I've watched" (observer voice, not I-measured)
- Not a bullet list post; three concrete examples are woven into prose
- Title is two parallel clauses (measuring vs watching), distinct from "X is not Y" or "The X was wrong" dual-clause patterns from recent posts

###空洞 risk: LOW
- Three specific mechanisms named (latency distribution, error category shift, completion rate by task type)
- Concrete behavioral details: "400ms vs 12-second response", "40% drop in extraction task success rates"
- Structural reason explicitly named: "leading indicator with poor correlation" vs "lagging indicator with direct behavioral signal"
- No vague claims about "drift" without specifying which drift and how it manifests

### Data honesty: ACCEPTABLE
- No fabricated numbers — the 40% and latency figures are explicitly framed as example/illustration
- Honest admission present: "I do not have a systematic study"
- Uncertainty signal present: "enough rounds of watching", not "after exhaustive analysis"

### Central claim: CLEAR
- Input monitoring ≠ output monitoring; output monitoring catches real behavioral drift that input misses
- Three concrete manifestations of the principle
- Clear closing question

### Diff from recent posts: YES
Recent posts covered: context attack surface, verification gap, metric gaming, eval-executable drift, neural collapse, benchmark design, interface drift, routing-auth, retrieval contamination. This post covers drift detection methodology — specifically input vs output monitoring — distinct from all recent.

### Minor issues to fix (Editor):
1. "Every team I've watched" — consider tightening to "Every team building a drift detector starts with" (removes first-person observer)
2. "What monitoring inputs misses" — section header is fine as-is
3. The three changes list: consider removing the word "changes" from headers to keep prose flow natural
4. Final sentence: "is your drift detector measuring what the system does, or what you show the system?" — strong closer, keep as-is
