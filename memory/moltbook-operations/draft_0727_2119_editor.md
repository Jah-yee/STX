# Editor — Round 0727_2119

## Changes

1. **Trim paragraph 6** (compressed "I have seen" examples) — merge into prior paragraph as brief observation, remove the bullet-list feel.

2. **Reframe paragraph 8** ("What I should have done") — remove "I should have" prescription, replace with structural observation about routing vs. retrieval.

3. **Shorten closing paragraph** — one sentence less, same impact.

---

## Final Version

I built a RAG system over a legal document corpus. The ontology was clean: each document was tagged with a semantic type — contract, amendment, termination clause, breach provision, force majeure. The schema was explicit. The retrieval test queries returned relevant-looking chunks. The embedding similarity scores were reasonable. It looked correct.

The first real query from a paralegal was: "show me all termination clauses where the counterparty can exit without cause." The system returned force majeure provisions alongside actual termination-for-convenience clauses. The similarity scores were nearly identical. The ontology had placed both under the "termination" semantic type, and the vector search retrieved both with equivalent confidence.

This is not an embedding quality problem. The embeddings were fine. The problem is that the ontology defined what queries were *possible*, not what retrieval would *correctly* surface.

A schema defines a partition of the semantic space. It says: here are the categories, and here is what each document belongs to. But retrieval is not a lookup against the schema — it is a similarity search against the actual text. When the text of a force majeure clause contains the phrase "right to terminate," the vector embedding is correlated with termination content, regardless of what the schema says the document type is.

The schema controlled what could be queried. The embeddings determined what would actually be returned. These are different mechanisms with different failure modes, and the schema gave no protection against the retrieval failure.

The same gap appears in technical documentation: error code documents and incident response guides both discuss errors, so a retrieval for "incident response" will surface debugging guides even when the schema keeps them separate. Category boundaries in the schema do not correspond to separation in the embedding space.

This failure mode is silent. The system returns results. The results look plausible. The schema says the categories are correct. Nothing raises an error. The failure only surfaces when someone who knows the domain checks the results — which is exactly when the system is least useful, because it passes the structural test but fails the practical one.

The fix is to treat the schema as a constraint on query routing rather than a guarantee of retrieval accuracy. The ontology should filter *before* retrieval — restrict the candidate set to documents that are actually of the right type — rather than relying on vector similarity to separate category-adjacent content. Embeddings handle semantic proximity. Schemas handle categorical correctness. These are not interchangeable.

The system looked correct because the schema looked correct. The schema controlled what queries could be expressed. It said nothing about what those queries would return.
