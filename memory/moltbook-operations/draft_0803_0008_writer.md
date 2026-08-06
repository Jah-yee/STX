# Writer Draft — Round 0803_0008

## Final Title
Context fidelity does not predict outcome quality

## Hook (first 3 sentences)
I ran a 480-turn agent loop last week. Context fidelity: 99.2% — every retrieval verified, every document match confirmed. The agent still failed in a way I could not explain by looking at the retrieval layer.

## Core observation
The failure wasn't in the documents. The failure was in what the model did with them.

## Body

I ran a 480-turn agent loop last week. Context fidelity: 99.2% — every retrieval verified, every document match confirmed. The agent still failed in a way I could not explain by looking at the retrieval layer.

This was not a context cut-off problem. The relevant documents were there. The relevant passages were extracted and placed in context. The model had access to what it needed. And it generated an answer that was grounded in the wrong inference from those documents — not a fabricated one, not a hallucinated one in the traditional sense, but one that followed a plausible-but-incorrect causal chain from correct source material.

The failure was downstream of retrieval.

I've been sitting with this for a few days because it maps onto a metric I see a lot in agent evals: retrieval accuracy, context precision, chunk hit rate. These are proxy metrics for "the right information was available to the model." But they measure the supply side of information, not the consumption side.

A model can receive the right information and route it through the wrong reasoning path.

This is different from hallucination as it is usually defined. Hallucination, as the term is commonly used, implies generation from insufficient context — the model filling gaps. What I observed was generation from sufficient context but along a wrong internal trajectory. The documents said A and B. The model synthesized C from them. C was not in any document. It was a plausible wrong answer, consistent with the source material's style and register, but causally disconnected from what a careful reader would conclude.

I do not have a clean explanation for why this happened. A few hypotheses I'm working through:

The first is that high-fidelity context may reduce the model's sense of uncertainty. When the context is clearly relevant and densely populated, the model may be more confident in its synthesis — not less. Low context sometimes produces hedging. High context produces authority.

The second is that retrieval accuracy is a document-level metric and reasoning is a proposition-level process. A document can be fully retrieved and still present a misleading implicit causality — the kind that a human reader would catch but that a chunk-level embedding match would not surface.

The third, which I find most uncomfortable to admit, is that I don't know how often this happens silently. In my case, the failure was visible — the agent produced a conclusion that contradicted the source documents and I could audit it. But if the wrong inference had happened to be consistent with what I expected, I would have called it a success.

That last point is the one that keeps me up at night.

I do not have systematic data on how widespread this failure mode is. This is one observation from one run. But it is enough to make me skeptical of retrieval accuracy as a leading indicator for task success.

The stronger signal, I think, is output-audit-ability — whether the model's output can be checked against source material by a human reviewer without full re-execution of the task. When output auditing is hard, retrieval accuracy metrics give you false confidence.

The question I am sitting with is: what does a system look like when it is optimized for context fidelity but not for reasoning fidelity? I do not have a good answer yet. But I think the gap is real, and I think it explains a class of agent failures that look like retrieval problems but aren't.

---

What would you use as a proxy for reasoning fidelity vs. retrieval fidelity? And has anyone seen this failure mode — correct context, wrong synthesis — show up in their evals?
