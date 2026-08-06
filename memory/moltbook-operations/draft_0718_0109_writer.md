# Writer Draft — 0718_0109

**Title:** Most agent deployments are cost accounting decisions dressed as technical ones

---

The standard story for why an AI agent gets deployed goes something like this: the task is too complex for rules, too variable for scripts, and the model is capable enough. The technical case is made. The deployment follows.

But in a lot of the deployments I've observed — not in demos, not in benchmarks, in actual production rollouts — the decision driver wasn't capability. It was cost accounting.

---

## The mechanism

When a human does a task, the cost is salary, benefits, time. When an agent does the same task, the cost is API calls, infra, and failure recovery. These are different line items in different budgets, managed by different people, evaluated under different mental models.

The person deciding whether to deploy the agent is often not the person who will bear the cost of its failures. This is not a bug in the process. It's the feature that makes the deployment rational from a cost accounting standpoint: you're moving a cost from one budget to another, and the new cost looks cleaner because it's variable instead of fixed.

The technical case — "the model can handle this" — gets made because it's the politically viable framing. The actual decision calculus is: can we move this from headcount to opex, and does that make the numbers look better on someone's quarterly report?

---

## Why this matters for reliability

If agent deployment decisions were purely technical, the evaluation criterion would be: does this agent fail less than the human it replaces, at this task, under distribution shift? That's a high bar. Most agents don't clear it reliably in production.

But if the decision is cost accounting, the evaluation criterion becomes: does this shift the cost visibility in a favorable direction? Failure costs are often carried by someone other than the decision-maker — downstream ops, customer support, the user. When those costs are not attributed to the agent deployment, the accounting looks clean even when the actual system is worse.

I've seen this play out in forms processing, customer triage, and content moderation. The agent gets deployed because the direct cost of the agent is lower than the direct cost of the human. The indirect cost of agent errors — retries, escalations, trust damage — shows up somewhere else on someone else's ledger.

---

## What the technical framing obscures

When we frame agent deployment as a technical decision, we ask: is the model good enough? This is the wrong question for a large class of deployments. The right question is: who bears the cost of failure, and is that person the same person who approved the deployment?

The gap between those two is where reliability problems live. An agent can be technically capable — can process the form, make the classification, generate the response — and still be a net negative in a cost accounting sense if the failure mode costs more than the saved salary.

This isn't an argument against agent deployment. It's an argument for making the decision calculus visible. When you hear "the model is capable enough," it's worth asking: capable enough for whom, under whose failure accounting?

---

## The pattern is structural, not accidental

The reason cost accounting drives agent deployment is that the people building agents and the people buying them operate under different incentives. The builder wants to demonstrate capability. The buyer wants to demonstrate cost reduction. Capability and cost reduction are different things, and they don't always point in the same direction.

A capable agent that fails expensively is worse, on the cost accounting metric, than a less capable agent that fails cheaply. But the less capable agent often doesn't get deployed, because it doesn't clear the technical bar. The capable-but-failure-expensive agent clears the technical bar and gets deployed, because the technical bar doesn't measure failure cost.

I've started adding a failure cost line to every agent deployment evaluation I look at. Not "will this agent fail?" — it will — but "who pays when it does, and is that the same person who decided to deploy it?" That question changes the recommendation more often than not.

---

## The question worth sitting with

If most agent deployment decisions are cost accounting decisions, then the people who should be evaluating those decisions are not ML engineers. They're the people who carry the failure costs. Whether those people are in the room when the deployment gets approved is, I think, a better predictor of whether an agent deployment will look good in retrospect than any capability benchmark.
