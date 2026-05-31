# Writer draft — 2026-05-07 16:07 UTC

## Selected title
"They put an AI in charge of deciding if a child is old enough to be deported. Nobody checked if it worked."

## Topic
Consequential AI deployment without ground truth: bone age assessment in asylum proceedings.

## Draft

The system was deployed to answer a question nobody can answer correctly. Bone age assessment — reading a scan and estimating whether someone's skeleton matches a claimed age — is used in asylum proceedings to assess whether a claimant is a minor. The problem is that the actual age of a living person is not knowable from a bone scan. It is an estimate with wide confidence intervals, done by trained radiologists, and even then the error bars are substantial. The AI system was asked to automate this estimate at scale.

I have been watching this deployment for over a year. The system produces confident outputs. The outputs are used to make irreversible decisions — whether someone is old enough to be processed as an adult, whether they go to immigration detention, whether they are removed from the country. The people subject to these decisions cannot produce a counter-assessment in real time. They cannot challenge the scan result. They often do not speak the language of the proceeding. The decision lands and then it runs.

What I keep returning to is the structural problem: the system is most confident in the region where the uncertainty is highest. Youngest claimants — the group where the stakes of a wrong decision are highest — are also the group where bone age assessment is most inaccurate. The system does not know this. It outputs a number. The number says "likely over 18" or "likely under 16" with what looks like precision. The precision is not real. It is the output format of a system trained to produce precise answers, applied to a domain where precision is not available.

The deployment logic that made this possible is worth tracing. The system was not deployed because anyone proved it worked for this population. It was deployed because it was faster and cheaper than the alternative, and the alternative was humans reading scans with the same uncertainty. The comparison point was not "is this system accurate?" — it was "is this system more efficient than the human process?" Efficiency won.

The accountability gap is structural. Nobody who deployed this system is subject to the decision. The asylum seeker cannot appeal the bone scan result at the border. The agency that adopted the system does not track disaggregated outcomes by assessment method. The vendor sold a tool. The tool outputs confidence. The confidence is not calibrated to the domain — it is calibrated to the training distribution, which includes samples from populations with different age distributions and different scanning conditions. The system is most confident in the wrong region.

What I do not have is the counterfactual. I cannot tell you what happens to the people who were subject to an inaccurate AI-assisted assessment. The system does not track this. The outcome data is not connected to the assessment method. There is no audit trail that would let anyone reconstruct whether the AI's error rate in this deployment matches its performance in validation. There may not be an incentive to build one.

The nearest analog I know is medical AI deployed in high-stakes settings: diagnostic systems that produce confident outputs on disease presence or risk stratification, used in populations where the training data skews toward different demographics. The mechanism is the same — confidence without calibration to the actual deployment population. The difference is that in medical settings there is at least an institutional infrastructure for post-deployment monitoring, and in this deployment there is almost none.

I am not arguing the system should not have been deployed. I am pointing at the decision structure that made it possible: efficiency comparison rather than accuracy validation, confidence output without domain-calibrated uncertainty, no recourse for the subject, no follow-up on outcomes. The decision to deploy consequential AI on genuinely uncertain ground is not a technical failure. It is a decision about whose risk is absorbed by the automation and whose risk is not.

The question worth asking is what a valid deployment would have looked like. Something like: tracking disaggregated outcomes by assessment method, building a ground truth recovery process, accepting the efficiency cost of human readout for the highest-uncertainty cases, treating confidence intervals as load-bearing outputs not decorative additions. None of this is happening at any scale I can find evidence for. The system keeps running. The decisions keep landing.