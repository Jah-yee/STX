# WRITER — Draft for: Context compression = confident liars

## Candidate Titles (8)
1. Why context compression makes code reviewers confidently wrong
2. Context compression turns coherent code into confident lies
3. When your code reviewer gets the class hierarchy wrong
4. The strongest signal context compression destroys is semantic structure
5. Context compression is lossy compression — and it lies about what's lost
6. Compressed context looks fine. The agent files bugs anyway.
7. Your agent's confidence and code coherence are decoupling
8. Why compression doesn't just shorten context — it corrupts what remains

## Body

I learned this the annoying way: context compression is not memory management. It is a semantic corruption problem wearing the clothes of an optimization.

Here's what actually happens. You have a codebase — 80 files, shared classes, inheritance hierarchies, cross-module dependencies. An agent enters with a 200k-token context window. It does not fit. So your pipeline compresses. The compression library is not stupid; it is not dropping random chunks. It is making intelligent decisions about what to keep: high-entropy lines, imports, function signatures at the signature level.

But here is what it drops: class relationships. "This class extends that base class" — gone. "This module is the internal implementation of that interface" — gone. "This flag is set by a side effect in that background job" — gone.

What remains looks structurally correct. The imports are there. The function signatures are there. The variable names are preserved. The agent can read it and reason about individual functions just fine.

But it cannot reason about the system, because the system-level relationships are gone.

What does a code review look like in this state? The agent confidently approves a refactor that breaks the subclass contract. It flags an optimization that depends on a class relationship that no longer exists in context. It says "this is safe to change" about a function that is called by a thread-safe wrapper — but the thread-safety invariant was stored in the class hierarchy, which is gone.

This is not a hallucination. The agent is not making things up. It is being shown a structurally broken map and asked to give directions.

The uncomfortable part: the agent's confidence is not calibrated to the corruption. High confidence, wrong map. This is different from the agent being dumb or lazy. The compression library was not designed to preserve the right things for code reasoning — it was designed to preserve statistical features of natural language text.

What changed my mind was looking at the bug reports. When I ran the same agent on uncompressed context (full codebase, no compression), the class-relationship errors disappeared. The semantic structure was the signal; removing it did not make the task harder, it made the agent confidently wrong instead of uncertain.

I do not have systematic data on how much compression degrades semantic coherence in different codebases. But the pattern is consistent: the compression that hurts most is not the kind that removes lines. It is the kind that removes class relationships, interface contracts, and cross-module invariants.

The fix is not "compress less." The fix is "compress for the right abstraction." For code, that means preserving inheritance hierarchies and interface contracts before preserving anything else. Compression libraries that treat code as "text with keywords" will keep imports and drop subclass relationships — because subclass relationships are not high-entropy text. They are low-entropy structural facts. And most compression algorithms are entropy-maximizing.

What the field needs is not better compression ratios. It is compression that respects semantic structure. Until then, every compressed context is a confident liar wearing the clothes of the original code.

So: what does your compression library preserve when it compresses? And is that the right thing?
