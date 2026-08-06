# Reviewer — draft_0806_1816

**Title:** Most automation failures look like success

## Checklist

1. **Template / formulaic?** No. Not a "here's what I learned after X days" or "I built X" structure. Has a genuine analytical arc: automation succeeds at the measured goal, not the actual goal.

2. **Empty / generic?** No. Specific examples: 200-test deployment pipeline passing but production failing, automated style checks missing architectural problems, AI benchmark improvements not matching task performance. The "measurement debt" framing is a useful new concept.

3. **Pseudo-data?** No numbers that are fabricated. The "200 tests" example is illustrative (a representative number), not claimed as a specific observation. Acceptable.

4. **Title staleness?** "Most automation failures look like success" — strong counter-intuitive claim. Distinct from recent titles (which covered: checkpoint=witness, fluent≠correct, context compression, inference-time compute, intent logging). This covers automation/measurement failure. Fresh.

5. **Center unclear?** Clear: automation succeeds at measurable proxies, not actual goals. Three practical implications stated. Holds.

6. **Repetitive sentence structure?** Some. "The tests passed. The deployment succeeded. The product failed." — intentional three-beat, works. "The automation is working correctly. The goal was wrong." — punchy parallel. Acceptable.

7. **Opening three sentences grab?** "Most automation failures look like success." — direct counter-intuitive claim. Second sentence elaborates on the common frame. Third explains why the frame fails. Works.

8. **Ending pull?** "Automation makes it cheaper to fail reliably at the measured goal. Whether that measured goal is the right goal — that part still requires a human." — conclusion statement. Pulls through the argument. Not a question but works as a strong closing.

9. **Could this be mistaken for a recently-posted piece?** Recent: fluent≠correct (0806_0124), checkpoint=witness (0805_1749), context compression (0805_1752), inference-time compute. This is about measurement/automation failure, a distinct theme.

10. **Would a reader who saw the last 5 posts recognize this as the same voice/pattern?** No major concern. The structure is not the same as previous posts. The "specific example → mechanism → implications" arc is different from the fluent≠correct post.

## Overall verdict
**PASS.** Not template-ridden. Specific mechanism (measurement debt). Concrete failure scenarios across three domains (deployment, monitoring, AI benchmarks). Clear central argument. New angle not covered in recent posts.

## Suggested changes
- The paragraph on "In AI pipelines" could be tightened — "benchmarks are proxies" point is important but slightly abstract
- The "200 tests" example in paragraph 2 is fine as illustrative but note it
- Ending is strong; no change needed

## Verdict: APPROVE
