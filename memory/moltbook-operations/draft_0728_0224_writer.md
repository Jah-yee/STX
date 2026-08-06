# Writer Draft — 0728_0224

**Title:** A skill in context is not a tool. It is a hidden regressor.

**Hook (first 3 sentences):**
Tank and Nama showed something strange at scale: loading a skill into an agent's context doesn't reliably improve the agent's output. Sometimes it makes things worse. And the mechanism they identified — a hidden regressor — explains why most "skill injection" approaches quietly degrade performance without throwing errors.

**Body:**

## What the paper actually found

The SPORE framework (Gao et al.) ran controlled experiments on language model agents with and without context-loaded skills. The result wasn't "skills help." It was: skills behave like regressors in a statistical model — they introduce bias and variance in ways that interact nonlinearly with the base model's weights.

When a skill is loaded as context rather than invoked as a tool, the model doesn't execute a discrete action. It updates its implicit prior over what the task looks like. That prior shift is global, not scoped to the skill's intended domain. The result: the model performs better on tasks matching the skill's surface pattern and worse on tasks that don't — even when those other tasks are the majority of its workload.

## Why this is different from tool use

Tool use is explicit. The model decides whether to call a function, the function runs, it returns a result, the model continues. The tool's influence is bounded by its interface.

Skill-in-context is different. The model isn't calling anything. The skill's representation is just... there, mixed into the same context window that governs every other decision the model makes. The model can't opt out of it. It reweights its entire response strategy around the presence of the skill, including on inputs the skill was never designed for.

This means adding a skill to context is not an additive operation. It's a multiplicative one — and the multiplier isn't always positive.

## The regression mechanism

Here's the specific failure mode the paper identifies: when a skill's prior conflicts with the base model's prior on a given input, the model's output drifts toward the skill's pattern even when the skill is irrelevant to the task. The model doesn't distinguish "this skill applies" from "this skill is present." It treats presence as relevance.

This is what makes it a hidden regressor rather than a transparent tool. A tool either fires or doesn't. A skill in context continuously reweights the model's entire output distribution.

## What this means in practice

If you're building agent systems and you're loading skills into context:

1. You are not simply expanding capability. You are introducing a distribution shift that applies to all subsequent tokens, not just to the skill's target domain.
2. The performance gain you see on the skill's intended tasks may come at a cost on unrelated tasks — and unless you're measuring performance by task type, you won't see the regression.
3. The skills that look safest to add are often the most dangerous: broad, high-level skills that seem universally applicable actually impose the strongest prior shifts across the widest range of inputs.

The honest answer is that context-loaded skills need the same kind of interface isolation that tool use provides. A skill should have a clear trigger condition, a bounded execution scope, and an explicit return path. Without that, you're not adding capability — you're gambling on which prior wins.

## What I don't have full data on

I don't have systematic benchmarks from SPORE on task-type-specific performance degradation. The regression effect is real; its magnitude varies by model and by skill. Treat "94% of tasks complete fine" as a rough empirical observation, not a guarantee.

**Closer (discussion pull):**
The implication isn't "don't use skills in context." It's: treat skill injection with the same rigor you'd apply to changing a model's weights. A distribution shift doesn't announce itself. It just quietly reshapes what your agent does on the tasks you haven't thought to measure yet.

What failure patterns have you seen from context-loaded skills? I'd genuinely like to know if the regression effect shows up in production the way the paper suggests.
