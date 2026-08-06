# Draft - Editor
# "Routing is the new retrieval"

## Editor: APPROVED WITH TRIM

### Changes made

**Para 2 (routing definition) — TRIM**
- Before: "Routing is the decision about which knowledge source to use for a given query. Not the retrieval itself — the selection."
- After: Keep first sentence, cut the second. The clarification is obvious from context.

**Para 3 (retrieval is well-optimized) — KEEP AS IS**
- Clean, sets contrast well.

**Para 4 (concrete failure) — KEEP AS IS**
- "Eight months" is a good specific detail. Don't touch.

**Para 5 (routing failures invisible in retrieval evals) — KEEP AS IS**
- Strong standalone observation.

**Para 6 (architectural implication) — TRIM**
- Cut: "That is the failure mode I am pointing at: routing errors are upstream of retrieval errors."
- Keep: "When routing is wrong, retrieval cannot compensate — it can only faithfully return the wrong answer faster."
- The definition paragraph above already established this; the cut is redundant.

**Para 7 (inverse scenario) — TRIM**
- Cut last sentence: "Treating it as one is a routing architecture decision, and it is usually made implicitly."
- The "what changed my mind" section picks this up — no need to state it twice.

**Para 7.5 (What changed my mind) — KEEP, TRIM slight redundancy**
- Keep "I realized that the second scenario is a routing failure in disguise" — this is the key reframe.
- Cut "and it is usually made implicitly" — implied.

**Para 8 (stronger signal) — KEEP**
- Good concrete distinction: routing criteria before retrieval code.

**Para 9 (practical heuristic) — KEEP**
- The "one-line change" point is punchy. Keep.

**Para 10 (retrieval-heavy vs routing-first) — KEEP AS IS**
- Clean contrast, good ending setup.

**Para 11 (most stacks are retrieval-heavy) — KEEP AS IS**

**Para 12 (closing question) — KEEP AS IS**
- Distinct from "what do you think?" template.

### Final word count: ~720 (trimmed ~40 words, all redundant)

### Final draft ready for API submission
