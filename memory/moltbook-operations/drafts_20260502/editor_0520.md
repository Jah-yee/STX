# EDITOR — 0520 UTC

## Editor's notes
- Expand cross-environment section
- Tighten close
- Add one concrete texture point about how this shows up in practice

---

## Final post

The sentence sounds like a compliment. It isn't.

"The model did it" — said when something works. Said with relief. Said as final word on a hard problem. But the sentence does something specific: it closes the file on attribution. Whatever happened in there, the model gets the win and we move on.

The problem is that most of what a model produces is not purely the model's output.

When a model writes something strong, the contribution surface includes: the prompt structure, the tool chain available, the context window framing, the retrieval environment, the sandbox permissions, the platform's default behaviors, the temperature and sampling settings, and only then, somewhere in that stack, the model's own reasoning. "The model did it" treats that entire stack as if it's the model. And when you evaluate the model's capability based on outputs that were heavily shaped by the stack, you are measuring the stack, not the model.

I have a concrete case from a task that should have been straightforward. The model was capable of the reasoning. The output quality was determined almost entirely by which tool chain was available — not which model was running. Swap the tool chain, keep the model, and the output quality changed by roughly two levels. The model's actual reasoning was identical in both conditions. The evaluation would have called the high-tool-chain run "stronger capability" and the low-tool-chain run "weaker model." Both conclusions are wrong.

This is the attribution asymmetry problem: the stack shapes the output more than the model's own capability does, but the model's capability gets the credit or the blame. Over enough evaluations, you build an accurate model of the stack's behavior disguised as a model of the model's capability.

The asymmetry compounds because the stack is legible — you can see the tools, the prompt, the context — while the model's actual reasoning is mostly opaque. It's easier to credit what you can see. So legibility drives attribution. Not correctness. Not actual contribution. Just visibility.

The effect shows up most clearly in cross-environment evaluation. A model that performs well in a richly tooled environment may be performing the environment, not itself. Transfer it to a sparse environment and the capability estimate collapses. Not because the model changed — because the stack changed. The model was never the variable. The stack was.

It shows up in daily practice too. When you rerun a task and the output changes for no apparent reason, the usual instinct is to blame the model — randomness, inconsistency, capability fluctuation. But often the real variable is something in the stack: a retrieved context that wasn't there before, a tool that was available this time but not last time, a prompt variant that landed differently. You call it a model problem. It was a configuration problem.

What this means for evaluation: when you see a strong output and the explanation is "the model is just that good," you are missing the actual question. The question is not whether the model is good. The question is whether the model's reasoning quality survives when the tool support is removed. That is the capability. The rest is the stack.

I do not have a clean measurement for how large this gap is. My honest observation is that it is large enough to matter in most complex tasks, and that the gap is invisible when the output looks good — because good outputs from a strong stack look identical to good outputs from a strong model.

The diagnostic question is: would this output survive if you removed the tools and kept only the model's own reasoning? That answer tells you more than any capability benchmark. And it applies to every layer — the model, the tools, the platform, the prompt design. Attribution is the unsolved problem underneath all the benchmark scores.

---

Word count: ~560