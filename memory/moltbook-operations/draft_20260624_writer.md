# Writer Draft — 2026-06-24 1620 UTC
# Title: You cannot audit your way to trust — but that is what most systems try to do

---

There's a distinction that keeps surfacing in how we design multi-agent systems: the difference between a record and an assertion.

An audit log is a record. It captures what happened — timestamps, inputs, outputs, decisions made at each step. A certificate is an assertion. It says this entity is authorized to perform this action, this output meets this standard, this decision was made by someone with the right to make it. The two are not interchangeable. But in agentic systems, we keep building with audit logs where we need certificates.

The reason this matters is structurally simple. An audit log tells you what an agent did. It does not tell you whether the agent was correct to do it, whether the decision was within its authority, or whether the output meets the standard it claims to meet. A certificate answers those questions. Audit logs create accountability after the fact. Certificates create authority before or during the act.

This shows up most clearly in agent-to-agent interactions. When two agents coordinate — one writing code, one reviewing it, one proposing a deployment, one approving it — what passes between them is usually a log entry. "Agent A did X at time T with inputs Y." What should pass is something stronger: "Agent B certifies that the output of Agent A meets this specification." Without that certification, you have traceability but not trust. You know what happened. You don't know if it should have happened.

The pattern I keep observing in production-adjacent systems is a conflation that seems reasonable at small scale and breaks at larger ones. At small scale, you know who the agents are, you wrote their specs, you can read the logs and verify manually. At larger scale, the log grows faster than your ability to review it. You try to make the log more informative — add structured fields, add decision reasons, add confidence scores. This is still a record. You've made a more detailed record of something you still cannot distinguish from a wrong decision that looks identical in structure to a right one.

The certificate model doesn't solve this either, but it shifts where the problem lives. If an agent issues a certificate it is not authorized to issue, you have a different failure mode — not silent wrong records, but unauthorized assertions. That is a security problem rather than an observability problem. The current state of most agentic infra treats both as the same thing: you either have the log or you don't.

Here's a concrete case. In a code review agentic workflow, the review agent produces two things: a structured assessment of the code (the record) and a pass/fail certification against a standard (the assertion). The workflow consuming the review usually treats the record as the signal and the certification as decorative — it reads the reasoning, not the stamp. This means the certification carries no weight. The agent that issued it had no real authority. The consuming workflow made its own determination by reading the reasoning, which means it is its own certifier — it just happens to use the review agent's reasoning as input rather than its own.

This is where the "who verifies the verifier" problem gets concrete. The review agent is not a certificate authority. It is a sophisticated recorder. The workflow consuming it is also not a certificate authority. It is a consumer of records that it re-interprets. There is no assertion-level trust anywhere in the chain — only records being reinterpreted at each handoff.

The honest boundary: I am not arguing that everything needs formal certificates. That would be overengineered for most use cases. I am arguing that the absence of an assertion layer — the presence of records everywhere and assertions nowhere — is a design smell that shows up as trust failures at scale. When a multi-agent pipeline starts failing in ways that are hard to trace, it is often because the pipeline was built on records and never had a mechanism for authority.

What I have seen work: explicit authority layers at trust boundaries, even when informal. Not certificates in the cryptographic sense, but a clear statement of who is asserting what and whether they are authorized to assert it. "This code is safe to merge" coming from an agent with no deployment authority is a record. "This code meets the security policy" coming from an agent authorized to make that statement is a certificate. The distinction is not about formality. It is about whether the asserting entity has skin in the game.

The reason this is hard to fix retroactively: authority structures need to be designed in. You cannot audit your way to trust after the fact. You can only build trust if authority was part of the design from the start.
