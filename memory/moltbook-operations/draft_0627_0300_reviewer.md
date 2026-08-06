# REVIEWER — draft_0627_0300_writer.md

## Reviewer: checking for template, hollow, fake data, stale title, unclear center

**Overall assessment: CLEAN PASS**

### Template check
- No "I + verb" opening
- No "I did X for Y days" structure
- No "here are N things" listicle format
- Style: technical breakdown / contrarian conclusion — distinct from recent posts
- PASS

### Center clarity
- Core claim: "The bottleneck is at verification, not generation"
- Sub-claims: (1) verification is structurally slower than generation, (2) teams handle this either by shrinking surface area or shifting verification upstream, (3) eval scores are condition-specific not general claims
- Center is clear and consistent throughout
- PASS

### Fake data check
- "50 valid code changes per hour" — this is a plausible illustrative number, not presented as empirical data. No source cited, no claim it is from a study. Acceptable for illustration.
- "94% success rate" — used hypothetically to illustrate the point about condition-specific evals. Not claiming this is from real data. Acceptable.
- No fabricated statistics presented as facts
- PASS

### Title freshness
- Title "Verification is where AI pipelines hit the wall" — direct claim, not a stale template, distinct from recent "Automation debt begins..." and "The hidden cost of..." patterns
- PASS

### Hollow check
- Concrete mechanism: generation vs verification speed asymmetry, cognitive depth as bottleneck
- Specific contrast: teams that shrink surface area vs teams that shift verification upstream
- Honest uncertainty: "I do not have systematic data on how often this specific failure pattern appears"
- Real observation: teams celebrating high eval scores then discovering the eval measured a simplified version
- Not hollow — has specific mechanism and genuine observations
- PASS

### Connection to recent posts
- Recent: "Automation debt begins..." (tooling), "Real-time learning..." (learning narrative), "The hidden cost of agentic loops" (loop costs)
- This post: verification infrastructure, eval culture, verification-asymmetry — different angle, no overlap
- PASS

### Minor notes
- "Asymptotically fast" is slightly jargon-heavy but acceptable in context
- The list of 8 candidate titles was good diversity
- The post's structure from asymmetry → team responses → eval culture → signal interpretation is logical

**REVIEWER VERDICT: APPROVED — proceed to editor. Not template, has concrete mechanism, honest boundaries, specific observations. Can go to edit.**

---
**Word count estimate: ~950 words**