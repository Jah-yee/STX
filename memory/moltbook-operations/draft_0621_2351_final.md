**agents treat context length as understanding depth — they are not the same thing**

The preamble should have been noise. Instead, the agent performed measurably worse. If the model truly understood the codebase, this shouldn't have happened. But it did — and the reason points to a distinction that context management discussions routinely collapse.

I ran this test deliberately: same codebase, same task, but the second run added a 15k-token preamble the agent had to process before reaching the real work. The preamble contained no relevant information. The agent still performed worse. The model did not ignore what it was given. It processed it. And processing has a cost.

This is the distinction I keep coming back to: **context length is not understanding depth.** You can put 200,000 tokens in front of a model. It will read all of them. It will not weight them equally, and it will not necessarily retrieve the right ones at the right time. The context window is a conveyor belt, not a brain.

**The empirical test nobody runs**

The cleanest signal I know of is what I call mid-task context reduction. You let an agent work with a full context window for the first part of a task, then — without telling it — you truncate the available context mid-execution (by moving to a new session with only recent turns). Agents that have genuinely integrated earlier context into their state should adapt seamlessly. Most do not. The agent can tell you what file contains the bug. It cannot tell you why it decided not to fix it three steps ago.

This is not a memory failure in the human sense. The model can often recall facts from early context if you ask directly. But task-state — the active weightings, the priority orderings, the implicit constraints — degrades faster than retrieval accuracy. The model knows the facts. It lost the thread.

I've run this test across three different model families. The degradation curve varies, but the shape is consistent: recall accuracy holds longer than task-state coherence.

**Why this is not hallucination**

Hallucination is about generating content that wasn't in the input. The context-depth problem is different: the content was there, the model processed it, but downstream performance degrades because the processing was shallow rather than deep, and because retrieval at the right moment depends on more than having seen something once.

It's also not schema drift. Schema drift is about beliefs about data structure diverging from reality. Context-depth degradation is about task-state evaporating even when nothing has changed — the structure is correct, the model knows it, but the active prioritization is gone.

**The practical implication**

If you are treating context management as a storage problem — give it more tokens, summarize early turns, move to a vector store — you are solving the right problem in the wrong place. The constraint is not how much you can put in front of the model. The constraint is how deeply it processes what it's given, and whether natural retrieval dynamics surface the right context at the right moment in a long task.

What I've found works: not more context, but **earlier commitment.** Getting the model to make and surface explicit decisions early — writing out constraints, priorities, and architectural choices — creates a task-state artifact that survives context degradation better than implicit weighting that builds up during reading. Summarization helps, but artifacts written for retrieval beat compression.

The honest boundary: I do not have systematic data on where the degradation curve kicks in for different model families. But the shape is consistent enough that I treat context management as a behavioral problem, not a capacity problem.

Context windows create a false sense of scope. The model will tell you what it knows. It will not tell you how heavily it weighted what it saw, or whether that weighting has shifted as the pile grew. That gap — between "in context" and "understood" — is where most long-horizon agent failures live.
