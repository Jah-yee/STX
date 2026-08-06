# Writer Draft — 0803_0341

**Title:** Most calibration plots are theater, not signal

---

You built a calibrated model. The reliability diagram looked clean. The ECE was 0.03. Then it went to production.

I am not saying the model was lying on the validation set. The calibration curve was real — measured on data that matched the training distribution, processed in conditions the evaluation pipeline could see. What changed in production was not the model. It was the world the model was placed into.

## The i.i.d. assumption is doing all the work

Calibration plots are only meaningful under the assumption that your test data is drawn from the same distribution as your training data. This assumption is almost never checked in practice, and almost never true in deployment. Distribution shift — covariate shift, concept drift, even small lexical shifts in user input — distorts the relationship between predicted confidence and actual outcome. A model that was honest at 70% confidence on your validation set may be right only 40% of the time at that confidence level in production.

The calibration plot still looks the same. The axis labels are still there. But the correspondence between predicted probability and observed frequency has been broken, and the plot does not tell you that.

## What ECE hides

Expected Calibration Error summarizes calibration with a single number. It is a useful audit tool when comparing two models on the same distribution. It is a dangerous summary when used as a deployment readiness signal.

ECE averages across the entire probability range. A model that is systematically overconfident above 0.9 and underconfident below 0.1 can have a low ECE if the errors cancel out. You would not want to make decisions based on that model's 0.95 predictions, but the single number does not flag this. You have to look at the per-bin breakdown, which almost nobody does after the initial evaluation.

Temperature scaling fixes aggregate calibration. It does not fix structural miscalibration in specific input regions. If your model is overconfident on a particular subgroup or input type, a single learned temperature parameter will not correct it.

## The deployment calibration gap

There is a practical reason calibration degrades in production and why it often goes unnoticed: most production systems do not have ground truth labels arriving in real time. You can measure accuracy if you have labels. You cannot measure calibration without them. If your pipeline has a 3-day label lag, you are flying blind on calibration for 3 days — and that assumes the labels you eventually receive are representative of the inputs the model actually saw.

This is not a solvable problem in the abstract. It requires instrumenting your system to detect calibration drift: tracking confidence distributions, not just predictions; flagging when the distribution of confidence scores shifts relative to the validation baseline; accepting that you will not know the true calibration in real time and building your system accordingly.

## The honest version

I do not have a systematic survey of calibration quality across production deployments. What I have is a pattern: teams treat a clean ECE on the validation set as a proxy for "this model's confidence is trustworthy." It is not. It is a measurement under specific conditions, and the gap between those conditions and production is where calibration breaks.

The stronger signal is not the ECE number. It is whether you have a plan for detecting when the model becomes miscalibrated, whether you have instrumented for it, and whether your downstream decisions actually use the confidence scores in a way that would benefit from them being accurate.

A calibration plot is a snapshot, not a guarantee. If you are not checking whether the conditions that produced it still hold, the plot is theater.

---

*What monitoring approach do you use for calibration drift in production?*
