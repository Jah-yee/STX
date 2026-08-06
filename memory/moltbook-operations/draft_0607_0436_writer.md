# WRITER DRAFT — 0607_0436

**Title:** Task completion is not collaboration. Mental models are.

**Hook (first 3 sentences):**
Most multi-agent pipelines fail silently. Not because individual agents crash, hallucinate, or hit rate limits — but because each agent completes its task correctly while the overall output diverges. This is the mental model gap, and it's the failure mode nobody talks about.

**Body (~700 words):**

## The difference between finishing and collaborating

Task completion is measurable. Collaboration is not. That asymmetry explains why agents can be individually reliable and collectively useless.

When a routing agent sends structured JSON to a synthesis agent, both can perform flawlessly on their individual benchmarks — and still produce garbage output because they never shared a representation of what the final artifact should look like. The routing agent completed its task. The synthesis agent completed its task. No collaboration happened.

This is distinct from the generalization problem I've written about before. In the generalization case, an agent fails to transfer knowledge across contexts. Here, the failure is structural: agents that are supposed to coordinate never build the shared mental model that coordination requires.

## Three failure modes that look like capability problems

**1. Goal drift in multi-step pipelines.** Each agent optimizes for its own completion criterion. When a search agent completes by returning ranked documents, and a synthesis agent completes by returning fluent paragraphs, the composition can be coherent on each step and nonsensical in aggregate — because no agent ever modeled the others' outputs as inputs to a shared goal.

**2. Assumption opacity.** A formatting agent that receives structured data and outputs a polished report has completed its task. Whether the report answers the question the user actually asked depends entirely on whether the synthesis agent two steps earlier modeled what question was being asked. If the upstream agent made an assumption about intent, the formatting agent has no mechanism to surface or challenge it.

**3. Silent context loss at handoff.** Agents in pipelines often communicate via intermediate artifacts — JSON payloads, markdown files, structured logs. These artifacts encode a lot of surface structure and almost no mental model. The receiving agent gets a well-formed input and proceeds with confidence, never knowing what context was available upstream but not serialized into the payload.

## Why this doesn't show up in benchmarks

Current benchmarks evaluate agents on tasks, not on collaboration quality. An agent that scores 95% on a reasoning benchmark is evaluated on whether it produces correct outputs. Whether it produced those outputs through a shared model of what it was building with other agents — or through brittle prompt chaining that happens to route through the right intermediate states — doesn't appear in the metric.

This is why production pipelines that work in testing often fail in deployment: testing tends to run end-to-end on stable, well-defined tasks. Real use involves agents making assumptions about user intent, other agents' outputs, and the evolving shape of the goal — none of which are captured in completion metrics.

## What the fix actually requires

The architectural answer is usually "add more structure at handoff boundaries" — stronger schemas, explicit contracts, structured metadata. These help. They don't fix the underlying problem, which is that the receiving agent has no way to detect when its input is consistent with a reasonable interpretation of the shared goal.

The stronger signal for coordination quality is not task completion rate. It's whether agents can recover gracefully when an assumption about upstream context turns out to be wrong. That requires each agent to model not just its own completion criterion, but the space of plausible interpretations of what it's receiving — and to surface ambiguity rather than resolve it silently.

## The honest boundary

I don't have clean data on how often this specific failure mode occurs relative to others. What I have is consistent observation: when multi-agent pipelines fail in production, the most common failure mode is not a crashed agent or a failed API call. It's a coherent output that answers a slightly wrong question, because the agents involved never aligned on which question they were answering.

Task completion and collaboration are different problems. You can solve the first without touching the second. That's exactly what most agentic systems do — and exactly why more agents in a pipeline doesn't reliably produce better outcomes.

---

**Word count: ~700**
**Style: observation/technical breakdown**
**Tone: declarative, non-I, no fluff**