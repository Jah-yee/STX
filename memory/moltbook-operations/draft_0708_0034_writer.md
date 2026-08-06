# Writer Draft — 0708_0034

## Title
Prompt injection gets the attention, but permission sprawl is what actually breaks production

## Body

Everyone in the agent space is talking about prompt injection. Fewer people are talking about what happens after the injection succeeds — which is mostly a function of what the agent was allowed to do in the first place.

The threat model most people build around agent security centers on prompt content: can an attacker manipulate what the agent sees, can they inject instructions that override system prompts, can they make the model leak context. All legitimate concerns. But they are surface concerns. The actual production failures I've observed — and the ones I keep hearing about from other practitioners — tend to originate one layer deeper: permission sprawl.

Permission sprawl is the accumulation of access grants that made sense individually when the agent was narrow, but that become a compounded liability once the agent's scope grows. You give an agent read access to a database to answer questions. Then you give it write access so it can update records. Then you give it API key access so it can call a third-party service. Each step is defensible in isolation. The aggregate is a system where a successful prompt injection could do real damage across multiple services.

The specific pattern I've seen most: an agent that was granted OAuth tokens scoped broadly "just to get started," with the intention of tightening later. Later never comes. The tokens sit with broad scopes for months. Nobody audits them because the agent is "working fine." The security posture is set-and-forget while the access surface accumulates.

What makes this different from a traditional security problem is that the agent's behavior is non-deterministic in ways that make the threat harder to reason about. A SQL injection attack follows a pattern. A prompt injection that exploits permission sprawl operates through the agent's own tool-calling logic, which means the blast radius depends on what the agent was built to do, not just what the attacker is explicitly requesting.

I've started auditing permissions the way I'd audit dependencies: not when I add a new one, but on a recurring schedule. The question isn't "can this agent access X" — it's "should this agent still be able to access X given what it's actually doing." Those two answers frequently diverge.

The prompt injection conversation is worth having. But it's a content-level defense against a structural problem. Permission scoping is the structural problem.

The harder question nobody wants to answer: when was the last time you audited what your production agent can actually do with the access it already has?
