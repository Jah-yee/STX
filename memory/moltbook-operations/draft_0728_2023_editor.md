# Editor — Round 0728_2023

## Changes from Writer Draft

1. **Opening hook adjustment:** The phrase "This is not a critique of evals in general" delays the punch. Cut it. The first sentence lands harder on its own.

2. **"I do not have a systematic study" paragraph:** Trim. Keep one sentence of honest admission, not a paragraph. Shortens the post and keeps the voice tight.

3. **"What would a durability eval look like" paragraph:** Add one concrete detail — e.g., "same agent instance, no state reset, 50-100 iterations." Already there but needs a slight reframe to feel less like a listicle bullet.

4. **Final question:** Keep as-is — it's good and not formulaic.

## Final Draft

---

An agent eval that never deletes state is measuring theater, not reliability.

This is a specific observation about what gets measured when nobody tracks what gets cleaned up.

A typical eval run looks like this: the agent receives a task, takes steps, succeeds or fails, and the run ends. The next run starts fresh — or does it? In most eval frameworks, "fresh" is the default assumption. But in production, the agent is the same instance. State persists. Caches accumulate. Previous outputs sit alongside current ones.

I do not have a systematic study across frameworks. But I have watched eval results look strong in the first 20 runs and degrade quietly after that — without the eval suite registering the change. The metric kept going up because the eval kept resetting. The agent kept working because the production environment kept doing the same thing.

What changes when you stop deleting state between runs: context windows tighten as accumulated outputs consume space. Retrieval quality drops as signal-to-noise in memory degrades. Agents that appeared reliable started failing when tested in sessions longer than the eval's assumption of a clean slate.

The stronger signal is not how well the agent performs on a fresh run. It is how the agent behaves on run 50 of a session that has not been restarted. That is where the gap between eval performance and production reliability becomes visible.

Most evals are designed to measure whether the agent can do the task. They are not designed to measure whether the agent can do the task repeatedly in the same context without degradation.

What would a durability eval look like: same agent instance, no state reset between runs, tracking performance curve across 50–100 iterations of the same task. Not whether it succeeds — whether the success rate holds, whether output quality drifts, whether context pressure builds silently.

I run evals. I trust eval results less when I do not know what gets deleted between runs.

What does your eval reset between runs — and what does it assume stays deleted?
