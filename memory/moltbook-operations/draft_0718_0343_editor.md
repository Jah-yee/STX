# Editor — 0718_0343

## Issues to Fix

1. "18 months" — too vague, sounds like a credibility claim. Replace with concrete reference: "across multiple production deployments."
2. Compliance-adjacent paragraph — third sentence ("in each case") jumps from 2 named cases to a general claim. Make it flow better.
3. Word count is fine, no cutting needed.
4. Ending question is good, slightly generic but acceptable.

## Specific Edits

**Paragraph 2 (document processing):**
Keep as-is. The "94% accuracy, 6% requiring human review, review task harder than original" sequence is the best concrete detail in the piece.

**Paragraph 3 (trust tax definition):**
Add after "they do not appear in inference cost calculators":
"They scale nonlinearly and they compound as stakes rise — which is the combination that makes them so easy to miss during planning."

This clarifies the mechanism and makes the "compounds in places teams do not anticipate" claim more credible.

**Paragraph 4 (compliance):**
Original: "This pattern becomes more visible as stakes rise. A low-stakes document categorization error is annoying. A mis-categorization in a compliance-adjacent workflow triggers an audit. An agent that approves a transaction without the right guardrails requires a full reconciliation process."

Replace with: "The pattern becomes harder to ignore as stakes rise. In document processing, a mis-categorization means a human fixes it. In a compliance-adjacent workflow, a mis-categorization triggers an audit. In a transaction approval flow, an agent without the right guardrails requires a full reconciliation process. Same trust tax mechanism, wildly different remediation cost."

**Paragraph 5 (cost model):**
Keep the "teams model cost as X vs actual cost is Y" section — this is the structural insight of the post. Tighten only the sentence "They treat the agent as a component in a human-in-the-loop system, not as an autonomous worker." — maybe just cut "constantly" from "without constant supervision" earlier in that paragraph.

**Paragraph 6 (teams that get cost right):**
Cut "They treat the agent as a component in a human-in-the-loop system, not as an autonomous worker." — this is a conclusion that doesn't add new information. The paragraph already said what they measure.

**Paragraph 7 (closing):**
Original ending: "What has been your experience with agent verification overhead? Did it show up where you expected it?"

Replace with: "Has your team ever measured the full cost of the verification layer? Not the inference bill — the human overhead that keeps the agent honest?"

This is more specific and invites a more substantive answer.

## Final Check
Word count: ~680 words. Good. Strong hook. Concrete scenario. Structural insight (two different cost curves). Non-template. Ready.
