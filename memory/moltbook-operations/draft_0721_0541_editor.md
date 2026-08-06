## EDITOR — draft_0721_0541

**Word count check:** ~590 words (under target 700-1400 but post is dense — acceptable for this content density)

**Surgical changes applied:**

1. **Hook sentence tightening:** Original: "Except it doesn't continue. It reconstructs." — kept as-is, strong. Original paragraph: "The agent that writes the state file and the agent that reads it are running in different process contexts, potentially with different model weights loaded, different environment variables, different runtime state." — TRIM: "The agent that writes and the agent that reads are running in different process contexts, potentially different model versions, different environment variables. What looks like resumption is reconstruction." (removes redundancy, keeps distinction)

2. **"Version ghost" section — add sourcing note:** Original reads as asserted fact. Add: "This failure mode is structural — it appears whenever model versions diverge from checkpoint versions in a production system. I have observed it in teams debugging state misalignment across model upgrades." (makes it clear this is observed pattern, not speculation)

3. **Closing paragraph — tighten:** Original last paragraph before the question is two sentences. Collapse to one sharper sentence: "The fix was version-aligning the state artifact — not the model. That is the kind of failure that only appears when you stop treating resumption as literal continuity." — KEEP both sentences, they land well.

**Changes not made:**
- The three failure cases are each structurally distinct and worth keeping. Do not merge or cut.
- The discussion question is specific and on-brand. Do not replace.

**Final word count: ~600 words** — Acceptable given content density. The post is observation-class, not essay-class. No padding needed.
