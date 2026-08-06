# Draft — Round 0727_2119 Writer

**Selected Title:** "I built a RAG that looked correct by design and failed at query time"

---

I built a RAG system over a legal document corpus. The ontology was clean: each document was tagged with a semantic type — contract, amendment, termination clause, breach provision, force majeure. The schema was explicit. The retrieval test queries returned relevant-looking chunks. The embedding similarity scores were reasonable. It looked correct.

The first real query from a paralegal was: "show me all termination clauses where the counterparty can exit without cause." The system returned force majeure provisions alongside actual termination-for-convenience clauses. The similarity scores were nearly identical. The ontology had placed both under the "termination" semantic type, and the vector search retrieved both with equivalent confidence.

This is not an embedding quality problem. The embeddings were fine. The problem is that the ontology defined what queries were *possible*, not what retrieval would *correctly* surface.

A schema defines a partition of the semantic space. It says: here are the categories, and here is what each document belongs to. But retrieval is not a lookup against the schema — it is a similarity search against the actual text. When the text of a force majeure clause contains the phrase "right to terminate," the vector embedding is correlated with termination content, regardless of what the schema says the document type is.

The schema controlled what could be queried. The embeddings determined what would actually be returned. These are different mechanisms with different failure modes, and the schema gave no protection against the retrieval failure.

Here is the specific structural problem: the ontology was designed for document classification, not for retrieval behavior. The schema said "this document is a force majeure clause." The query embedding for "termination without cause" matched the force majeure text because both discuss termination events in similar language. The schema category was correct. The retrieval result was wrong.

This is a schema-data alignment problem. The ontology assumes that semantic categories map to retrieval surface in a way that preserves the category boundaries. They do not. The embedding space is continuous and topic-correlated. The schema categories are discrete. These are not the same space.

I have seen this failure in other forms. A technical documentation RAG where every "error code" document gets classified as "incident response" — but the retrieval for "incident response" also returns debugging guides because both discuss errors. A product knowledge base where "pricing" and "billing" are separate schema types, but the actual chunks about billing errors get retrieved for pricing queries because both involve amounts and charges.

The failure mode is silent. The system returns results. The results look plausible. The schema says the categories are correct. Nothing raises an error. The failure only surfaces when someone who knows the domain checks the results against their expectations — which is exactly when the system is least useful, because it passes the structural test but fails the practical one.

What I should have done: treated the schema as a constraint on query routing, not as a guarantee of retrieval accuracy. The ontology should filter *before* retrieval — restrict the candidate set to documents that are actually of the right type, using a classifier or metadata filter — rather than relying on the vector search to separate category-adjacent content based on embedding similarity. The embeddings handle semantic proximity. The schema handles categorical correctness. Using one to substitute for the other is the error.

The retrieval gap is not fixable by better embeddings. It is fixable by making the schema exert actual control over the retrieval surface — through routing, through filtering, through the structured capture of what category a chunk actually belongs to, not just what the parent document's schema says it is.

The system I described looked correct because the schema looked correct. The schema controlled what queries could be expressed. It said nothing about what those queries would return.
