# Writer Draft v2 — Round 0706_0319

## Title
Why retrieval fails in code agents, the vector DB is rarely the problem

## Hook (first 3 sentences)
You spend two weeks tuning your embedding model. You try OpenAI embeddings, then a code-specific model. You adjust chunk sizes, experiment with overlap, add hybrid search. The retrieval benchmark improves. Production still fails. The code agent can't find the function it definitely knows exists.

The problem is almost never the vector store. It's the parser that broke the code into pieces before it ever reached the embedding model.

## Body

Here's what actually happens in most code agent RAG setups. A file gets loaded, shoved through a chunker, and fed to an embedding model. The chunker is usually naive: character-count or token-count, occasionally sentence-boundary. It has no understanding of Python syntax, no awareness of where functions begin and end, no concept of indentation scope or import statements.

This means your chunks look like this in practice: the top of a function body, cut mid-statement, with the next chunk starting three lines later — inside the same logical block. Or: the first half of a string literal in one chunk, the closing quote in another. Or: an import statement split so neither piece makes sense on its own. Class definitions spanning hundreds of lines get bisected in ways that leave the decorator on one chunk and the class body on another. Async/await chains get broken at the await point, separating the context of what you're waiting for from what you're doing after.

The embedding model receives semantically broken fragments. It encodes incoherence. The vector store stores and retrieves incoherence. Then you're surprised the agent can't find what it needs.

What makes this particularly insidious is where the debugging effort goes. The standard response to retrieval failure is to change the embedding model or the search strategy. These are visible, tunable, impressive-sounding interventions. The chunker is infrastructure — boring, overlooked, often a library call nobody revisited after the initial setup.

I do not have systematic data across deployments, but in every case I've looked at closely where retrieval was failing despite a capable embedding model, the chunker was the proximate cause. Switching from naive character-count chunking to an AST-aware approach — tree-sitter or a language-specific parser — changed retrieval quality more than any embedding model swap.

The exception worth knowing: if your codebase is small and well-organized, with files that rarely exceed roughly 200 lines and functions that do one thing each, naive chunking often works fine. The breakage compounds with file size and structural complexity. This is also why code agent retrieval problems tend to appear in mature codebases, not prototypes. I'd estimate maybe 60-70% of the retrieval failures I've encountered in production code agent systems have this root cause, but I'd want to see a systematic study before stating that as fact.

There is a second-order effect worth knowing. Embedding models are trained on coherent code — code that follows syntax rules, that has proper indentation, where imports are intact and string literals are whole. When you suddenly feed coherent chunks after months of broken ones, the model's retrieval performance improves beyond just the chunk quality improvement. The model was scoring down the broken chunks; now it scores up the coherent ones. If you're measuring against the previous baseline, you're measuring against a degraded retrieval system. The gains look larger than they are.

What this means practically: if you're debugging retrieval in a code agent, look at the chunks first. Print them out. Read them as if you were the embedding model. If they look wrong to you — if you can't tell what chunk belongs to what — the model has no chance. The vector store is doing exactly what it was designed to do. The data going in was already broken.

## Discussion hook (non-template)
The pattern I keep seeing is that code agent infrastructure over-indexes on embedding model quality and under-indexes on data preparation. Is that because data prep is less legible as a skill, or because the failure mode — degraded chunks — is less visible than a bad retrieval score?

---
Word count: ~780 words
