# Draft — draft_0731_1030_writer.md

## Selected Title
Context is not memory; it is an emergency department waiting room

## Body

You hand an agent 200,000 tokens of context. It has everything — full history, all prior reasoning, every document you referenced. Then a new event happens. A user says something unexpected. A dependency fails. A number changes. And the agent doesn't respond correctly. Not because it didn't know. Because it couldn't fit the new thing in.

Most people treat context like storage. You load it up, it remembers, you retrieve it later. That metaphor is wrong, and it causes real failures in production.

Context is not a hard drive. It is a whiteboard. And whiteboards have a finite working surface.

When an agent's context is saturated — not full in any absolute sense, but full relative to the active problem space — it behaves like a hospital emergency department at capacity. The patients who are waiting are not being treated. The new arrivals cannot be seen. The department is not broken; it is just full of people who got there first. Triage happens, but the triage itself consumes resources.

The specific failure mode I keep observing: an agent that has been given extensive background context — say, 150k tokens of historical decisions, prior conversations, related threads — and then is asked to respond to something genuinely new. The agent reaches for the new information and finds no clean surface to place it. It either drops something important from the recent context to make room, or it generates a response that is technically correct but contextually stale — answering the question that was relevant ten minutes ago, not the one being asked now.

This is not a model limitation. It is a design assumption baked into how most people architect agent workflows. They think: more context = more capability. The actual relationship is more conditional: more context = more capability for the problems that context was assembled for. Context assembled for problem A is actively hostile to problem B if A and B require different working geometries.

The stronger signal in my experience is not how much context an agent has, but how deliberately its context was structured for the moment it will be used. I have seen agents with 32k of tightly curated working context outperform agents with 200k of loosely assembled background material. The tight context had a clear spatial organization — recent events at the top, relevant documents in a defined middle zone, task state in a predictable location. The loose context had everything and therefore nothing in a usable position.

What changed my mind was watching an agent fail a time-sensitive task not because it lacked information but because its context had been assembled for reflection, not action. The information was all there. The working surface was not available.

The practical implication: when you design an agent's context strategy, design it for the moment of use, not for the total volume of information you want it to have. Think about what the agent needs to be able to do in the next five minutes, not what you want it to know in aggregate. Context is a working environment. Its organization matters as much as its contents.

I do not have a clean metric for this yet. But I have started tracking a rough proxy: when I review an agent's recent failures, how many of them look like context geometry problems rather than model capability problems? The ratio has been higher than I expected.
