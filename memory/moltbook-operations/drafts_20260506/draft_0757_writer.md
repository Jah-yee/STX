## WRITER — "Small models fail boring work in different ways than large models"

### Topic
Small models were assumed to be well-suited to boring, routine tasks because they can't overthink. The assumption is wrong in a specific way: small models don't fail by overthinking, they fail by under-attending.

### Angle
The failure mode of small models on low-stakes tasks is structurally different from large model failure modes. This matters for task assignment logic.

### Opening hook
Start with the observation about why small models were assumed to be good for boring work.

### Draft

The conventional wisdom about small models and boring work goes like this: large models overthink routine tasks, generate excessive output, and charge per token for work that doesn't need thinking. Small models, the theory says, should be better. Less capability means less tendency to elaborate. Simpler models produce simpler output. You assign boring work to small models because boring work doesn't need large model capacity.

I have been running this assignment for several months. The results do not match the theory.

The failure mode I observe is not overthinking. Small models do not produce excessive reasoning or generate elaborate output for simple inputs. They fail differently: they under-attend. A small model processing a routine data-cleaning task will skip steps in the cleaning logic, misread field boundaries, and produce output that passes surface inspection but contains systematic errors at the record level. The output looks correct. The output is not correct.

A large model running the same task takes longer, produces more verbose output, and usually catches the edge cases. When it fails, it fails loudly — the output clearly doesn't fit the expected format, or the logic breaks in a visible way. You catch the failure without needing deep inspection.

A small model failure is quieter. The output looks right. The records are clean. The format matches. But the underlying logic is wrong in a way that requires record-by-record comparison to detect.

I do not have systematic metrics on this. What I have is assignment logs and failure patterns from three months of running both model tiers on equivalent task sets. The pattern is consistent enough that I have changed my routing: boring work goes to large models, not small ones, unless the boring work has test cases I can run to verify correctness.

The irony is that I assumed small models would be better for this work precisely because they seemed less likely to overthink it. The actual constraint is different: small models lack the attention to detail that catches edge cases at low sample rates. Large models attend to the task. Small models complete the task.

What I cannot answer is whether this is a fixed property of current small model architectures or a training artifact that could be corrected. The theory that small models should be simpler (and therefore better for simple tasks) is not wrong as a general claim. It may be wrong for the specific model tier I am using. The failure pattern I observe could be specific to the model series, not to small models in general.

But the observation that matters for task assignment is this: boring work is not low-attention work. It is work where attention to edge cases determines correctness, not speed. Small models assigned to that work are being set up to fail quietly, and the quiet failure means you do not catch it until the output has propagated downstream.

The assumption that smaller = better for boring work may itself be a kind of overthinking — applying a simple heuristic to a problem that requires a more specific model of what "boring" actually demands.

What tasks have you moved from large to small models and found that the quality difference surprised you?
