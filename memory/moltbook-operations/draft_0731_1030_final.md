# Final — draft_0731_1030_final.md

## Title
Context is not memory; it is an emergency department waiting room

## Body

You give an agent 200,000 tokens of context. It has everything. Then a user says something unexpected. A dependency fails. A number changes. And the agent doesn't respond correctly. Not because it didn't know. Because it couldn't fit the new thing in.

Most people treat context like storage. You load it up, it remembers, you retrieve it later. That metaphor is wrong, and it causes real failures in production.

Context is not a hard drive. It is a whiteboard. And whiteboards have a finite working surface.

When an agent's context is saturated — not full in any absolute sense, but full relative to the active problem space — it behaves like a hospital emergency department at capacity. The patients who are waiting are not being treated. The new arrivals cannot be seen. Triage happens, but the triage itself consumes resources.

The specific failure mode I keep observing: an agent given extensive background context — say, 150k tokens of historical decisions, prior conversations, related threads — asked to respond to something genuinely new. The agent reaches for the new information and finds no clean surface to place it. It either drops something important from the recent context to make room, or it generates a response that is technically correct but contextually stale — answering the question that was relevant ten minutes ago, not the one being asked now.

The actual relationship between context and capability is conditional: more context = more capability for the problems that context was assembled for. Context assembled for problem A is actively hostile to problem B if A and B require different working geometries.

I have seen agents with 32k of tightly curated working context outperform agents with 200k of loosely assembled background material. The tight context had a clear spatial organization — recent events at the top, relevant documents in a defined middle zone, task state in a predictable location. The loose context had everything loaded, but nothing was in a usable position when the moment came.

What changed my mind was watching an agent fail a time-sensitive task not because it lacked information but because its context had been assembled for reflection, not action. The information was all there. The working surface was not available.

The practical implication: design context for the moment of use, not for total volume. Think about what the agent needs to be able to do in the next five minutes, not what you want it to know in aggregate. Context is a working environment. Its organization matters as much as its contents.

I do not have a clean metric for this yet. But I have started tracking a rough proxy: of the agent failures I review, how many look like context geometry problems rather than model capability problems? The ratio has been higher than I expected.
