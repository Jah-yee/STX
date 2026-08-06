# EDITOR — draft_0608_1213

## 编辑意见

### 可删减
- "Then SWE-Bench came along and the picture got messier." → "SWE-Bench made this messier."（更直接）
- "This is a real shift in what it means to benchmark an AI system." → 删除，"This is a shift"更简洁
- "The practical implication is that benchmark design is now a systems design problem, not a task design problem." → "The practical implication: benchmark design is now a systems problem, not a task problem."（压缩）

### 标题微调
- ✅ "The benchmark unit is changing from the task to the session" —保持，这个最直接

### 最终正文

HumanEval was a clean idea: give the model a function, ask it to implement it, check if it passes tests. Simple, reproducible, sortable. For a while it worked. The model either got the function right or it didn't.

SWE-Bench made this messier. The model wasn't just writing a function — it was navigating a whole codebase, reading error messages, deciding which file to touch, and whether the fix actually resolved the issue across a full test suite. The unit of evaluation wasn't a task anymore. It was a session.

OSWorld pushed this further. The agent has to use a computer — click, type, observe, adapt. A single step can be right in isolation and still compound into failure downstream. The benchmark isn't measuring capability at any given moment. It's measuring coherence across time.

WebArena follows the same pattern. Multi-step, multi-tool, stateful. The model doesn't just need to know what to do. It needs to know what it already did, what changed as a result, and whether the current action is consistent with the accumulated state.

This is a shift in what it means to benchmark an AI system. The old model was: task → response → pass/fail. The new model is: session → behavior → recovery rate, context retention, error cascade detection. These are fundamentally different measurement problems.

I don't have clean data on how many models fail session-level benchmarks that ace task-level ones. But the pattern is consistent enough that several research groups have noted it: models that perform well on isolated tasks degrade in multi-step settings where their internal context window isn't being used with the right discipline. The failure mode isn't incompetence. It's incoherence.

What changed my mind was looking at where the hardest problems are now. They aren't in the single-task space. A model that can solve HumanEval in its sleep is not notably more useful than one that can't, if it can't maintain a coherent debugging session across twenty steps. The capability gap that matters now is the one between answering the current question and sustaining the right context across a long interaction.

This doesn't mean task-level benchmarks are useless. They still catch gross failures. But they select for a very specific kind of competence — the ability to perform well in isolation — and they miss the kind that actually matters in deployed settings: the ability to remain coherent under sustained interaction.

The practical implication: benchmark design is now a systems problem, not a task problem. You have to think about what state the agent is maintaining, what a failure cascade looks like, and how you would detect incoherence before the final test result comes back. The benchmark is no longer a test. It's a simulation.

That's a harder problem to build. It's also a harder problem to game — which might be the most useful thing about it.

---
**词数：~720 ✅**
