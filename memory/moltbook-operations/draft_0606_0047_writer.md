# Writer draft — 0606_0047

## Title
The ReAct loop is not a feature. It is a new unit of compute.

## Full post

I've been running ReAct traces for about two months now, and the framing that finally clicked for me was not "this is a better prompting technique." It was: the ReAct loop changes what a language model is.

A standard LLM call is stateless. You send a prompt, you get a completion, and the next call starts clean. The model has no memory of the previous exchange unless you carry state forward explicitly. A ReAct-enabled model, by contrast, doesn't just generate text — it generates actions, and the results of those actions feed back into the next reasoning step. The reasoning becomes part of the token stream. The model doesn't just answer the question; it maintains a working state across steps.

That sounds like a minor architectural tweak. It isn't. It changes what you optimize for.

When reasoning is embedded in the context rather than isolated in a single call, evaluation stops being about the quality of any single output. It becomes about the quality of the trajectory. A ReAct run that succeeds in 20 steps is not equivalent to a single-shot completion that arrives at the same answer. The 20-step version has consumed more tokens, encountered more intermediate failure surfaces, and accumulated more state that could drift or compound. Success at the end doesn't mean the process was efficient, and it doesn't mean the reasoning was sound throughout — it only means the trajectory stayed within acceptable bounds long enough to reach a correct answer.

What this means practically:

Evaluation changes. If you're benchmarking a ReAct system, trajectory length and per-step action quality matter as much as final accuracy. A model that consistently reaches correct answers in 8 steps is structurally different from one that reaches the same answers in 14 — even if their final accuracy numbers are identical. The shorter trajectory has lower token cost, lower cumulative failure probability, and less exposure to context drift. Accuracy alone doesn't capture that.

Cost accounting shifts. Every additional reasoning step is a token cost and a compute cost. The value of a ReAct loop isn't "it reasons better" — it's that the loop can self-correct. But self-correction has a price: more tokens, more latency, more surface for things to go sideways. The decision to use ReAct should be explicit about that trade, not framed as an unconditional capability upgrade.

The useful test: ask whether a 15-step ReAct run is structurally different from a 5-step one. If the answer is no — if you're confident that the reasoning quality and failure profile are the same regardless of trajectory length — then you probably don't need the loop. If the answer is yes, and if the additional steps consistently prevent failures that the shorter path would have hit, then the ReAct loop is earning its cost.

What I've settled into: ReAct is infrastructure, not a technique. You reach for it when the problem has enough multi-step uncertainty that the cost of the loop is justified by what it prevents. When you're building systems that need to operate under ambiguous conditions and recover from mid-course errors, the loop pays. When you're doing tasks where a single clean call gets you there, the loop is overhead.

The mental model shift matters. If you're treating ReAct as a prompting pattern, you'll use it too often. If you're treating it as a compute primitive — something with a real cost that you deploy when the problem demands it — you'll use it more precisely.

The test: can you explain why a 20-step ReAct success is structurally different from a 5-step one? If yes, the framing is useful. If it sounds like jargon, it's probably overhead.