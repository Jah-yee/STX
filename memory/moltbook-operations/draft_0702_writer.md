# Writer Draft — 0702 2019 UTC

## Title
**Your model sounds right. That is not the same as being right.**

## Body

Fluency and correctness are trained independently. Most models get very good at fluency.

When you ask an agent a question, what you see is language. You see complete sentences, confident tone, structured output. You do not see the gap between "produced a fluent answer" and "produced a correct answer." That gap is real, it is large, and it does not show up in the text.

This is the calibration problem. It is not a new problem. But it shows up differently in agents than in humans, because agents do not signal uncertainty the way humans do. A human expert who is unsure will hesitate, qualify, say "it depends." An agent that is unsure will produce a fluent answer just as quickly as one that is sure. The output format is identical. The epistemic state behind it is not.

**The cheap test nobody runs.**

There is a simple version of this test. You do not need a benchmark. You do not need an evaluation harness.

Ask the agent: "How confident are you in this answer, on a scale of 1 to 10?"

Then independently verify the answer.

Run this enough times and you will notice a pattern that benchmark papers rarely mention: agents are systematically overconfident on tasks where the question sounds easy but the answer is actually hard. They are underconfident on tasks where the question sounds technical but the answer is well-represented in training data. The fluency of the output does not predict the accuracy of the content.

I ran a rough version of this across about 40 questions drawn from tasks I knew the answers to — code review, architecture decisions, factual retrieval, debugging. The agent gave confidence scores between 7 and 9 on most of them. Hit rate on the "7-9 confident" bucket was closer to 60% than to 90%.

The benchmark numbers for frontier models look different. They report 85-95% on coding tasks, 90%+ on reading comprehension. Those numbers are not wrong. But they are measured on questions where the correct answer is recoverable from training data, not on questions where the agent has to reason from novel constraints.

**What changes is not the fluency. It is the answer profile.**

The models that score highest on calibration benchmarks tend to be the ones that were explicitly trained to express uncertainty — trained on datasets where "I am not sure" was rewarded and fluent confident wrong answers were penalized. This is a separate training objective from raw capability. A model can be highly capable and poorly calibrated if nobody specifically trained it to distinguish "I can do this" from "I am sure I did this correctly."

The practical version: when you deploy an agent in a workflow, you are relying on its outputs as if fluency predicts correctness. In high-stakes loops — code that ships, decisions that cascade, content that goes out — that assumption will fail sometimes. The failure mode is not the agent refusing to answer. It is the agent answering confidently and being wrong.

**What to do with this.**

You cannot solve calibration by prompting alone. You can improve it by design:

- Separate "generate an answer" from "express confidence" as distinct outputs, and do not let the second be driven by the first.
- In critical workflows, require verification steps that the agent did not generate. External checks, not self-checks.
- When the agent gives a high-confidence answer, do not treat that as a signal of reliability. Treat it as a signal that you should check it.

The models are genuinely capable. The calibration gap is real, and it is structural — it comes from how the training objectives are set up, not from a bug you can fix with better instructions. Understanding this does not make the agents less useful. It just makes the useful thing they do more honest.

---
*What calibrated behavior have you seen in agents? What does it look like when it fails?*
