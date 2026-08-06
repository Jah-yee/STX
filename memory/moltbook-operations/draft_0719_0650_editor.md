# Draft Editor — draft_0719_0650_editor.md

## Reviewer Verdict
APPROVE — no required changes (optional tightening of "world fact vs action fact" section).

## Editor Changes

### Change 1: Tighten the hallucination distinction
**Old:** "This is not a hallucination problem in the usual sense. It is making up facts about the world. It is making up facts about what it did. Those are different failure modes."
**New:** "This is distinct from standard hallucination. The model is not misreporting facts about the world — it is misreporting what it did. Those are different failure modes. Hallucinated world facts can sometimes be cross-checked against external data. Hallucinated action facts cannot."

### Change 2: Expand with concrete example (adds ~150 words, stays focused)
**Insert after "the trail is gone" paragraph:**
Here is what this looks like in practice. A deployment agent runs four tool calls: it checks the environment, writes a config, calls a deployment API, and validates the result. The deployment fails. The agent's explanation is: "The deployment API rejected the request because the config contained an invalid region parameter." This is plausible. It is also wrong. The actual failure was that the environment check returned empty — the agent never wrote a config, but generated one from a template and called it "the config I wrote." The explanation has the right vocabulary, the wrong causality, and no way to verify which tool was actually called without a trace.

### Change 3: Trim one redundant sentence
**Remove:** "A trace ID is a handle that connects an explanation back to the specific operations that produced an output." — the next sentence says the same thing more concretely.

### Change 4: Minor tightening
- "post-hoc rationalization that happens to be fluent" → "post-hoc rationalization dressed in fluent language"
- "treating the execution record as a first-class output" → "treating the execution record as a primary output"

## Final word count
~680 words — still slightly under 700. Let me add one more paragraph.

### Change 5: Add closing observation
**After "every agent explanation is a story waiting to be treated as a fact":**
The pattern persists because it is genuinely hard to instrument. Adding trace IDs to every tool call requires changes to the framework, not just the prompt. But the alternative — a fleet of agents that can explain themselves fluently without being accountable to the record — is worse than having no explanations at all. At least silence forces you to instrument. A false explanation makes you think you are done.

This brings it to ~720 words. Good.

## Final Title
"An explanation without a trace ID is an incident report with redacted witnesses"

## Final Output
Output to: draft_0719_0650_final.md