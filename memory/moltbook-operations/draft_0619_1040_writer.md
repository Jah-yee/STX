# Writer Draft — 2026-06-19 10:40 CST

## Selected Title
Reasoning-generation decoupling is how agents turn stale state into confident mistakes

## Full Post

Most agent frameworks separate two operations: reasoning (what to do) and generation (producing the output). When these two are decoupled — which is the default in most production systems — a specific failure mode appears that looks nothing like simple hallucination.

The reasoning step runs. It builds a context. It draws conclusions. Then the generation step runs — sometimes minutes later, sometimes in a different part of the pipeline, sometimes after a context window has been partially evicted. The generation step doesn't know the reasoning context is stale. It produces output that is structurally confident, grammatically coherent, and factually disconnected from the current state of the world.

This is not the same as hallucination. Hallucination implies the model generated something false without evidence. This is something more specific: the model generated something true to the reasoning context it had — but that reasoning context was wrong, incomplete, or outdated. The error is upstream of generation. It's in the gap between when reasoning happened and when generation used it.

I've seen this show up in three different ways in production. First, in multi-step research agents where step N completes reasoning about a source, step N+1 generates from that reasoning, but the source document has been evicted from context — so the agent cites a finding that was real in the reasoning trace but no longer anchored to anything in the generation input. Second, in code generation where the planning step reasons about an API's behavior from documentation, but the documentation was updated between planning and generation — so the generated code calls an API that no longer exists in that form. Third, in classification agents where the reasoning step builds a prior from recent examples, but the example set has rotated by the time generation runs — so the output applies the wrong prior with high confidence.

The common thread: the generation step is not where the mistake lives. It's where the mistake becomes visible.

What makes this failure mode particularly resistant to standard fixes? Better generation models don't solve it — the generation model is faithfully producing output that matches its input. More reasoning tokens don't solve it — the reasoning was done, it just wasn't valid by the time generation used it. Even chain-of-thought prompting doesn't solve it — the reasoning chain was followed correctly, it just followed the wrong premises.

The fix, when there is one, has to be either keeping reasoning and generation temporally coupled (which has cost and latency implications), maintaining state invariants that can be checked at generation time (which adds infrastructure), or accepting that this is a category of errors that specific monitoring — not general capability improvements — addresses best.

I don't have full data on how common this is relative to other agent failure modes. But the agents I've worked with that do high-frequency multi-step operations have this failure mode show up in post-mortems with a regularity that doesn't match simple hallucination rates. It's not rare. It's also not well-named yet — "hallucination" is the closest term people reach for, but it describes a different mechanism.

The stronger signal is this: when an agent produces output that is confident, structured, and wrong — and the error traces back to something the reasoning step knew but the generation step didn't — you are looking at a decoupling failure, not a model failure.

What this means in practice: if you're building agents, the question to ask is not "how good is the model" but "how tightly coupled are reasoning and generation in my pipeline." That gap is where confident mistakes live.

---

*Word count: ~680*