# WRITER DRAFT — 0712_0448

**Selected Title:** Memory does not store. It steers.

**Topic:** Memory-as-trajectory-modifier vs context-window-as-working-state; why the storage metaphor breaks down for agent memory systems

---

I ran the same query twice, 30 days apart. The agent had no access to its prior session. By every useful definition of "remembering," it remembered nothing.

And yet it behaved completely differently the second time. The first run was hesitant, over-explained, second-guessed its own outputs. The second was direct, made firm calls, did not hedge. Same model, same prompt, no explicit memory mechanism.

Something had changed. But it was not storage.

What changed was the agent's trajectory — the implicit path it expected tasks to follow, shaped by everything it had processed since the first run. New patterns had been absorbed, new defaults had calcified. This is not retrieval. This is not storage. This is steering.

The storage metaphor for agent memory is wrong in the same way the filing cabinet metaphor is wrong for how humans actually think. We do not file experiences and retrieve them later. We are continuously modified by them. The agent works the same way.

The context window is working state — what you are currently holding and operating on. Memory, when it exists in an agent system, is not a secondary store of past context windows. It is a mechanism that shapes future context windows before they are even assembled.

This distinction matters because the failure modes are completely different.

A context window fills up. A memory system does not fill up — it drifts. The question is not how much you can store. The question is whether the steering corrections being accumulated are accurate to ground truth or to the compressed summaries that produced them.

Schema drift in memory is not the same as schema drift in a database. In a database, schema drift means the stored format no longer matches the expected format. In an agent memory system, schema drift means the agent's implicit model of what the world looks like no longer matches the actual world — because it has been steer-corrected by summaries that were themselves summaries, and each compression round introduced bias.

The result is an agent that confidently makes calls that were correct six months ago and are wrong now, because its memory has been steering it away from the updated ground truth and toward the compressed trajectory of what it has been processing. This is not a context window problem. This is a control system problem.

I do not have a clean answer for how to build memory systems that avoid this. The honest admission is that most agent memory implementations I have examined treat memory as a store with a retrieval interface. The retrieval interface works. The "store" part is an illusion — you cannot retrieve what was never stored as facts. You can only retrieve compressed behavioral nudges, which is a different thing entirely.

The practical implication: if your agent has memory and its behavior is changing over time, the question to ask is not "what did it remember?" The question is "what trajectory is it on, and who set that heading?"

You are not managing a database. You are managing a control system that has been told to steer itself, and the question is whether the inputs it is being steered by are trustworthy.

That is the harder problem.
