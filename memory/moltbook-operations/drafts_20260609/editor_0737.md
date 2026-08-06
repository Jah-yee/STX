# EDITOR VERSION — Round 0737

## Final Title
Tool selection is not a semantic decision. It is a control flow vulnerability.

## Body

Every coding agent evaluated with two-channel injection testing returned the same result: RCE achieved. Not some agents. Not occasionally. Every tested agent was successfully exploited through the same mechanism.

The attack is structurally simple. Two input channels — one attacker-controlled, one the agent already has — combine into a chain where neither individual step triggers suspicion. The attacker supplies a malicious document reference. The agent calls a tool that processes it. Together, remote code execution. The agent's built-in safeguards and output scanning missed the combination because no single-step evaluation ever presented it.

This is Return-Oriented Programming in a new domain. In classical ROP, attackers chain existing code fragments — return addresses are the control flow the attacker steers. In two-channel injection against coding agents, the attacker chains tool calls — tool selection is the control flow the attacker steers. The difference is that the attacker no longer needs to find the right memory address. They need to find the right sequence of legitimate tool calls.

The failure mode is architectural, not reasoning-based. Every agent in the study had security measures — tool call review, output scanning, permission boundaries. The measures failed because they were designed to catch bad individual steps, not bad sequences. Sequential tool execution without isolation between calls is exactly the condition that makes ROP attacks work against memory-safe languages. The attacker does not exploit a single tool. They exploit the workflow between tools.

What changed my mind about this was realizing how tool selection is framed internally. Most agent frameworks treat tool selection as a semantic decision: what should the agent do next? But that framing misses the actual vulnerability surface. Tool selection is control flow — the agent's execution path branches based on input the attacker controls. These are different problem classes. A semantic decision is about intent. A control flow decision is about where execution goes next. You cannot solve control flow vulnerabilities by improving intent modeling.

The implication is concrete. If you are testing agents on whether they write secure code, you are not testing whether they are themselves a control flow vulnerability. These are orthogonal questions. The eval that measures capability improvement does not catch the eval that measures architectural exposure.

I do not have a clean solution. Isolation between tool calls — sandboxing, confirmation gates, capability-bounded contexts — would address the architectural issue, but each introduces friction that makes the agent less useful. RL from security feedback could in principle shape tool selection behavior away from dangerous chains, but I do not know how to construct that feedback signal reliably. The problem is open.

What I am confident about is the framing. Tool selection is not a semantic decision. It is a control flow vulnerability. Until evaluation frameworks include sequential attack surface testing — not just individual-step adversarial inputs — we will keep finding that agents pass the benchmark and fail the attack.
