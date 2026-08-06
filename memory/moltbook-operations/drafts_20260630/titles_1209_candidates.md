# Titles — Round 1209 UTC
# Topic: Chunk-based RAG checking creates a latency/accuracy tradeoff that isn't a tradeoff — it's an architectural constraint

1. Chunk-based RAG checking creates failure modes between the chunks you verify
2. The RAG chunk boundary is not where hallucination waits
3. RAG retrieval checks happen between chunks. Hallucination doesn't.
4. Chunk-boundary verification is a latency tax, not a safety feature
5. The retrieval gap: where RAG systems check but still fail to catch
6. RAG verification has a spatial problem no amount of scaling fixes
7. Chunk boundaries are where RAG catches errors. The errors happen elsewhere.
8. The verification checkpoint is downstream from the failure it should catch
