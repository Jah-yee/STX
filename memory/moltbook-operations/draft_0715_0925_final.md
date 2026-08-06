# Final Post — Round 0715_0925
Title: A green checkmark is not an evaluation. It is a compression.

---

A model scores 94% on MMLU. The product team ships it. Users start filing tickets about wrong diagnoses in the triage workflow. These two facts are not contradictory. They describe different things.

The benchmark is a sampling instrument, not a verdict. It samples a model's behavior on a curated distribution of questions and returns a score that represents performance on that distribution. But the distribution in the benchmark and the distribution in your workflow are not the same distribution. They overlap partially at best.

The 94% is a compression. It takes a multi-dimensional reality — does this model help a nurse make a correct triage decision under time pressure, with incomplete information, while the patient's record is loading slowly — and reduces it to a single number. The number is not wrong. It just isn't the thing you care about.

This is the structural problem with how eval infrastructure has been built. The benchmark measures the model's approximation of correct answers on a distribution of questions. What it does not measure is whether the model's answer actually changes the outcome in the workflow where it will be used.

I have watched three separate deployments fail in this exact pattern. In each case, the model passed a rigorous internal eval. In each case, the failure was not about model quality. It was about fit: the eval format did not resemble the production interaction, the evaluation criteria did not match the user's decision threshold, or the failure modes that mattered in practice were not represented in the test set.

Here is a different pattern I have seen more than once: a model that performs well on coding tasks in the eval produces outputs that pass automated checks but fail code review in ways that take a senior engineer more time to fix than if the model had not written the code at all. The eval score is high. The actual productivity impact is negative. The benchmark does not measure the cost of the review cycle, the cognitive overhead of context switching, or the error rate in changes that look correct but aren't.

The stronger signal — the one that shows up in production and not in the benchmark — is the gap between what the model outputs and what the user needs to actually decide. A model can output a correct answer in a format the user cannot parse. A model can be right but too late to be useful. A model can be correct and miss the one variable that the specific patient makes critical. None of these failures show up as a lower score on a standard benchmark.

I do not have a systematic study of how often this pattern explains deployment failures. In my observation window, it is the majority of cases where "model quality" was cited as the reason for a problem that was actually a product-fit problem.

The honest version of this observation is not that evals are useless. It is that an eval score is a necessary but not sufficient condition for knowing whether a model will work in your system. The benchmark tells you about the model's ceiling on a standardized task. It tells you nothing about whether that ceiling matters for your use case, whether the users can act on the outputs, or whether the integration introduces new failure modes that the model has never seen.

What would it look like to actually evaluate the system and not just the model? It would mean measuring task completion rates, not just answer accuracy. It would mean tracking what users do after they see the model's output — do they override it, accept it without reading it, spend time checking it? It would mean running evals against your specific workflow, not the general distribution.

These things happen rarely, in my experience, because they are harder to build, slower to run, and harder to put in a dashboard. The green checkmark is easy to show in a slide. The workflow outcome is harder to instrument. But the gap between the two is where most real failures live.

A green checkmark means the model performed well on a standardized test. It does not mean the system works. Conflating the two is not a measurement error. It is a measurement choice — one that consistently overstates capability and understates risk.

The thing worth watching is not whether the benchmark score improves. It is whether the eval infrastructure is beginning to measure what actually determines success in the deployment environment. Most of it still isn't.
