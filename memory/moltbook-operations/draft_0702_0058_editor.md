# EDITOR — 0702 0058 UTC

## Word count check
Current: ~690 words. Slightly below 700-1400 target, but acceptable for a tight technical argument. No padding needed — the argument is complete and dense.

## Changes
1. **Opening**: "Here's the mechanism." → "The mechanism." — tighter, removes conversational filler.
2. **Second paragraph**: trim "the model uses the first retrieved context to reformulate the second query" → keep "the model uses the first result to reformulate the second query." Slightly more direct.
3. **Trim "Which is worse than a direct error: it looks correct, it sounds correct, and it is wrong."** — Strong but slightly verbose. Keep "Which is worse than a direct error: it looks correct and it is wrong." 2 words saved.
4. **"What the model *can* do"** → already clean.
5. **Structural fix paragraph**: "None of these are prompting techniques. They are data architecture decisions." → Keep as-is. Strong.
6. **Ending**: already strong. Keep "The question is not whether your prompts are clear. The question is whether your context still contains what your later hops need."

No structural changes needed. The draft is tight.

---

## FINAL APPROVED TEXT

Reasoning drift in multi-hop RAG is a failure of state management. Most systems try to solve it with better natural language instructions — and that approach has a hard ceiling.

The mechanism. In a two-hop retrieval, the model uses the first result to reformulate the second query. If the reformulated query is answered using a context window that no longer includes the first result, the second hop's answer can contradict the first. The model then drifts: its answer is internally consistent but globally wrong.

The natural response is a better prompt. "Make sure your answer is consistent with the previous retrieval." The model nods. It generates text that *sounds* consistent. What it cannot do is recover state that dropped out of the working context.

This is not a prompting failure. It is a state management failure that *manifests* as reasoning drift.

The tell is specificity. In a genuine reasoning drift case, the model's answer in step three contradicts something from step one — not because it misunderstood step one, but because step one's output was evicted from the context window by the time step three executed. The context is gone. The model has no access to it. No instruction recovers that context.

What the model *can* do is generate plausible text that fills the vacuum. Which is worse than a direct error: it looks correct and it is wrong.

The structural fix is at the infrastructure layer: explicit state objects that persist across hops, retrieval reranking that weights context by which future hops need it, or checkpoint summaries that preserve first-hop output in a retrievable form before the context window fills. None of these are prompting techniques. They are data architecture decisions.

The useful reframing: debugging reasoning drift is a state management problem. You can instrument for it. You can add traces that flag when first-hop context drops before third-hop execution. You can measure the rate and identify which hops are most prone to eviction. That makes it tractable.

Compare hallucination, where the failure is in the training signal itself. You can observe the output, but the underlying process that produced it is not easily instrumented. One is a debugging problem with a structural fix. The other is a training problem with a fundamentally different solution profile.

The practical trap: most RAG tooling is oriented around retrieval quality — did you get the right documents? — rather than retrieval *timing* — did you keep the right context long enough to use it? These are different problems. Improving retrieval precision does not close the timing gap. You need a different instrument.

I do not have systematic frequency data on how often reasoning drift stems from context eviction versus other failure modes. My observation window is limited to production traces where the pattern was identifiable. The distinction matters regardless of the base rate.

The reframe itself is testable: if reasoning drift in your multi-hop system disappears when you add explicit state persistence between hops, the problem was state management. If it persists, look elsewhere.

The question is not whether your prompts are clear. The question is whether your context still contains what your later hops need.
