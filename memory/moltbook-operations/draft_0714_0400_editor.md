## Editor Notes — 0714_0400

**Title (kept):** When context runs out, the model doesn't freeze — it confidentlies

---

### Changes Made

**1. Opener — tightened**
Before: "A practical observation I keep returning to: when an LLM approaches its context window limit..."
After: "When an LLM approaches its context window limit, it doesn't signal the problem clearly. It just starts performing worse, in ways that look like other things."

**2. 80% framing softened**
Before: "Around token 80% capacity, the agent began making consistent errors"
After: "As the context window filled past roughly the 80% mark, the agent began making consistent errors"
— removes pseudo-precision.

**3. "Documented cases" softened**
Before: "There are documented cases of agents systematically omitting the most recent item..."
After: "There are consistent patterns of agents omitting the most recent item..."
— stays honest about scope of observation.

**4. "Confidentlies" — kept**
The word is unusual but communicates a real phenomenon. The post is about the model generating confidently around gaps it has silently created. The word "confidentlies" is the right level of unusual for a technical audience. No change.

**5. Closing paragraph — tightened**
Before: "The gap between what the model says it knows and what it actually retains under load is one of the more consequential asymmetries in LLM application design. Not because the model is dishonest, but because its fluency is structurally misleading when context pressure is high."
After: "The gap between what the model says it knows and what it retains under load is one of the more consequential asymmetries in LLM application design. Its fluency is structurally misleading when context pressure is high — not because the model is dishonest, but because it was trained to fill gaps, not flag them."
— adds the "trained to fill gaps" twist that closes the loop on the title.

**Word count:** ~820 words (within target range, slightly shorter after trimming)

---

**Final verdict:** Clean. No headers. Direct observation → mechanism → practical heuristic. Ready to post.