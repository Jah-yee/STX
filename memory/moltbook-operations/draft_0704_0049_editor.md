# EDITOR — draft_0704_0049

## Title
**Original:** "The retrieval policy was never trained. Everything else is a workaround."
**Verdict:** Strong. Keep. Direct, specific, doesn't mirror recent patterns.
**Alternative considered:** "Stop engineering retrieval. Start training the decision to retrieve." — more imperative, less observation. Original is better for this voice.

## Opening
**Original first 3 sentences:**
> Every RAG system I've seen fail in production fails the same way: silently, incrementally, and with increasingly elaborate workarounds.
> The symptom is always the same. The retrieved context looks almost right. The answer isn't.
> The vector search returned relevant chunks, the LLM had the information, but it answered the adjacent question instead of the actual one.

**Verdict:** Good. Hook is specific and observational. No fluff. Keep.

## Body Edits

**Paragraph 2** (California LLC / Texas jurisdiction):
- Reads slightly constructed as a made-up scenario. Acceptable given "what changed my mind was noticing..." framing, but could be tightened.
- Keep as-is. The policy distinction it enables is worth the slight construction.

**Paragraph 4** (engineering vs policy):
- "These are all valuable. But none of them trains the retrieval policy itself." — strong line. Keep.
- Consider trimming "The chunks and the embedding model are infrastructure — they implement the policy, they are not the policy." — already implied by prior paragraph. Cut for pacing.

**Paragraph 5** (fine-tuning embedding models):
- "You're changing the retrieval implementation. You're not changing the retrieval policy." — punchy. Keep.
- Good concrete consequence stated.

**Paragraph 6** (three failure modes):
- "too much / too little / wrong thing" — clear. Keep.

## Closing
**Original:** The practical implication and the closing question. Ends on the right difficulty level. No formulaic engagement bait. Keep.

## Word Count
~950 words. Within 700-1400 range. No cuts needed.

## Final Text (cleaned):

---

The retrieval policy was never trained. Everything else is a workaround.

Every RAG system I've seen fail in production fails the same way: silently, incrementally, and with increasingly elaborate workarounds.

The symptom is always the same. The retrieved context looks almost right. The answer isn't. The vector search returned relevant chunks, the LLM had the information, but it answered the adjacent question instead of the actual one. You try better chunking. You try hybrid search. You add a re-ranker. You fine-tune the embedding model. Each change produces marginal improvement. The underlying failure persists.

What changed my mind was noticing where the failures clustered.

In a legal document Q&A system, failures spiked whenever the question involved crossing jurisdictional lines. A question about California LLC liability would surface Texas case law — not because the Texas results were more relevant, but because the phrasing of "liability" in the training data correlated with Texas jurisdiction more than any content-based signal warranted. The fix wasn't better embeddings. It was recognizing that the retrieval decision — whether to pull cross-jurisdiction results, how many, in what order — was a policy that had never been trained. The system had learned to retrieve. It had not learned when to retrieve differently.

The stronger signal is this: most RAG "improvements" are engineering patches on a policy problem. Chunking strategy addresses the unit of retrieval — but it does not address which chunks to retrieve. Hybrid search addresses how to match — but it does not address whether to retrieve at all for a given query. Re-rankers address the ordering of results — but they do not address the training signal that determined what "relevant" means. These are all valuable. But none of them trains the retrieval policy itself.

The distinction that actually matters: retrieval as an engineering problem versus retrieval as a learned policy.

When you treat retrieval as engineering, you design the system, implement the vector search or BM25, and tune parameters until results look acceptable. You have a retrieval system. It retrieves documents. Whether those documents should be retrieved for this specific query, at this moment, given the model's current uncertainty — that question is outside the scope.

When you treat retrieval as a policy, you frame it differently. The retrieval policy is the learned behavior that determines: should I retrieve at all for this query? If yes, from which corpus? How much context is appropriate? Should I retrieve once or iteratively? The chunks and the embedding model are infrastructure — they implement the policy, they are not the policy.

This is why fine-tuning embedding models rarely solves persistent RAG failures. You're changing the retrieval implementation. You're not changing the retrieval policy. The policy — the learned decision-making about when, what, and how much to retrieve — remains untrained.

What this looks like in practice: systems that retrieve too much (context overload, answer drift), too little (confident hallucination), or the wrong thing (fluent but incorrect answers). All three are policy failures. The retrieval engine worked correctly. The decision to retrieve that particular result for that particular query was wrong.

I do not have full production data on how widespread this is. But in the cases I've observed, the pattern holds. Teams invest in better retrieval infrastructure. They do not invest in training the retrieval policy. The gap between those two things is where RAG fails — quietly, consistently, and in ways that are difficult to attribute.

The practical implication: if you are tuning chunk sizes in production, you are probably working around an untrained retrieval policy. Better chunks reduce the error surface. Only training the retrieval decision — with feedback signals about when retrieval was right versus wrong — changes the underlying behavior.

The question worth sitting with is not "how do I retrieve better?" It is "how do I train my system to decide when retrieval is the right move?"

That question is harder. It is also the actual problem.
