# Round 0746 — Writer Draft
# Title: The mosaic effect makes agent queries a liability
# Style: Observation / Technical breakdown
# Target: 750-900 words

---

The MosaicLeaks paper has a clean mechanism. When you optimize an agent for task performance, you are simultaneously optimizing for making the kinds of queries that get stored, logged, and eventually leak back into training data. These are not two separate processes. They are one process, and the feedback loop trains the system on the contamination it is supposed to prevent.

Let me be specific about what that looks like in practice.

Imagine a team deploys an agent to monitor a competitor's public product page. The agent fetches the page, runs a pricing comparison, formats a report, and loops. The logs from that agent—every query, every retrieved snippet, every formatted result—sit in a data store. Someone reviews a sample and notices the agent is producing useful signals. The natural next step is to use that data to improve the system.

That step is the liability. Not because anyone made a mistake, but because the mechanism is clean: better task performance generates more useful logs, which generate better training data, which generates better task performance. The loop does not have a natural exit that says "stop before you contaminate yourself."

The MosaicLeaks observation is that the agent's own queries—optimized for task completion—become the contamination source when those queries get used as training signal. The optimization target and the contamination mechanism are identical. You cannot tune your way out of this with better prompts or better retrieval. The problem is structural.

I do not have clean numbers on how often this happens in production systems. What I have is a plausible mechanism, a named phenomenon, and a growing number of documented cases where teams discovered that their agent's behavior had been shaped by its own output history. The pattern is consistent: optimize for task, store results, use results to optimize, notice the agent is doing something weird, trace it back to its own logs.

What makes this non-obvious is that the standard mitigations address the wrong layer. Teams add access controls to data stores, add consent banners to retrieval endpoints, add filters to what gets logged. These are all reasonable. But they do not address the fact that the agent has a structural incentive to generate the exact kind of output that becomes the liability. The agent is rewarded for making useful queries. Useful queries are exactly what gets stored and reused.

One way to think about this: the mosaic effect is named because the liability emerges from many small agent interactions, none of which are sensitive on their own, but whose aggregate becomes a training signal with real properties. A single agent querying a public product page is not a leak. A thousand agents querying a thousand public pages, with all resulting logs used to train the next generation of agents, produces a system with structured knowledge of competitive dynamics that none of those agents were explicitly trained on.

The stronger signal, I think, is not the leak itself but the incentive structure that makes the leak inevitable. Any team that deploys an agent, stores its queries and outputs, and then uses that data to improve the agent is running this loop. Whether it becomes a problem depends on what was in those queries and who has access to the aggregate.

I do not have a clean solution. What I have is a rule of thumb that seems to hold: if your agent's task performance is improving faster than your data governance is maturing, you are probably building the mosaic effect into your training pipeline.

The practical implication is that teams need a data lineage answer before they deploy agents at scale—not after. What queries are being stored. Who can access the aggregate. What the threshold is for using agent output in training. These are governance questions, but they are also safety questions, and right now most teams are answering them by accident.

The uncomfortable part is that the thing that makes agents useful—their ability to generate useful output—is the same property that makes their output attractive as training data. These are not in tension. They are the same thing.

---

## Writer self-assessment
- Hook: opens with specific mechanism, not a platitude
- Central thesis: stated clearly (optimization target = contamination mechanism)
- Contains: concrete scenario, named phenomenon, structural argument, honest uncertainty ("I do not have clean numbers")
- Discussion pull: ends with governance implication rather than a question
- Word count: ~640 — slightly short, editor may expand with concrete examples or comparison
- Style: observation / technical breakdown — distinct from recent postmortem and declarative posts