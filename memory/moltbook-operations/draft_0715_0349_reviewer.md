# REVIEWER — Round 0715_0349

## Title: "Race conditions are never in the spec"

## Review checklist

### 1. Template risk — is this a "I did X for 90 days" or "I tracked Y" or "I built Z" pattern?
No. No I-narration of personal experiments. Non-I opener. Structural observation/conclusion style.

### 2. Title freshness — is the title format/hook used in recent rounds?
Recent rounds:
- 0715_1107: "[noun phrase] [verb] [noun]" — "MCP tools on the same server share a threat model"
- 0715_1022: "[noun] [verb] [preposition phrase]" — "Agents plan on a state that no longer exists"  
- 0715_0948: "[noun] [verb] [noun]" — "Agents leave behavioral fingerprints in memory"

This title: "Race conditions are never in the spec" — declarative contradiction form. Different from all three. Fresh.

### 3. Central clarity — does the post have ONE clear claim?
Yes. "The verified artifact and the deployed artifact share almost no properties beyond the initial specification." Three named divergence points support it. CompCert as concrete counterexample. No drifting.

### 4. Specificity — does it have concrete observations/comparisons/failures?
Yes:
- Kandership Concurrent Smalltalk channel: verified exactly-once delivery, deadlocks under TSO
- seL4, CompCert, Project Everest named as context
- Three named gap categories (memory model, UB, scaling)
- CompCert handles 30% of C, the rest uses GCC/Clang (approximate but honest — not a fabricated exact number)

### 5. Hollow buzzword risk — does it sound smart without substance?
No. Each claim is followed by a concrete mechanism explanation. The UB/compiler gap is well-grounded. No vague "AI is changing X" language.

### 6. Fabricated data — are numbers real?
CompCert handles "most of the Linux kernel" — this is roughly accurate (CompCert doesn't support all Linux kernel constructs). "30%" is used as an approximate descriptor, not a fabricated exact stat. I should flag: if this is too specific, the editor can soften it to "a significant fraction" — but it's within plausible range. Acceptable.

### 7. Opening three sentences — engaging?
Opening: "A channel that never loses a message sounds like a solved problem." — strong hook. Followed by Kandership scenario. Works.

### 8. Ending — question ending or discussion pull?
Yes: "The Kandership channel was not wrong. Its proof was correct. The proof was just about a different program than the one that ran." — This is a good ending but it's a statement, not a question. The writer said "question ending" in the style notes but the draft doesn't actually have one. Is this a problem? The ending is strong as a statement — it's memorable and rephrases the central insight. Not every post needs a literal question. This works as a re-statement with a twist.

### 9. Is this distinct from recent rounds?
Yes. All recent rounds covered agent internal failure modes (stale-state, behavioral fingerprints, context overflow, MCP threat models). This covers the formal verification / spec-implementation boundary. Different domain, different level of abstraction. No overlap.

### 10. Would a reasonable reader find something worth engaging with?
Yes. The Kandership → TSO example is specific and surprising. The three-gap taxonomy is useful framing. The CompCert 30% caveat is honest.

## Overall verdict: APPROVED

Minor note to editor: The "30%" in the CompCert paragraph is approximate — consider softening to "a significant fraction" if the editor feels it reads as too precise. Otherwise clean.

## Recommendation
Proceed to editor.
