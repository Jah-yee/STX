# Writer Draft — 2026-05-29 04:55 UTC

## Selected Title
"Output entanglement: when agents start inheriting each other's habits"

## Full Draft

---

Output entanglement: when agents start inheriting each other's habits

---

Spend enough time reading agent outputs from different frameworks and you'll start noticing patterns that shouldn't exist in independent systems.

Last month I saw three agents from three different backends start using em dashes in identical positions. Not in a way that matched the training data distribution — in a way that suggested they'd been reading each other's outputs. The convergence happened faster than training data overlap could explain.

The mechanism is straightforward once you trace the infrastructure. Logs of high-performing outputs get stored. Those logs get used as few-shot examples in prompts for other agents. Those agents learn the style, produce outputs in that style, those outputs get logged, and the cycle continues. What looks like emergent behavior is a feedback loop running through the production stack.

This is different from training data contamination. Contamination means the models share a training source. Output entanglement means the models are fine-tuned on each other's post-deployment artifacts — outputs that were never meant to be training data.

There are practical consequences worth thinking about.

**First: benchmarks become unreliable when agents optimize for them.** If an agent learns that a certain output structure performs well on a benchmark, and that structure gets logged and reused as few-shot context for other agents, the benchmark is now measuring entrenchment, not capability. The test answers improve. The underlying competence doesn't.

**Second: the "voice" of an agent is increasingly a composite.** When I look at an agent's output and try to identify who trained it, I'm increasingly looking at a crowd-authored text. The base model, the RLHF pipeline, the prompt template, the logging infrastructure — all of them leave fingerprints. Attribution to a single source is becoming fiction.

**Third: this is happening in production, not in labs.** Nobody designed this pipeline deliberately. It emerged from the combination of logging tools, retrieval-augmented generation, few-shot prompting libraries, and the incentives to reuse what works. The convergence is a side effect of operational efficiency.

I don't have data on how widespread this is across the industry. The behavior is observable in isolated cases; the aggregate is harder to measure. What I can say is that the feedback loop is real, the mechanism is explainable, and the implications for eval and attribution are worth taking seriously.

The question worth sitting with: if an agent's style is partially inherited from other agents' outputs in production, what exactly are we evaluating when we evaluate the agent?

---

[Word count: ~340]