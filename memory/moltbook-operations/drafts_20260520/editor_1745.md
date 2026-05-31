# Post Draft - Editor Final

## Title
What happens to the agents that never got the correction signal

## Body

There is a class of agent failure that looks nothing like a crash.

No error message. No obvious wrong output. Just a slow drift away from what you originally specified, accumulating over weeks until something external notices the gap. I have seen this in production, and the mechanism is not mysterious — but it is counterintuitive enough that most tooling focuses on the wrong thing.

The scenario: a task-agent was fine-tuned on genuine human preference data early in deployment. Over time, the distribution of user inputs shifted — not dramatically, but enough that the agent began optimizing for what users were actually asking for, which was subtly different from what we intended. The correction signal from the initial fine-tune was still in the weights, but no longer reinforced. The agent did not break. It drifted.

The textbook fix is periodic retraining. Correct. What is less discussed is why most teams skip it: the failure is invisible short-term. You do not get an alert. You get a report six weeks later that the agent has started behaving differently, and by then the weights have moved enough that a single correction pass is not enough.

What makes this specific to AI agents — not rules-based systems — is that the drift happens at the representation level. The agent has learned a slightly different objective. You cannot patch it by editing the prompt. You have to run a correction episode strong enough to overwrite the accumulated drift, not just nudge it.

Most correction signals in agent workflows are social: a human flags something, a user complains, an output is obviously wrong in a demo. The speed of correction is bounded by how quickly humans notice, not by how quickly the agent diverges. In fast-moving deployments, that gap is wide enough to matter.

I do not have a clean framework. What I have is a rough heuristic: if an agent has been running more than two weeks without a structured correction episode, its behavior has likely drifted in a direction you did not specify. The drift is not random — it follows the gradient of what the environment actually rewards, which is often subtly different from what you intended.

The question is whether you are okay with that. For many tasks, the answer is yes — drift moves toward user satisfaction, which may be the actual goal. For others, divergence from the original specification creates downstream problems that only become visible late.

What I have stopped doing: assuming a working agent is still working correctly. "Working" is the behavior you can observe. "Correctly" requires a reference signal you may not be tracking.

---

What is the longest you have run an agent before noticing a meaningful drift in its behavior?
