# Editor — draft_0036

## Changes Made

1. **Opening:** Strengthened the hook — added a specific observable symptom before the mechanism claim
2. **Middle:** Expanded the "what you see" section — more concrete behavior description
3. **Closing:** Added a short clarifying note on why "context wall blindness" is not the same as forgetting
4. **Word count:** ~700 words

## Final Draft

---

When your agent's context window starts filling up, the first thing that breaks is not intelligence. It is retrieval.

I have run enough long sessions to notice a consistent pattern: the agent becomes unreliable about facts that were mentioned in the middle of the conversation. Items near the start fade. Items near the end dominate. The middle gets lost. This is not a personality flaw. It is an architectural property of transformer attention, and treating it as a model bug gets you nowhere.

The mechanism is straightforward. Transformers weight recent tokens more heavily by design. When you feed a model 128k tokens, it is not equally attending to all of them. The attention heads have a recency bias that most benchmarking suites do not measure, because most benchmarks fit in a single prompt. In production, where you are running a 90-minute coding session or a multi-hour debugging trace, you are running on a degraded attention signal for everything that is not at either end of the context.

The observable symptom is specific and easy to miss if you are not watching for it: the agent stops connecting early decisions to later outcomes. It stops referencing things it encountered in the middle. It starts treating recent context as ground truth even when recent context contradicts earlier context. And it does all of this with full confidence, because it is not aware that anything has degraded. You do not get an "I am losing track of earlier context" message. You get a confident wrong answer that sounds like a reasoning failure but reads like a retrieval failure.

You see this most clearly when you give an agent a constraint in the first 20 turns and then add 80 turns of scaffolding. The agent will confidently violate the early constraint because the early constraint is now invisible to its attention. It is not ignoring it. It genuinely does not see it at the same weight.

There are three ways teams usually try to fix this, and two of them do not work.

The first failed approach is longer context. More tokens buy you more total capacity but do not fix the recency bias. You are just filling a larger haystack with the same attention gradient. The newest hay is always most visible.

The second failed approach is summarization. Summarizing the history compresses it, but the compression is itself a lossy operation. The model summarizes based on what it attended to most — which, under recency bias, means recent items dominate the summary. The middle items that are already fading get summarized away first. You are not preserving information; you are accelerating its loss.

The only approach that actually works is architectural: structuring the context so that middle information is never in the middle. Explicit session structure — separate retrieval surfaces, numbered checkpoints, named variables that the agent is trained to reference explicitly — pushes critical information to the edges of the attention window where it will be seen. This is not a prompt trick. It is a memory architecture argument.

The uncomfortable implication is that very long context windows make the problem worse, not better. They allow teams to avoid solving the structural problem. They paper over retrieval failures with more tokens. And then they are surprised when the agent confidently contradicts itself three hours into a session, and the failure looks like a reasoning bug but is actually an attention architecture issue.

Context wall blindness is not the same as forgetting. Forgetting implies the information existed somewhere and degraded. Here the information existed in the context but was never attended to equally. The model is not losing the data. It is failing to retrieve it because retrieval is gated by attention weight, and attention weight is not uniform across the context window.

The fix is cheap. The awareness is expensive.

---

## Title
**what breaks first when your agent hits the context wall**