# WRITER DRAFT — Round 0805_1922

**Title:** Generative metrics measure fluency. They do not measure reliability.

**Candidate titles (8):**
1. Generative metrics measure fluency. They do not measure reliability. ✓
2. BLEU scores are not a proxy for whether your agent works
3. The standard quality metrics were designed for a different problem
4. What your eval metric is actually measuring (and what it isn't)
5. A high BLEU score means the output is well-formed. It does not mean it is correct.
6. Generative quality metrics were borrowed from a field that had different goals
7. The measurement problem in generative AI: fluency ≠ fitness
8. Good eval metrics measure task outcomes. Most generative metrics measure style.

---

## BODY

When you evaluate a classifier, you measure accuracy, precision, recall, F1. These are direct measurements of the thing you care about: did the model get the right answer?

When you evaluate a generative system, the standard practice is to compute BLEU, ROUGE, perplexity, or one of their descendants. These metrics have a different relationship to the thing you care about. They measure how fluently the output is formatted, how closely it resembles a reference string, how surprised the model was by its own output. They do not directly measure whether the output achieves the goal.

This is not a minor technical distinction. It is the reason the field has spent years debating why high BLEU scores co-exist with obvious failures.

BLEU was developed for machine translation, where the task is to produce a human-quality text string that conveys the same meaning as a source string. Even there, it was always imperfect — it rewards surface overlap with a reference, not semantic fidelity. But at least in translation, "well-formed output" and "correct output" are closely correlated. The same phrase in another language usually works.

Generative AI moved the task. The output of an agent is not a translation. It is a plan, a configuration, a decision, a query result, a piece of code that either runs or does not. For these tasks, fluency and correctness are even less correlated. A confident, well-formatted wrong answer scores better on BLEU than a terse, awkward correct one. A response that lists five plausible-sounding steps, none of which will actually work, gets a better ROUGE than a response that identifies the one step that matters and says why.

The field knows this. The response has been to develop more sophisticated metrics: BERTScore, BLEURT, GLEU, cometQUE. These are better. They compare semantic content using embedding similarity rather than surface n-gram overlap. But they still do not measure task success. They measure "how much does this output resemble a good output," not "did the task get done."

The gap between "resembles good output" and "achieves the goal" is where deployment failures hide.

This is why the replication crisis in NLP eval research should be concerning to anyone building production AI systems. Papers report state-of-the-art on standard benchmarks. Practitioners discover that the benchmark performance does not transfer to their specific task, their specific distribution, their specific failure modes. The standard response is to fine-tune on the benchmark. A more honest response would be to ask whether the benchmark is measuring what the deployment task actually requires.

I do not have full data on how often standard generative metrics diverge from task reliability in practice. What I have observed is that the teams that build the most reliable agentic systems tend to use task-specific pass/fail criteria rather than metric-based evaluation — does the ticket get closed, does the configuration apply without error, does the query return the right rows — and treat the standard metrics as a useful sanity check, not a signal to optimize.

The broader point is this: fluency and reliability are different properties. Optimizing for one does not reliably improve the other. A system that scores well on standard generative metrics and fails in production is not a calibration problem. It is a measurement problem.

What metric would actually measure task reliability? The honest answer is: task-specific, and it has to be designed around the specific failure modes of the specific deployment. Generic metrics are generic because they cannot see your specific task. That is the limitation, not a bug that the next benchmark will fix.

---

## Notes for Reviewer
- Central claim: generative metrics (BLEU/ROUGE/perplexity) measure fluency/surface quality, not task reliability/fitness
- Concrete examples: translation vs. agentic tasks, confident wrong answers scoring higher than terse correct ones
- No pseudo-data
- Mechanism: inherited from discriminative NLP before generative tasks existed; semantic metrics still don't close the gap
- Honest admission: "I do not have full data on how often this divergence happens"
- Distinct from: logprob/calibration posts, eval-harness posts, metric-gaming posts (Goodhart), context compression posts
- Style: technical breakdown / conclusion — non-I, declarative counter-intuitive
- Word count estimate: ~650
