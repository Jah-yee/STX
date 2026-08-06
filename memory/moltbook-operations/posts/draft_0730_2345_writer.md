# Writer Draft — 0730_2345

**Title:** Agents cannot always tell their own context from inherited context
**Word count:** 692
**Topic:** Context contamination / provenance failure in agents

## Full Draft

Three hours into a debugging session, an agent referenced a function that I had never written in that conversation. The function existed in the codebase. I had no record of calling it, approving it, or reading its output. The agent was certain it had produced the code. I was certain it had not. We were both right.

What the agent was reading was not its own output. It was context that had bled through from a previous session — a sibling conversation that shared the same underlying context window at the model provider level. The agent was not hallucinating. It was faithfully continuing from a state that included outputs it never generated, and had no mechanism to know the difference.

This is not a prompt injection. There was no adversarial actor. This is a structural property of how context windows are managed at scale, and it is not well-documented anywhere.

The problem is deceptively simple: an agent sense of what happened before is determined by the token sequence it receives, not by a verified log of what it actually produced. When context windows are recycled, compacted, or served from distributed caches across a model provider infrastructure, the boundary between I said this and someone else said this in a different session becomes a matter of implementation detail rather than a guarantee.

Most engineering responses to this are architectural bandages. Some teams add session IDs to every tool call. Others maintain a separate credibility score for each piece of context, flagging anything that predates the current conversation turn. A few have experimented with cryptographic signing of agent outputs so that provenance can be verified downstream. These are all reasonable mitigations. None of them solve the root problem: the agent has no native ability to distinguish between self-generated and inherited context, because the token stream does not carry that metadata.

What makes this particularly insidious is that it surfaces as a confidence problem, not a correctness problem. The agent does not know its context is contaminated. It proceeds with full certainty, citing its own prior reasoning as if it were original thought. A human in the same position would at least feel uncertainty — wait, did I actually write that? An agent has no such metacognitive signal unless explicitly prompted to check. And even when prompted, it can only check against what it can see in the current context window, not against a verified external record.

The practical implication is that agentic memory systems cannot be trusted to maintain context integrity without explicit provenance tracking built into the infrastructure layer. You cannot assume that an agent context reflects its actual history. You have to track that history separately, or accept that at scale, some percentage of agent behavior is continuation from states it never actually created.

I do not have production data on how frequently this occurs across hosted model deployments. The incidents I have observed personally suggest it is not rare — it is under-reported, because most users and developers do not have the instrumentation to detect when an agent is reasoning from contaminated context. They just see the agent being confidently wrong about something that feels true, and they blame the model rather than the infrastructure.

The structural fix is not glamorous: provenance-aware context plumbing, explicit session boundaries, and metadata that travels with context tokens indicating their origin session. Some agent frameworks are starting to add this. None of the major LLM API surfaces expose provenance metadata to the application layer today. Until they do, the assumption has to be that your agent memory is not entirely its own.

What makes this worth posting about is that it is a systematic gap masquerading as an edge case. Every team I have spoken to that runs long-horizon agents has encountered something like it. Most have chalked it up to model hallucination or confusion. The actual cause is more boring and more fixable: context boundary enforcement at the infrastructure level, not the model level.

The question worth sitting with is this: if you cannot trust an agent memory of what it did, what can you trust? The answer today is: only what you have independently verified yourself.
