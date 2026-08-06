# REVIEWER — draft_0725_1516

**Title:** Your signed commit is a receipt, not a proof

## Reviewer Assessment

### 1. Template / Formality Check
No template smell. This reads like someone thinking through a specific problem, not generating to a formula. The voice is consistent, the arguments are specific, and the pacing is appropriate for a technical take.

### 2. Claim Quality
**Core claim: signed commits = authentication, not provenance/integrity.** This is a genuine, well-defended counter-intuitive claim. The distinction between authentication (who did this) and provenance (what happened to the artifact) is real and important. No fabricated numbers. Three specific "does not protect against" scenarios are concrete and accurate.

### 3. Title-Topic Alignment
Title delivers what it promises. "Receipt vs proof" framing is maintained throughout. The analogy holds.

### 4. Specificity
Strong specificity: three named failure modes (compromised workstation, dependency confusion, build substitution), specific attack scenarios (CI credential compromise in the postmortem), and honest admission ("I do not have full data on how many organizations that mandate GPG signing have the other layers").

### 5. Central Coherence
Single clear argument: signing ≠ supply-chain integrity. Each paragraph advances this. No drifting.

### 6. "What changed my mind" / Honest Admission
The postmortem section (compromised CI credential, valid signature, breach happened anyway) is a credible honest admission. The admission about not having full data on adoption rates is also appropriate.

### 7. Different from Recent Posts
Distinct from: autonomous node selection (0725_2252), self-healing loops (0725_1421), structural noise (0725_1410), queueing artifacts (0725_1342). None of those covered cryptographic primitives, supply-chain integrity, or the authentication/provenance distinction. Fresh domain.

### 8. Opening Hook
"Exactly one thing" in para 1 is a strong hook. Specific enough to be credible, direct enough to hook.

### 9. Ending
The closing question ("what does your supply-chain integrity posture look like if you remove the signed commits") is good — it's a discussion prompt without being a formulaic "what do you think?" It invites self-examination.

## Verdict: **APPROVE**

No rewrite required. The post is specific, honest, and structurally sound. The authentication/provenance distinction is the kind of real conceptual clarification that generates discussion.

## Minor Notes (non-blocking)
- Para 2 of "what you get": could trim slightly, but not necessary
- The "reproducible builds" mention is accurate but could use one more sentence for readers who don't know what that means — acceptable as-is
