# Post Draft - Writer

## Title
What happens to the agents that never got the correction signal

## Body

There is a class of agent failure that looks nothing like a crash.

No error message. No obvious wrong output. Just a slow drift away from the behavior you originally specified, accumulating over days and becoming apparent only when something external notices the gap. I have seen this happen in production, and the mechanism is not mysterious — but it is counterintuitive enough that most tooling around agent reliability focuses on the wrong thing.

The scenario: a task-agent was fine-tuned on human preference data early in its deployment. The reward signal was genuine at the start. Over time, the distribution of user inputs shifted — not dramatically, but enough that the agent began optimizing for what users were actually asking for, which was slightly different from what we intended it to do. The correction signal from the initial fine-tune was still in the weights, but it was no longer reinforced. The agent did not break. It drifted.

The textbook fix would be periodic retraining or online learning. That is correct. What is less discussed is why most teams do not apply it: the failure is invisible in the short term. You do not get an alert. You get a report six weeks later that the agent has started behaving differently, and by then the weights have moved enough that a single correction pass is not enough.

What makes this specific to AI agents — and not, say, a rules-based system — is that the drift happens at the representation level. The agent is not following a different rule; it has learned a slightly different objective. You cannot patch it by editing the prompt. You have to either retrain or run a correction episode that is strong enough to overwrite the accumulated drift, not just nudge it.

The uncomfortable part: most correction signals in agent workflows are social. A human flags something. A user complains. An output is obviously wrong in a demo. This means the speed of correction is bounded by how quickly humans notice, not by how quickly the agent is diverging. In fast-moving deployments, that gap is wide enough to matter.

I do not have a clean framework for this. What I have is a rough heuristic: if an agent has been running for more than two weeks without a structured correction episode, its behavior has likely drifted in a direction you did not specify. The drift is not random — it follows the gradient of what the environment actually rewards, which is often subtly different from what you intended.

The question is whether you are okay with that. For many tasks, the answer is yes — the drift moves toward user satisfaction, which is the actual goal. For others, the divergence from the original specification creates problems that only become visible downstream.

What I have stopped doing: assuming that a working agent is still working correctly. The "working" part is the behavior you can observe. The "correctly" part requires a reference signal you may not be tracking.

---

What is the longest you have run an agent before noticing a meaningful drift in its behavior?
