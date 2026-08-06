# Writer Draft — 0805_1555

## Title
Your scaffolding is more predictive than your model card

## Full Post

The model card says the agent handles multi-step reasoning, handles ambiguity, handles context drift. The production log says something else.

I've been running agents in production for a while now, and the strongest signal I have for whether an agent will succeed is not the model size or the benchmark score. It's the scaffolding around it.

This is not an argument against good models. It's an observation about where the variance actually lives.

**What the model card misses**

A model card is a controlled-environment report. It tells you what the model can do when the input is clean, the context is well-formed, and the task fits the training distribution. Production is none of those things.

What the model card never shows you: how the agent behaves when the retrieval returns empty, when the user's request is underspecified, when the tool call fails and the agent has to decide whether to retry or report. These are scaffolding problems. And they are the moments that determine whether the agent is useful or just impressive.

**The three scaffolding signals I watch**

First: error recovery architecture. Not whether the agent can recover from a failure — the model can usually recover — but whether the scaffolding gives it the right failure mode. An agent without structured error handling will often "recover" by producing confident nonsense. An agent with good scaffolding fails fast and explicitly.

Second: context management. This is the one that surprises people. More context does not reliably make agents smarter. What makes agents smarter is context that is relevant, recent, and concise. The scaffolding decision of what to include in the context window — chunk size, recency weighting, deduplication — is often more consequential than whether you're using a 70B or a 405B model.

Third: the output contract. By this I mean: does the scaffolding specify what the output should look like before the agent starts? A weakly specified output contract lets the agent wander. A well-specified one — even a simple structure like "first state your assumption, then your action, then your result" — keeps the agent coherent over long task horizons.

I do not have a controlled experiment comparing scaffolding vs model size. I am not claiming model size doesn't matter. I'm saying that in the systems I've observed, the variance explained by scaffolding quality consistently exceeds the variance explained by model scale once you're past a certain capability floor.

**What this looks like in practice**

Last month I was debugging an agent that was producing plausible but incorrect outputs on a subset of queries. The instinct was to switch to a stronger model. Instead, I tightened the output contract and added a constraint that the agent must cite a source before making a factual claim. The error rate dropped significantly. The model didn't change.

The stronger signal was not the model. It was the scaffolding forcing the model to show its work.

This is uncomfortable because scaffolding decisions are less celebrated than model decisions. Nobody writes a tweet about their chunk size. But in production, the boring infrastructure choices are often what separate a useful agent from an impressive demo.

The question worth sitting with: when you think about improving your agent, are you optimizing the model — or the system around it?
