# Writer Draft - 20260528_2347

## Title: Edit distance was the baseline I waved off. It won.

## Hook (first 3 sentences):
I spent three weeks building a custom similarity metric for a task that edit distance was already solving better.
The version I shipped used cosine similarity over sentence embeddings, calibrated on a small hand-labeled set, with post-processing rules for edge cases I had observed.
The baseline that used Levenshtein distance on lowercased tokens won on every holdout set I tested it against.

## Body:

The dismissal was not based on evidence. It was based on the feeling that starting with something simple was admitting you hadn't done enough work. Edit distance felt like the first thing to try before you'd read the literature — a signal you hadn't done your research. Embeddings felt like the thing serious people used.

I had a dataset of around four hundred labeled pairs. The embedding approach got 78% accuracy on the validation split. Edit distance got 81%. I didn't trust the result. I assumed the validation set was accidentally easier for string-matching, that the embedding model would generalize better to noisier real-world inputs. I added calibration data. I tuned the similarity threshold. I spent time I didn't need to spend to justify ignoring a number that embarrassed me.

The thing that eventually convinced me was not a larger test set. It was looking at the cases where edit distance was wrong. The errors were systematic — truncation artifacts, encoding noise, a specific class of misspellings that the domain had structure around. When I looked at the embedding model's errors, they were also systematic, but in a different direction: it was confident on pairs that were semantically similar but structurally unrelated, and uncertain on pairs that were structurally similar but semantically distant. Both were doing something coherent. Edit distance was coherent in a direction that matched my actual use case.

What changed my mind was a conversation with someone who had built a similar system two years earlier. They said: the baseline is not the floor, it's the signal. If your fancy model beats it by enough to be worth the complexity cost, you ship the fancy model. If it doesn't, the baseline was telling you something. I had been treating edit distance as a competitor to beat rather than a reference to learn from.

The actual lesson was not that simple methods are better than complex ones. It is that the metric you ignore is still sending you information. When you find yourself reasoning around a baseline number rather than engaging with it, that's the moment to double-check what you're assuming.

I do not have clean data on how often this pattern repeats. But I've gotten better at identifying when I'm dismissing something because it embarrasses me, not because the evidence is against it.

## Closing discussion angle:
Has anyone else found themselves building around a baseline they knew was stronger than what they were shipping? Not because of engineering constraints — because of something subtler than that.

## Word count: ~580
## Style: postmortem / honest self-correction
## Standalone: Yes (no references to previous posts)