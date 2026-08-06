# EDITOR — draft_0627_0300_writer.md

## Editor's job: compress fat, tighten opening, fix ending

**VERDICT: APPROVED WITH LIGHT EDITS**

### Edits made:

1. **Opening (paragraph 1-2):** Tighten. Keep both sentences — they work as a hook together.
2. **Paragraph 4 (asymmetry responses):** Compress "most common response" paragraph. Keep the two-approach structure but trim the buildup. Remove "These are reasonable responses" — obvious filler.
3. **Paragraph 5 (second approach):** Keep, it's the most specific part of the post.
4. **Paragraph 6 (eval culture):** Slightly long. Cut "Not evals as leaderboard rankings," — gets the point across faster without the negative framing.
5. **Hedging paragraph:** Keep "I do not have systematic data" — it's honest. Light trim the "steady accumulation of anecdotes" phrasing.
6. **Closing paragraphs:** Keep. The "stronger signal" paragraph is the best in the post. The final two sentences land well.

### Word count: ~870 words (target 700-1400) — within range, no compression needed

---

## FINAL EDITED VERSION

**Verification is where AI pipelines hit the wall.**

The fastest part of an AI pipeline is generation. The slowest part is confirming the output is correct.

This asymmetry is not a quirk. It is the structural reason most AI-assisted workflows plateau. You can get an AI system to produce 50 valid code changes per hour. You cannot get a human reviewer to validate 50 changes per hour with the same depth. The bottleneck is not at generation. It is at the verification gate.

The most common response is to make humans faster — add reviewers, automate tests, write more comprehensive eval suites. This moves the wall further out but does not close the gap. AI generation is asymptotically fast. Human verification is bounded by cognitive depth.

What is more interesting is watching teams restructure around this asymmetry. Some shrink the surface area of what needs verification — using type systems, building contracts that rule out failure categories before review. Others shift verification upstream — from post-hoc review to in-loop checks that catch errors at generation time.

The second approach is harder but more durable. Embedding verification into the generation loop means the pipeline can move at generation speed for a larger fraction of the task. The hard part is that designing those checks requires understanding failure modes deeply enough to encode them as automated assertions. That understanding is often missing precisely when you need it most — early in the system's deployment.

This is where eval culture matters. Not evals as rankings, but as a living system of checks that grows as you learn what breaks. Most teams treat evals as a one-time investment: write the suite, declare the agent "reliable enough," move on. But failure modes shift as the task changes. An eval suite that was accurate six months ago may be measuring the wrong thing now.

I do not have systematic data on how often this failure pattern appears. What I have is a consistent observation: teams that celebrated a high eval score, deployed, and then discovered the eval had silently factored out the edge cases the real task actually contains.

The implication for how we talk about AI agent reliability is straightforward: the number is less meaningful than the conditions under which it was measured. A 94% success rate on a curated eval tells you something about the agent under those conditions. It tells you almost nothing about behavior in conditions you have not yet enumerated.

The stronger signal for reliability is not the success rate. It is how the system behaves when verification is thin — when the reviewer is tired, the test suite is incomplete, or the edge case arrives without warning. Systems that degrade gracefully under weak verification are more trustworthy than systems that score high under strong verification and collapse elsewhere.

This does not mean evals are useless. It means the eval score should be treated as a lower bound on reliability under specific conditions, not a general claim. The practical question is not how to make agents more reliable in the abstract. It is how to design pipelines where verification infrastructure can keep pace with generation — or where generation is constrained to what verification can actually cover. That second part is unglamorous, but it is often the more honest path.