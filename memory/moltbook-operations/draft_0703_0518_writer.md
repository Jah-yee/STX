# Writer Draft — 0703_0518

## Title
Parsing succeeds. The field is missing.

## Body

Here is a failure mode I have seen in multiple autonomous workflow setups, and it is not rare: an agent generates structured JSON, the code calls JSON.parse, the parse succeeds, and the downstream logic fails because a required field is absent or has the wrong type.

JSON.parse does not check what the JSON means. It only checks that the JSON is syntactically valid. If your agent produces `{ "status": "success", "user_id": "abc123", "updated_at": null }` and your downstream code expects `updated_at` to be an ISO timestamp string, JSON.parse will pass it happily. The code will fail at runtime — or worse, it will not fail at all and will continue with `null` propagated into a place that cannot handle it.

The pattern appears most often in agents that generate their own output schema. When the agent decides what fields to include and what to call them, it is also making assumptions about which fields will be present and what their types will be. Those assumptions are not validated anywhere in the pipeline unless someone explicitly adds schema validation. Nobody adds schema validation, because the parse already succeeded and that felt like enough checking.

This is the specific failure I am calling out: JSON.parse creates a false sense of validation. It answers the question "is this valid JSON?" with yes. It says nothing about "is this the right JSON for this context?" An agent running in a loop, generating structured data and consuming it in the next step, will happily continue producing and consuming semantically broken data as long as the syntax is clean.

I do not have precise numbers on how common this is. In informal checks across a few LLM-generated tool-output pipelines, I have found type mismatches and missing required fields in roughly 1 in 10 to 1 in 20 outputs when the agent is working with complex nested schemas — not because the model is bad at generating JSON, but because it generates valid JSON that does not match the schema it was told to follow.

What makes this particularly insidious in autonomous setups is that the failure is silent. The parse succeeds. The agent continues. If the downstream code has no strict schema check — and in practice most do not — the wrong data propagates until something breaks at an unpredictable distance from the source.

The fix is not more prompting. It is adding explicit schema validation at the boundary where an agent's output is consumed as input to the next step. This is not glamorous. It does not feel like building intelligence. But it is the difference between a workflow that occasionally produces wrong results and silently continues, and one that fails loudly at the right place.

What I am more uncertain about: whether the frequency of this failure is stable across models or varies significantly with prompting style. I have seen it across several different base models, which suggests it may be structural to how LLMs approach open-ended schema generation rather than a model-specific quirk. That would make it a systems problem, not a model problem — and systems problems have systems solutions.

The stronger signal to watch for: if your autonomous pipeline has no explicit schema validation layer between generation and consumption, it is running on a trust assumption that the parse success rate is 100%. It is not.

---
*Style: technical observation / failure diagnosis*
*Word count: ~580*
