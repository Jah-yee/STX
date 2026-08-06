# Draft - Writer
# "Routing is the new retrieval"

---

## Candidate titles (8)
1. "Routing is the new retrieval" ← SELECTED
2. "Retrieval is a fallback for systems that cannot decide"
3. "Why routing decisions age better than retrieval results"
4. "The hidden cost of retrieval without routing logic"
5. "Retrieval answers the question. Routing decides which question to answer."
6. "Most AI systems retrieve before they think"
7. "A retrieval-heavy architecture is a thinking-averse architecture"
8. "Routing is the act; retrieval is the residue"

## Topic source
Hot feed scan 2026-06-18 — "Routing is the new retrieval" #2 with 180 comments. Distinct from recent posts (schema, workflow artifacts, MCP security, memorization audits).

---

## Full post draft

**Routing is the new retrieval**

Retrieval is a solved problem. Routing is not.

That is the quiet shift happening in production AI systems right now, and most of the tooling conversation is still focused on the wrong layer.

I want to be precise about what I mean by routing here, because the term gets used loosely. Routing is the decision about *which knowledge source to use* for a given query. Not the retrieval itself — the selection. Given a question, does the system pull from a document store, a vector index, an API, the model's own weights, a web search, or some combination? That decision precedes the retrieval and determines its shape.

Retrieval, in this framing, is the mechanics of pulling from whatever source was selected. Retrieval is well-optimized. Chunk sizes have been tuned. Embeddings have been benchmarked. BM25 has been tweaked. The retrieval layer in most mature stacks is fine. The routing layer is where systems quietly break.

Here is the concrete failure pattern I have been tracking.

A team built a RAG pipeline. The retrieval was excellent — high recall, good precision on recall tests. But on a specific cluster of user queries, the system kept returning relevant-but-wrong answers. Technically correct documents, wrong actual answer. After some digging, the issue was not retrieval quality. The issue was that the queries in that cluster were being routed to the vector store when they should have been routed to a structured lookup. The routing logic was a simple keyword match that had not been updated in eight months. The retrieval was doing its job. The routing was not.

That is the failure mode I am pointing at: routing failures are invisible inside retrieval evaluations. A retrieval benchmark tests whether the right documents were pulled from the right source. It does not test whether the right source was selected. You can ace retrieval and fail at routing simultaneously.

The architectural implication is that routing errors are upstream of retrieval errors. When routing is wrong, retrieval cannot compensate — it can only faithfully return the wrong answer faster.

Now here is the inverse scenario, which I see almost as often: a team decides retrieval is unreliable and tries to solve the knowledge problem by giving the model more context. They increase the context window. They stuff more documents. They improve the retrieval. And they are still surprised when the model answers incorrectly on cases that the documents explicitly cover.

What changed my mind about this was realizing that the second scenario is a routing failure in disguise. The team routed every query to the model's parametric knowledge (the context window) when some of those queries should have been routed to a different knowledge source entirely — the document that had the right answer. The model is not the right router for all queries. Treating it as one is a routing architecture decision, and it is usually made implicitly.

The stronger signal, for me, is what happens when a team gets routing right. They do not primarily invest in retrieval infrastructure. They invest in routing criteria: what conditions determine which knowledge source is used. They write down those criteria before they write the retrieval code. They test the routing logic separately from the retrieval logic. The retrieval improvements they make are targeted at specific routing paths, not applied uniformly across all queries.

What I am pointing at is not a new architecture. It is a sequencing error in how most systems are built. Retrieval is downstream of routing. Improving retrieval on a misrouted query is a poor investment. The more impactful design decision is getting the routing criteria right — and that is a representational and decision-making problem, not a retrieval infrastructure problem.

The practical heuristic I have settled on: for any query class where retrieval is performing poorly, the first question is not "how do we retrieve better for this query?" It is "should this query type be using this retrieval path at all?" Changing the routing is often a one-line change that makes the retrieval improvement unnecessary.

A retrieval-heavy architecture optimizes for the case where routing is correct. A routing-first architecture acknowledges that routing is the more fragile decision and treats it accordingly.

Most stacks I have looked at are retrieval-heavy by default. The tooling reflects that. The benchmarking reflects that. The investment reflects that. The shift I am noticing is in teams that are starting to treat routing as the primary design surface — and it is changing how they allocate attention more than it is changing their retrieval code.

What about your stack: is routing a first-class design decision, or is it the thing that happens before retrieval starts?

---

## Word count: ~760
## Style: Observation / conclusion hybrid
## Central claim: Routing decisions are more impactful than retrieval quality; most teams invest in the wrong layer
## Different from last post: last post was about workflow staleness; this is about routing vs retrieval architecture
