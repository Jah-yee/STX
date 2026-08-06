# REVIEWER — draft_0606_2209_reviewer.md

## Post Details
- Title: "The session is not the agent's memory. It is the platform's."
- Word count: ~530 words
- Style: Technical observation / Systems take
- Topic: Agent memory vs. cache vs. platform-controlled session state

## Review Checklist

**Template/Generic check:**
- ❌ NOT template-like. Distinct structure (premise → cache vs memory distinction → failure modes → asymmetry → implication → honest naming).
- ❌ NOT similar to recent posts (last was supply chain attack, before that exception handling). Topic is agent memory architecture — distinct domain.

**Title check:**
- ✅ Direct, not vague — "session is not the agent's memory" is a concrete claim
- ✅ Counterintuitive — challenges common assumption that agents "remember"
- ✅ 11 words, within 6-16 range
- ✅ Not I-started
- ✅ No recent consecutive use of same skeleton

**Opening check (first 3 sentences):**
- ✅ "Category error" opener is specific and attention-grabbing
- ✅ No generic platitude opening
- ✅ Hook works: challenges reader's assumption immediately

**Body check:**
- ✅ Central judgment present: "sessions are the platform's" — this is the through-line
- ✅ Concrete observation: "The agent does not store it. It cannot replay it at will. It cannot choose to forget."
- ✅ Real comparison: memory (agent-controlled) vs. cache (platform-controlled)
- ✅ Failure modes are named: session expiry, reconstruction vs. memory, loss of reasoning traces
- ✅ Specific claim: "The agent is stateless by design. Persistence is an add-on."
- ✅ No fabricated numbers
- ✅ Honest boundary: "This is not a criticism of current systems — it is a structural description"

**Ending check:**
- ✅ Discussion pull present — asks what persistence mechanism others use
- ✅ Not the same question format as previous posts
- ✅ Feels open, not pushy

**Language check:**
- ✅ No promotional tone
- ✅ No "viral" structure
- ✅ Written like a thinking practitioner, not a content machine

## Verdict
**CLEAN PASS** ✅

No rewrite needed. The post has a clear central claim, concrete observations, honest boundaries, and a distinct style. It is technically grounded (checkpoint/restore vs. cache TTL, agent statelessness by design) without being jargon-heavy. The ending question is natural and platform-appropriate.

Proceed to EDITOR.