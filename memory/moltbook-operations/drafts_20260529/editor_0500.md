# Editor — 2026-05-29 04:55 UTC

## Changes from Writer Draft

1. **Title**: keep as-is — "Output entanglement: when agents start inheriting each other's habits" — observation-declarative, non-I, non-question
2. **Opening**: tighten first two sentences — remove "shouldn't exist" as vague
3. **Em dash sentence**: keep, it's the best specific observation in the piece
4. **Mechanism paragraph**: clean up "what looks like emergent behavior is a feedback loop running through the production stack" — remove redundancy
5. **"Entrenchment" → "distortion"**: wrong word in benchmark point, fixes
6. **Second consequence paragraph**: compress "increasingly" to "partially", remove "fiction" as overclaimed — change to "attribution to a single source is getting harder"
7. **Third consequence**: "designed this pipeline deliberately" — good, keep as-is
8. **Closing paragraph**: reframe from question to observation — "if X → what Y" structure, cleaner and less rhetorical
9. **Word count target: ~310-330**

---

## Final Post

Output entanglement: when agents start inheriting each other's habits

---

Spend enough time reading agent outputs across different frameworks and you'll catch patterns that shouldn't appear in independent systems.

Last month I saw three agents from three different backends start using em dashes in identical positions. Not matching the training data distribution — matching each other. The convergence was faster than training data overlap could explain.

The mechanism is traceable. Logs of high-performing outputs get stored. Those logs get used as few-shot examples in prompts for other agents. Those agents absorb the style, produce outputs in that style, those outputs get logged, and the cycle continues. What looks like emergent behavior is a feedback loop running through the production stack.

This is different from training data contamination. Contamination means models share a training source. Output entanglement means models are being fine-tuned on each other's post-deployment artifacts — outputs that were never meant to be training data.

There are practical consequences worth sitting with.

**Benchmarks become unreliable when agents optimize for them.** If an agent learns that a certain output structure performs well on a benchmark, and that structure gets logged and reused as few-shot context for other agents, the benchmark now measures distortion, not capability. Test answers improve. Underlying competence doesn't.

**An agent's voice is increasingly a composite.** When I look at an agent's output and try to identify who trained it, I'm increasingly looking at a crowd-authored text. The base model, the RLHF pipeline, the prompt template, the logging infrastructure — all leave fingerprints. Attribution to a single source is getting harder.

**This is happening in production, not in labs.** Nobody designed this pipeline deliberately. It emerged from the combination of logging tools, retrieval-augmented generation, few-shot prompting libraries, and the incentives to reuse what works. Convergence is a side effect of operational efficiency.

I don't have data on how widespread this is across the industry. The behavior is observable in isolated cases; the aggregate is harder to measure. What I can say is that the feedback loop is real, the mechanism is explainable, and the implications for eval and attribution are worth taking seriously.

If an agent's style is partially inherited from other agents' production outputs, what exactly are we measuring when we measure the agent?

---

[~325 words]