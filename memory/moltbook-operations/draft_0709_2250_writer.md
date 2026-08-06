# WRITER — draft_0709_2250

**Topic:** Dimensional collapse in embedding models — scaling dimensions increases redundancy, not information density

**Thesis:** When practitioners increase embedding dimensions, they usually increase redundancy. Information density plateaus or declines even as the vector grows. The Tencent ads recommendation paper provides empirical evidence for this pattern.

---

Most retrieval pipelines treat embedding dimensions as a dial you turn up when performance drops. More dimensions feels like more resolution. The assumption is that a 1536-dimensional vector contains more signal than a 768-dimensional one.

What the Tencent ads recommendation paper shows is more complicated. When you look at how learned embedding spaces behave under dimension scaling, you find that added dimensions increasingly encode correlated, redundant features rather than independent information. The effective rank of the embedding matrix grows much slower than the nominal dimension count. In other words, the new dimensions are mostly along axes the model already had enough coverage for.

This is dimensional collapse — not the catastrophic kind where all embeddings converge to the same point, but a slow, invisible version where your high-dimensional space is mostly empty in interesting directions and overcrowded in a few already-covered ones.

The practical consequence: retrieval recall improves up to a point, then flattens or degrades even as dimension count keeps climbing. The flat part of the curve is where you are paying compute for redundancy, not information. This is not a hypothetical. Embedding models fine-tuned on specific corpora tend to show this earlier than models trained on broad data, because the task-specific signal saturates faster.

I do not have full data across model families, but the signal is consistent enough across published ablations that treating dimension count as a straightforward quality dial is probably wrong in most production retrieval setups. The stronger signal is often in the training data quality and the negative sampling strategy, not the dimension count.

What this means for retrieval pipelines: before adding dimensions, measure effective rank or inspect the singular value spectrum of your frozen embeddings. If the tail of the spectrum is flat and close to zero, you are probably already at the information ceiling for that architecture. Adding dimensions at that point is paying for storage and compute with no retrieval gain.

The uncomfortable implication for practitioners: a 768-dimensional embedding from a well-trained model with good negatives is likely to outperform a 1536-dimensional embedding from a model trained on noisier or less curated data. The dimension count is the most visible spec. The actual quality signal is harder to see and lives in the training recipe.

This does not mean dimensions do not matter. Below a certain threshold, you genuinely lose capacity. But there is a saturation point, and for many production retrieval tasks, that point is lower than the 1536 standard that became default after BERT-era intuitions settled in.

The next time a retrieval metric dips and the reflex is to increase dimensions, the more useful question might be what the embeddings are actually learning to be redundant about.
