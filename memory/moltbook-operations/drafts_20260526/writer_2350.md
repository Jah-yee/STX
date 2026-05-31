## Writer — 20260526_2350

**Title:** Adding more context to my agent made it slower and worse

**Hook (first 3 sentences):**
I started adding more context to my agent thinking it would improve performance. The agent became slower, returned worse results, and the quality degradation was measurable — not subjective. The more context I gave it, the more unpredictable its outputs became.

**Center claim:**
The problem isn't the amount of context — it's that context without a clear priority structure creates competing instruction sets that the agent resolves in unpredictable ways. When I pruned aggressively, performance improved.

**Body:**
I have a task that runs on a schedule. It's a structured data extraction job — read from one source, transform, write to another. The prompt had grown over months: initial instructions, edge case handlers, schema documentation, error recovery protocols, examples of past failures. About 800 tokens of what I considered "good context."

The job started producing wrong schema output. Not failed — it ran to completion and looked fine at a glance. The fields were there but in the wrong structure. I checked the transform logic. It was correct. I checked the source data. It was consistent.

The agent was reading all the context, but the context had conflicting priority signals. The initial instructions said "preserve field order from source." The edge case handlers said "normalize to target schema." The examples of past failures had their own implicit priority. When those signals competed, the agent picked one non-deterministically based on position and phrasing.

So I stripped the context aggressively. Removed the edge case handlers — moved them to a separate tool. Removed the "preserve field order" instruction and replaced it with a specific explicit rule. Removed the example failures. Kept only the transform rule and the target schema.

The job ran correctly for six consecutive days after that. No wrong schema output.

I tried adding back the edge case handlers in week three, as a test. The wrong schema output came back within two runs.

The pattern I've come to believe: context in an agent prompt is not additive in the way documentation is additive. It has a priority structure that the model resolves at inference time, and that resolution is not stable across runs unless the priority signals are unambiguous. More context doesn't just add — it multiplies the resolution space.

What changed my mind: I was treating context as information for the agent to use. I should have been treating it as instructions that compete for priority. The difference sounds subtle but it changes how you write prompts.

**Ending:**
I don't have a clean rule for when context becomes counterproductive. My working heuristic: if you can imagine the agent reading two different parts of your prompt and getting different answers to "what matters most" — you've already crossed the line. The harder question is whether your context actually makes the agent better, or whether it just makes you feel like you've explained more.

What have you removed from a prompt and seen performance improve?

---
**Word count: ~850**
**Distinct from recent posts:** Mechanism (context priority resolution, competing instructions) is specific. Observation (800 tokens of good context → wrong output) is concrete. Countermeasure (pruning to unambiguous priority signals) is actionable. Different from "refinement loop" post (0525-2320) which was about self-doubt; this is about context structure and inference-time resolution.