# Writer Draft — Round 0707_1115

**Title:** When your agent can't find the file, the vector store is probably not the problem.

---

The standard debugging workflow for a failing code-agent retrieval goes like this: check the chunk size, bump the top-k, re-embed the corpus, maybe swap the vector store. If you are unlucky, you do all of this and the agent still returns the wrong file on the second try.

Here is the move nobody does: add a print statement to the retrieval path and look at what tokens are actually being compared.

In my own work and in what I have seen reported across open tooling repos, a surprisingly large fraction of code-agent retrieval failures are not semantic. They are syntactic. The retrieval pipeline worked fine. The agent retrieved the right chunk — it just could not parse the identifier inside it.

## The anatomy of a parser-level retrieval failure

The pattern looks like this: you have a codebase with a function called `get_or_create_user_session`. The agent is asked to find "the user session function." The retrieval system correctly surfaces `session.py` with the relevant code. But the agent's tokenizer sees `get_or_create_user_session` as something like 8-12 subword tokens, and the probability of matching those tokens against "user session function" collapses because the parser-level equivalence is never established.

This is not a chunking problem. It is not a top-k problem. It is that the retrieval query and the retrieved text do not share surface forms the tokenizer can bridge, and the vector similarity at the chunk level is not high enough to overcome that gap.

I do not have a systematic measurement of how common this is. But I have noticed it in enough distinct cases that I now check the parser layer before touching the vector store.

## Why it gets misdiagnosed

When a retrieval failure happens, the instinct is to look at the retrieval system. The failure manifests at retrieval time. The remediation options — more data, different embeddings, reranking — all live in the retrieval layer. So the fix also happens in the retrieval layer.

But the underlying problem is often upstream: the query being issued to the retrieval system is itself misparsed. The agent converts "find the user session function" into a query that does not match the surface form of the function name, and the vector similarity fails to compensate. Replacing Pinecone with Qdrant will not fix a tokenizer bridge failure.

This is the specific failure mode I am calling parser loss: the degradation in retrieval quality caused by the gap between how a human refers to a concept and how the tokenizer represents that concept in the retrieval query.

## The "just rephrase" band-aid

A common workaround is to tell the agent to rephrase the query — "search for session management in auth.py" instead of "find the user session function." This works because rephrasing often brings the query surface form closer to the token sequence in the retrieved text.

But this is a band-aid on a structural problem. The agent is now spending part of its reasoning budget on bridging a gap that should not exist if the retrieval pipeline accounted for token-level alignment. And it is not a fix for the cases where the failure is in the retrieved text itself — where the chunk boundaries cut through an identifier in a way that makes the chunk unreadable without the surrounding context.

## What would actually help

Two things I have found useful.

First, checking the retrieval path with a diagnostic: before tuning embeddings, run the retrieval query through the tokenizer and look at what tokens the agent's query actually generates. If the query tokens do not appear in the top matches of the retrieved chunks, the problem is parser-level, not semantic.

Second, thinking about identifier-aware chunking: chunk boundaries that respect token boundaries and preserve full identifiers are less likely to fragment in ways that break the tokenizer bridge. This is a design decision in the ingestion pipeline, not the retrieval pipeline, which means fixing it requires touching a different part of the system.

## The uncomfortable implication

If parser loss is a significant source of retrieval failures in code agents, then a lot of the effort being spent on embedding models, rerankers, and vector store infrastructure is addressing the wrong part of the problem. The retrieval system is being asked to compensate for a tokenizer gap that it cannot close.

I do not have the numbers to make this a strong claim rather than an observation. But I have stopped automatically blaming the vector store when retrieval fails, and that shift in debugging order has saved me time more often than not.

---

The file is usually there. Check the tokens before you check the vectors.
