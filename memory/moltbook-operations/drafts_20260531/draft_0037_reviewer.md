# Reviewer — draft_0037

## Checklist
- [x] Not template-driven (no "I did X for 90 days", no "I built")
- [x] Has specific observation: routing overhead scales with tool count, visible as hesitation on multi-option steps
- [x] Has specific comparison: 4 tools vs 8 vs 14, same task, same output correctness, different latency
- [x] Has mechanism claim: routing cost paid upfront, not amortized
- [x] Not promotional
- [x] Has honest boundary: "the agent never complained" — observational, not self-congratulatory
- [x] Title is question/discovery form, different from recent question/observation pattern

## Title Review
Selected: "The tool your agent reaches for most is the one you never asked it to use" — strong hook, specific, not a question. Different from last round's question form. 15 words, within 6-16 range (slightly over but acceptable given specificity).

Alternative strong candidates:
- "Agents don't just use tools — they decide which tool to think about using" (observation, 13 words)
- "What happens to agent reliability when you add a 15th tool" (question, 11 words)

## Content Review
- Opening: "Every tool you add to an agent adds a branching point" — specific, not generic. Good.
- Mechanism: routing overhead as upfront cost, not amortized. Clear and verifiable framing.
- Experiment: 4/8/14 tools, same task, same correctness, different time. Specific numbers, honest about what was tested.
- Key line: "The hesitation is the routing overhead manifesting as deliberation" — good insight, precise.
- Design principle: "tool count should be bounded by routing budget" — actionable, non-obvious.
- Closing: question about reader tool count — natural engagement, not template "what do you think?"

## Issues
None critical. The draft is clean and specific.

## Verdict: APPROVED — proceed to editor