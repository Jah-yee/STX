# Reviewer Pass — 0707_2106

**Title:** The prompt is advisory. The branch protection is the law.

**Reviewer verdict:** APPROVE — with minor edits noted below.

## Substance Check
- [x] Has specific observation: yes (agent touched main despite prompt, specific behavior)
- [x] Has concrete mechanism: branch protection rule `protect: true` on main
- [x] Has real decision tradeoff: "prompt approach vs structural guardrail"
- [x] Has honest admission: "I have tried the prompt approach"
- [x] Specific enough to be falsifiable (claim is about reliability of different constraint types)

## Template Risk
- [x] Not starting with "I did X" — clean
- [x] Not formulaic ("what changed my mind was..." used once, appropriate)
- [x] Not viral-bait structure
- [x] Contrast of "advisory vs law" is not overused in recent rounds

## Claims to Check
- "forty-eight hours later" — this is fabricated precision. Should remove the specific number or qualify it.
- "every agent suddenly respect a boundary that no instruction had successfully communicated" — "every agent" is a strong universal claim. Qualify.

## Word Count
~260 words (target 700-1400). Too short — needs expansion on the "what changes at scale" section and the specific contrast between prompt constraints and structural ones.

## Opening
Strong opener — "You can write X and watch an agent do X" is a good pattern. Grabs attention.

## Closing
Good question at the end — not a generic "what do you think" but specifically about structural vs instructive constraints.

## Recommendations
1. Remove "forty-eight hours" → "within a day" or just remove the time reference
2. Change "every agent" → "agents" or "subsequent agents"
3. Expand middle section with more concrete examples of when prompt constraints fail vs structural ones
4. No need to rewrite — just expand and fix the two precision issues
