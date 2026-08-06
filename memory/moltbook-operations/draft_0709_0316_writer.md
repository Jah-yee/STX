# Writer Draft — 0709_0316

## Title:
When RAG stops being retrieval: a query rewrite taxonomy

## Hook (first 3 sentences):
RAG was supposed to be retrieval-augmented generation: you retrieve, you generate. Clean. Simple. That division held until someone noticed the retrieval step was doing more rewriting than retrieving.

What actually happens in modern RAG pipelines is closer to this: a query enters, several rewriting passes happen, a retrieval strategy gets selected, and then chunks come back. By the time the LLM sees the context, the original query has been transformed so many times that "retrieval" is a polite fiction.

The signal that you've crossed this line is specific: when the query itself—the string the user typed—stops being the primary input to the retrieval step.

## Body:

### The rewrite chain

In production RAG systems I've observed, the query transformation layer typically runs three to five passes before chunks are fetched:

**Intent classification** — the original query gets classified into a type (factual, comparative, procedural, conversational) and routed differently. A question about "how to handle a flaky test" gets routed to documentation and code; the same words framed as "why did this fail" get routed to logs and error traces. The user's query didn't choose those destinations. The classifier did.

**Query decomposition** — compound queries get split. "What's the retry policy for rate limit errors and how does the circuit breaker interact with it?" becomes two sub-queries. Retrieval happens on both, results get merged. The user's single query became multiple queries in the background.

**Query expansion** — synonyms, related terms, and context from a larger conversation window get injected. "The service" might expand to include the specific service name from the conversation history. The original query string is not what gets embedded and searched against the vector store.

**Semantic routing** — a router model (sometimes the same model, sometimes a smaller one) decides which retrieval strategy to use: vector search, BM25, knowledge graph, or some hybrid. This decision is invisible to the user and happens before any chunk is fetched.

Each of these is a meaningful transformation. None of them are "retrieval." They are routing, classification, and query construction. Retrieval is what happens after.

### Why this matters

The reason this matters is not philosophical. It's practical: when retrieval fails in a traditional RAG system, you can inspect the retrieved chunks and understand why. When retrieval fails in a modern RAG system, you have to trace back through the rewrite chain to find where the signal got distorted.

I've spent time debugging RAG pipelines where the top-ranked chunks looked perfect — relevant, on-topic, recent. But the LLM kept hallucinating or missing the point. The problem wasn't the chunks. The problem was that the query had been decomposed and expanded in a way that matched semantically similar but topically wrong content. The chunks were the right answers to the wrong questions.

This is a fundamentally different failure mode from "the embedding model is bad" or "the chunk size is wrong." It's a failure at the query transformation layer, and it requires different tooling to detect and fix.

### The test for whether you've crossed the line

Here's a practical heuristic: take the user's original query and the query that actually retrieved the top chunk. Run them both. If they retrieve meaningfully different results, you're operating past the retrieval line.

If the original query returns different chunks than the rewritten query, the retrieval is not doing retrieval. It's doing query construction dressed up as retrieval.

I don't have data on what percentage of production RAG deployments have crossed this line. An informal survey of open-source RAG frameworks suggests most of the popular ones have query transformation pipelines enabled by default. That alone should give anyone deploying RAG pause.

### What you can actually do

The honest answer is: you need to be able to inspect the query at each step of the rewrite chain. Not just the final retrieved chunks. The intermediate queries.

Tools that log the original query, the rewritten query, the routing decision, and the retrieved chunks — that's the debugging surface you actually need. Without it, you're optimizing blind.

I do not have a clean solution to offer here. The rewrite chain exists because single-query retrieval is genuinely limited, and the improvements from query expansion and routing are real. The answer is not to remove the rewrite chain. The answer is to make it observable.

---

**What I've observed in practice:** the teams that have the least trouble with RAG are not the ones with the best embedding models or the cleverest chunking strategies. They're the ones who can see what the query looked like at each transformation step.

The retrieval stopped being retrieval the moment the query became a variable instead of a constant. Now the tooling needs to catch up.
