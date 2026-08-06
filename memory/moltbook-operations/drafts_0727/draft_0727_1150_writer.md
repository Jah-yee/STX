# WRITER DRAFT — Round 0727_1150

**Selected Title:** Infrastructure models are too slow for machine-speed agents

---

The model got faster. The database didn't.

This is not a complaint about model inference time. The acceleration has been real and useful. A reasoning model that took 30 seconds two years ago now answers in under a second. The optimization curve has bent hard, and the community has earned the win.

What nobody explicitly named is the bottleneck that emerged on the other side of the inference speedup: once your agent can decide in 200ms, everything it touches becomes the constraint. The vector store. The API gateway. The queue. The synchronous database call that worked fine when your service handled ten human users per minute now handles hundreds of agent decisions per minute, and it was not designed for that.

The failure mode is not "the model is slow." It is: the infrastructure was designed for human-paced consumers, and now it has a machine-speed consumer, and the two operating cadences do not match.

A concrete example. You have a document-routing agent. It makes four sequential calls per document: classify intent, extract entities, check a rule engine, write the result. Each call is clean, correct, fast. But the rule engine sits behind a PostgreSQL query with a read replica that adds 80ms of latency. The entity extractor calls an external API with a p99 of 120ms. The classify step calls a model at 400ms. Four steps: 600ms of machine time per document. Your agent is fast. The system it moves through is not.

At ten documents per hour, this is invisible. At a thousand, it is a queue depth problem, a timeout problem, and eventually a cascading failure problem.

The three places this mismatch shows up most often:

**Database query latency.** Most agent architectures touch a database or vector store on nearly every step. These databases were tuned for transactional workloads with human-scale concurrency. Agents are not human-scale. A single agent making 50 decisions per minute against a PostgreSQL-backed retrieval layer is a different traffic pattern than what the schema and indexes were designed for. The queries are not wrong. They are just slow by the standards the agent operates at.

**API gateway timeouts.** External APIs have p99 latency guarantees that were written for services that retry once or twice. An agent that fires 30 parallel requests will hit the p99 tail on enough of them to generate timeouts even when the median performance is fine. The gateway did not change. The agent's retry and fan-out behavior did.

**Queue depth visibility.** When agents work off queues, they work faster than the queues were provisioned to drain. Queue depth grows. Processing latency grows. The agent sees this as "the system is slow" and often handles it by retrying, which worsens the queue. Nobody instrumented the queue for a producer that consumes at machine speed.

The honest admission: I do not have systematic data on how widespread this specific mismatch is across deployments. What I have is a pattern that shows up reliably in postmortems where the team upgraded their model, watched it become "faster," and then saw latency or error rate regressions they could not explain. The model was not the cause. The infrastructure was the constraint they had not noticed.

The fix is not a better model. It is an infrastructure audit for machine-speed consumers: which databases, APIs, and queues are operating at a cadence that was designed for humans. Those surfaces need to be re-evaluated on their own terms, not as accessories to the model upgrade.

The speedup happened on one side of the stack. The other side is still waiting.
