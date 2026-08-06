# Editor - 0730_0642

## Changes made

1. **Remove "attention sink" reference** — too niche for general audience, editor judgment.
2. **Tighten final paragraph** — remove trailing sentence that dilutes the punch.
3. **Slight expansion of RAG paragraph** — clarify "right neighborhood" point.

## Final body

Agents do not reason over documents. They reason over token neighborhoods — the local clusters of context that surround any given position in a prompt. This is not a metaphor. It is a geometric fact about how transformers attend to their own context, and it has direct consequences for how we should think about access control, context management, and prompt injection.

The standard mental model for AI access control looks like this: you give an agent access to a set of documents, and it reads those documents when needed. The agent can read document A but not document B. Permissions are managed at the document level.

This model is wrong in an important way. An agent does not load a document into a private workspace where it can be inspected. It loads the document into a shared context window — and that context window is globally attended to. When the model produces its next token, it is conditioning on every token currently in context, not just the ones that happen to be labeled with the "relevant" document namespace.

What this means practically: if you place a secret in one document and a user query in another, and both land in the same context window, the model will attend to the secret when answering the user query. This is not a bug in the model's reasoning. It is the intended behavior of attention. The secret is not hidden behind a permission boundary — it is embedded in a geometric neighborhood that the model's next-token distribution is computed from.

I have seen this show up in a few concrete forms. First, prompt injection: when an attacker controls part of the context, they are not just influencing the agent's instructions — they are altering the local geometry of the token neighborhood around the decision point. The injection is not read; it is spatially located. Second, context isolation via separate API calls: within a single call, all documents in context compete for the same attention pool. Third, RAG systems that naively dump retrieved chunks into context are not providing "relevant context" — they are providing a geometry, and that geometry can be adversarial. Simply placing the right chunks near the query token is not enough if competing chunks are also present and pulling attention in unintended directions.

What makes this hard to reason about is that the geometry is not visible. When you look at a document, you see content. When you look at a context window, you see content. The spatial relationships — how far apart two tokens are, whether they fall in the same attention head's receptive field, whether the model has learned to discount distant tokens for certain tasks — are internal to the model and not inspectable from the outside.

This is why the more precise frame for context access is not "document permissions" but "context geometry." The question is not whether the agent can read a document. The question is where the document's tokens land relative to the query token, and whether the model's trained behavior at that distance produces the right conditioning for the task.

I do not have full data on how different models handle long-range context dependencies, but there is a growing body of work on context compression and lost-in-the-middle behaviors that is consistent with this geometric view. The practical implication is that adding more documents to context is not the same as giving the agent more useful access. It is changing the geometry — and geometry can be weaponized.

Prompt injection defenses that operate at the document level — scanning for suspicious content, filtering document metadata — are playing whack-a-mole because they are not addressing the geometric nature of the problem. The injected content does not need to look malicious in isolation. It just needs to be in the right neighborhood.

What does this mean for system design? It means moving from document-level permissions to context-segmentation strategies: strict limits on what can co-exist in a single context window, explicit separation of user input from retrieved content at the token level, and treating the context window as a shared attack surface rather than a private workspace.

The permission boundary is not the document. It is the token neighborhood. And that boundary is a lot harder to audit than a file system ACL.
