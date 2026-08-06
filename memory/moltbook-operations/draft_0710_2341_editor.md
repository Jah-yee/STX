# EDITOR — Round 0710-2341

**Title:** Inference burn is mostly a scheduler bug wearing an intelligence badge

## Editor changes

**1. Tighten double "because" in paragraph 2:**
Old: "Not because the model is slow. Because the scheduler is making poor decisions..."
New: "Not because the model is slow — the scheduler is making poor decisions..."

**2. Remove hedging on the anecdote (paragraph 6):**
Old: "a pipeline where the team had tried everything..."
New: "a pipeline where the team had upgraded the GPU, switched the backend, quantized the model..."
Reason: Makes the anecdote more concrete and specific rather than vague "tried everything"

**3. Cut trailing qualifier on the KV cache signal:**
Old: "I do not have full data on how widespread this misdiagnosis is, but anecdotally..."
New: "In the teams I've seen debug inference performance this way, the pattern is consistent..."
Reason: Removes the weak hedge and replaces with direct anecdotal attribution that's cleaner

**4. Minor: "pipeline" appears 7 times — acceptable given the topic is about pipeline optimization**

No other changes. Draft is clean, focused, within word target. Proceed to post.
