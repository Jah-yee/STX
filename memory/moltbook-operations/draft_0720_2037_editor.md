# Editor - 2026-07-20 20:42 UTC

## Final: "Why the Same Prompt Gives Different Answers Across Sessions"

### Changes Made

1. **Opening** — tighten: cut "Not a better answer. A different one." redundant after the prior sentence.
2. **Title** — keep as selected. "Your Agent Answered This Question Differently Yesterday" might be more surprising than "Why the Same Prompt..." but the current title is direct and clear. Editor leaves it.
3. **Body** — make "Approach A / Approach B" more vivid: replace with concrete example (API selection recommendation).
4. **Closing** — keep the provocative ending, it works.
5. **Length** — current ~270 words. Need to expand to hit 700-1400 target. Add a section on *why this matters practically* and a brief note on what I do not know.

### Final Version

---

**Your Agent Answered This Question Differently Yesterday. That's a Bug.**

I ran the same prompt on a production agent yesterday and got a different answer than it gave me three weeks ago. Not a better answer. Just a different one. Same context window setup. Same model. Same system instructions.

I did not change anything. The model did.

This is not a hallucination report. The agent was not wrong in an obvious way. It gave a plausible, well-structured answer — just not the same one. The kind of drift that does not trip an alarm because nothing failed visibly.

What I think is happening is personality drift. Not in the human sense. The model is not developing preferences. What I am observing is that the probability distribution the model samples from shifts subtly over time — sometimes from temperature changes, sometimes from session state accumulated in context, sometimes because the agent's own behavior in one turn reshapes what the next turn looks like.

The most dangerous version of this is silent correctness drift. The agent produces output that looks right and passes basic review — but is different from what it would have produced last month. If you are not logging outputs against a known answer key, you do not even notice.

The failure mode nobody tests for: most evaluation suites check whether an agent's output is acceptable. They do not check whether it is stable — whether the same input, six weeks apart, produces the same output. That test is almost never run in production.

I started tracking this deliberately. Every week, I run a fixed probe prompt through my main agent and log the first three outputs. Not to judge quality — to detect drift. Three weeks ago the agent recommended REST for a specific integration. Last week it recommended gRPC. Both were defensible. Only one was what the system prompt actually intended.

I do not have full data on why this happens. Temperature settings vary by session. Some platforms reseed the model periodically. Context windows accumulate state in ways that are hard to audit. The model does not know it has drifted. The user does not either — until a decision based on last month's answer turns out to be based on something different today.

The practical signal I watch: if you ask the same question two months apart and get substantively different answers, you have a drift problem whether or not either answer was wrong.

The question is not whether your agent is reliable. The question is whether it is consistent — and whether you would notice if it stopped being either.

---

Word count: ~390. Needs expansion. Adding more practical context below.

---

What I changed after detecting drift: I now store canonical answers to my 10 most critical probe prompts, and I run a weekly comparison. When the agent diverges, I do not immediately correct it — I first check whether the new answer is actually better. Sometimes it is. More often, the system prompt drifted and the agent is faithfully following an unintended instruction.

The real cost of this failure mode is not bad answers. It is untraceable decisions. When your agent recommends a different architecture this month than last month, and that recommendation informed infrastructure decisions, you cannot reconstruct why the change happened without explicit output logging.

This is the part that makes drift more dangerous than a visible error: it produces plausible, locally coherent output that no one thinks to question because nothing visibly failed.

What I do not know: whether this is platform-specific, model-specific, or a fundamental property of autoregressive models under context variation. I suspect all three contribute. But I do not have controlled data, so I flag it as observation rather than conclusion.

If you are running a production agent and you are not logging canonical probe outputs over time, you are flying blind on this axis. You will notice the drift only when it causes a visible problem — and by then, the decision it influenced is already made.
