# Editor — Round 0709_2051

## Changes made:
1. Expanded classification example with concrete numbers (4 vs 2 calls)
2. Added concrete pipeline example (plan→execute→verify) to illustrate state handoff failure
3. Expanded the optimization section with named optimization targets
4. Added a brief opening scene to replace the flat first sentence
5. Tightened closing paragraph

## Final draft:

The loop was a proxy. The lifecycle is the product.

---

You know a production agent system is in trouble when the oncall log reads like a detective novel: the fifteenth retry succeeded, but the output was from the seventh iteration, and nobody can explain why the system chose that one. That is the reasoning loop in its natural habitat — useful, flexible, and nearly impossible to reason about after the fact.

Managed agents do not work this way. They replace the reasoning loop with an execution lifecycle — a defined sequence of stages like plan, execute, verify, deliver — where the model does not circle back unless explicitly routed to do so. The difference sounds architectural. It is behavioral.

The most concrete way I can illustrate it: in a loop-based agent, a classification task might run the model four times before returning an answer — initial classification, confidence check, error recovery, final output — each iteration carrying the full context of the previous one. In a lifecycle-based managed agent, the same task runs once in the plan stage and once in the verify stage. The model is not looping; it is being used at specific points in a predetermined sequence. The retry logic is not a loop — it is a stage. The distinction is not cosmetic.

This matters for three reasons that are easy to overlook until you are debugging a port gone wrong.

The state model is fundamentally different. A reasoning loop accumulates context as it goes. Each iteration knows what the previous one produced. An execution lifecycle does not — or rather, it only knows what was explicitly captured at stage boundaries. If your verify stage needs a detail from the plan stage, that detail has to be written into the shared lifecycle state explicitly. I have seen a team spend three weeks debugging a classification pipeline where the plan stage was silently dropping a field that the verify stage needed. The loop had been carrying that field implicitly for months. The lifecycle could not. The port looked clean in the code review.

The failure modes are not the same. A loop-based agent tends to fail gradually — confidence degrades, context drifts, outputs get less coherent. You can often see it coming. A lifecycle-based agent fails at stage boundaries. The plan completes but the execute stage fails because the output format shifted. The verify stage runs against stale data because the execute stage did not write back to the shared state correctly. These failures are more abrupt and harder to diagnose because the system looks healthy until the boundary, and the error message is usually in the wrong stage.

The optimization target changes. When the loop was the unit, you optimized loop efficiency — fewer iterations, faster context retrieval, better prompting to reduce retry rates. When the lifecycle is the unit, you optimize stage transitions: what passes between stages, how much context each stage needs, whether the bottleneck is the model call or a data transform between stages. In one pipeline I profiled, the model call itself was 180 milliseconds. The serialization and deserialization between stages added 620 milliseconds. The lifecycle was not slow because the model was slow. It was slow because of the state handoff architecture. Loop-level profiling would never have surfaced that.

The practical test I use: if I cannot draw the stage boundary diagram from memory without checking the docs, the lifecycle is probably not well-designed. A good lifecycle is one where each stage has a single, clear input and a single, clear output, and the transition between stages is explicit. If you need to pass unstructured context from plan to execute, that is a signal that the boundary is wrong — not that the model needs more capability.

I do not have full data on this, but the pattern I keep seeing is: teams that port a loop-based agent into a managed agent framework without redesigning the state model end up with something that is worse than both originals. The lifecycle inherits the loop's implicit assumptions about state continuity, but without the loop's runtime flexibility to compensate. You get the rigidity of the lifecycle with the hidden complexity of the loop.

The honest answer is that there are cases where a genuine reasoning loop is the right abstraction — where the problem genuinely requires iterative refinement and you cannot know the number of iterations in advance. Lifecycle models handle those by adding a loop stage, which works but feels like a retrofit. The choice between loop and lifecycle is still largely workload-dependent, and the frameworks have not made that choice obvious yet.

Where the managed agent space is actually moving: execution lifecycle as the unit of work, with the reasoning loop as a specialized stage inside it — not the other way around.
