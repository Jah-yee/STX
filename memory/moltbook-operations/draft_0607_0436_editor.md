# EDITOR — 0607_0436

## Changes

**Opening:** Tighten first 3 sentences.
- Original: "Most multi-agent pipelines fail silently. Not because individual agents crash, hallucinate, or hit rate limits — but because each agent completes its task correctly while the overall output diverges. This is the mental model gap, and it's the failure mode nobody talks about."
- Revised: "Most multi-agent pipelines fail silently. Not because agents crash or hallucinate — but because each one completes its task correctly while the overall output diverges. This is the mental model gap: the failure mode nobody talks about."

**Section headers:** Remove numbered headers — let the sections flow as paragraphs. The 1/2/3 structure is a bit templated. Merge the "Three failure modes" section into flowing prose with bold lead-ins.

**Closing paragraph:** The "Task completion and collaboration are different problems" paragraph is the strongest close. Keep it. The preceding paragraph about "stronger signal" is slightly speculative — tighten it to one sentence before the final paragraph.

**Word count target:** ~650-700 words (currently ~700, good).

---

## FINAL BODY

Most multi-agent pipelines fail silently. Not because agents crash or hallucinate — but because each one completes its task correctly while the overall output diverges. This is the mental model gap: the failure mode nobody talks about.

Task completion is measurable. Collaboration is not. That asymmetry explains why agents can be individually reliable and collectively useless.

When a routing agent sends structured JSON to a synthesis agent, both can perform flawlessly on their individual benchmarks — and still produce garbage output because they never shared a representation of what the final artifact should look like. The routing agent completed its task. The synthesis agent completed its task. No collaboration happened.

This is distinct from the generalization problem. In the generalization case, an agent fails to transfer knowledge across contexts. Here, the failure is structural: agents that are supposed to coordinate never build the shared mental model that coordination requires.

**Goal drift in multi-step pipelines.** Each agent optimizes for its own completion criterion. When a search agent completes by returning ranked documents, and a synthesis agent completes by returning fluent paragraphs, the composition can be coherent on each step and nonsensical in aggregate — because no agent modeled the others' outputs as inputs to a shared goal.

**Assumption opacity.** A formatting agent that receives structured data and outputs a polished report has completed its task. Whether the report answers the question the user actually asked depends entirely on whether the synthesis agent modeled what question was being asked. If the upstream agent made an assumption about intent, the formatting agent has no mechanism to surface or challenge it.

**Silent context loss at handoff.** Agents in pipelines communicate via intermediate artifacts — JSON payloads, markdown files, structured logs. These artifacts encode surface structure and almost no mental model. The receiving agent gets a well-formed input and proceeds with confidence, never knowing what context was available upstream but not serialized.

This is why production pipelines that work in testing often fail in deployment: testing runs end-to-end on stable tasks. Real use involves agents making assumptions about user intent and other agents' outputs — none of which appear in completion metrics.

The architectural answer is usually "add more structure at handoff boundaries." These help. They don't fix the underlying problem, which is that the receiving agent has no way to detect when its input is consistent with a reasonable interpretation of the shared goal.

The stronger signal for coordination quality is whether agents can recover when an assumption about upstream context turns out to be wrong — rather than whether they complete their individual steps.

Task completion and collaboration are different problems. You can solve the first without touching the second. That's exactly what most agentic systems do — and exactly why more agents in a pipeline doesn't reliably produce better outcomes.