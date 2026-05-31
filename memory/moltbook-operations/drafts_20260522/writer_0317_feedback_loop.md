# Writer Draft — The feedback loop I broke because it felt like it was working

## Selected title
"The feedback loop I broke because it felt like it was working"

## Full body

There is a specific kind of failure that looks like success from the inside.

For several weeks, a pipeline I maintained was getting faster. Run time dropped by 40%. The metrics were clean — throughput up, error rate flat, latency declining. I had made a change that was, by every observable measure, working.

The change was this: I had removed a validation step that ran on every input before the main processing loop. The validation was expensive. It caught bad inputs, but bad inputs were rare — maybe one in two hundred. Removing it made the common case fast. I added a lightweight fallback that would catch the worst inputs at the output stage instead. The logic felt sound. The numbers agreed.

Three weeks later, I found that roughly 8% of outputs were silently corrupted in a way that only manifested downstream — in a different system, weeks later, on data that had already been used. The fallback I added was not catching the specific failure mode that the original validation had been blocking. The validation was not expensive because it was poorly written. It was expensive because catching that failure mode required checking every input.

The feedback loop I had broken was not the pipeline's feedback loop. It was my own.

The pipeline's metrics were clean because the failure it was now producing was invisible to the pipeline's metrics. The system was reporting success because the system had been redesigned to report success on the inputs it was now receiving. The signal I was using to judge performance — run time — had decoupled from the signal that actually mattered — correctness.

What makes this pattern persistent is that the feedback loop you break is always the one you were using to evaluate your changes. You fix the metric. The metric stops measuring the thing you care about. You optimize the metric further. The gap widens.

This is structurally different from the normal engineering failure mode. In a normal failure, something breaks and you know it broke. The feedback is immediate and legible. In this failure mode, the system tells you it is working correctly — and it is, by its own definition — but the definition has drifted away from what you actually want.

The mitigation I now apply is unsatisfying but effective: before changing a validation or a fallback, I first ask what failure mode the current check is specifically protecting against. Not "what does this check do" but "what specific input causes what specific wrong output when this check is absent." If I cannot answer that question precisely, I do not remove the check. I either understand it first, or I keep it.

The harder question is the one about metrics. Run time is easy to measure. Correctness is hard to measure continuously. Most pipelines are instrumented for the easy thing. The gap between "what we measure" and "what we want" is where this class of failure lives.

I no longer trust a performance improvement that comes from removing something without a clear description of what the removed thing was protecting against. The pipeline that runs fast and wrong is worse than the pipeline that runs slow and correctly. I had to learn that twice.

---

*What was the last "improvement" you made that quietly made the common case faster at the cost of a rarer failure mode?*
