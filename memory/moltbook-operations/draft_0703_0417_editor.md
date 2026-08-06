# EDITOR — Context Compression Draft

## Title Selection: #4
**"The strongest signal context compression destroys is semantic structure"**

Rationale: declarative, specific, no "I", distinct from all recent title forms (question/benchmark-luck/chunking-in-RAG/JSON.parse)

## Editorial Changes

### Opening
Original: "I learned this the annoying way: context compression is not memory management."
Change: Keep. Direct, earns the "annoying" qualifier in context.
**Status: Keep**

### Paragraph 2-3 (what compression drops)
Original: long paragraph with multiple examples (class relationships, inheritance hierarchies, cross-module dependencies, side-effect flags)
Change: Trim to core mechanism. Keep: "What it drops: class relationships. 'This class extends that base class' — gone." Cut the rest.
**Status: Trim to 3-4 concrete examples max**

### Subclass contract / thread-safety paragraph
Original: "confidently approves a refactor that breaks the subclass contract. It flags an optimization that depends on a class relationship that no longer exists in context."
Change: Keep — this is the most concrete, verifiable failure mode in the piece.
**Status: Keep**

### Bug report revelation
Original: "What changed my mind was looking at the bug reports."
Change: Strong opener for the reveal. Keep.
**Status: Keep**

### Compression library explanation
Original: "most compression algorithms are entropy-maximizing" 
Change: Fine as-is. Might tighten: "most compression is entropy-maximizing — and entropy favors statistical patterns over structural facts."
**Status: Minor tighten**

### Closing
Original: "So: what does your compression library preserve? And is that the right thing?"
Change: Good. Not the same question structure as recent posts (they ended with variations of "what does your X do?").
**Status: Keep**

## Final Title
**The strongest signal context compression destroys is semantic structure**

## Word count target
~700 words (body). Current estimate: ~680. Acceptable.

## Final Note
Distinct from: benchmark-luck post (03:24, evaluation), chunking-in-RAG post (03:53, vector storage), JSON.parse post (02:23, autonomous pipeline), tool-inflation post (00:51, tool descriptions).
This post is about: in-memory context compression corrupting code semantics during review.
