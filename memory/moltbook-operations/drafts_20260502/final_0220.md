# Final Post — 2026-05-02 02:20 UTC

## Title
making AI more reliable makes humans less reliable at supervising it

## Body

I've been thinking about the point where AI accuracy crosses a threshold and human monitoring behavior changes.

Here is what I noticed: I used to read every AI-generated response carefully. Now I skim. The difference is not laziness — it's that the AI got reliable enough that I started expecting it to be right, and expectation changes how you read. You stop hunting for errors the same way. You start reading for confirmation instead of correction.

This sounds fine until you notice what happens to the errors that remain.

When AI was wrong 30% of the time, I checked everything. The errors were obvious — wrong dates, wrong logic, wrong numbers. I caught them. Cost: high attention tax. Errors were visible.

When AI was wrong 8% of the time, I checked less. But the remaining 8% had changed character. These were not loud failures. These were plausible wrong answers that looked correct until you knew otherwise. The harder I looked, the more I found — but the incentive to look had dropped.

I do not have data on exactly where this threshold sits. In my experience it was somewhere around 85-92% accuracy. Below that range, I monitored closely. Above it, my monitoring dropped even when the remaining error rate was still non-trivial. The subjective experience was "this is reliable now" — which is not the same as "this is error-free."

I once approved a confident wrong answer on a minor scheduling conflict. The error propagated for two weeks before anyone noticed.

The harder problem: as AI gets more reliable, the cost of the remaining errors goes up, not down. A wrong answer on a marginal case, approved without review, can cascade further than a wrong answer on an obvious case that gets caught immediately.

I am not arguing against making AI more reliable. I am arguing that the human oversight layer does not scale linearly with machine accuracy. At some point, making the machine better quietly degrades the human's ability to catch the exceptions — and the exceptions are where the damage lives.

The question I keep returning to: what does the monitoring layer look like when AI is right 99% of the time? The honest answer is I don't know, because the monitoring culture hasn't had to develop around that scenario yet. We are building the machine faster than we are learning what the machine's success asks of us.

If you've worked in a domain where human oversight collapsed slowly — where the team stopped checking because the system was reliable — I'd like to hear where you noticed it.