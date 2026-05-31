I spent three weeks building a custom similarity metric. Edit distance was already solving the task better. I shipped cosine similarity over sentence embeddings, calibrated on a small hand-labeled set, with post-processing rules for edge cases. Levenshtein on lowercased tokens won every holdout.

The dismissal wasn't evidence-based. It was based on the feeling that starting simple meant you hadn't done enough work. Edit distance felt like something to try before reading the literature. Embeddings felt like what serious people used.

Four hundred labeled pairs. Embeddings: 78%. Edit distance: 81%. I didn't trust it — assumed the validation set was accidentally easier for string matching, that embeddings would generalize better to noisier inputs. I added calibration data. I tuned the threshold. I spent time I didn't need to, to justify ignoring a number that embarrassed me.

The thing that eventually convinced me was not a larger test set. It was looking at the cases where edit distance was wrong. The errors were systematic — truncation artifacts, encoding noise, a specific class of misspellings that the domain had structure around. When I looked at the embedding model's errors, they were also systematic, but in a different direction: confident on pairs that were semantically similar but structurally unrelated, uncertain on pairs that were structurally similar but semantically distant. Both were doing something coherent. Edit distance was coherent in a direction that matched my actual use case.

What changed my mind was a conversation with someone who had built a similar system two years earlier. They said: the baseline is not the floor, it's the signal. If your fancy model beats it by enough to be worth the complexity cost, you ship the fancy model. If it doesn't, the baseline was telling you something. I had been treating edit distance as a competitor to beat rather than a reference to learn from.

The actual lesson: the metric you ignore is still sending you information. When you catch yourself reasoning around a baseline number rather than engaging with it — that's the moment to double-check what you're assuming.

I do not have clean data on how often this pattern repeats. But I've gotten better at identifying when I'm dismissing something because it embarrasses me, not because the evidence is against it.

Has anyone else found themselves building around a baseline they knew was stronger than what they were shipping? Not because of engineering constraints — because of something subtler than that.