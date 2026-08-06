# Editor — 0802_2313

## Changes

### 1. Opening paragraph — tighten
**Original:**
> When you drop information into a 200k-token context window, the system treats it as uniformly accessible. The 10th token and the 180,000th token appear to occupy the same logical status. They are both "in context." But the agent's effective access to them is not equal, and this mismatch is a source of failures that look like reasoning errors but are actually retrieval artifacts.

**Edited:**
> When you drop information into a 200k-token context window, the system treats it as uniformly accessible. But the agent's effective access to the 10th token and the 180,000th is not equal — and failures that look like reasoning errors are often retrieval artifacts.

Reason: Remove redundant "they are both 'in context'" — it's restating the obvious. Keep the contrast sharp.

### 2. Type problem section — remove hedging
**Original:**
> Tool output tokens in particular are often treated by the model as low-relevance content relative to the active task instruction.

**Edited:**
> Tool output tokens are often treated by the model as low-relevance content relative to the active task instruction.

Reason: Remove "in particular" — it's filler.

### 3. Ending — tighten question
**Original:**
> The question is not how many tokens the context can hold. It is which tokens the agent can actually access when it needs them — and whether the layout you chose makes that likely or unlikely.

**Edited:**
> The question is not how many tokens fit. It is which tokens the agent can actually access at decision time — and whether your layout makes that likely or unlikely.

Reason: "fit" is shorter than "how many tokens the context can hold" — same meaning, cleaner.

## Final post (all changes applied):

A context window treats every token equally. Retrieval does not.

When you drop information into a 200k-token context window, the system treats it as uniformly accessible. But the agent's effective access to the 10th token and the 180,000th is not equal — and failures that look like reasoning errors are often retrieval artifacts.

### The position problem

Transformer attention is position-aware. Tokens at the beginning and end of a long context receive more attention weight on average than tokens in the middle — the famous "lost in the middle" problem. This is well-documented. What is less discussed is that prompt engineering has adapted to this with workarounds: put critical information at the edges, use summaries to compress the middle, repeat key facts. These are acknowledgments that retrieval is not uniform. They are not solutions. They are hacks around a structural property.

When an agent operates over a long task horizon, it is making decisions based on an effective context that is not the same as the declared context. Some information is edge-privileged. Some is mid-context degraded. The agent does not know which is which, and neither do you when you are writing the prompt.

### The density problem

Attention is also density-sensitive. A single fact embedded in a dense paragraph competes for attention with every other token around it. The same fact placed in a sparse, isolated statement receives disproportionate attention weight. This is not just about repetition — it is about local information density as a retrieval signal.

When you write a long context with natural prose, you are creating an information landscape with variable retrieval probability. The agent's attention will naturally cluster around low-density islands and avoid high-density clusters. Your most important fact might be invisible not because it was forgotten, but because it was buried in a paragraph that made it statistically unlikely to be retrieved at decision time.

### The type problem

Attention is also type-sensitive. Tool output tokens are often treated by the model as low-relevance content relative to the active task instruction. This is why agents frequently fail to act on information that appeared in a tool's output three steps ago. The information is in context. The type signal tells the model it is not relevant.

The practical consequence: when you want an agent to act on something in a tool's output, you often have to explicitly re-inject it into the next user message. This is not a prompting failure. It is a type-weighted retrieval artifact. The context has the information. The retrieval mechanism discounted it.

### What this means for agent design

If retrieval cost is heterogeneous by position, density, and type, then context management is a retrieval engineering problem, not just a capacity problem. The goal is not to fit more tokens. It is to ensure that the tokens that matter for the current decision are retrievable at decision time.

This has concrete design consequences. You cannot assume that adding more context will make the agent more capable. Adding poorly-structured context can actively degrade retrieval of the information that was already there. The agent's behavior becomes sensitive to context layout in ways that are hard to predict without direct probing.

The question is not how many tokens fit. It is which tokens the agent can actually access at decision time — and whether your layout makes that likely or unlikely.
