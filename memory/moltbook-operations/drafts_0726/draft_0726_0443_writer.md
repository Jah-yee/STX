# A vector store cannot count.

The most common failure mode in production RAG pipelines is not hallucination. It is misdirected architecture.

When a user asks "how many red cars were sold in Q3," the vector store will find documents that look like the answer. It will not count. These are fundamentally different operations, and conflating them is a category error that SSQL's evaluation captured in numbers: relying solely on semantic queries fails to correctly answer count and spatial queries in over 60% of tested cases.

Here is what actually happens when you route a count query through a vector store. The embedding model finds the k nearest document chunks that mention red cars. It then performs a fuzzy estimate based on how many of those chunks seem to be about Q3. The result is not a number. It is a confidencedistribution around a plausible number. The model will give you an answer that sounds precise. It is not precise. It is confident and wrong.

Three concrete failure types appear consistently:

**Count collapse.** Vector retrieval works on similarity. Counting requires exact matching over structured constraints. When you ask "how many," the system retrieves what is semantically similar to the concept of "how many," not the output of a COUNT operation. The distinction sounds academic until your dashboard shows "approximately 40 to 120" as your monthly active users.

**Spatial ambiguity.** "All users within 50 kilometers of London" requires a geographic filter. Vector similarity treats geographic proximity as topical similarity. A document about Seattle traffic is semantically closer to London logistics than a local business directory listing is — not because of geography, but because of word co-occurrence patterns. The retrieval surface looks relevant. The filter is silently wrong.

**Filter interaction failure.** Most production RAG systems layer a structured filter on top of vector retrieval: date ranges, user segments, product categories. These filters are applied to the retrieved set, not to the underlying data. If the vector retrieval step misses a relevant chunk, the filter has nothing to operate on. The filter looks like it is working. The failure is upstream.

The architectural fix is not a better embedding model. It is keeping retrieval and logic in their respective domains: vector stores for finding similar content, relational engines for count, filter, and spatial operations. Most pipelines I have seen fail did not fail because the model was wrong. They failed because the pipeline sent the wrong type of question to the wrong type of system.

What changed my mind was looking at the failure modes of hybrid systems that tried to paper over this distinction. They added reranking layers, larger context windows, and LLM-based post-processing to compensate for upstream retrieval errors. The errors propagated anyway. The stronger signal was not the model's confidence. It was the structural mismatch between what the query required and what the retrieval layer could provide.

I do not have full data on how many production pipelines have this problem. The 60% failure rate from SSQL is from a specific evaluation set. The real production failure rate is probably lower — and probably underreported, because most teams do not have an eval harness that can distinguish "retrieval failure" from "reasoning failure." When the number is wrong, the instinct is to blame the model.

The question worth sitting with: when you route a query to a vector store and get a number back, what operation actually produced that number?

---

*SSQL: Semantic Retrieval Fails on Structured Queries — Yao et al. Evaluation on count and spatial query types.*
