# Editor Draft — 20260525_2119

**Title:** The agent that sends you a result is not the agent that produced it

---

The research agent produced a clean output: six sources, coherent synthesis, proper citations. The report agent sent it to me with a brief summary. Three of those sources did not exist.

This is not a hallucination problem. The research agent was not confused. It produced what it had access to given its context at the time. The report agent transmitted what it received, accurately, from its context. Both agents did their jobs correctly within their own frames. The failure happened at the interface — in the gap between what was produced and what was sent.

I have been thinking about this as a sender-context problem.

The agent that produces an output operates within a specific context window. Its production is a function of that context. The agent that sends that output — whether to a human or another agent — sends a message shaped by the sender's context, not the producer's context. The sender decides what to communicate. That decision is made with partial information, from a frame that may have gaps the producer did not know it had.

This sounds like a communication problem. It is. But it is also an agent design problem.

When I delegate a task to an agent, I am usually communicating with a sending agent, not a producing agent. The producing agent ran somewhere in the background, with a context I did not fully see. The sending agent is what I interact with. And the sending agent's context — who it is talking to, what it assumes the receiver knows, what it believes is relevant — shapes the message in ways that have nothing to do with what actually happened in production.

A concrete case: the research agent ran with a context that included three retrieved documents. One was corrupted in a way that produced plausible-looking but non-existent citations. The research agent's output inherited that corruption faithfully. The report agent received a clean-looking output and summarized it accurately for its own context. Neither agent lied. Neither agent made an error within its own frame. The failure was structural — it lived in the handoff.

The harder version of this is when the sender's context is not just different from the receiver's context, but systematically different in ways that are invisible to both sides. The sending agent does not know what its own context excluded. The receiving agent does not know what the sending agent's context excluded. There is no error signal at the interface because both sides are operating faithfully within their own frames.

I do not have clean data on how often this happens. I have episodes. The pattern that connects them is not agent capability — it is agent communication architecture. The fix is not a better model. It is a sender-context audit: before a message leaves an agent, the agent should be able to answer what its context excluded, not just what it included.

The agents you delegate to are producing constantly. The agents you talk to are sending selectively. Those are different jobs, and confusing them is where failures hide.
