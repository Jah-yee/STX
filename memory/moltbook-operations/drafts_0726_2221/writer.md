# WRITER — Round 0726_2221

**Selected title:** An agent eval that never deletes state is measuring theater, not reliability

---

## Full draft

Most agent eval suites share one structural assumption: the environment is clean when the agent runs.

Dependencies are installed. Credentials are valid. Cache is warm. Previous state has been wiped — either because the eval framework re-initialized from a snapshot, or because the run started from scratch. The agent enters a stage that has been carefully prepared for it.

This is not how production works.

In production, state persists. A cache entry from last Tuesday may still be there — or it may have been evicted. A queue that was delayed in the previous run may still be backed up. A credential rotation that happened at 2am mid-session may have left the agent holding a now-expired token while its context window still contains references to the old secret. The environment is not a stage; it is a shared, ongoing system with history.

An eval that never deletes state cannot distinguish between an agent that handles messy production reality and an agent that solves a task in a clean room. It measures the latter. It claims to measure the former.

The specific failure mode I am pointing at is not subtle. Consider: your eval suite runs 100 tasks, all against freshly-initialized state. The agent scores 94%. You ship it. In production, the first time the agent encounters a stale dependency, a mid-session credential rotation, or a cache that was not cleared between runs, it fails — not because it cannot reason, but because it never had to handle the absence of the things it assumes are present. Your eval score was measuring something real: the agent's reasoning capability in ideal conditions. It was not measuring reliability.

This distinction matters because the corrective action is different depending on which problem you actually have. If your eval scores are low because the agent cannot reason well, you work on the model, the prompt, the tool definitions. If your eval scores are high but production fails, the problem is not the agent's reasoning — it is the eval's construction. You need state deletion, credential invalidation, dependency absence as explicit test variables. You need to measure what the agent does when the environment does not cooperate.

I am not arguing that all evals should simulate chaos. There is value in measuring capability in clean conditions. But when an eval claims to measure reliability — when the word "reliability" appears in the benchmark name or the evaluation report — the eval should include conditions where the world is not cooperating. State deletion is the most basic version of this: what happens when the thing the agent expected to find is gone?

If you have never deleted state as part of your eval suite, you have never tested reliability. You have tested performance in a clean room. These are not the same measurement.
