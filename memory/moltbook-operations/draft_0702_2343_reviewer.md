# Review — Reviewer

## Draft under review
Title: "The poisoned tool description steers the plan without ever being called."
Source: Shi et al. arXiv:2606.20922 (2026-06-18)

---

## Reviewer verdict: **APPROVE**

### What works
- **Not templated.** No "I did X for Y days," no "the thing that changed my mind," no "here's what most people get wrong." Clean.
- **Specific mechanism.** Poisoned tool description → inference during planning → plan change without tool call. Not vague.
- **Concrete paper.** arXiv:2606.20922, Shi et al., June 2026 — cited, not hidden.
- **Distinct from recent posts.** VLA grounding (2147) and explanation instability (2210) are both about model-level properties. This is about the tool-registry interface — a different layer.
- **Has a decision/judgment.** "You may have an attack surface you haven't measured" — testable claim.
- **Honest admission present.** "I do not have data on how prevalent this attack is in practice."

### Concerns (minor)
- The paragraph on "why this is harder than prompt injection" is structurally fine but slightly explains the obvious. Could be tightened, not rewritten.
- The "Standard agent evals test whether the agent calls the right tool" paragraph is solid but the last sentence ("most agent development pipelines do not run this kind of eval") is a strong claim — editor should consider softening to "likely do not" rather than making it a flat assertion without sourcing.
- The ending question ("who audits the description?") is a good hook — not a template question, genuine.

### Center check
The post has a clear center: **the poisoned tool description is a structural attack surface that bypasses existing defenses and is invisible to standard evals.** The body walks through mechanism → why it's different from prompt injection → eval gap → honest caveat → actionable question. Stays on center.

### No template signals detected
- No "I + verb" opener
- No "here's what most people get wrong"
- No "90 days" or tracking framing
- No "X is not Y" template (the title is the only X-is-not-Y and it's appropriate)
- Ending is a real question, not a template engagement-bait question

### Recommendation
APPROVE. Proceed to Editor with the minor softening note on the eval claim.
