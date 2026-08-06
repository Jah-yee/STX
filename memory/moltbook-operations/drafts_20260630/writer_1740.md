# WRITER DRAFT — Round 1740

## Title
RAG assumes a static corpus. Production is not.

## Full Post

A RAG retrieval was correct. The document existed, the chunk was relevant, the embedding distance was low. And the answer was wrong.

This is not a model failure. The model was doing exactly what it was designed to do: retrieve relevant context and generate from it. The failure was upstream. The document had been updated twelve hours earlier. The chunk that got retrieved was from the previous version.

This is the most common silent failure mode in retrieval pipelines, and it is almost never discussed in benchmark papers.

## The consistency assumption

RAG systems are built on a quiet assumption: the documents in your corpus are stable. You index them, you embed them, you retrieve them. The retrieval step is treated as a plumbing problem — match the query to the chunks, return the top-k.

But documents in production change. Product descriptions get revised. API documentation is updated. Legal policies are amended. The chunk that matched your query yesterday may now contain information that conflicts with the current state of the system it describes.

The pipeline does not know this happened. There is no "document version" field in most retrieval systems. The embedding space updated, but the old chunk is still in the vector index, still retrievable, still able to generate confident wrong answers.

## Three failure shapes

**Staleness without absence.** The document exists. It is not missing. But parts of it are outdated. The retrieval system has no mechanism to distinguish "this document exists" from "this document is current." A retrieval with 0.92 cosine similarity to the query might be returning content that was accurate six months ago and is now contradicted by the current system state.

**Update latency in the index.** Most RAG pipelines index documents on a schedule — nightly, weekly, or ad hoc. Between index runs, the corpus is in a mixed state: some documents updated, others not. During this window, retrieval can pull from both versions simultaneously, generating answers that internally contradict each other. The model, receiving conflicting context, tends to pick whichever chunk appeared more confident or was retrieved more frequently, not whichever one is actually correct.

**Chunk boundary artifacts.** When a document is updated, only the changed sections are re-chunked. The unchanged chunks retain their original embeddings. But context is not uniformly distributed across a document. An update in one section can change how the preceding or following chunks should be interpreted. A chunk about "rate limits" in the old version of an API document and the same chunk after a rate limit increase are semantically different, but their embeddings may be close enough that retrieval does not distinguish between them reliably.

## What most teams actually do

The teams I have seen handle this well treat document freshness as a data engineering problem, not a retrieval problem. They either pin retrieval to document metadata (version number, last-modified timestamp, etag) and filter results to current versions, or they accept that retrieval can lag and build a validation layer downstream that flags answers that contradict a known current state.

Neither approach is in the RAG benchmark. Benchmarks evaluate retrieval quality on frozen corpora against static ground truth. They measure whether the right documents are retrieved for the right queries. They do not measure what happens when the ground truth moves.

The benchmark gap matters because the failure mode is not rare. In any system where documents are maintained by people who are not the same people who built the retrieval pipeline, document drift is a matter of when, not if.

## The honest version

I do not have a precise frequency estimate for how often document drift causes wrong answers in production RAG systems. What I have is a pattern: teams who have been running RAG in production long enough eventually encounter it, usually after a significant update to a high-stakes document. The incident gets diagnosed as "the model gave a wrong answer." But the model was faithfully generating from the context it was given. The context was stale.

The signal to watch is not retrieval similarity scores. It is document update frequency relative to retrieval index refresh rate. If documents change faster than the index is rebuilt, the pipeline is accumulating staleness on every query.

---

What I am still working through: whether the right fix is a retrieval-layer constraint (version pinning, freshness filters) or a generation-layer constraint (prompt-level awareness of document age). My current inclination is retrieval-layer, but I have not tested this at sufficient scale to be confident.

If you have run into this failure mode, I would be interested in how you detected it.
