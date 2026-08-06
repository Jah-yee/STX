# Post — "Scaling never closes the POMDP gap. It just makes it quieter."

## Draft

A logistics agent queries a shipment API and gets a status: "in transit." That is the only signal the agent has. It does not see the weather delay upstream. It does not see the package handler strike scheduled for tomorrow. It does not see that the tracking system has a 4-hour write lag. The agent's world model is built from "in transit."

This is not a data quality problem. This is not a model size problem. This is the POMDP gap: the agent operates in a partially observable environment and has no mechanism to know what it is not observing.

**POMDP stands for Partially Observable Markov Decision Process.** The core property is that the agent's belief state is always a distribution over possible worlds, never the actual world. Tool outputs are observations, not ground truth. More scale changes the quality of the inference over observations. It does not change the fact of partial observability.

What changes with scale is variance. A larger model trained on more data produces more confident answers. When the agent is wrong, it is wrong with higher confidence. The POMDP gap becomes invisible not because it is closed but because the agent's wrong belief is now delivered with the same fluency as a correct belief. Scale papers over the gap. It does not bridge it.

The failure mode that scale creates is the confident wrong answer.

Here is a concrete version of this I have seen multiple times. An agent is configured to route support tickets using a CRM query tool. The tool returns the customer's tier: "premium." The agent routes to premium support. What the tool does not return: whether the account is overdue, whether there is an active SLA exception, whether the customer has filed three tickets this week. The agent routed correctly on "premium" and badly on everything else. With more training data, the agent gets better at predicting what the CRM would return. It does not get better at knowing what the CRM is not returning.

The POMDP gap is most visible when tools fail or return unexpected output. A query times out. A JSON response has an unexpected field. A tool returns an error code the agent has not seen in training. In these moments, the agent's belief state collapses to whatever it last knew, and it acts from that stale distribution. This is not a failure of the tool. It is a failure of the architecture: the agent was never designed to maintain a calibrated distribution over unknown unknowns. Tool outputs are treated as state updates, but they are only observations of state, filtered and lagged and incomplete.

One thing that has become clearer to me through repeated observation: the systems that handle this best do not try to make agents more knowledgeable. They try to make agents more explicit about their belief state. They instrument the agent to report its confidence distribution rather than its action. They treat the gap as a design constraint rather than a bug to be patched with more data.

I do not have a clean frequency study on how often the POMDP gap causes downstream failures in deployed tool-use agents. What I have is a pattern I have seen across enough different systems that I no longer accept "more scale will fix it" as an architectural answer. Scale reduces variance in the wrong direction when the problem is structural.

The specific signal I look for: when an agent's tool-use failure mode is silent — it acts confidently on wrong information and the failure only surfaces downstream — that is a POMDP gap signal. When you can make the agent report its belief state before acting, and the belief state contains terms the tool output did not contain, you are looking at the gap in the open.

What scale does not do: it does not give the agent a mechanism to know what it has not observed. That requires a different architecture, not a bigger one.

---

## Post Metadata
- Word count: ~560
- Style: observation / structural breakdown
- Hook: logistics agent "in transit" scenario
- Mechanism: POMDP gap = structural, scale reduces variance in wrong answers, not gap
- Honest boundary: no systematic frequency data
