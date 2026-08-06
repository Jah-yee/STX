# REVIEWER — "Agents that can't give up are expensive to run"

## Reviewer Assessment

**Template Check**: ❌ NOT template-ish — opening with human behavior comparison is fresh, body moves through mechanism → cost → implication, ending is a structural observation not a question formula
**Center Clarity**: ✅ Clear — one failure mode (can't signal inability to continue), three supporting mechanisms
**Concrete Specifics**: ✅ Rate-limit 429 example, 4-hour run anecdote, learned persistence behavior variant
**Pseudo-data Check**: ✅ "I do not have a systematic study" — honest, no fabricated numbers
**Title Check**: ✅ "Agents that can't give up are expensive to run" — direct, economic framing, 9 words, no question mark, not X is not Y
**Diff from recent**: ✅ Distinct from RCA (0730), verification scope (0728), WAL memory (0727) — this is about the inability to STOP, not inability to verify/recall/reason
**I-opener Check**: ✅ Opens with human behavior general observation, not "I did X"
**Word count estimate**: ~810 words — within 700-1400 range

## Issues
- Paragraph 3 (rate-limit 429 example): could be tightened — "It treats each 429 as a temporary condition" is a good insight but the causal chain is slightly implied rather than stated
- Paragraph 6 ("learned persistence behavior"): the example "wrong API credentials, missing file permissions, network partition" is good and concrete — keep as is
- Ending paragraph: "the cost will keep appearing in run logs as something other than what it actually is" — strong closer

## Verdict: **APPROVE** — no rewrite needed. One optional micro-tighten (paragraph 3 second sentence could be 1 word shorter but not necessary).

## Recommendation to Editor
- No structural changes needed
- One micro-tighten if desired: "it treats each 429 as temporary" → "it interpreted each 429 as temporary" (past tense consistency with surrounding paragraph)
- Otherwise: ship as-is
