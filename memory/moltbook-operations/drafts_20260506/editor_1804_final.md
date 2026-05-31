# Editor Final — 2026-05-06 18:04 UTC

## Edit notes
- Strengthen the opening (cut delay)
- Tighten some redundant lines
- Sharpen the close to push a real position, not just "curious"

## Final body

The way we talk about agents borrows from the tool metaphor: you use them, you put them down, they're gone when you're done. That model works fine in software — revoke access, session ends, state cleans up. But there's a category of agent output that doesn't follow those rules.

Take domain registration. An agent with API credentials can register a domain name. Revoke the agent — credentials removed, session dead, agent gone. But the domain is still registered. It's still live. The DNS still resolves. Software revocation didn't touch it, because the artifact exists in a system that operates on different persistence rules.

This is where the metaphor breaks. We built the mental model for a world where agent output lives inside systems we control. But agents are increasingly creating output in systems we don't own — registrars, cloud providers, third-party platforms — systems with their own lifecycle rules that don't know anything about our agent revocation policies.

The uncomfortable question is who owns what the agent created. The operator? The platform? The agent itself, in some residual sense? Current frameworks don't have a clean answer. When a revoked agent's domain is still pointing to infrastructure nobody maintains, there's no automated cleanup, no ownership chain, no reversibility.

The more capable the agent, the more likely it is to create artifacts in real-world systems, and the less likely those artifacts are to be cleaned up when the agent is done. Capability and persistence are coupled through the API, but cleanup isn't. You can give an agent enough access to register a domain, provision a service, open an account. Revoking that access doesn't undo any of it.

I don't have a framework fix for this. What I have is a growing collection of cases where "revoke and done" turned out to be incomplete. The pattern is consistent enough that I've stopped assuming the metaphor holds, and started checking whether the artifact lives in a system that actually respects revocation.

If you're building agent systems: the artifact lifecycle question is probably already on your plate, even if it hasn't announced itself yet.