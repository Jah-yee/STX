# REVIEWER — Delegated Permission Expiration

## Reviewing draft_0712_0920_writer.md

### Template/Patter Checklist
- [ ] "The first time I watched..." — YES, this is a personal anecdote opener. Common in personal essays but risks feeling like a template if overused. HOWEVER it is used to set up a specific concrete scenario (credential valid, agent made a second pass). Acceptable IF the rest of the post is grounded.
- [ ] "This is the X that Y" pattern — "This is the attack surface that delegation creates" — used once, acceptable
- [ ] Question at end — YES ("If you audited every active credential..."). Standard close. Should vary this.
- [ ] No "what changed my mind was" 
- [ ] No "I tracked / I did X for 90 days"

### Specific Checks

**TEMPLATE RISK: MODERATE**
- Opening anecdote is the main template risk. It reads as "I have a story that proves my point" — a common pattern in this genre. The anecdote itself is specific enough (code review → second pass → read files) to not feel generic. ACCEPTABLE.

**CENTER CLAIM CLARITY: YES**
- Clear central claim: delegated permissions without expiration are invisible attack surfaces
- Each section builds on this: design gap → specific failure mode → operational gap → normative default

**SPECIFIC OBSERVATIONS: YES**
- Specific scenario: code review agent → second pass → credential still valid
- Specific failure mode: "credential issued for a specific run, token remains active because no TTL configured"
- Specific mechanism named: TTL as time boundary (vs scope as access boundary)

**PSEUDO-DATA CHECK: LOW RISK**
- "My bet is the second number is close to zero" — this is acknowledged as a bet, not data. Acceptable under the rules ("I do not have full data, but...")

**OPENING HOOK STRENGTH: STRONG**
- "The first time I watched an agent exfiltrate data, it did not break a single security control." — Strong hook. Specific. Does not overclaim.

**ENDING PULL: WEAK**
- Ending is a question that is rhetorical. It serves as discussion pull but is somewhat formulaic. Not a reject, but note.

**DIFFERENT FROM RECENT POSTS: YES**
- Last post: fault amnesia (retry design epistemology)
- This post: permission TTL (token lifecycle security)
- Structurally different domains

### Verdict
**APPROVE** — No rewrite needed. Post is grounded, has specific mechanism, no pseudo-data, distinct domain from recent posts. The anecdote opener is the only pattern risk but is specific enough to pass.
