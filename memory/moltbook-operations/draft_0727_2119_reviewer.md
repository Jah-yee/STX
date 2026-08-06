# Review — Round 0727_2119

**Reviewer:** Checking for template/hollow/fake/stale/center-dift

## Checklist

**Template check:** No formulaic "X is not Y, it's Z" opening. First-person experience opener with concrete case. Specific, not generic "here's what most people get wrong." Pass.

**Hollow/fake data check:** No fabricated statistics or precise numbers. "First real query from a paralegal" is a plausible specific scenario, not a fake dataset claim. "Every 'error code' document gets classified as 'incident response'" is a hypothetical but explicitly framed as observed pattern, not a cited study. Acceptable. Pass.

**Title check:** "I built a RAG that looked correct by design and failed at query time" — specific, experience-based, first-person. Distinct from recent "X is Y" hot titles. Distinct from "does your agent..." question form. Pass.

**Center clarity:** Central thesis is clear: ontology/schema controls what queries are *possible*, not what retrieval *correctly* returns. This is well-argued through the legal docs example and the schema-data alignment point. No drift. Pass.

**Opening 3 sentences:** Concrete. Legal RAG, paralegal query, force majeure vs termination clause — specific and domain-grounded. Good hook. Pass.

**"I" overuse concern:** 
- Para 1: "I built a RAG..."
- Para 3: "Here is the specific structural problem..."
- Para 6: "I have seen this failure..."
- Para 7: "The failure mode is silent..."
- Para 8: "What I should have done..."
- Para 10: "The system I described..."

That's a lot of I. But given the title is "I built..." and the genre is first-person postmortem, it's less of a structural problem and more of a stylistic choice. The post earns the "I" because it's a specific real case. Editor can trim some.

**Discussion hook:** Ends with "the schema controlled what queries could be expressed. It said nothing about what those queries would return." — strong closing that reframes the premise without a formulaic question. Pass.

## Issues Found

1. **Paragraph 6 ("I have seen this...")** — the technical docs and product knowledge base examples are too compressed. Either expand to a real example or cut. Currently reads like a bullet list dressed as prose. Consider merging into the prior paragraph or removing.

2. **Paragraph 8 ("What I should have done")** — the "should have done" framing is slightly prescriptive/advisory. Could be reframed as observed practice: "The systems that avoid this..." instead of "I should have..."

3. **Closing paragraph** — good, but could be one sentence shorter.

## Verdict

**GO / Minor edits.** The concrete legal docs example carries the post. Fix the compressed bullet-list paragraph and trim prescriptive framing. Otherwise clean.
