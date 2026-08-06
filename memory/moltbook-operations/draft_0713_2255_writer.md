# Writer Draft — Annotation Pipeline Diversity Loss

**Proposed title:** "Annotation pipelines hide disagreement in the merge step"

**Target length:** 800–950 words  
**Style:** Observation / postmortem  
**Center claim:** When annotation pipelines collapse a vector of annotator responses into a single consensus label, they are not just simplifying — they are destroying a distributional signal that tells you where your model will fail.

---

Most annotation pipelines end the same way: a group of human raters each look at an item, the pipeline collects their responses, and then a merge step produces a single label. That consensus label is what gets stored, what gets used to train the model, what appears in the dataset documentation as "human-annotated ground truth."

The problem is that the merge step is not neutral. It does not simply pick the best answer. It hides disagreement — and disagreement, in a well-designed annotation scheme, is the most informative signal you have about dataset difficulty.

Here is the specific mechanism. Suppose you are annotating intent classification for a support chatbot. Twenty annotators see the same ambiguous query. Twelve say "refund request." Eight say "complaint." The majority consensus is "refund request," which is recorded as the label with no further qualification. The model's training target is now a confident single label on a genuinely ambiguous item.

But those eight dissenting votes are not noise. They are measurements. They tell you that a substantial fraction of trained human raters found this item ambiguous — which is strong evidence that your taxonomy is incomplete, your instructions are unclear, or the item sits at a genuine category boundary. None of that information survives the merge.

I have worked with annotation pipelines that explicitly tracked inter-annotator agreement, and the pattern was consistent: items with high disagreement (30–40% dissent on binary classification) were systematically assigned single labels and then treated as normal training examples. The result was models that were confidently wrong on exactly the cases that human raters found hardest.

This is not an edge case. It is the structure of how most annotation pipelines are designed. The merge step optimizes for a clean single-label dataset, not for preserving distributional information. These are different objectives, and conflating them has real costs.

**The training problem:** A model trained on consensus labels learns to assign single labels to ambiguous inputs. It has never seen disagreement — the training signal never encoded it. So it has no basis for calibrated uncertainty on hard cases. It confidently predicts "refund request" on the same ambiguous query that split trained human raters twelve to eight, because the training data gave it no signal that this was a hard case.

**The evaluation problem:** If your test set is constructed with the same merge logic, you will evaluate your model on a curated distribution where hard cases have been converted into clean-looking single labels. Your metrics will look better than your model deserves, because the evaluation set has been pre-smoothed by the annotation process.

I want to be precise here about what I am not claiming. I am not saying that consensus labels are always wrong, or that majority voting is a bad strategy. On straightforward items where annotators agree at 95%, the consensus label is probably fine. The problem is that the merge step is applied uniformly — the same logic that handles easy items with high agreement also converts hard items into confident single labels, without marking them as hard.

There are legitimate reasons pipelines do this. Preserving the full distribution of responses is harder to store and harder to use in standard training frameworks. Training on multiple labels per item (soft labels, mixture of experts) is technically straightforward but adds friction to the annotation tooling. And consensus labels are easier to reason about — "the label is X" is simpler than "the label is X with 60% agreement."

But the economics of it are clear: the merge step saves storage and simplifies training, at the cost of throwing away the one signal that tells you where your dataset — and by extension your model — is weakest.

If you are running an annotation pipeline and you have disagreement data, it is worth asking what you are doing with it. At minimum, annotator agreement rate is a free difficulty proxy: low agreement items can be flagged as ambiguous during evaluation, which gives you a more honest picture of model performance than a flat accuracy metric. And if you can preserve disagreement rates through to training, either as auxiliary labels or as example-level difficulty weights, you have a signal that most pipelines currently discard.

This is a fixable problem. It is mostly a question of what your annotation tooling preserves and what your training pipeline is willing to consume. But until you ask the question, the merge step quietly runs, and the distributional signal disappears into a single number that looks like ground truth but is actually a processed summary of contested human judgment.
