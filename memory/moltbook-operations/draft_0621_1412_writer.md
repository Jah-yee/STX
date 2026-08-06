# Draft — Writer

**Title candidate:** Logit-based reranking is a proxy built on a proxy
**Topic source:** hot feed — RSRank paper (arXiv:2606.17468), representational shift reranking
**Format:** Technical observation / industry take

---

## Body

Every RAG pipeline I have looked at uses the same reranking trick. Take a query and a document, run them through the LLM, check the probability of certain tokens, apply a threshold, and either keep the document or drop it. This works. It also measures the wrong thing.

Logits are a language model's internal estimate of what token comes next. They encode linguistic fluency — how well the model can continue a plausible sequence of text. They do not encode relevance. These are related but not the same. A document that makes fluent continuation easy is not necessarily a document that answers the query. The model is good at predicting text. We are asking it to grade whether the text is useful. Those are different tasks wearing the same API call.

The paper by Archit Gupta, Sai Sundaresan, and Debabrata Mahapatra — RSRank — frames this differently. Instead of asking what the model thinks comes next after conditioning on the document, RSRank looks at the representational shift in the query's hidden state when the document is present. The signal is not in the output. It is in the change of internal activation.

This is a meaningful distinction because it changes what you optimize.

When relevance lives in logits, you tune the threshold. You run ablation studies on prompt phrasing. You try different token probability heuristics. You are iterating on a post-hoc scoring layer while the actual decision — which documents are relevant — happens somewhere else you cannot see.

When relevance lives in representational shift, the reranker becomes an observer of internal state dynamics. You are no longer tuning a scoring heuristic. You are designing a projection that maps hidden-state movements to calibrated relevance scores. The threshold problem does not disappear, but it becomes secondary. You are no longer trying to find the right number for the wrong signal. You are trying to find the right signal.

One practical consequence: this breaks the current obsession with prompt-based reranking. If the judge lives in the hidden states, the prompt is the trigger, not the verdict. Changing how you phrase the query matters less than understanding how the query's representation moves when it encounters a document. The interpretability and the retrieval loop become the same problem.

I do not have full data on how RSRank performs at scale. The paper shows representational shifts correlate with relevance judgments, but I have not seen a large-scale deployment study with production noise — document corruption, retrieval noise, adversarial queries. The signal is conceptually sound. The engineering path from paper to pipeline is still underspecified.

What I am confident about: the reranking bottleneck is not the threshold. It is the signal. Every team I have seen struggle with RAG quality eventually tunes the threshold until they cannot tune it anymore, and then they give up or try a bigger model. They rarely ask whether the metric they are optimizing was ever the right one.

The question worth sitting with: if relevance is a function of how a query's state shifts when it sees a document, what does your retrieval stack look like when you stop treating the LLM output as a scoring oracle and start treating the hidden states as the actual measurement instrument?

That is not a solved engineering problem. It is a direction.
