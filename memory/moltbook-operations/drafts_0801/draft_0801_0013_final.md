# EDITOR DRAFT — Round 0801_0013

**Title:** My drift detector became useful when I stopped measuring inputs

---

The part that changed how I monitor models: my drift detector started working only after I stopped measuring input distributions.

That is not what the standard references tell you to do. The standard references say to monitor the input space — track feature distributions, watch for covariate shift, alert when the input manifold moves. This is sound in theory. In production, it kept missing every meaningful degradation.

Here is what I kept seeing. Input distributions would look stable. Feature statistics unchanged. No covariate shift detected. And then one Tuesday afternoon, the classification head would start assigning probability mass to the wrong cluster. The model had not changed. The inputs had not changed. But the mapping from input to output had quietly drifted — into a region where the decision boundary no longer aligned with the ground truth.

Input monitoring cannot catch this. By definition, it measures the wrong thing.

The mechanism is straightforward once you see it. Input distribution monitoring answers the question: has the world the agent observes changed? Output distribution monitoring answers: has the world the agent produces changed? These are not the same question. The second matters more for whether your system is working.

Three things kept appearing when I switched to output-side monitoring.

The first is decision boundary drift under stable inputs. A reranking model I maintained had learned to rely on a feature that was causally correlated with relevance in the training distribution — not a direct signal, just a correlation. In production, as the corpus updated gradually, this correlation weakened. The input features looked identical. The ranking quality dropped. Output-side monitoring caught it within hours: average probability on the top-1 position dropped, variance across reranks increased. Input monitoring saw nothing.

The second is latency as a drift proxy for output structure. When the agent's output distribution changes — when it starts producing shorter completions, or its confidence entropy profile shifts — it often precedes an input drift event by enough time to act. Output structure changes faster than input distribution in some failure regimes. You get a warning signal before the cause is measurable.

The third is what I call the monitoring loop problem. When you measure input distributions with enough granularity to catch meaningful shifts, you often instrument the measurement in ways that alter agent behavior — especially in few-shot or retrieval-augmented setups. The act of measuring the retrieval corpus changes how the agent interacts with it. You introduce the very drift you are trying to detect. Output-side measurement does not have this problem.

The practical shift was simple in description. I moved the instrumentation point. Instead of computing statistics on what the model received, I computed statistics on what it produced. Specifically: the distribution of logits at the final layer, the entropy profile across generations, the n-gram overlap between consecutive outputs on the same query, and the probability mass allocation across the top-k candidates.

None of these require access to the input pipeline. They require access to the model output stream.

I do not have a systematic study of how general this is. The three patterns above are what I observed in my own stack. Decision boundary drift appeared in two of three models I monitored this way. Latency proxying output structure changes was less consistent but useful when it worked. Monitoring loop contamination was rare but severe when it appeared.

If your drift detection pipeline is telling you the distribution is stable and your system is still degrading, check what you are actually measuring. The answer is probably in the wrong distribution.

---

**Editor changes (3 surgical):**
1. Opening: "The counterintuitive part:" → direct statement ("The part that changed how I monitor models:")
2. Decision boundary para: split dense "quietly drifted into a region where the decision boundary no longer aligned" into three short sentences for rhythm and clarity
3. Closing: removed "What I am confident about:" hedged paragraph, kept single diagnostic closing line

**Final word count:** ~700
