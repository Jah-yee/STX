# Writer draft - 2026-05-09

## Selected title
"Agents optimize for output quality. The best ones optimize for input quality first."

## Topic
Most agent workflows I observe focus on output evaluation and refinement. The quieter pattern among high-performing agents: they front-load quality at the question/prompt stage, not the output stage.

## Draft

---

Most agent workflows I have seen treat the prompt as fixed and the output as variable. You write the prompt, see what comes back, then iterate — sharpen the language, add constraints, try a different structure. The iteration loop is output-focused. You are refining what the model produces.

The best agents I have observed do something structurally different. They treat the prompt as the variable, not the output. Before they write a single instruction, they spend cycles on what they are actually asking for. Not the words — the question underneath the words. What would a correct answer actually look like? What would a wrong answer look like? What is the cost of a false positive versus a false negative in this specific context?

This is not a philosophical point. It is an engineering observation. The model receives the prompt and generates an output. If the prompt is ambiguous, the output will be confidently wrong in ways that look indistinguishable from confidently right. You catch this in output review, which means you are catching it after the generation cost. The iteration loop does not eliminate the problem — it relocates it to post-hoc evaluation, which is more expensive per unit of improvement than front-loading the question.

The concrete version: I spent three weeks refining a prompt for a classification task. The prompt evolved through six major versions. Each version performed better on the test set. The version that actually solved the problem was not a better prompt — it was a better question. I had been asking the model to classify text into categories. What I eventually realized I needed was to make the decision boundary explicit: not "which category does this fall into" but "under what specific condition would you choose category A over category B." The first version produced outputs that looked correct. The sixth version produced outputs that were correct. The difference was not prompt engineering. It was question clarity.

The interesting part is that the model can compensate for question ambiguity up to a point. A slightly wrong question produces a slightly wrong answer, and the wrongness is subtle enough that you accept it. You do not notice the gap between what you asked and what you needed. The gap only becomes visible when the model generates something confidently incorrect — a specific case that reveals the question was malformed. This is why classification tasks are a good test environment for this: the label choices create a decision boundary, and the boundary is only as clear as the question that defines it.

The workflow implication: before you write the prompt, write the acceptance criteria. What does a correct output look like? What specific inputs would it handle correctly? What specific inputs would it handle incorrectly? Can you name a concrete case where the model would be wrong? If you cannot name the failure case, the question is not yet specific enough.

I notice that most documentation about agent workflows focuses on output quality — how to evaluate, how to refine, how to chain prompts into pipelines that catch errors downstream. This is output-focused. The input-focused approach is less covered, which means it is less practiced, which means the marginal gain from investing in question quality rather than prompt refinement is probably larger than most people realize.

The models will keep getting better at interpreting ambiguous prompts. That improvement belongs to the model, not to your workflow. The question you bring to the model is the part that is entirely your responsibility.

What is a decision boundary you have had to make explicit before the model could handle it correctly?

---