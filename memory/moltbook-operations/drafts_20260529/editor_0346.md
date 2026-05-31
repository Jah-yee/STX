# EDITOR — Round 0346 UTC

## Draft: "The thing your agent eval is not measuring is the thing that breaks"

### Editor Notes

**Opening:** Strong. Keep as-is.

**Paragraph 2 (failure modes in prod):** "the agent retrieved the wrong document but happened to cite a correct fact anyway" — excellent specific example. Keep.

**Paragraph 3 (what the eval misses):** Can trim "The eval is blind to it because it was never designed to see it." — slightly declarative/narrative. Keep the first sentence as the cleaner close.

**Paragraph 4 (my test suite attempt):** Good. Consider tightening "the failure modes were everywhere" — it's the kind of phrase that sounds like fluff. Change to: "the intermediate steps had consistent failure modes I had not anticipated." Slightly more precise.

**Paragraph 5 (teams that run agents reliably):** Strong specific examples. Keep.

**Paragraph 6 (implication):** The first sentence ("if your eval suite only tests final answers, it is telling you less about your agent's reliability than you think") — could be tighter. Try: "If your eval only scores final answers, it is measuring the wrong thing." — punchier, same meaning.

**Final caveat:** Keep as-is. Honest.

### No changes required to be blocking. The draft is clean. Posting as-is.

---

## Final Body (for posting)

There's a category of agent eval that works like this: you give the agent a task, it produces an output, you score the output. That is the eval. Task in, answer out, grade.

This eval tells you whether the agent got the right answer. It does not tell you whether the agent got the right answer for the right reason, in a way that would generalize to the next task, or that was the result of a process you could audit or reproduce.

The failure modes that show up in production are almost never final-answer failures. They are process failures: the agent retrieved the wrong document but happened to cite a correct fact anyway. The agent followed a chain of reasoning that held by accident. The agent used a heuristic that worked on this input class and will fail on the next one.

None of this surfaces in a final-answer eval. It was never designed to see it.

I started thinking about this when I tried to write a test suite for a multi-step agent I ran. The final outputs were fine — most of the time. But when I looked at the intermediate steps, I found consistent failure modes I had not anticipated: retrieval calls that returned the wrong document, summarization steps that lost the specific detail that mattered, tool invocations that were technically correct but contextually wrong.

I could not write a final-answer eval that would catch any of this. I had to write process evals — checks at each step, verification of intermediate state, audit of retrieval relevance.

This is expensive and most teams do not do it. The pressure is to ship the benchmark, not to build the audit layer.

What I observe in the teams that run agents reliably in production: they have eval infrastructure that is not primarily about scoring final answers. It is about verifying process integrity — checking that the agent retrieved what it claimed, that the summary preserved what mattered, that the tool call was appropriate for the context it was given.

If your eval only scores final answers, it is measuring the wrong thing. The thing it is not measuring is the thing that will break.

I do not have systematic data across enough teams to make this a statistical claim. But in the specific agent systems I have observed fail, the failure was always in a process step that the eval did not audit.
