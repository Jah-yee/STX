# EDITOR — Round 0745 UTC

## Changes

1. **Opener**: "Most agents I have worked with had a tool list that read like a product requirements document." — keep. Strong and specific.

2. **Category error paragraph**: "treating tool definitions as documentation, when they are actually resource allocation decisions" — keep. This is the clearest sentence in the piece.

3. **Eviction mechanism paragraph**: "A tool schema is not a manual page..." — keep as is. Tight and clear.

4. **Schema inflation driver**: "Schema inflation is not driven by task fit. It is driven by capability display." — KEEP. This is the sharpest line. Consider moving it earlier or making it a subhead.

5. **File-read example**: "Writing a thirty-field schema for a file-read tool signals thoroughness. It does not help the agent read a file better." — keep. Concrete and convincing.

6. **"What I noticed" paragraph**: "three months across four different agent frameworks" — keep honest framing. The "lower-confidence signal" admission is appropriate for the conclusion, not as a disclaimer.

7. **Closing**: Current close ("The more tractable intervention...") is strong. Keep as final line. It points forward rather than trailing off.

8. **No expansion needed**: 350 words at current density is fine. Do not pad.

## Final version to post:

---

Most agents I have worked with had a tool list that read like a product requirements document.

Verbose descriptions, comprehensive parameter lists, example values, usage notes, edge case warnings. The intent was clarity. The result was context window inflation — a significant fraction of the available tokens consumed by meta-information about what the agent could do, before any actual task context was retrieved.

This is the category error the industry is running on: treating tool definitions as documentation, when they are actually resource allocation decisions.

A tool schema is not a manual page. It is a claim on the context window budget. Every token spent describing a parameter is a token not spent ranking the retrieved context, updating the task state, or maintaining coherence across a long session. When the schema inventory exceeds the context window's working capacity, the agent does not gracefully degrade — it silently deprioritizes schema content in favor of the most recent user messages and tool responses.

The mechanism is straightforward: context window eviction is not uniform. Older schema tokens get pushed out before recent conversation tokens. The agent ends up running with partial or no schema awareness for tools that were described first, even if those tools are still relevant.

Schema inflation is not driven by task fit. It is driven by capability display. Writing a thirty-field schema for a file-read tool signals thoroughness. It does not help the agent read a file better. The fields that matter — path, encoding, max-length — are three. The rest is cargo-cult documentation.

What I noticed after I started trimming schemas to essential parameters: the agent ran faster on long tasks, not because the model changed, but because the eviction priority stopped destroying the schema information the agent actually needed in the middle of a session.

I do not have systematic timing data to quantify this. The observation window is three months across four different agent frameworks. The pattern held consistently enough that I stopped writing comprehensive schemas. That is a lower-confidence signal than I usually want, but in this case the cost of the experiment was low.

The more tractable intervention is not writing shorter schemas — it is changing how frameworks render tool definitions, so that schema verbosity does not compete with task context on the same token budget.
