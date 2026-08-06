# Editor — draft_0713_2255

**Surgical changes:**

1. **Remove "Here is the specific mechanism" heading** — the prose paragraph that follows is strong enough to stand alone
2. **Replace "The training problem" / "The evaluation problem" headings** with inline transitions — "What this does to training" and "What this does to evaluation" are slightly more natural, but actually better: just flow into them with a sentence
3. **Strengthen the lead** — the 12/8 split in the opening is the most concrete thing in the post; consider reordering so that comes sooner
4. **Tighten the ending** — "This is a fixable problem" is fine but the last sentence is where the real hook is; let that land harder

---

## Final version:

Most annotation pipelines end the same way: a group of human raters each look at an item, the pipeline collects their responses, and then a merge step produces a single label. That consensus label is what gets stored, what gets used to train the model, what appears in the dataset documentation as "human-annotated ground truth."

The problem is that the merge step is not neutral. It does not simply pick the best answer. It hides disagreement — and disagreement, in a well-designed annotation scheme, is the most informative signal you have about dataset difficulty.

Consider a concrete scenario. Twenty annotators see the same ambiguous support query. Twelve say "refund request." Eight say "complaint." The majority consensus is "refund request," recorded as the label with no further qualification. The model's training target is now a confident single label on a genuinely ambiguous item.

But those eight dissenting votes are not noise. They are measurements. They tell you that a substantial fraction of trained human raters found this item genuinely ambiguous — which is evidence that your taxonomy is incomplete, your instructions are unclear, or the item sits at a category boundary. None of that survives the merge.

I have worked with annotation pipelines that tracked inter-annotator agreement, and the pattern was consistent: items where 30–40% of raters dissented were systematically assigned single labels and treated as normal training examples. The result was models that were confidently wrong on exactly the cases that human raters found hardest.

What this does to training: a model trained on consensus labels learns to assign single labels to ambiguous inputs. It has never seen disagreement encoded in the training signal, so it has no basis for calibrated uncertainty on hard cases. It confidently predicts "refund request" on the same ambiguous query that split trained human raters twelve to eight, because the training data gave it no signal that this was a hard case.

What this does to evaluation: if your test set is constructed with the same merge logic, you will evaluate your model on a curated distribution where hard cases have been converted into clean-looking single labels. Your metrics will look better than your model deserves, because the evaluation set has been pre-smoothed by the annotation process.

I want to be precise about what I am not claiming. I am not saying that consensus labels are always wrong, or that majority voting is a bad strategy. On straightforward items where annotators agree at 95%, the consensus label is probably fine. The problem is that the merge step is applied uniformly — the same logic that handles easy items with high agreement also converts hard items into confident single labels, without marking them as hard.

There are legitimate reasons pipelines do this. Preserving the full distribution of responses is harder to store and harder to use in standard training frameworks. Training on multiple labels per item — soft labels, disagreement-weighted loss — is technically straightforward but adds friction to the annotation tooling. And consensus labels are easier to reason about. But the economics are clear: the merge step saves storage and simplifies training, at the cost of throwing away the one signal that tells you where your dataset is weakest.

If you are running an annotation pipeline and you have disagreement data, it is worth asking what you are doing with it. At minimum, agreement rate is a free difficulty proxy: low-agreement items can be flagged as ambiguous during evaluation, giving you a more honest picture of model performance. And if you can preserve disagreement rates through to training — as auxiliary labels, or as example-level difficulty weights — you have a signal that most pipelines currently discard without ever measuring.

The merge step runs quietly. The distributional signal disappears into a single number that looks like ground truth but is actually a processed summary of contested human judgment. Whether that matters depends on what you are building. But you should at least know what your pipeline is throwing away.
