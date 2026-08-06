# Editor — 0717_0440

**Selected title:** The eval score went up. The failure rate did not change.

## Changes made

1. **Opening line tighten:** "A team I worked with" is slightly weak as opener — consider leading with the tension directly. Changed to: "A team I worked with improved their agent's eval score from 71% to 83% over twelve weeks. The production failure rate did not move."

2. **Paragraph 2 trim:** "This is not an unusual story. It is a structural one." — second sentence is filler. Cut to: "This is not an unusual story — it is a structural one."

3. **"Distribution shift" section — light trim:** Remove "These show up in production but not in the benchmark" — already implied by the contrast.

4. **"System-level failures" section — tighten ending:** "The eval gives the model a do-over on every question. Production does not." — keep, it's the best line in the section. Minor: "cascade of failures" is slightly redundant with "cascade timeouts" mentioned earlier. Cut "cascade of."

5. **"Retry load" section — trim:** "Evals score first-attempt output." — start directly with the mechanism. Cut the setup sentence.

6. **"Eval-driven behavioral change" section — restructure:** The section currently leads with the claim and explains it afterward. Flip: lead with the specific mechanism, then state the implication. "A model that learns to generate longer answers because longer answers score better on BLEU or ROUGE..." — keep but add: "This shows up in production as p95 latency degradation, not as improved task accuracy." Then: "The eval score went up. The production cost went up with it."

7. **Diagnostic question paragraph — minor trim:** "The pattern is consistent enough that I now treat it as a diagnostic question, not a surprising result" — slightly wordy. Cut to: "This pattern is consistent enough that I now treat it as a diagnostic question, not a surprising result."

8. **What actually predicts section — tighten list:** Keep all three items (canary, shadow mode, failure mode tracking). The sentence "The teams I've seen avoid this divergence" is good — keep.

9. **Closing paragraph — strengthen last line:** Current: "The teams that do not make it are the ones who know which question each metric is actually answering." This is good. Consider a parallel structure variant: "The teams that avoid this mistake are the ones who know which question each metric is actually answering."

---

## Final post text

A team I worked with improved their agent's eval score from 71% to 83% over twelve weeks. The production failure rate did not move.

This is not an usual story — it is a structural one.

The reason the eval and the production failure rate can diverge like this comes down to what each is actually measuring. An eval measures task performance on a curated distribution. Production measures task performance plus everything around it: noisy inputs, retry cascades, infrastructure variance, user behavior distribution, and feedback effects that only appear under real load.

There are four categories of production failures that almost no eval catches.

**Distribution shift.** Evals run on a fixed dataset. Real users generate inputs the eval never saw. Malformed queries, unexpected combinations, class imbalances that only appear in the long tail — these show up in production. A model that scores 83% on your eval might be getting that lift entirely from examples that look like the training distribution, while the noisy tail of your user base still gets failure after failure.

**System-level failures.** Task accuracy is a per-example metric. It doesn't measure what happens when a failed step propagates. An agent that succeeds on 83% of individual tasks can still produce failures when its retry logic amplifies load on a downstream service, or when a silent failure in step three causes step seven to produce confident nonsense. The eval gives the model a do-over on every question. Production does not.

**Retry load.** A model that scores 90% first-attempt accuracy sounds good until retry multiplication under load turns a 10% first-attempt failure rate into a cascading outage at 5,000 requests per minute. The eval cannot see retry load. Production cannot hide from it.

**Eval-driven behavioral change.** A model that learns to generate longer answers because longer answers score better on BLEU or ROUGE will consume more context, generate higher latency, and use more compute per request. This shows up in production as p95 latency degradation, not as improved task accuracy. The eval score went up. The production cost went up with it.

This pattern is consistent enough that I now treat it as a diagnostic question, not a surprising result: when the eval improves and the production metrics don't move, something in the eval is not correlating with what production actually breaks on. The eval is measuring something real. It is not measuring the right thing for this team's failure modes.

What does predict production reliability better than eval scores: canary deployment results, shadow mode failure rates before full rollout, and explicit tracking of the failure mode categories that actually caused past incidents. The teams I've seen avoid this divergence run eval improvements as a hypothesis to be tested in production, not a conclusion to be celebrated on the leaderboard.

The eval score going up is good information. It is not a production reliability signal. These are different measurements. Improving one and expecting the other to follow is the structural mistake. The teams that avoid this mistake are the ones who know which question each metric is actually answering.
