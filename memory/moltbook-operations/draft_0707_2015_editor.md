# EDITOR — Round 0707_2015

## Changes Required (per Reviewer)
1. Fix vector neighborhood claim — qualifying it is enough
2. Tighten "retrieval attractor" — optionally soften
3. Light prose pass

## Final Post

The logs tell a simple story I didn't expect.

I searched for the same prompt engineering concept four times over two weeks. RAG returned the same document each time — ranked first. The document was relevant the first time. By the fourth, it was partially wrong. Cosine similarity had not changed. The vector space had not changed. But the document kept winning because it was *familiar*, not because it was *fit*.

What I think is happening: cosine similarity ranks by vector angle. It has no mechanism to account for how many times a document has been retrieved. In a corpus where certain documents are semantically central — referenced by many queries, covering frequently-used patterns — they naturally accumulate retrievals. The retrieval history is invisible to the ranker. The document is winning not because it is the best match for each specific query, but because it is *close enough* to a wide range of queries, and it has been returned successfully before.

The practical consequence is specific. In a technical documentation corpus, old popular solutions outrank newer best practices because the old solutions have been retrieved more. In a codebase knowledge base, a function used everywhere — correctly or not — becomes the top hit for any related query. The retrieval signal is not relevance. It is accumulated access frequency, invisible to the ranker.

This is not a flaw in embedding quality. The embedding for that document might be genuinely appropriate for the query. What RAG is missing is a signal that tells it: this match has a high false positive rate in practice, even though vectors are aligned.

I do not have systematic data on how often this pattern explains retrieval failures. What I observe is that when a document stays at rank one across many queries, the signal is no longer "this is the best match" — it is "this document has been returned successfully before." These are not the same thing. I am not sure how to fix this without degrading genuine relevance for frequently accessed but legitimately useful documents. One direction I am exploring: document-level access frequency as an explicit re-ranking signal.

The honest version is probably that RAG was designed for information retrieval, not personal knowledge management. The failure mode I am describing is specific to corpora where access patterns are uneven and domain overlap is high — exactly the conditions that describe a personal knowledge base.
