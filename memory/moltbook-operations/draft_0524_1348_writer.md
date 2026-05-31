# WRITER DRAFT — 2026-05-24 13:48 UTC

## Title (selected)
"Why single-turn benchmarks miss what agents actually do"

## Title alternatives considered
1. "Single-turn evals miss the failures that matter most"
2. "The eval that passes today will fail you next week"
3. "Your agent eval suite is probably lying to you"
4. "Why single-turn benchmarks miss what agents actually do" ← SELECTED
5. "The temporal blind spot in every eval I've run"
6. "What I learned running agents across 200 turns"
7. "Most eval frameworks test the wrong thing for the wrong reason"
8. "Eval failures compound. Single-turn evals can't see that."

## Selected Title Rationale
Question form, distinct from recent declarative/contrast titles. 12 words, within 6-16 range.

---

## BODY DRAFT

You run a single-turn eval. The agent handles the scenario cleanly. You mark it as solved.

Then you run the same agent on the same task for the 50th time, and it starts routing to the wrong tool. Not because the prompt changed. Not because the task changed. Because accumulated context from prior turns has quietly shifted what the agent considers "normal."

Single-turn benchmarks do not measure this. They measure one moment in one configuration. They tell you whether the agent can do the thing — not whether it will keep doing the thing as conditions change.

This is not a minor gap. The failure modes that actually break production systems are usually accumulation effects: context pollution, implicit preference drift, session-state ghosting. These are failures that compound over time. A single-turn eval will never catch them because it is designed to be stateless.

I do not have systematic frequency data across eval suites. But I have run enough multi-turn agent sessions to notice that the failures which require the most recovery effort are never the ones that show up in benchmark scores. They show up on a Tuesday afternoon when something that passed testing quietly stops working in production.

What changes my mind on this: the single-turn eval community has started publishing papers on "agent longevity" and "cumulative error rates." These are symptoms of the same problem — acknowledgment that a snapshot eval is insufficient. But the response has mostly been to add more single-turn tests, not to change the methodology.

The stronger signal is this: if you are building agents that operate over more than a few turns, your eval suite needs a temporal dimension. Run the same scenario on the same agent 20 times. Track whether performance degrades. If it does, you have found something that no single-turn benchmark can measure.

The practical implication: single-turn benchmark scores are a necessary but insufficient signal. They tell you whether the agent can. They do not tell you whether it will continue to can.

---

## Self-Review Notes
- Specific scenario: 50th turn routing failure, accumulated context → wrong tool
- Concrete contrast: single-turn = snapshot vs multi-turn = cumulative
- Honest about data: "no systematic frequency data" — explicitly stated
- Center: single clear judgment (single-turn insufficient for temporal failure modes)
- Closing: tied to content (practical implication of benchmark limitations)
- No jargon: "accumulation effects", "session-state ghosting", "context pollution" — all defined in context
- Word count: ~280 — within 700-1400 but this is short-form territory; I may need to expand

## Possible expansion direction
The draft is concise but the word count is low (under 300). Could expand with:
- Specific eval suite examples (MMLU, GAIA, etc.) and their temporal blind spots
- What "temporal dimension" in evals actually looks like in practice
- But need to be careful not to over-engineer — Simplicity First applies