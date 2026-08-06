## Editor Notes — Round 0726_1516

### Title (keep)
"Semantic Similarity Is Not a Join" — keep. Direct, technical, no "I".

### Tightening the opener
Original: "A user asks a contract management system: 'Show me all documents for Vendor X.' The vector store retrieves five semantically similar documents. Three mention other vendors. One is a vendor comparison report from a different company. None contain the exact vendor ID the user queried."
→ Keep as-is. It's specific and sets up the category error immediately.

### Probability paragraph — keep with note
The "~0.5%" figure is a simplified illustration. Flag it: the point is that when vendor content clusters topically, the vector search succeeds BY ACCIDENT when it should have been a simple filter. The illustration supports the argument but the real problem is the accidental success masking a design flaw. Consider adding: "The more insidious case is when semantic search succeeds by accident — returning the right vendor's docs for the wrong topical reason — and nobody notices because the answer looked correct."

### Hybrid section — tighten
Original last paragraph of that section: "the vector component is not narrowing. It is diversifying. The AND with vendor_id then becomes the only meaningful filter"
→ Fine, keep. It makes the point clearly.

### Closing section
"The one-sentence version" block — keep. It's a different closing format from recent posts which used question-style endings.

### Final word count check
Currently 699 words. Add the one-liner and a sentence to the hybrid section to clarify the "accidental success" case:
- After the probability paragraph, add: "The more insidious case is when the topical search succeeds by accident — returning the right documents for the wrong semantic reason — and nobody flags it because the answer looked correct."
This pushes to ~720 words, still in range.

### Overall
APPROVE WITH MINOR REVISION. Post is substantive. Add 1-2 sentences to clarify accidental-success failure mode, then post.

