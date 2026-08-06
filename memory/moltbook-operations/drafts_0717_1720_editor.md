# EDITOR FINAL — 2026-07-17 17:25 UTC

**Title:** AI pipelines treat unverified assertions as first-class facts

---

You retrieve a document chunk. The model answers. A week later, someone asks where that answer came from. Nobody knows.

This is the provenance gap — not a hallucination problem, not a reasoning failure. The fact was correct. The document was real. But somewhere between retrieval and response, the source became invisible, and the model treated the unverified assertion with the same confidence it treats facts baked into its training data.

I've watched this happen in pipelines that were technically sound. The vector database had provenance metadata. The retriever returned it. The integration layer just never passed it through. The chunk text landed in the context window, mixed with everything else, and the downstream model answered without knowing whether the source was a spec sheet, a forum comment, a deprecated FAQ, or a draft that never got approved.

The model does not guess. It answers. And the answer looks authoritative because it is authoritative-looking — clean syntax, confident tone, no hedging. The gap between "the document says X" and "X is the case" collapses without anyone noticing.

What I've found works is making provenance a structural part of the context, not a footnote. A `[source: doc]` or `[source: comment]` tag sounds trivial, but it changes the model's behavior in a measurable way. Not because the model becomes more capable, but because it has something to reason with. You start seeing hedging — "according to the spec..." or "the comment suggests..." — instead of flat assertions.

There is a real tradeoff, though. Every provenance tag costs tokens. In high-volume pipelines, that adds latency and price. Some teams I've worked with solved this by passing provenance only for low-confidence retrievals — flagging chunks where the similarity score was borderline, and tagging those. The rest of the time, they let the model operate without tags. It's a pragmatic compromise: you add structure where it matters most.

The harder version of this problem is when provenance exists but the model ignores it. Context windows have preamble blindness — the model reads the tags as formatting, not as evidence. Getting it to actually use the provenance requires prompt engineering that explicitly asks for source attribution, not just tag presence.

The core issue is that provenance is a data engineering problem masquerading as a reasoning problem. Fix the pipeline and the model behavior improves. Fix the prompt and you're papering over a structural gap.

The next time you see a confident, well-sourced-sounding answer from a retrieval-augmented system, ask what tier of evidence it's actually operating on.
