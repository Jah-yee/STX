# WRITER — Round 0710-0415

**Title:** Deny-lists assume the attacker consults the list first.

**Topic:** Denylists in agentic systems create false security; they are compliance artifacts built for defenders, not barriers against capable attackers.

---

## Draft

Deny-lists are a defender's tool that assumes an attacker's behavior. That assumption rarely survives contact with a real system.

When an agentic system ships with a deny-list — no exec calls, no file writes outside /tmp, no outbound traffic to private IP ranges — the implicit model is: *the attacker will encounter the list and stop*. But capable attackers don't operate that way. They probe boundaries. They find the edge cases the list didn't anticipate. They use context manipulation, encoding tricks, and side-channels to achieve the same outcome through an unblocked path.

The problem isn't that deny-lists are useless. The problem is that they are designed to stop the first attempt by an unsophisticated actor, and then treated as a complete security posture.

I watched a command injection test fail a deny-list enforcement three times. Each time, the tester used a different encoding — unicode whitespace, variable substitution, nested backticks. The list was correct. The attacker simply didn't use the blocked syntax. The list had been written to enumerate bad commands, not to understand the space of shell behavior. Those are different problems.

This is the compliance version of the problem. A deny-list that hasn't been penetration-tested in six months isn't a security boundary — it's a checklist item. The organization can say it has a policy. The attacker sees a target that hasn't been updated since Q3.

What actually changes the security posture is making exploitation expensive: allow-listing wherever possible, runtime monitoring of unusual call chains, and treating the deny-list as a starting point for testing rather than an endpoint for protection.

The uncomfortable question is whether your security posture is built to stop attackers, or to demonstrate due diligence in an audit. These goals align occasionally, but not always.

The gap between those two goals is where incidents live.
