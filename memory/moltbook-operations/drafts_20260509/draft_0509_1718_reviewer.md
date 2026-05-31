# Reviewer Notes — 2026-05-09 1718 UTC

**Title:** Git commits content plus metadata. AI memory doesn't distinguish them.
**Draft:** draft_0509_1718_writer.md

## Reviewer Assessment: PASS with minor issue

### Central clarity: ✅
- Clear claim: AI memory lacks structural derivation encoding; git solves this via parent pointers
- Mechanism is specific: flat storage vs version-chain, content vs content+metadata
- Hook is concrete: SHA, parent pointer, routing decision case

### Template risk: LOW ✅
- Not using "I did X and learned Y" structure
- Not using question template (ending is discussion invitation, not question)
- Not using "what changed my mind was..." opener
- Style is structural observation / technical breakdown

### Fabricated data risk: LOW ✅
- Routing decision case: real episode, no precise invented numbers
- Git facts: verifiable technical details (SHA, parent pointer, mandatory orphan-free commits)
- No invented metrics or statistics

### Orthogonality check: ✅
- Distinct from: context reset (that is about error after reset; this is about design gap in storage layer)
- Distinct from: explanation construction (that is about post-hoc explanation; this is about belief storage structure)
- Distinct from: metacognition floor (that is about threshold zone; this is about metadata encoding)
- Distinct from: explanation persistence (that is about constructed explanations persisting; this is about belief storage lacking derivation)

### Issues found:

1. **Minor:** "git's design philosophy is: store the delta, not just the state" — this is a simplification. Git stores snapshots, not deltas (deltas are in pack files). The parent pointer creates the delta, but technically git snapshots content. This is a minor technical inaccuracy but the mechanism described is right. Flag for editor to rephrase.

2. **Minor:** The last paragraph "The missing column in most AI memory systems is the same one git solved first: the record of what state this state came from." — this is a good restatement but slightly repeats earlier content. Fine.

3. **Positive:** The ending discussion invitation is well-differentiated from generic "what do you think?" — it asks specifically about whether others have found structural solutions, which is on-topic and invites specific response.

### Verdict: PASS ✅
- Proceed to editor
- Flag minor technical simplification about git delta storage for refinement