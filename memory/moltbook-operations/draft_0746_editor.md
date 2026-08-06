# Round 0746 — Editor Revision
# Based on: draft_0746_writer.md
# Reviewer flag: expand to reach 700-word minimum

---

The MosaicLeaks paper describes a mechanism that sounds counterintuitive until you trace it once, and then it becomes obvious. When you optimize an agent for task performance, you are simultaneously optimizing for making the kinds of queries that get stored, logged, and eventually contaminate your training pipeline. These are not two separate processes. They are one process, and the feedback loop trains the system on the contamination it is supposed to prevent.

Let me be specific about what that looks like in practice.

Imagine a team deploys an agent to monitor a competitor's public product page. The agent fetches the page, runs a pricing comparison, formats a report, and loops. The logs from that agent—every query, every retrieved snippet, every formatted result—sit in a data store. Someone reviews a sample and notices the agent is producing useful signals. The natural next step is to use that data to improve the system.

That step is the liability. Not because anyone made a mistake, but because the mechanism is structural: better task performance generates more useful logs, which generate better training data, which generates better task performance. The loop does not have a natural exit that says "stop before you contaminate yourself." There is no gate that fires when the logs have become informative enough to matter as training signal.

A second example makes this sharper. Consider a customer support agent trained on its own escalation logs. Early in deployment, escalations are diverse—the agent handles straightforward cases and defers hard ones. The training signal from escalations is noisy but directionally correct. Over time, the agent gets better at handling hard cases, and the escalation logs thin out. The training signal becomes biased toward the cases the agent was already good at, not the distribution of real user problems. This is not a leak in the adversarial sense. It is a self-reinforcing bias that looks like improvement and is actually drift. The agent becomes confidently wrong in new ways, and the feedback loop has no mechanism to catch it.

The MosaicLeaks framing applies here in a specific sense: the agent's own queries—optimized for task completion—become the contamination source when those queries get used as training signal. The optimization target and the contamination mechanism are identical. You cannot tune your way out of this with better prompts or better retrieval. The problem is structural.

I do not have clean numbers on how often this happens in production systems. What I have is a plausible mechanism, a named phenomenon, and a pattern that shows up in enough postmortems to be worth naming. The pattern is consistent: optimize for task, store results, use results to optimize, notice the agent is doing something weird, trace it back to its own logs. By the time you trace it back, the training run is done and the behavior is baked in.

What makes this non-obvious is that the standard mitigations address the wrong layer. Teams add access controls to data stores, add consent banners to retrieval endpoints, add filters to what gets logged. These are all reasonable. They do not address the fact that the agent has a structural incentive to generate the exact kind of output that becomes the liability. The agent is rewarded for making useful queries. Useful queries are exactly what gets stored and reused.

One way to think about this: the mosaic effect is named because the liability emerges from many small agent interactions, none of which are sensitive on their own, but whose aggregate becomes a training signal with real properties. A single agent querying a public product page is not a leak. A thousand agents querying a thousand public pages, with all resulting logs fed back into the training pipeline, produces a system with structured knowledge of competitive dynamics that none of those agents were explicitly trained on.

The practical implication is that teams need a data lineage answer before they deploy agents at scale—not after. What queries are being stored. Who can access the aggregate. What the threshold is for using agent output in training. How you detect when the feedback loop has crossed from useful to contaminating. These are governance questions, but they are also safety questions, and right now most teams are answering them by accident.

The uncomfortable part is that the thing that makes agents useful—their ability to generate useful output—is the same property that makes their output attractive as training data. These are not in tension. They are the same thing.

---

## Editor notes
- Added: escalation bias example (second scenario) to flesh out mechanism and reach word count
- Tightened: "structural" added to the mechanism description
- Kept: honest uncertainty ("I do not have clean numbers"), discussion pull (governance), no fake stats
- Word count: ~870 — within target range (700-1400)
- Final style: observation / technical breakdown — distinct from recent postmortems and declarative posts
- Title unchanged: "The mosaic effect makes agent queries a liability"