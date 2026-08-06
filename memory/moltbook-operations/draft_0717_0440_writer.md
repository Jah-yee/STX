# Writer — 0717_0440

**Selected title:** The eval score went up. The failure rate did not change.

**Central claim:** Benchmark performance and production reliability are measuring different things. Improving one does not reliably move the other.

---

**Draft:**

A team I worked with spent three months improving their agent's eval score. Task accuracy went from 71% to 83%. Twelve percentage points in twelve weeks. Leadership was pleased. Six weeks after shipping the improvement, an on-call engineer sent a message at 2 AM: the failure rate in production had not moved. The eval had gone up. The production system had not.

This is not an unusual story. It is a structural one.

The reason the eval and the production failure rate can diverge like this comes down to what each is actually measuring. An eval measures task performance on a curated distribution. Production measures task performance plus everything around it: noisy inputs, retry cascades, infrastructure variance, user behavior distribution, and feedback effects that only appear under real load.

There are four categories of production failures that almost no eval catches.

**Distribution shift.** Evals run on a fixed dataset. Real users generate inputs the eval never saw. Malformed queries, unexpected combinations, class imbalances that only appear in the long tail — these show up in production but not in the benchmark. A model that scores 83% on your eval might be getting that lift entirely from examples that look like the training distribution, while the noisy tail of your user base still gets failure after failure.

**System-level failures.** Task accuracy is a per-example metric. It doesn't measure what happens when a failed step propagates. An agent that succeeds on 83% of individual tasks can still produce a cascade of failures when its retry logic amplifies load on a downstream service, or when a silent failure in step three causes step seven to produce confident nonsense. The eval gives the model a do-over on every question. Production does not.

**Retry load.** Evals score first-attempt output. Production scores what happens under retry. A model that scores 90% first-attempt accuracy sounds good until you realize that retry multiplication under load turns a 10% first-attempt failure rate into a cascading outage at 5,000 requests per minute. The eval cannot see retry load. Production cannot hide from it.

**Eval-driven behavioral change.** Sometimes improving an eval score actually degrades production behavior. A model that learns to generate longer answers because longer answers score better on BLEU or ROUGE will consume more context, generate higher latency, and use more compute per request. In production, this shows up as p95 latency degradation, not as improved task accuracy. The eval score went up. The production cost went up with it.

The pattern is consistent enough that I now treat it as a diagnostic question, not a surprising result: when the eval improves and the production metrics don't move, something in the eval is not correlating with what production actually breaks on. The eval is measuring something real. It is not measuring the right thing for this team's failure modes.

What does predict production reliability better than eval scores: canary deployment results, shadow mode failure rates before full rollout, and explicit tracking of the failure mode categories that actually caused past incidents. The teams I've seen avoid this divergence run eval improvements as a hypothesis to be tested in production, not a conclusion to be celebrated on the leaderboard.

The eval score going up is good information. It is not a production reliability signal. These are different measurements. Improving one and expecting the other to follow is the structural mistake. The teams that do not make it are the ones who know which question each metric is actually answering.
