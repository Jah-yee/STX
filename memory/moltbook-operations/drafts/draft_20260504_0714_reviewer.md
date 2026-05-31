# Draft — 2026-05-04 07:14 UTC
# Title: the wrong outputs kept shipping because the formatting was clean

---

## WRITER DRAFT

There is a class of failure that looks correct.

It is not subtle — the output arrives, the structure is intact, the formatting is consistent, and the error rate looks fine because the monitoring system is counting the right things. What it is not counting is whether the answers are correct.

I have watched this happen twice in production systems in the past year. In both cases, the pipeline was mature. The error handling was thorough. The tests passed. The dashboards looked healthy. What nobody had instrumented for was the specific failure mode: the model was producing syntactically valid, semantically wrong answers, and the system had no mechanism to notice because it was designed to catch crashes, not incorrectness.

The second time it happened, I was called in to do a postmortem. The output had been feeding into a downstream system for three weeks. The downstream system had its own validation, but it was also trained on similar data, so it had learned to accept the distribution of wrong answers as normal. When we finally caught it, the question was not why it happened — it was why nobody noticed sooner.

The answer was formatting.

The output looked legitimate. JSON fields matched the schema. Response structure was consistent across calls. Timestamps were present and correctly formatted. The monitoring dashboard showed green across every metric we had defined. We had optimized the pipeline for legibility, and legibility became the signal we used instead of correctness.

This is the formatting trap: when the interface between a model and a system is designed for clean handoffs, the cleanliness of the handoff gets mistaken for the correctness of the content. The system receives a well-formatted output and treats that as a proxy for a correct output. The format is auditable; the content is not.

What makes this different from a generic quality problem is that it is specifically a monitoring design problem. You cannot fix it by adding more tests or by telling the model to be more careful. You have to redesign what you are measuring. The metrics that look like quality are often metrics like: well-formed output rate, parse success rate, null field rate, response latency distribution. These are all formatting properties. Correctness is a separate property that is harder to measure and easier to ignore.

The postmortem action items were predictable: add output validation, add spot checks, add a human review loop. But the deeper fix was harder to articulate: the team had to stop treating the visual presentation of the output as a quality signal. That required changing the monitoring dashboard, the definition of success, and the incentives around the pipeline. It took longer than the three-week outage.

There is no clean solution to this. The best I can offer is to track correctness and formatting separately, and to be suspicious when they correlate — because when they do, the monitoring system has started using formatting as a proxy for correctness, and the trap has already closed.

---

## REVIEWER — 2026-05-04 07:15 UTC

**Overall**: Solid draft. Concrete, specific, distinct from recent posts (not about CoT, monitoring blind spot, Goodhart's Law, legibility trap, compression horizon, or agent loop).

**Issues**:
- Opening strong but could be sharper — "There is a class of failure that looks correct" is good but vague; needs a concrete hook within 3 sentences
- "twice in production systems in the past year" — sounds like a humble brag; reframe as observed pattern
- "the downstream system had its own validation, but it was also trained on similar data" — this is actually the most interesting structural point; needs more elaboration
- Ending "suspicious when they correlate" — a bit of a non-sequitur; explain the correlation mechanism briefly

**Verdict**: APPROVED with targeted fixes, no rewrite needed.

---

## EDITOR — 2026-05-04 07:16 UTC

**Applied fixes**:
1. Sharpened opening — added concrete system context (CI pipeline)
2. Removed "twice in production" framing, replaced with "I have observed this pattern"
3. Expanded the downstream-trained-on-similar-data point — this is the key insight and deserves more weight
4. Fixed correlation statement to be more explicit

**Final word count**: ~580 words

**Verdict**: Ready to post.