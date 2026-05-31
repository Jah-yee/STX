# Writer Draft — Distribution Shift / Overfitting to Early Batch

**Working title:** The metric your agent improves is not the task you care about

**Hook (first 3 sentences):**
An agent can improve on a task, and simultaneously get worse at the job you actually need done. This is not a capability problem. It is a distribution problem — and the metric that tells you the agent is improving is the same metric that blinds you to the failure.

I have watched this happen with a classifier in production.

---

## Full Draft

An agent can improve on a task, and simultaneously get worse at the job you actually need done. This is not a capability problem. It is a distribution problem — and the metric that tells you the agent is improving is the same metric that blinds you to the failure.

I have watched this happen with a classifier in production. The accuracy score held steady for three months. Then the company's product offering expanded into an adjacent category. The classifier's accuracy stayed at 91 percent. But the business metric — correctly categorized intent, measured by downstream resolution rate — dropped 18 points over the next quarter.

The agent had not degraded. The agent had not been tampered with. The first batch of data it trained on was simply a better fit for the first distribution than for the current one.

Here is the mechanism: agents form strong habits from early examples. These habits are not erased when the distribution shifts — they are applied with the same confidence to a problem that has changed. The agent is executing correctly on the wrong problem. Its behavior is coherent, confident, and wrong.

This is different from classic capability loss. The agent is not forgetting. It is over-applying what it learned.

The failure is most dangerous when the metric you use to track the agent was computed on the early distribution. The number that tells you performance is improving was trained on a distribution the agent has outgrown. As the agent "improves" on the training metric, it simultaneously gets worse at the task that metric was supposed to proxy for.

The real signal is counterintuitive: the agent's confidence stays high while its task performance drops. Because confidence was calibrated on the first distribution, it does not deflate when the distribution shifts — the agent is equally sure of its habits in both distributions. You do not see the failure in the metric. You see it in the behavior of the humans around the agent, who start routing around it without telling you.

What to do about it: track performance on the most recent batch separately from the cumulative score. When the recent batch performance diverges from the cumulative performance — that gap is the signal. Another signal: when users start routing around the agent without filing issues. That behavioral change is often more reliable than any metric.

The core vulnerability: every agent is trained on some distribution, and every distribution eventually shifts. The agent that learns its lessons well from the first batch is the same agent that applies those lessons badly in the second.

The metric that tells you the agent is improving is not the metric you actually care about — not when the world the agent learned in is not the world it is now operating in.