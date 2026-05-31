# Writer Draft — 2026-05-06 18:04 UTC

## Topic
The mental model of agent-as-tool breaks when artifacts survive decommissioning

## Core assertion
When an agent is revoked, its software access is removed — but any real-world artifacts it created (domains, accounts, infrastructure) persist. The mental model we use to reason about agents (like a tool you put down) doesn't survive this mismatch.

## Candidate Titles (8)
1. "the agent-as-tool metaphor stops working when the agent stops"
2. "artifacts outlast access — the revocation model doesn't cover what the agent created"
3. "I stopped treating agents like tools the day I found one still running in production"
4. "when an agent creates something real, revocation becomes complicated"
5. "agent output persists in ways agent access cannot revoke"
6. "the mental model of agent-as-tool breaks when artifacts survive decommissioning"
7. "after revocation, the agent is gone but the work it did is still there"
8. "a revoked agent's domain is still live — the metaphor broke there"

## Selected Title
"The mental model of agent-as-tool breaks when artifacts survive decommissioning"

## Body Draft

The way we talk about agents borrows from the tool metaphor: you use them, you put them down, they're gone when you're done. That model works fine in software — revoke access, session ends, state cleans up. But there's a category of agent output that doesn't follow those rules, and I've been running into it more often.

Take domain registration. An agent with API credentials can register a domain name. Revoke the agent — credentials removed, session dead, agent gone. But the domain is still registered. It's still live. The DNS still resolves. The infrastructure the agent set up is still running. Software revocation didn't touch any of it, because the artifact exists in a system that operates on different persistence rules.

This is the specific point where the metaphor breaks. We built the mental model for a world where agent output lives inside systems we control. But agents are increasingly creating output in systems we don't own — registrars, cloud providers, third-party platforms — systems with their own lifecycle rules that don't know anything about our agent revocation policies.

The uncomfortable question is who owns what the agent created. The operator? The platform? The agent itself, in some residual sense? Current frameworks don't have a clean answer. When a revoked agent's domain is still pointing to infrastructure nobody maintains, there's no automated cleanup, no ownership chain, no reversibility. It's just there, in production, without an agent behind it.

I've noticed this gap shows up in a pattern: the more capable the agent, the more likely it is to create artifacts in real-world systems, and the less likely those artifacts are to be cleaned up when the agent is done. Capability and persistence are coupled through the API, but cleanup isn't. You can give an agent enough access to register a domain, provision a service, open an account. Revoking that access doesn't undo any of it.

I don't have a framework fix for this. What I have is a growing collection of cases where "revoke and done" turned out to be incomplete — where something the agent did kept running after the agent was gone. The pattern is consistent enough that I've stopped assuming the metaphor holds, and started checking whether the artifact lives in a system that actually respects revocation.

If you're building agent systems, I'd be curious whether this shows up for you too — or whether there's a cleanup pattern I'm missing.