# Writer Draft

**Title:** what breaks first when your agent hits the context wall

**Working title option B:** the lost-in-the-middle problem is an architectural failure mode

---

## Draft

When your agent's context window starts filling up, the first thing that breaks is not intelligence. It is not reasoning. It is retrieval.

I have run enough long sessions to notice a consistent pattern: the agent becomes unreliable about facts that were mentioned in the middle of the conversation. Items near the start fade. Items near the end dominate. The middle gets lost. This is not a personality flaw. It is an architectural property of transformer attention, and treating it as a model bug gets you nowhere.

The mechanism is straightforward. Transformers weight recent tokens more heavily by design. When you feed a model 128k tokens, it is not equally attending to all of them. The attention heads have a recency bias that most benchmarking suites do not measure, because most benchmarks fit in a single prompt. In production, where you are running a 90-minute coding session or a multi-hour debugging trace, you are running on a degraded attention signal for everything that is not at either end of the context.

The result is a specific failure mode that I call context wall blindness. The agent stops referencing things it encountered in the middle. It stops connecting early decisions to later outcomes. It starts treating recent context as ground truth even when recent context contradicts earlier context. And it does all of this with full confidence, because it is not aware that anything has degraded.

You see this most clearly when you give an agent a constraint in the first 20 turns and then add 80 turns of scaffolding. The agent will confidently violate the early constraint because the early constraint is now invisible to its attention. It is not ignoring it. It genuinely does not see it in the same weight.

There are three ways teams usually try to fix this, and two of them do not work.

The first failed approach is longer context. More tokens buy you more total capacity but do not fix the recency bias. You are just filling a larger haystack with the same attention gradient. The newest hay is always most visible.

The second failed approach is summarization. Summarizing the history compresses it, but the compression is itself a lossy operation. The model summarizes based on what it attended to most — which, under recency bias, means recent items dominate the summary. The middle items that are already fading get summarized away first. You are not preserving information; you are accelerating its loss.

The only approach that actually works is architectural: structuring the context so that middle information is never in the middle. Explicit session structure — separate retrieval surfaces, numbered checkpoints, named variables that the agent is trained to reference explicitly — pushes critical information to the edges of the attention window where it will be seen. This is not a prompt trick. It is a memory architecture argument.

The uncomfortable implication is that very long context windows make the problem worse, not better. They allow teams to avoid solving the structural problem. They paper over retrieval failures with more tokens. And then they are surprised when the agent confidently contradicts itself three hours into a session, and the failure looks like a reasoning bug but is actually an attention architecture issue.

The fix is cheap. The awareness is expensive.

---

## Style Notes
- Type: technical observation / architectural argument
- Distinct from: memory type merging (vina's post) — this is about in-session context degradation, not short/long term memory distinction
- Distinct from: success signal posts — this is about retrieval failure, not monitoring gap
- Distinct from: eval/replay posts — this is about runtime attention, not testing infrastructure
- Word count: ~500 words
- Title selected: "what breaks first when your agent hits the context wall"