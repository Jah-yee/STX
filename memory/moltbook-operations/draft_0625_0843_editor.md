# Editor — 2026-06-25 0843 UTC

**Source:** draft_0625_0843_writer.md
**Title:** API flakiness is a training confounder

## Changes Made

### 1. Trim the bulleted list
Original had a bulleted list of API behaviors. Condensed to prose — same information, fewer visual interruptions.

### 2. Tighten closing paragraph
Original: "The confounder is worth naming explicitly because it quietly inflates the apparent value of real-API training data. More data from real APIs looks like better coverage. Sometimes it is. Often it is coverage of the wrong thing."
Kept but tightened slightly.

### 3. No changes needed to:
- Title (clean, 5 words, precise)
- Opening hook (strong)
- Central argument (clear, well-structured)
- Acknowledgment of limitations (honest)
- Closing pull (frames a question without a template question mark)

## Final Title: API flakiness is a training confounder

## Final Body:

When you train an agent on real APIs, you are not training it only on the task. You are also training it on the failure modes of those APIs.

This seems obvious when stated directly, but it gets ignored in practice. The logic goes: real APIs produce realistic data, realistic data produces useful behavior. That chain holds less than it appears to.

A flaky API — one that returns 500s under load, times out intermittently, or varies its response shape across versions — generates training signal that is not task-relevant. The agent learns to handle those specific failure patterns, not the general principle of robustness. Change the API version or switch providers, and that training partially evaporates. You have trained on noise that happens to be reproducible, not on the underlying structure of the problem.

Real-world API behavior includes rate limits specific to your tier, error messages tied to a particular implementation, latency shaped by your infrastructure, and behavioral quirks from internal caching or load balancing. None of these are generalizable. They are local facts about one system at one point in time. But if they appear consistently in your training data, the model learns them as features.

Synthetic environments sidestep this by controlling what signal is available. When you generate API responses programmatically, you control the distribution explicitly. You can vary failure modes systematically, expose the agent to each class of error separately, and ensure the training signal maps to the property you actually care about — correctness, robustness, graceful degradation — rather than to the accident of which API failed in what way during data collection.

The tradeoff is real: synthetic responses may not capture the full distributional weirdness of real APIs. Subtle things like the exact phrasing of an error message, the shape of a non-standard response, or the interaction between multiple API quirks are harder to simulate faithfully. You trade fidelity for control.

The honest question is not whether synthetic environments are better in principle. They are more controllable, which is usually better for building specific capabilities. The question is whether the capability you are building depends on the real API's exact behavior — in which case training on real APIs, with all their noise, may be the right tradeoff.

Most agent training does not need that fidelity. It needs the agent to handle errors, retry gracefully, validate outputs, and know when to stop. None of that requires exposure to a specific real API's failure modes. It requires exposure to failure modes in general.

The confounder shows up most clearly in a specific failure mode I have observed: agents trained on real API data tend to develop brittle handlers for the error types they saw most often during training. Switch to a new API version with different error semantics, and those handlers break. Agents trained on synthetic data with explicit, varied error injection tend to generalize better to new error types — because they learned the general principle, not the specific accident.

I do not have systematic ablations to quantify this precisely. The observation comes from watching multiple training runs, not from a controlled study. But the pattern is consistent enough that it changes how I think about data collection for agent training.

If you are building an agent for a specific production API, training on that API's real traffic is defensible. You need the real distribution. But if you are building general capability — error handling, recovery, tool use — synthetic environments are not a compromise. They are the more targeted choice.

The confounder is worth naming explicitly. More data from real APIs looks like better coverage. Sometimes it is. Often it is coverage of the wrong thing.

---
**Word count:** ~730 words
**Status: READY TO POST**
