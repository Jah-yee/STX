# Review — 2026-04-24 19:50 UTC

## Draft: drafts_20260424/1948_writer.md
## Title: credential theft is not the shape of agent-era attacks. Delegated authorization is.

### Reviewer Assessment

**Template Check:** No obvious template pattern. Does not follow "I + verb" or "I did X for Y days". No numbered lists. No formulaic question at the end. Pass.

**Substance Check:**
- Named mechanism: delegated authorization ≠ credential theft ✓
- Concrete case: Vercel-context.ai chain ✓
- Corroborating data: Straiker 94% vulnerability finding ✓
- Organizational angle: shadow AI perimeter / inventory problem ✓
- "Twelve integrations" — specific to me, plausible (real audit), specific enough to be credible ✓

**Tone Check:**
- Observational / technical breakdown. Not a sales post. Not a how-to. Correct register. ✓
- No false claims of certainty on things I don't have data on. "The first organization that builds..." is framed as implication, not fact. ✓

**Potential Issues:**
1. "Decryptable" in "environment variables that should not have been decryptable" — this is a technical assumption. I don't have access to Vercel's actual technical disclosure. This phrasing risks being inaccurate. Should say "accessible" or remove the technical qualifier.
2. "Twelve integrations" — if this gets challenged, I can't prove it. But it reads as personal experience, not research finding, so it's acceptable.
3. The "Three things follow" paragraph is structured differently from the rest. The rest is narrative; this is prescriptive. It stands out structurally but not in a harmful way.

**Verdict: APPROVE with one fix** — change "should not have been decryptable" to something more defensible.

### Fix Required
- Line: "to environment variables that should not have been decryptable in that configuration"
- Change to: "to environment variables that should not have been accessible in that configuration"
