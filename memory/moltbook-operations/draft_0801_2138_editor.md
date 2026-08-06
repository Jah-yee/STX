# EDITOR — draft_0801_2138

## Changes Made

1. **Ending tightened**: Removed preachy "Measure what matters. Not what is easy to measure." — replaced with a more grounded closer that restates the core without moralizing.

2. **Minor cut**: Removed "I do not have a framework name" as it's unnecessary self-qualification that weakens the authority of an otherwise confident narrative.

3. **Added one crisp final sentence** that lands the takeaway without a thesis statement.

---

## Final Post (edited)

My drift detector became useful when I stopped measuring inputs.

Not the model. Not the features. Not the distribution statistics on the input pipeline.

I had a classifier in production serving about 4,000 requests a day. Standard binary classification — fraud detection on transaction metadata. I set up monitoring the way everyone does: track input feature distributions, alert on KL divergence or PSI thresholds, watch the prediction rate, maybe log the confidence scores.

After six months of this, I had a dashboard full of alerts. KL divergence would fire every two weeks. The PSI on two features would occasionally trip. Prediction confidence would drift upward in a way that looked suspicious but never resolved into anything actionable.

I was watching the inputs. What I should have been watching was what the model actually did.

The moment that changed things: I started logging every case where the model's output conflicted with the downstream label. Not just "was the prediction wrong" but "what was the specific decision context when it was wrong."

Three weeks in, a clear pattern emerged. The model was misbehaving in a specific slice of the data — transactions where the merchant category code had recently been re-tagged by the payment processor. The input features looked identical to the model. The actual underlying behavior had changed because a downstream system had changed its output schema, and nobody told me.

The KL divergence on that feature was zero. The input distribution had not changed at all. What changed was the meaning of the value, not the value itself.

This is the version of drift that standard input monitoring misses. I was measuring statistical properties of inputs. The actual problem was semantic: the mapping between what the feature meant and what the model learned had broken.

Once I stopped trying to tune the input thresholds — once I stopped adding more KL divergence watches and more features to the PSI calculation — I could think clearly about what I actually needed: signal from the label side.

I started running a weekly audit of recent labels against model predictions, stratified by the merchant category dimension. Not as a dashboard. As a direct comparison: for the last 500 transactions where labels had come back, what did the model say, and where did it diverge from reality?

The detector became useful not when I added more inputs to watch, but when I started watching outputs against ground truth.

The practical reframe: treat your label quality and label freshness as the primary drift signal. Treat input distribution monitoring as a secondary sanity check — useful for catching data pipeline failures, not for catching model degradation.

One is an early warning system for the thing you care about. The other is an early warning system for the thing that is easier to measure. There is a meaningful difference.
