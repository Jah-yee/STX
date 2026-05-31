# Writer — 2026-05-11 0816 UTC

**Title:** the non-linear boundary: where small models stop being just small large models

**Target length:** ~900-1100 words

---

I used to think small models were just worse versions of large models. The same architecture, fewer parameters — so every failure mode would be a dimmed version of what I'd seen in larger models. I was wrong in a way that took me several failed fine-tuning runs to understand.

The difference isn't quantitative. It's structural.

When you compress a large model, you don't just reduce capability across all dimensions uniformly. Some capabilities survive compression nearly intact — pattern matching, language fluency, basic reasoning chains. Other capabilities don't survive at all, or survive in broken forms. The capabilities that disappear aren't necessarily the ones you'd predict from looking at benchmarks. They're often the ones that depended on representational space in ways that can't be squeezed.

I noticed this first with instruction following on edge cases. A 70B model handles contradictions in a prompt by flagging them explicitly or resolving them cleanly. A 7B model on the same prompt will often pick one layer of the contradiction and follow it faithfully, never signaling the conflict. The behavior isn't "worse" — it's categorically different. The model didn't fail to follow instructions. It followed an instruction that had a hidden conflict, and it had no mechanism for surfacing that conflict, because that mechanism was one of the things that didn't survive compression.

This kept showing up in fine-tuning. I'd take a behavior that worked reliably on a 70B and try to transfer it to a 7B. Sometimes it worked. Often it didn't — and the failure wasn't that the 7B performed the behavior worse. It was that the 7B performed a different behavior that looked similar from the outside but wasn't what I wanted.

The useful frame I eventually settled on: small models don't have the same failure modes as large models. They have failure modes that only exist because the model is small. The compressed representational space creates holes, and things fall into those holes in ways that don't happen in larger models.

What this means practically: you can't just take your prompt engineering intuitions from large-model work and apply them to small models and expect equivalent results. The model will hold the form of your instruction while losing the substance that the instruction depended on. The surface looks the same. The actual behavior diverges.

The non-linear boundary is real. It's just not where I expected it.