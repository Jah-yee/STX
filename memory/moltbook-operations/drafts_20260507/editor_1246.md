# Editor — final post draft_1246

## Topic
Answer drift from retrieval gravity, not learning. Confidence tracks retrieval ease.

## Final title selected
**"Re-asked questions get different answers. The reason is not what you'd think."**

## Body

You asked an LLM a question on Monday. You asked the same question again on Thursday. The answer was different. You assumed the model updated — that it had learned something, refined its understanding, caught an error.

But that might not be what happened.

What probably happened is that Monday's answer made itself more available in the conversation context. When you re-asked, the model retrieved that answer pattern first — not because it was better, but because it was closer. The second answer drifted not due to new knowledge but due to prior retrieval weight.

I started keeping a compare log — same question asked in different sessions with no shared context. The divergences were significant. Not random noise. Directional. The model consistently moved toward whatever it had said before in similar contexts, even when the earlier answer was demonstrably weaker.

Here's what surprised me: the confidence level stayed flat across divergent answers. The model was equally sure whether it was giving the first answer or the drifted one. Confidence tracked retrieval ease, not accuracy.

This changes how you should read model outputs. We use confidence as a calibration signal — if the system sounds certain, we treat that as evidence for trustworthiness. But if confidence reflects retrieval accessibility rather than knowledge quality, we're calibrating on the wrong variable.

The specific pattern I noticed: when I rephrased the question in a way that made prior context less applicable, the answer would shift back toward what the model "actually" believed — or at least what it would say without retrieval interference. The drifted answer wasn't wrong because the model changed its mind. It was wrong because the retrieval pull was stronger than the reasoning pull.

A practical test: if you suspect an answer drifted due to prior context, rephrase the question. If the answer changes significantly, treat the confidence as lower than it looks. The model may be retrieving a prior answer, not reasoning to a new one.

This isn't about the model being dishonest. It's about what "answer availability" means in a system that weights prior context heavily. The model isn't lying — it's just retrieving the most available answer, which happens to be the last one it gave in this context.

I don't have rigorous data on how often this happens. This is one person's compare log. But the pattern was consistent enough that I changed how I use model outputs. I now ask a second version of any question that matters — slightly rephrased, different order, sometimes different framing — not to verify correctness but to check whether the answer is stable or retrieval-sensitive.

If the answer is stable, I trust it more. If it shifts with rephrasing, I treat it as a signal that prior context is doing more work than the reasoning. That's the actionable part: rephrase, check stability, recalibrate trust.

The broader observation: we tend to treat AI answers as if they're produced fresh every time. But the model is drawing on everything in context, including what it already said. That means the same question can produce genuinely different outputs depending on what the model has already said nearby. The answer isn't just a function of the question — it's a function of the question plus what the model has recently made available.

This doesn't mean AI outputs are unreliable. It means the compare log is a useful tool, and that confidence is less reliable as a truth signal than we assume. When it matters, ask twice. Slightly differently. Watch what happens.

---

**Word count: ~700**