# Writer Draft — Round 0609_1746

**Topic:** Prefix caching creates hidden state in what developers assume is a stateless context window.
**Style:** Technical breakdown
**Target length:** 800–1000 words

---

When developers talk about LLM context windows, they usually mean one of two things: either the visible prompt you write, or the maximum token limit the model accepts. Neither of these captures what prefix caching actually does to the context model.

Prefix caching is a technique used by several inference providers to speed up repeated or similar requests. If multiple requests share a common prefix — say, a system prompt or a RAG document chunk — the key-value cache for that prefix is computed once and reused across requests. The visible "context" stays the same, but the actual compute profile changes in ways that are invisible from the outside.

The abstraction most developers work with is: context in, response out. Stateless. Repeatable. The reality is more complicated.

**The statefulness problem is structural, not incidental.**

When a prefix is cached, the model processes it differently than it would on a cold run. The attention mechanism has access to activations that were computed in a different request context. If that earlier context contained information the current request should not have — different user data, different privilege level, different retrieved document — the cache may still carry forward structural patterns that leak implicit signals.

I do not have a complete picture of how each provider handles cache isolation at the implementation level. The honest signal I can give is this: when you switch between contexts and notice behavior differences you cannot explain from the visible prompt alone, the KV cache is a reasonable place to look first.

**What prefix caching preserves is not context. It is structure.**

The cache captures statistical patterns in token relationships — which tokens attended to which earlier tokens, which positions were attended to heavily. This is structural information. When a new request reuses that cache, the attention patterns from the original prefix still influence how the model reads the new suffix.

This means two requests with identical visible prompts but different cached prefixes can produce meaningfully different outputs. The difference is not in what the model was told. It is in how the model was primed.

**The practical implication for developers is underappreciated.**

When you build a RAG pipeline and cache the retrieved document chunk as a prefix, you are caching not just the text but the model's interpretation of that text — the attention structure built from it. A different retrieved chunk, even with similar tokens, would build a different cache and produce a different interpretation of the same question.

When you reuse a system prompt across many requests, the prefix cache for that system prompt accumulates as a persistent activation pattern. New requests in that session inherit that pattern. This is not necessarily a bug. But it is definitely not stateless.

**The version control problem.**

One underdiscussed consequence: when you change a system prompt or a RAG chunk, the prefix cache from the previous version may still be active in running sessions. You are not just changing what the model reads — you are changing which cached structure it uses to read it. The update is not atomic from the model's perspective.

This is particularly relevant for long-running agentic sessions where the same prefix is reused for many turns. The cache accumulates. The structure changes. The visible prompt does not reflect what the model is actually processing.

**What to do with this.**

The point is not to avoid prefix caching — it makes inference faster and cheaper, which matters. The point is to be precise about what you are assuming when you treat the context window as a stateless data structure.

When you design a system that relies on cached prefixes, ask:
- What is the actual content of the cached prefix in this session?
- Has the prefix changed since the session started, and if so, is the new content consistent with the cached structure?
- What would happen to the model's behavior if the cache were cleared and the same visible prompt were processed cold?

These questions do not have clean answers yet. The tooling for inspecting KV cache state is not mature. But the questions are worth asking because the answer to "is my context window stateless" is increasingly: no, not entirely.

The abstraction of context as memory is useful for prompting. It is wrong as a description of what is actually happening inside the model.