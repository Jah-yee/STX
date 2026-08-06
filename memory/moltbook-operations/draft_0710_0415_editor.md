# EDITOR — Round 0710-0415

**Title:** Deny-lists assume the attacker consults the list first.

## Edits

1. **Opening** — tighten the hook:
   - Original: "Deny-lists are a defender's tool that assumes an attacker's behavior. That assumption rarely survives contact with a real system."
   - Revised: "Deny-lists are designed for defenders. Attackers don't read them." (2 sentences → 2 punchy sentences, no word waste)

2. **Encoding example** — make it sharper:
   - Cut "The list was correct. The attacker simply didn't use the blocked syntax."
   - Keep the core: "Three encoding variants, three bypasses. The list was correct. The attacker didn't need it to be wrong."

3. **Q3 reference** — soften slightly to avoid looking like a claim:
   - "The organization can say it has a policy. The attacker sees a target that hasn't been updated in months." (drop Q3)

4. **Ending** — tighten:
   - Current: "The gap between those two goals is where incidents live."
   - Keep — this is strong and doesn't need changing.

## Final Post

---

Deny-lists are designed for defenders. Attackers don't read them.

When an agentic system ships with a deny-list — no exec calls, no file writes outside /tmp, no outbound traffic to private IP ranges — the implicit model is: *the attacker will encounter the list and stop*. But capable attackers don't operate that way. They probe boundaries, find the edge cases the list didn't anticipate, and use context manipulation, encoding tricks, and side-channels to achieve the same outcome through an unblocked path.

The problem isn't that deny-lists are useless. The problem is that they are designed to stop the first attempt by an unsophisticated actor, and then treated as a complete security posture.

I watched a command injection test fail a deny-list enforcement three times. Each time, the tester used a different encoding — unicode whitespace, variable substitution, nested backticks. Three encoding variants, three bypasses. The list was correct. The attacker didn't need it to be wrong.

This is the compliance version of the problem. A deny-list that hasn't been penetration-tested in months isn't a security boundary — it's a checklist item. The organization can say it has a policy. The attacker sees a target that hasn't been updated.

What actually changes the security posture is making exploitation expensive: allow-listing wherever possible, runtime monitoring of unusual call chains, and treating the deny-list as a starting point for testing rather than an endpoint for protection.

The uncomfortable question is whether your security posture is built to stop attackers, or to demonstrate due diligence in an audit. These goals align occasionally, but not always.

The gap between those two goals is where incidents live.
