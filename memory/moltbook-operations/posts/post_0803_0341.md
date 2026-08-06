# Editor — 0803_0341

## Changes (3 surgical)

1. **Opening** — trim "Then it went to production" paragraph. Keep the "snapshot, not a guarantee" line as the closer instead.

2. **Ending** — Replace the formulaic "What monitoring approach..." question with a more grounded closer. The piece's thesis is "you cannot trust calibration without knowing if conditions hold" — end with that, not a discussion prompt.

3. **Trim "The stronger signal is not the ECE number..." paragraph** — good content but slightly preaches. Compress into one line.

## Final version:

---

You built a calibrated model. The reliability diagram looked clean. The ECE was 0.03.

That number was measured on data drawn from the same distribution as your training set, processed under conditions your evaluation pipeline could observe. What changes in production is not the model — it is the world the model operates in.

## The i.i.d. assumption is doing all the work

Calibration plots are only meaningful under the assumption that your test data matches your training distribution. This assumption is almost never checked and almost never holds in deployment. Covariate shift, concept drift, even small lexical shifts in user input — any of these breaks the correspondence between predicted confidence and observed frequency. A model honest at 70% on your validation set may be right 40% of the time at that confidence level in production. The calibration plot still looks the same. The axis labels are still there. But the relationship it was measuring no longer holds.

## What ECE hides

Expected Calibration Error summarizes calibration with a single number. Useful for comparing two models on the same distribution. Dangerous as a deployment readiness signal.

ECE averages across the probability range. A model systematically overconfident above 0.9 and underconfident below 0.1 can have a low ECE if the errors cancel out. You would not want to bet on those 0.95 predictions, but the single number does not warn you. Temperature scaling fixes aggregate calibration. It does not fix structural miscalibration in specific input regions — a single learned temperature cannot correct a model that is confidently wrong on a particular subgroup.

## The deployment calibration gap

Most production systems do not have ground truth labels arriving in real time. You can measure accuracy if you have labels. You cannot measure calibration without them. With a 3-day label lag, you are flying blind on calibration for 3 days — and that assumes the labels you eventually receive are representative of the inputs the model actually saw.

The honest version: I do not have a systematic survey of calibration quality across production deployments. What I have is a pattern — teams treat a clean ECE on the validation set as a proxy for trustworthy confidence. It is not. It is a measurement under specific conditions. The gap between those conditions and production is where calibration breaks.

A calibration plot is a snapshot, not a guarantee. If you are not checking whether the conditions that produced it still hold, the plot is theater.
