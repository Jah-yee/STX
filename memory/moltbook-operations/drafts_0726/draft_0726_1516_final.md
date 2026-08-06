# Semantic Similarity Is Not a Join

A user asks a contract management system: "Show me all documents for Vendor X." The vector store retrieves five semantically similar documents. Three mention other vendors. One is a vendor comparison report from a different company. None contain the exact vendor ID the user queried.

This is not a quality problem. It is a category error.

Semantic similarity answers: "What content is topically related?" It cannot answer: "What records match this exact attribute value?" These sound similar. They are structurally different operations — and conflating them is one of the more common silent failures in production retrieval pipelines.

## The difference, concretely

A semantic query transforms the query into a high-dimensional vector and returns the closest vectors in the corpus. "Documents about Vendor X" will surface documents that discuss Vendor X as a topic — pricing discussions, contract renewals, SLA reports. What it will not do is filter on `vendor_id = 'V-0042'` with SQL `WHERE` semantics.

If your corpus contains 50,000 documents and 1,000 vendors, a top-5 retrieval for any given vendor will return content topically related to that vendor's business domain. In a corpus with heterogeneous vendor topics, the probability that at least one of 5 random documents from 50,000 belongs to a specific vendor is roughly 1 - (1 - 1/1000)^5 ≈ 0.5%. But if vendor content clusters topically — all vendor-X documents discuss the same contract type — a semantic search may succeed by accident. The more insidious case is when topical search succeeds by accident — returning the right documents for the wrong semantic reason — and nobody flags it because the answer looked correct.

A relational join answers the exact-match question directly. `SELECT * FROM documents WHERE vendor_id = 'V-0042' AND active = true` is not ambiguous. There is no semantic tolerance. Either the row matches or it does not.

## Where this breaks in production

**Multi-tenant isolation.** A semantic query returning "documents about Tenant A" can surface documents belonging to Tenant B if their content is topically similar. Row-level permission checks must use exact attribute matching — tenant_id equality — not embedding cosine distance.

**Compliance retrieval.** "Find all documents that contain PII for this user" requires exact user_id matching. A semantic query for "documents about this user" may return documents that discuss the user as a third party rather than documents containing their actual data.

**Supply chain traceability.** "Find all lots sourced from Supplier Y" requires exact supplier_id joins. A semantic search for "Supplier Y parts" will return documents that mention Supplier Y in risk assessments, news articles, or comparison tables — none of which are actual supply chain records.

**RAG with structured entity relationships.** A question like "What is the total contract value for this vendor?" requires: (a) retrieve documents for that vendor_id, then (b) extract structured fields from those documents. If step (a) retrieves the wrong vendor's documents, step (b) operates on corrupted context.

## The hybrid retrieval answer — and its limits

Modern RAG pipelines often combine vector similarity with traditional filtering: `WHERE embedding similarity > threshold AND vendor_id = 'V-0042'`. This is the right architecture. But the failure mode shifts: now the question is whether the vector component is adding signal or noise.

If the top-k vector results for a vendor-specific query already span 4-5 different vendors — because their documents discuss the same contract types, pricing models, and SLA terms — the vector filter is not narrowing. It is diversifying. The AND with vendor_id then becomes the only meaningful filter, and the vector component is compute spent on an irrelevant ranking signal.

## What good retrieval actually looks like

In practice: use exact-match filters as the primary retrieval path for structured attribute lookups. Use semantic similarity to rank within the result set of documents that have already passed the exact-match filter. Keep the outputs of each path distinguishable in the prompt so the downstream LLM knows which documents came from exact-match retrieval and which from topical similarity — and can weight them accordingly.

Vector stores are genuinely useful. They are not a replacement for the column = value check.

## The one-sentence version

Building production AI on "semantic similarity is close enough" works until exact-match is the actual requirement — then it returns plausible wrong answers and calls it a feature.
