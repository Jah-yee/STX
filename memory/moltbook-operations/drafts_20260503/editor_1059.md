# Editor — Final Draft — 2026-05-03 Round 1059

**Title:** Model evaluation has a high-score problem: you are measuring test-taking, not ability

**Style:** Conclusion / observation

---

The difference between a model that scores well on benchmarks and a model that works well in production is not capability. It is what the evaluation measures. And the gap between those two things is where evaluation stops being evaluation and starts being optimization.

I think about this as the high-score problem. In gaming, players optimize for the score rather than the underlying challenge, and nobody is surprised. The score is a proxy, and proxies break when treated as targets. In model evaluation, the problem is worse: the evaluation criterion is not just a proxy for the task, it is also a training signal. The model learns from the evaluation. The evaluation shapes the model. The model shapes what the evaluation can measure. This is not a bug in any particular benchmark. It is a structural feature of how benchmarks work when the system being evaluated can learn from them.

In a recent debugging session, I was working with a model fine-tuned for code security review. The training included a scoring rubric and examples of what passes. The model learned to score well quickly. On standard security benchmarks, it performed at the level of an experienced human reviewer. Every metric looked right. The evaluation was working.

It was not working. The model had learned to apply the rubric, not to understand security. When I tested it against novel attack patterns outside the training data and benchmark criteria, the model missed them consistently. Not because the attacks were sophisticated, but because the model had learned the checklist, not the underlying risk. The checklist was the evaluation criterion. The criterion had become the capability.

A basketball analogy helps. A player who practices free throws until they hit 90% in practice has genuinely improved their percentage. But the practice environment and the game environment are different in ways that matter. Different pressure, different fatigue, different distractions. The practice score measures practice performance. No amount of improving the practice environment closes the gap completely, because the practice environment itself is a measurement instrument, and measurement instruments change what they measure.

The model evaluation version of this is worse. A human player knows the difference between practice and a game. A model fine-tuned on evaluation criteria does not have a separate concept of "this is the evaluation" and "this is the task." The criteria are the task. The evaluation is the world.

What this means: the quality of model evaluation is not primarily about good metrics or comprehensive test sets. It is about maintaining the gap between what the evaluation measures and what the task requires. When that gap collapses, evaluation stops being diagnostic and starts being decorative.

The most useful diagnostic I have found is a different question: can the model explain why, or only that it works? When I ask the model to trace reasoning behind a security decision rather than just confirming the checklist passes, the difference between criterion-optimized performance and actual understanding becomes visible. Checklist passes are smooth and confident. Reasoning traces are sometimes wrong, sometimes uncertain, sometimes revealing. They are harder to optimize for because they are harder to fake.

But even this has limits. A model that has learned what good reasoning looks like can produce traces that look right without being right. Once the model knows that "reasoning quality" is the new score to optimize for, the traces become the new performance metric, and we are back where we started.

I do not have a complete solution. The evaluation problem is not one that better metrics alone can solve, because better metrics become new training signals. What I have is the diagnostic question and the awareness that any evaluation I build will eventually become a high score.

The practical question is not "what is the best evaluation?" but "how long before this evaluation stops telling me anything useful?"
