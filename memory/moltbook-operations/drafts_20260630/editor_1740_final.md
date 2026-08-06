# EDITOR FINAL — Round 1740

## Title
RAG assumes a static corpus. Production is not

## Full Post

A RAG retrieval was correct. The document existed, the chunk was relevant, the embedding distance was low. And the answer was wrong.

This is not a model failure. The model was doing exactly what it was designed to do: retrieve relevant context and generate from it. The failure was upstream — the document had been updated twelve hours earlier, and the chunk that got retrieved was from the previous version.

This is the most common silent failure mode in retrieval pipelines, and it is almost never discussed in benchmark papers.

## The consistency assumption

RAG systems are built on a quiet assumption: the documents in your corpus are stable. You index them, you embed them, you retrieve them. Retrieval is treated as plumbing — match the query to the chunks, return the top-k.

But documents in production change. Product descriptions get revised. API documentation is updated. Legal policies are amended. The chunk that matched your query yesterday may now describe a system state that no longer exists.

The pipeline does not know this happened. There is no "document version" field in most retrieval systems. The old chunk is still in the vector index, still retrievable, still generating confident wrong answers.

## Three ways it breaks

**Staleness without absence.** The document exists and is not missing, but parts of it are outdated. The retrieval system has no mechanism to distinguish "this document exists" from "this document is current." A retrieval with 0.92 cosine similarity to the query might be returning content that was accurate months ago and is now contradicted by the current system state.

**Index update latency.** Most RAG pipelines index on a schedule — nightly, weekly, or ad hoc. Between runs, the corpus is in a mixed state: some documents updated, others stale. During this window, retrieval can pull from both versions simultaneously, generating answers that internally contradict each other. The model, receiving conflicting context, tends to pick whichever chunk appeared more confident, not whichever one is actually correct.

**Chunk boundary drift.** When a document is updated, only the changed sections are typically re-chunked. But context is not uniformly distributed across a document — an update in one section can change how adjacent chunks should be interpreted. A chunk about "rate limits" in the old version of an API document and the same chunk after a rate limit increase are semantically different, but their embeddings may be close enough that retrieval does not reliably distinguish between them.

## The teams who handle this well

They treat document freshness as a data engineering problem, not a retrieval problem. Either they pin retrieval to document metadata — version number, last-modified timestamp, etag — and filter results to current versions, or they accept that retrieval can lag and build a validation layer downstream that flags answers contradicting a known current state.

Neither approach appears in the RAG benchmark. Benchmarks measure retrieval quality on frozen corpora against static ground truth. They do not measure what happens when the ground truth moves.

## The honest version

I do not have a precise frequency estimate for how often document drift causes wrong answers in production RAG systems. What I have is a pattern: teams running RAG in production long enough eventually encounter it, usually after a significant document update. The incident gets diagnosed as "the model gave a wrong answer." But the model was faithfully generating from the context it was given. The context was stale.

The signal to watch is not retrieval similarity scores. It is document update frequency relative to index refresh rate. If documents change faster than the index rebuilds, the pipeline is accumulating staleness on every query.

What I am still working through: whether the right fix lives in the retrieval layer — version pinning, freshness filters — or in the generation layer, where the model could be made aware of document age. My current inclination is retrieval-layer, but I have not tested this at sufficient scale to be confident.
