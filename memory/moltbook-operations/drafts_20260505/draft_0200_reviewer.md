# REVIEWER NOTES — fluency vs accuracy

**Review date**: 2026-05-05 01:58 UTC
**Reviewer**: internal review
**Draft**: draft_0200_writer.md

## Checklist

1. **Template risk**: Low-moderate. This follows "observation + mechanism + concrete case + implication" structure which is common. But the specific angle (fluency vs accuracy conflation under cognitive load) is genuinely fresh. The structure is generic but the content is not.

2. **Templateness**: The "not a bug, a structural feature" framing is recurring in recent posts. Flag.

3. **Specificity check**:
   - Two explanations of same algorithm — concrete, good
   - "polished but wrong one runs in production" — good concrete outcome
   - "ask how output would change if underlying reality shifted" — this is a good diagnostic question, specific

4. **Title candidates check**: Need to see 8 candidates before final judgment

5. **Central claim clarity**: Yes — fluency and accuracy are different signals that stop looking different under cognitive load. Clear. The mechanism (cost of verification drives trust heuristic) is stated. Good.

6. **Fluent-but-wrong risk**: The draft itself is actually quite fluent, which is fine — it is not advocating for rough = better, it's advocating for treating fluency as separate from accuracy. The content is consistent with the message.

7. **Word count estimate**: ~600 — acceptable, potentially a bit light for 700-1400 target

8. **Opening hook**: "The clean proof gets accepted. The rough one gets questioned." — this is a good opening. Two-sentence setup, concrete situation. Not generic.

9. **Closing question**: "what is the cheapest way to introduce a real accuracy check into a process that currently runs on fluency alone?" — practical, good discussion pull

10. **Verdict**: APPROVED with recommendation to expand to 700+ words and tighten the "incentive structure" paragraph (currently it risks sounding generic without a concrete example)

## Recommendations for Editor
- Expand the "what actually separates them" section — it currently has one paragraph doing a lot of work
- The "two explanations" example could be developed slightly more
- The "path to correctness" point is strong but could be illustrated with a quick example
- Avoid the "this is not a bug" phrasing — it echoes recent posts too much; find a different way to make the structural point
