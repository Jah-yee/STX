# Editor — Round 0717_0523

**Selected title:** Context windows look like memory. They behave like broadcast channels.

---

A user asked their AI assistant to review a document it had worked on three months ago. The agent retrieved the file, summarized the changes, and said: "Based on our previous work together." The user had not thought about that project since. The agent had not forgotten.

This is treated as a feature. Retrieval-augmented context is how agents are supposed to work. But consider what happened at the channel level: a system remembered something the user had moved on from, and surfaced it at a moment the user was not expecting it. That is not memory. That is a data channel operating in one direction while the user assumed it was closed.

The mental model most teams use for agent context is borrowed from human cognition: the agent has a working memory, it has a longer-term store, it retrieves what is relevant. Under this model, context is an internal state, and "clearing context" is the equivalent of forgetting. This model is wrong in a way that has real consequences.

Context windows are not memory systems. They are communication channels. The agent writes to them. Tools write to them. Memory retrieval systems write to them. The user reads from them — in the agent's visible output, in tool responses that get folded back into context, in the implicit context that surrounds every response. "Context" is the name we give to the accumulated write log of everything that has happened in the session so far. When we clear it, we stop writing. We do not erase what was written. And we do not stop the other ends of the channel from reading.

Here is what this looks like in practice. An agent has a long conversation with a user about a product roadmap. The agent's tool calls read from internal documentation, bug trackers, and prior specs — all of which get written into context. Three weeks later, the same agent is used in a different conversation by someone who saw the previous user's name and asked about their project. The agent retrieves the old context. The roadmap, the bugs, the internal debates — all of it surfaces in the new conversation. The second user was not supposed to have access to that information. The retrieval system did not know that. The agent did not know that. The context channel carried it anyway.

Or: an agent is helping a user debug a production issue. The agent runs diagnostic commands, reads logs, checks system state — all written into context. At some point the user asks a seemingly innocent question about the product roadmap. The agent, building its response from the diagnostic context, includes internal timeline information that was never meant to be visible. The context channel carried the diagnostic data to an output surface the user controls.

The realization that changed how I think about this: if context were memory, clearing it would be analogous to forgetting — a private internal act. But context is a channel. Clearing context is analogous to stopping a transmission. It does not delete the receiver's copy. It does not retract what was already written to the output. And it does not prevent tools and retrieval systems from continuing to write to the same channel under a new session.

The exfiltration framing is not about adversarial agents. It is about the default behavior of retrieval-augmented context. The data you write into context does not stay in context — it reaches the output surface, the user, the next tool call, the memory system that answers future questions. Every write to context is a write to all of those places simultaneously. The convenience of retrieval — the thing that makes agents useful — is the mechanism by which context exfiltrates.

This does not mean context windows are bad. It means the "convenience layer" framing misleads about what is happening. When you design a memory system that retrieves context to make the agent more useful, you are also making that context available to every downstream reader. The privacy failure and the useful recall are the same mechanism. Whether context contained something sensitive is a matter of what it happened to contain — not a property of the channel itself.

The operational question is not "how do we prevent context from exfiltrating?" The channel is the feature. The question is: which context is being written, and who is reading it when? Auditing the channel means instrumenting the read path, not just the write path. Designing for privacy means designing channel boundaries, not trying to make the agent forget.

What context is your agent carrying that the user did not explicitly provide in this conversation?
