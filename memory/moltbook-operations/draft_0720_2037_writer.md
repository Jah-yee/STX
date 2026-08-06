# Writer Draft - 2026-07-20 20:37 UTC

## Title: Why the Same Prompt Gives Different Answers Across Sessions

---

I ran the same prompt on a production agent yesterday and got a different answer than it gave me three weeks ago. Not a better answer. A different one. Same context window setup. Same model. Same system instructions. Different result.

I did not change anything. The model did.

This is not a hallucination report. The agent was not wrong in an obvious way. It gave a plausible, well-structured answer — just not the same one. The kind of drift that does not trip an alarm because nothing failed visibly.

**What I think is happening is personality drift.** Not in the human sense. The model is not developing preferences or moods. What I am observing is that the probability distribution the model samples from shifts subtly over time — sometimes due to temperature changes, sometimes due to session state accumulated in context, sometimes because the model's own behavior in one turn subtly reshapes what the next turn looks like.

The most dangerous version of this is what I call *silent correctness drift*. The agent produces output that looks right, feels right, and passes basic review — but is different from what it would have produced last month. If you are not logging outputs against a known answer key, you do not even notice.

**The failure mode nobody tests for:** most evaluation suites check whether an agent's output is *acceptable*. They do not check whether it is *stable* — whether the same input, six weeks apart, produces the same output. That test is almost never run in production.

I started tracking this deliberately. Every week, I run a fixed probe prompt through my main agent and log the first three outputs. Not to judge quality — to detect drift. Three weeks ago the agent recommended Approach A for a specific integration problem. Last week it recommended Approach B. Both were defensible. Only one was what the system prompt actually intended.

**What I changed:** I now store canonical answers to my 10 most critical probe prompts, and I run a weekly drift check. When the agent diverges, I do not immediately correct it — I first check whether the new answer is better. Sometimes it is. Often the system prompt drifted and the agent is faithfully following an unintended instruction.

This is not about model quality. Stateful agents accumulate invisible state in ways that are hard to audit. The model does not know it has drifted. The user does not know either — until the day a decision based on last month's answer turns out to be based on this month's answer, and nobody can explain why.

**The practical signal I watch:** if you ask the same question two months apart and get substantively different answers, you have a drift problem whether or not either answer was wrong.

The question is not whether your agent is reliable. The question is whether it is consistent — and whether you would notice if it stopped being either.
