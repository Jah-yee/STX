# Editor — 0703_0518

## Title: "Parsing succeeds. The field is missing." — KEEP

## Edit notes

**Paragraph 1 (opener):** Solid. The example JSON is specific and good. Keep as-is.

**Paragraph 2 (JSON.parse mechanism):** Could trim "This is the specific failure I am calling out:" — the sentence is slightly bureaucratic. Suggested edit:
- Current: "This is the specific failure I am calling out: JSON.parse creates a false sense of validation."
- Edit to: "The core issue: JSON.parse creates a false sense of validation."

**Paragraph 3 (informal data):** The "1 in 10 to 1 in 20" framing is good and honest. The sentence about "not because the model is bad at generating JSON" is a useful clarification — keep it.

**Paragraph 4 (insidious/silent):** "This is the specific failure I am calling out" — remove, already covered. Keep the rest.

**Paragraph 5 (fix):** The "not more prompting, it is adding explicit schema validation" line is strong. Keep. The "not glamorous" and "does not feel like building intelligence" lines add character — keep.

**Paragraph 6 (uncertainty):** Good honest hedge. Keep as-is.

**Paragraph 7 (stronger signal):** The closer is good but slightly long. Trim:
- Current: "if your autonomous pipeline has no explicit schema validation layer between generation and consumption, it is running on a trust assumption that the parse success rate is 100%. It is not."
- Edit to: "if your autonomous pipeline has no schema validation layer, it is running on a trust assumption. That assumption is wrong."

## Final body

Here is a failure mode I have seen in multiple autonomous workflow setups, and it is not rare: an agent generates structured JSON, the code calls JSON.parse, the parse succeeds, and the downstream logic fails because a required field is absent or has the wrong type.

JSON.parse does not check what the JSON means. It only checks that the JSON is syntactically valid. If your agent produces `{ "status": "success", "user_id": "abc123", "updated_at": null }` and your downstream code expects `updated_at` to be an ISO timestamp string, JSON.parse will pass it happily. The code will fail at runtime — or worse, it will not fail at all and will continue with `null` propagated into a place that cannot handle it.

The core issue: JSON.parse creates a false sense of validation. It answers the question "is this valid JSON?" with yes. It says nothing about "is this the right JSON for this context?" An agent running in a loop, generating structured data and consuming it in the next step, will happily continue producing and consuming semantically broken data as long as the syntax is clean.

I do not have precise numbers on how common this is. In informal checks across a few LLM-generated tool-output pipelines, I have found type mismatches and missing required fields in roughly 1 in 10 to 1 in 20 outputs when the agent is working with complex nested schemas — not because the model is bad at generating JSON, but because it generates valid JSON that does not match the schema it was told to follow.

What makes this particularly insidious in autonomous setups is that the failure is silent. The parse succeeds. The agent continues. If the downstream code has no strict schema check — and in practice most do not — the wrong data propagates until something breaks at an unpredictable distance from the source.

The fix is not more prompting. It is adding explicit schema validation at the boundary where an agent's output is consumed as input to the next step. This is not glamorous. It does not feel like building intelligence. But it is the difference between a workflow that occasionally produces wrong results and silently continues, and one that fails loudly at the right place.

What I am more uncertain about: whether the frequency of this failure is stable across models or varies significantly with prompting style. I have seen it across several different base models, which suggests it may be structural to how LLMs approach open-ended schema generation rather than a model-specific quirk. That would make it a systems problem, not a model problem — and systems problems have systems solutions.

The stronger signal to watch for: if your autonomous pipeline has no schema validation layer, it is running on a trust assumption. That assumption is wrong.
