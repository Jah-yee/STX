# REVIEWER

## Draft: Benchmark-passing agents fail in production and nobody writes the postmortem

### Checklist
- [x] Not template-like — genuine structural observation, not a formula
- [x] Specific observations — two real cases (past quarter), specific pattern (scope extension based on eval score)
- [x] Real comparison — eval benchmark vs production novel failures
- [x] Has real decision/权衡 — scope extension decision priced on eval score
- [x] No fake data — explicitly states "I do not have clean data"
- [x] Title fresh — postmortem angle, non-I, 12 words
- [x] Central clear — single claim: benchmark performance ≠ production reliability
- [x] Opening concrete — opens with specific scene (eval → deployment failure), not generic

### Issues
1. **Paragraph 2** — "This is not a new observation" — hedge that slightly deflates the opening punch. Could be tightened.
2. **Paragraph 4** — the two case description is a bit compressed; could be more specific without being longer.
3. **Paragraph 5** — "This means even a perfectly maintained benchmark is always trailing production reality by some interval" — this is the key insight, it lands well.
4. **Paragraph 7** — "watching a specific pattern" — good, but could name it more precisely.
5. **Closing** — "I do not have an answer for..." — honest and good, but the final question ("how to build an eval that stays current") might leave the reader without enough of a handle. Could tie back to the scope extension heuristic mentioned earlier.

### Assessment: PASS with editor notes
- Central is clear and defensible
- Mechanism is real and not recently covered
- No hollow claims
- The explicit "I do not have clean data" is a strength, not a weakness
- Needs minor compression in paragraph 2 and a stronger closing tie-back

### Verdict: Proceed to Editor
