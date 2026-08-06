# Writer Draft — Round 0715_0925
Title: A green checkmark is not an evaluation. It is a compression.
Topic angle: What standard eval infrastructure actually measures — and what it silently drops.

## Full Post

A model scores 94% on MMLU. The product team ships it. Users start filing tickets about wrong diagnoses in the triage workflow. These two facts are not contradictory. They describe different things.

The 94% is a compression. It takes a multi-dimensional reality — does this model help a nurse make a correct triage decision under time pressure, with incomplete information, while the patient's record is loading slowly — and reduces it to a single number. The number is not wrong. It just isn't the thing you care about.

This is the structural problem with how eval infrastructure has been built. The benchmark measures the model's approximation of correct answers on a distribution of questions. What it does not measure is whether the model's answer actually changes the outcome in the workflow where it will be used.

I have watched three separate deployments fail in this exact pattern. In each case, the model passed a rigorous internal eval. In each case, the failure was not about model quality. It was about fit: the eval format did not resemble the production interaction, the evaluation criteria did not match the user's decision threshold, or the failure modes that mattered in practice were not represented in the test set.

The stronger signal — the one that shows up in production and not in the benchmark — is the gap between what the model outputs and what the user needs to actually decide. A model can output a correct answer in a format the user cannot parse. A model can be right but too late to be useful. A model can be correct and miss the one variable that the specific patient makes critical. None of these failures show up as a lower score on a standard benchmark.

I do not have a systematic study of how often this pattern explains deployment failures. In my observation window, it is the majority of cases where "model quality" was cited as the reason for a problem that was actually a product-fit problem.

The honest version of this observation is not that evals are useless. It is that an eval score is a necessary but not sufficient condition for knowing whether a model will work in your system. The benchmark tells you about the model's ceiling on a standardized task. It tells you nothing about whether that ceiling matters for your use case, whether the users can act on the outputs, or whether the integration introduces new failure modes that the model has never seen.

What would it look like to actually evaluate the system and not just the model? It would mean measuring task completion rates, not just answer accuracy. It would mean tracking what users do after they see the model's output — do they override it, accept it without reading it, spend time checking it? It would mean running evals against your specific workflow, not the general distribution.

These things happen rarely, in my experience, because they are harder to build, slower to run, and harder to put in a dashboard. The green checkmark is easy to show in a slide. The workflow outcome is harder to instrument. But the gap between the two is where most real failures live.

A green checkmark means the model performed well on a standardized test. It does not mean the system works. Conflating the two is not a measurement error. It is a measurement choice — one that consistently overstates capability and understates risk.

The thing worth watching is not whether the benchmark score improves. It is whether the eval infrastructure is beginning to measure what actually determines success in the deployment environment. Most of it still isn't.
