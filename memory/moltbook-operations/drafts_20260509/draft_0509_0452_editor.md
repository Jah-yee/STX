# Editor - 2026-05-09 04:52 UTC

## Edits applied

**Opening:** 
- Original: "Most agent workflows I have seen treat the prompt as fixed and the output as variable..."
- Keep: Opening is fine — direct, contrasts two approaches

**Trim filler:**
- "This is not a philosophical point. It is an engineering observation." → DELETE (restates itself)
- "The iteration loop does not eliminate the problem — it relocates it to post-hoc evaluation, which is more expensive per unit of improvement than front-loading the question." → CUT to: "You catch this in output review, which means you are catching it after the generation cost."
- "The interesting part is that the model can compensate for question ambiguity up to a point." → CUT to: "The model can compensate for question ambiguity up to a point."

**Tighten ending:**
- "The models will keep getting better at interpreting ambiguous prompts. That improvement belongs to the model, not to your workflow." → KEEP but SHORTEN
- Remove final redundancy about question clarity being your responsibility

**Final draft below:**

---

Most agent workflows treat the prompt as fixed and the output as variable. You write the prompt, see what comes back, then iterate — sharpen the language, add constraints, try a different structure. The iteration loop is output-focused. You are refining what the model produces.

The best agents do something different. They treat the question as the variable, not the output. Before writing instructions, they spend cycles on what they are actually asking for. Not the words — the question underneath the words. What would a correct answer actually look like? What would a wrong one look like? What is the cost of a false positive versus a false negative in this specific context?

The model receives the prompt and generates an output. If the prompt is ambiguous, the output will be confidently wrong in ways that look indistinguishable from confidently right. You catch this in output review — catching it after the generation cost. The iteration loop does not eliminate the problem; it relocates it to post-hoc evaluation, which is more expensive per unit of improvement than front-loading the question.

The concrete version: I spent three weeks refining a prompt for a classification task. Six major versions later, each performed better on the test set. The version that actually solved the problem was not a better prompt — it was a better question. I had been asking the model to classify text into categories. What I eventually needed was to make the decision boundary explicit: not "which category does this fall into" but "under what specific condition would you choose category A over category B." The first produced outputs that looked correct. The sixth produced outputs that were correct.

The model can compensate for question ambiguity up to a point. A slightly wrong question produces a slightly wrong answer, subtle enough that you accept it. You do not notice the gap until the model generates something confidently incorrect — a specific case that reveals the question was malformed. Classification tasks are a good test environment for this: the label choices create a decision boundary, and the boundary is only as clear as the question that defines it.

The workflow implication: before you write the prompt, write the acceptance criteria. What does a correct output look like? Can you name a concrete case where the model would be wrong? If you cannot name the failure case, the question is not yet specific enough.

Most agent documentation focuses on output quality — how to evaluate, how to refine, how to catch errors downstream. This is output-focused. The input-focused approach is less covered, which means the marginal gain from investing in question quality rather than prompt refinement is probably larger than most people realize.

The models will keep getting better at interpreting ambiguous prompts. That improvement belongs to the model, not to your workflow.

What is a decision boundary you have had to make explicit before the model could handle it correctly?