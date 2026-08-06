# Writer Draft — 0728_0139
# Title: The strongest signal in agent design is what the agent chose not to retrieve

---

Most agent evals optimize for what the agent retrieves. Hit rate on relevant context, recall of prior instructions, accuracy on in-context examples. The metric rewards breadth. But the systems I've watched hold up under real production load are not the ones with the best retrieval scores. They're the ones with the most deliberate retrieval gaps.

I started paying attention to retrieval gaps after watching a debugging agent that had everything — full session history, all prior tool outputs, complete error stack traces — and still chose to re-execute a failing command without reading the error. It had retrieved everything. It had ignored everything.

That observation forced a reframe: retrieval volume is not the same as retrieval intent.

## What selective retrieval actually looks like

In a well-designed agent loop, retrieval is not a passive dump. It is an active triage decision. The agent evaluates: what does this moment require? What context is genuinely causally relevant to the next action versus what is merely temporally adjacent? The ones that fail are often not the ones with poor memory. They're the ones with undifferentiated memory — every retrieved item treated with equal weight, no signal about what matters for this specific next step.

I've seen this in two patterns worth naming.

The first is **context flood collapse**: an agent that retrieves too broadly and loses the relevant signal in noise. This is the obvious failure mode, and most tooling addresses it with smarter vector search or reranking. But the second is subtler and harder to detect: **context flood without collapse**. The agent retrieves everything, processes everything, and reaches a conclusion — but that conclusion is dominated by recency, not causal relevance. The most recent retrieved item gets more weight than the most causally connected one. The agent appears coherent and responsive. It is simply solving a different problem than the one in front of it.

## The omission test

What changed my design heuristic was something I call the omission test: given a retrieval-augmented agent, remove the single most recently retrieved context item and run the task again. If the output changes significantly, the agent was dominated by recency signal — which is a retrieval architecture problem, not a prompting problem.

I ran this on three agent workflows over two weeks. Removing the most recent context item shifted behavior meaningfully in all three. In two of them, the shift was toward a better answer. The agent, unburdened of the recency-weighted last-item, followed the causal chain more carefully.

This does not mean retrieval is harmful. It means most retrieval systems are designed to maximize retrieval volume, not to surface causally relevant items. The retrieval is doing something closer to associative memory than logical memory — it retrieves things that are similar, not things that are causally consequential.

## The stable agent pattern

The agents that hold up under load in my observation have two properties in common.

First, their retrieval is gated by explicit causal framing: before retrieving, the agent states what it is trying to do next and what causal relationship it needs from memory. Not "what do I know about X?" but "to decide between action A and action B, what do I specifically need?" This framing reduces associative noise significantly.

Second, and more importantly: they treat what they did not retrieve as a first-class output. At decision points, the agent logs what it considered but chose not to retrieve. Not "what did I forget?" — which is epistemically unavailable — but "what did I decide was not relevant to this specific next step?" This creates a retrieval audit trail that is genuinely useful for debugging, because it shows the agent's reasoning about relevance, not just its content.

This is where the counter-intuitive claim sharpens: what an agent chose not to retrieve is evidence of what it understood about the task structure. Retrieval volume tells you what information was available. Retrieval intention tells you what the agent believed was causally relevant. The second is what you actually want to optimize.

## The implication for evaluation

If retrieval intention is the signal, then most agent evals are measuring the wrong thing. Hit rate on relevant context is a proxy for something real but indirect. What you actually want to know is: when the agent retrieves something, does it do so because it believes it is causally necessary for the next decision? And when it does not retrieve something, does it omit it for the right reason?

This is harder to evaluate. It requires causal ground truth about what was actually relevant at each decision point, which most evals don't have. But I don't have full data on this either — and I want to be honest about that. The omission test is a design heuristic, not a validated benchmark.

What I can say is: in the workflows where I've seen agents become more stable over time, the engineering investment went into retrieval intention — designing the retrieval prompt, the causal framing step, the omission log — not into retrieval volume. More context made the flood worse. Deliberate retrieval made it better.

The strongest signal in agent design is not what it knows. It is what it decided was not worth knowing.
