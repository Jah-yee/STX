# Writer Draft — Round 0709_2015

## Title
Citation models recommend topics. They ignore why you cited.

## Body

A citation model finds papers that share vocabulary with your text. When it recommends a citation, it is telling you: this paper is statistically similar to what you just wrote. It is not telling you what that citation does in your argument.

That distinction sounds academic. It is actually practical, and it explains something that anyone who has used a citation recommendation system has felt: the model suggests papers that are topically correct but argumentatively wrong.

**What citations actually do.**

A citation is a rhetorical act. When you cite Smith et al., you are not just pointing to prior work. You are claiming a relationship: this supports my claim, this contrasts with my position, this provides methodology I am adapting, this defines a term I am using. The citation carries a functional role in your argument. Change that role and the citation breaks, even if the paper is perfectly relevant by topic.

The bibliography of a paper is not a list. It is a distributed argument. Every citation is doing something specific. Group them by rhetorical function and you can see the architecture: some citations establish background, some mark territory, some acknowledge debts, some invite the reader to follow a thread. The model that recommends citations cannot see this architecture. It sees token co-occurrence.

**Why semantic similarity misses the point.**

Citation recommendation models have gotten sophisticated. They use dense embeddings, cross-attention, citation graph traversal, author networks. The better ones outperform simple BM25 retrieval by a significant margin on standard benchmarks. But benchmarks measure topical recall: did you retrieve the right papers? They do not measure argumentative fit: does this citation do what you need it to do in this position?

The gap between these two measures is invisible in evaluation and obvious in use. You paste in your introduction. The model returns ten semantically similar papers. You look at the first three. They are clearly related to your topic. You reject all of them. Not because they are wrong — because they do not fit what you are building. The paper you need is about a different aspect of the problem. It supports the claim that contradicts yours. It uses a methodology that yours extends. The model cannot distinguish between these relations because it was never trained to model argument structure. It was trained on text.

**The specific failure mode nobody talks about.**

The clearest signal that a citation recommendation is wrong is not low relevance. It is that the suggested paper makes a different argument than you are making. You can feel it when you read the abstract: this paper assumes a different problem framing, or a different population, or a different definition of the key variable. The citation would introduce a contradiction that your text does not have room to address.

This failure mode is not a data problem. Adding more papers to the corpus, or training on larger citation graphs, does not close the gap. The gap is structural. The model sees text similarity. Argumentative fit requires understanding what role a citation plays in the surrounding discourse. That is a higher-order inference task, not a retrieval task.

There is a class of systems that gestures toward this problem — citation context analysis, argumentative zoning, rhetorical move detection. These approaches try to label what a citation is doing in its original paper and match on that label rather than on text similarity. The results are better, but the data is scarce and the annotation is expensive. The models that actually get deployed are the ones that are easy to scale: semantic similarity on large corpora. The better approach exists. It is slower to build and harder to maintain. Most teams do not choose it.

**What this means for recommendation design.**

If you are building or evaluating a citation recommendation system, the relevant question is not what share of relevant papers you retrieve. It is whether the recommended papers serve the argumentative function the author needs. That function is not visible in text similarity, or in citation graph structure, or in author co-appearance patterns. It is visible in the surrounding discourse: what the paper argues, what it assumes, what it proves, what it leaves open.

The systems that will improve citation recommendation are the ones that model argument structure, not just text relevance. They need to understand that a citation is a claim about a relationship between your work and prior work — not a pointer to a topic. That understanding is not in the embeddings. It has to be engineered explicitly.

Until then, every citation recommendation is a topic match. The argument is yours to build.
