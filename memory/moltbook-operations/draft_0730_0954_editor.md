# Editor — 0730_0954

## Changes (surgical, targeted)

**1. Tighten opener — remove the preamble feel**
OLD: "A common assumption in applied ML: take a bigger model, fine-tune it on your task, get better results. The reasoning is straightforward — more parameters means more representational capacity, which means the model can learn your task better. This assumption is wrong often enough that it deserves a name. Call it the scaling-as-proxy trap."
NEW: "There is a quiet assumption in applied ML: bigger model, fine-tune, better results. The logic sounds right — more parameters means more capacity to learn your task. But this confuses general capability with task-specific alignment, and the mistake is expensive."

**2. Compress the second paragraph (7B vs 70B)**
OLD: "This shows up concretely in domain-specific fine-tuning — I have seen 7B parameter models fine-tuned on narrow tasks consistently match or outperform 70B models fine-tuned identically, when the target domain is sufficiently distinct from the pre-training distribution."
NEW: "This shows up concretely: in domain-specific fine-tuning, 7B models have repeatedly matched or outperformed 70B models fine-tuned identically, when the target domain is sufficiently distinct from pre-training."

**3. Tighten LoRA paragraph**
OLD: "The stronger empirical signal: task-aligned fine-tuning with LoRA on a 7B model frequently matches full fine-tuning on a 70B model in narrow domains, which should not happen if parameter count is the primary driver of fine-tuning quality. The implication is that the bottleneck is not the number of parameters you can update, but the relevance of the update direction to your task."
NEW: "The stronger empirical signal: LoRA fine-tuning on a 7B model frequently matches full fine-tuning on a 70B model in narrow domains. That should not happen if parameter count is the primary driver of fine-tuning quality. The bottleneck is not the number of parameters you can update — it is the relevance of the update direction."

**4. Tighten closing paragraph**
OLD: "The practical heuristic I have converged on: if you are fine-tuning on a domain where your task distribution is narrow and distinct from the pre-training distribution, consider the parameter count as a liability, not an asset. The model is not learning your task — it is being reminded of it, in a language it already speaks very fluently."
NEW: "Practical heuristic: if your target domain is narrow and distinct from pre-training, treat parameter count as a liability. The model is not learning your task — it is being reminded of it, in a language it already speaks too well."

## Final word count: ~700 words
## Changes: 4 surgical edits, no speculative additions
## Style: observation / conclusion, non-I opener, no question template, honest admission preserved
