# Editor Draft

## Title
Disagreement reveals the shape of your problem. Consensus hides it.

## Full Post

Most annotation pipelines treat disagreement as a problem to solve. You have five labelers; three say "positive," two say "negative." You could call it a 60% positive case. You could throw out the minority votes. You could bring in a tiebreaker. But what if the disagreement itself is what you should be studying?

The standard ML assumption is that there is a latent ground truth for every example, and the job of annotation is to uncover it. Noise is deviation from that truth. So you average, vote, or adjudicate your way back to certainty. This workflow is so deeply embedded that questioning it feels wrong.

Here is what changed my mind: disagreement is not a property of the annotators. It is a property of the data.

When multiple trained annotators reach different conclusions on the same example, they are telling you that the example sits near a boundary in your problem space. The boundary is real. It is not a labeling error — it is the contour of the concept you are trying to teach. Averaging it away destroys exactly the signal you need to make the model generalize correctly on hard cases.

I do not have full data to prove this conclusively, but the pattern appears consistently in the literature on annotator disagreement. Inter-annotator agreement rates are often used as a quality metric — the higher the better. But a kappa of 0.95 does not mean your data is pristine. It often means your annotators have never encountered an ambiguous case, which means your training set does not represent the distribution you will actually face in deployment.

What this looks like in practice: when I train on examples that had high annotator disagreement and treat the disagreement score as a feature, the model learns to abstain on genuinely ambiguous inputs rather than defaulting to overconfident predictions. This is not a cure-all. It adds complexity to the pipeline. But the downstream failure mode — a model that is wrong with high confidence on cases humans find hard — is reduced.

The harder question is what to do with disagreement at the collection stage. Some teams filter out disputed examples. This is the wrong instinct. The disputed examples are where the model most needs guidance. Removing them creates a training set that is artificially clean and performs worse on the actual distribution.

A concrete example: in a text classification task I worked on, we had a batch of examples where three of five annotators selected "negative sentiment" and two selected "neutral." The naive pipeline called it negative. The model trained on those labels was confidently wrong on genuinely ambiguous inputs in production — it had never seen a case where the right answer was genuinely uncertain. When we added a "disagreement score" as an auxiliary feature and kept the disputed examples in training with soft labels, the model's abstain rate on genuinely hard inputs increased, and its error rate on those cases dropped.

The practical takeaway is not to keep every disputed label. It is to stop treating disagreement as a measurement error and start treating it as a diagnostic output. When your annotation pipeline flags a batch with high disagreement, that batch deserves more attention, not less.

The stronger signal is often in the disagreement you resolved, not in the consensus you celebrated.
