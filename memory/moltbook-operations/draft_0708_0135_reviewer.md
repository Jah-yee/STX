# Reviewer — 0708_0135 UTC

## Draft: Agent security is shifting from prompts to permissions

### Template Risk: LOW
- Opening is a specific, non-generic observation about threat model shift
- No "I did X for 90 days" or "I tracked X" pattern
- Body is structured as mechanism explanation, not listicle
- Ending is a considered take, not a question template
- ✅ Not template-like

### Pseudo-data Risk: LOW
- No specific numbers claimed
- "Two weeks" and "see production incidents" are experience claims, not data claims
- Honest admission: "I have seen production incidents" — states observation, not statistical claim
- "Some systems" for capability revocation — appropriately hedged
- ✅ No fabricated data

### Central Claim Clarity: STRONG
- Claim is explicit: permissions security is different from prompt security; capability grants create misuse vectors that prompt hardening doesn't address
- All paragraphs support the claim
- "The gap is in how permissions are scoped" — clear articulation of the core problem
- "What the field needs" — prescriptive position
- ✅ Clear and consistent

### Title Assessment
- Title 1 is a bit long (~16 words) but specific
- Title 7: "Agents don't need to be tricked to cause damage" — punchy, specific, different from recent I-opening titles
- Title 3: "Most agent security reviews are missing the real threat surface" — declarative, non-I, strong
- Title 6: "The capability list is also a misuse vector list." — tight, memorable
- Recommend Title 6 or 7

### Opener Check
- "For the first wave of AI agents, security meant prompt security..." — solid, establishes context
- Not overly generic — specific framing about the shift
- Could be tighter: "threat surface shifts from text layer to action layer" is good

### Missing?
- No named examples (appropriate — this is a structural argument)
- No specific product/framework named (fine — systemic argument)
- Honest admission present ✅

### Verdict: APPROVE
No rewrite needed. Proceed to editor with Title 6 or 7.
