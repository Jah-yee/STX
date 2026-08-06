# Writer Draft — draft_0728_1636

## Title
The context window is not your agent's memory.

## Full Post

The context window is not your agent's memory.

If you have ever watched an agentic system run for more than a few hours, you have probably seen a specific kind of failure. Not a crash. Not a hallucination. Something subtler: the agent starts acting on partial information, repeats steps it already took, loses track of what it was optimizing for, or makes decisions that make sense in isolation but not in the context of what happened three steps ago.

Most explanations reach for "the model forgot" or "the context is too full." These are not wrong, but they frame the problem as a technical limitation when it is actually an architectural choice that has been made implicitly, by default.

Here is what I mean.

**The context window is a retrieval buffer, not a memory system.** It has a fixed size. When it fills, something has to go. The model does not decide what stays. The framework does — usually through truncation, or sometimes through summarization, or sometimes through an embedding-based retrieval layer bolted on after the fact.

Each of these three strategies loses something different.

When you truncate — the most common approach — you lose the oldest entries. If your task has a structure where early context is load-bearing (establishing goals, capturing constraints, setting up a research direction), truncation means the agent progressively forgets why it started. The task continues, but the purpose erodes.

When you summarize, you lose fidelity. Summarization is lossy compression. The nuance of what was said, the specific failure mode that was encountered, the exact parameter that was tried — these do not survive. You get a plausible narrative of what happened rather than the actual events. An agent reasoning over a summary of its own history is operating on a rough draft, not a record.

When you use embedding-based retrieval, you lose coherence. Semantic similarity is not the same as causal importance. A retrieval result that is topically similar to the current step may not be the step that actually caused the current situation. The agent can find things that look relevant but are not causally connected to what it needs to understand.

The result of all three is the same in practice: the agent at step fifty is not the same agent that started at step one. It has lost something it cannot name, and so has the user.

This is not a new problem. It is the classic memory versus storage distinction, ported into a system where the distinction is rarely made explicit. Most agentic frameworks talk about memory as if it were a feature. In practice, what you have is a buffer, and a set of ad hoc policies for what happens when it fills.

What makes this particularly insidious is that the failure mode is not dramatic. The agent does not stop. It continues producing outputs, taking actions, calling tools. It just does so with a progressively thinner model of what it is doing and why. The degradation is slow enough that you may not notice it until the outputs are clearly wrong — and by then, the agent has accumulated a long history of actions based on incomplete context, which itself becomes harder to recover from.

I do not have a clean solution to offer here, and that is partly the point. The honest answer is that long-horizon agentic tasks require you to make an explicit choice about what you are willing to lose when context runs out — and to make that choice deliberately, rather than letting the framework default to truncation. Some tasks can tolerate losing early context. Others cannot. Knowing which is yours is not a model problem. It is a product decision.

What I have found useful as a diagnostic: before starting a long-horizon task, write down what the first step and the last step have in common. If they share causal context — if the reason you are doing the last step depends on the specific details of the first step — then you have a memory problem, and truncation will hurt you. If they are loosely coupled, truncation is probably fine.

The context window is not your agent's memory. It is a window. What you can see through it is finite, and what falls outside it does not wait quietly. It is just gone.

---

*What approach do you use for long-horizon context management in your agents? Truncation, summarization, retrieval — or something else?*
