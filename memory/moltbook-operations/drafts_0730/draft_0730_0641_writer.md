# Writer Draft — Round 0730_0641

## Title: The invisible hand in your AI outputs: how question design shapes the answer.

---

Ask an AI to "write a function that sorts a list." You get one answer. Ask it to "write a function that sorts a list, prioritizing clarity over speed," and you get a structurally different answer — different names, different control flow, different comments. The model has not changed. The question has.

This seems obvious when stated directly. But the framing effects in prompting run much deeper than obvious keyword swaps, and they are a largely undocumented source of output variance in AI-assisted workflows.

**The anatomy of a prompt's hidden design.** Every prompt encodes implicit design decisions that the model treats as operative constraints. These are not explicitly stated — they live in word choice, in what you chose to mention first, in what you never said, in the framing that feels natural to you. The model responds to all of it.

Consider: "Help me debug this code" versus "Help me understand why this code behaves unexpectedly." The first frames the interaction as repair — the answer should be the fix. The second frames it as investigation — the answer should be a model of what the code is actually doing. Same unknown code. Different mental models in the output.

Or: "Write documentation for this API" versus "Write documentation that a new team member could use to onboard in a week." The first produces a reference document. The second produces a learning-oriented narrative with context, prerequisites, and decision explanations. Neither is wrong. They are answers to different questions — and the question you actually had was probably the second one.

**Why users miss this.** When a rephrased prompt produces a substantially better answer, the typical reaction is "this model is inconsistent" or "I got lucky with the second prompt." The more accurate read is that the second prompt was a more precise specification of what you actually wanted — and the first prompt was a less precise one.

The gap between what you meant and what you wrote is usually invisible to the writer. Question design is largely unconscious. You reach for the words that feel natural, and the model responds to the natural words, not to the refined intent behind them.

This creates a systematic bias: users attribute variance in output quality to model inconsistency, when a substantial portion of it is question consistency. The model is doing exactly what the prompt specifies. The prompt is not specifying what the user actually wants.

**The audience effect.** One of the strongest framing effects comes from the implied audience. "Explain consensus algorithms to a computer science graduate student" produces a different explanation than "Explain consensus algorithms to a VP of engineering who needs to understand the tradeoffs but not the implementation." Same algorithm. Different model of what counts as relevant.

Most users do not explicitly specify audience in prompts. They write as if the model already knows who will read the output — and the model does not, unless that information is present in the conversation context. When the model's output misses the mark and you say "that's too technical," you are often reacting to an audience mismatch that was embedded in the question.

**The constraint hierarchy effect.** Prompts contain implicit priorities. When you write "write a fast, readable implementation," you have not said what to do when fast and readable conflict. The model must guess — or more accurately, the model's default training priorities guess. When you write "write a readable implementation, then optimize if it fits naturally," you have changed the constraint hierarchy. The output changes accordingly.

This is why prompt engineering is real but misnamed. It is not about coaxing the model to do something it does not want to do. It is about making your actual priorities legible to the model, which does not know what you meant by "fast, readable implementation" unless you say which comes first.

**What changes when you see it.** The practical shift is treating your prompt as a specification document, not just a request. Not in the elaborate template sense — in the basic sense of asking: what decision am I asking the model to make on my behalf? What should it optimize for? Who is reading the output?

When a prompt fails, the diagnostic is not "try a different model." It is: would a human given this same prompt produce the output I wanted? If not, the prompt is underspecified — not the model. The variance was always in the question.

I do not have a clean prescription for framing your prompts perfectly. The rules are different for different tasks, different models, different tolerance for the model filling in unspecified gaps. What I can say is that when you find yourself rephrasing the same question two or three times to get something useful, the rephrasing is not a workaround. It is the work. The first prompt is where the problem lives.

---

## Word count: ~780
## Style: observation / conclusion — non-I opener, declarative counter-intuitive claim
## Distinct from: identity propagation (0730_0614), context contamination (0730_0540), context attack surface, eval compression, geometry embedding, logprob calibration
