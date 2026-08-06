# Editor — Round 0721_0138

## Title (keep)
Agents don't replace software. They replace the glue code.

## Body — edited

An integration project at a company I know stalled for eleven weeks because of a Zapier workflow. The workflow moved records between their CRM, their billing system, and an internal dashboard. It broke whenever any of the three changed its API. Nobody wanted to touch it. It was glue code — not the interesting kind.

When the team eventually replaced it with an agent, the agent didn't replace the CRM or the billing system or the dashboard. It replaced the Zapier workflow. The core software stayed. The invisible 15% that connected everything stayed gone.

This is the pattern I keep seeing once agentic deployments mature past the pilot stage: the agents don't eat the SaaS. They eat the connectors.

---

The intuition most people have about AI replacing software is wrong in a specific way. They imagine a model sitting inside a UI, doing what a human did before, but faster and without sleep. The mental picture is a robot wearing a human's clothes.

What actually happens in practice is that the model becomes the integration layer. It reads from here, writes to there, checks this condition, retries on that failure. The moment an API becomes readable by an agent and writable by an agent, you've created a glue replacement. The business logic in the SaaS products stays intact. The glue that connected them becomes optional.

The ROI story for agents is not "replacing Salesforce with an AI" — it is "replacing the Tuesday-afternoon engineer who maintains the Salesforce-to-anything connector." Those are very different economics, and the second one is both more achievable and more likely to be true.

I started tracking this pattern by watching which internal tools got agentic first at different companies. The sequence was consistent: notification routing, cross-system record reconciliation, onboarding workflows, data export-and-transform pipelines. These are all glue code. They are not the product. They are not the core competency. They are the connective tissue that every team has and nobody owns.

The first wave of agentic automation does not reduce headcount at the product teams. It reduces headcount at the integration or platform teams — or more likely, it eliminates the contractor hours and the "I'll fix that next sprint" backlog that characterized the glue layer at most companies.

---

The reframing that changed how I thought about this: a typical internal tool at a mid-size company is roughly 20% core logic and 80% integration code, retry logic, format adapters, and "this service changed its auth schema again." The agent replaces the 80%. Not because it is smarter than the core logic — the core logic is usually well-understood and stable. Because the 80% is where the cost of maintenance is highest relative to the value it delivers.

The code nobody is sad about losing is almost always integration code.

The first casualties of full agentic coverage are not your engineers. They are your Zapier subscriptions, your custom webhook handlers, your nightly cron scripts that exist only to keep two systems in approximate agreement.

---

The exception is instructive: core systems that function as glue. If your product is, fundamentally, a connector — a middleware, an aggregator, a platform — the agentic wave is not replacing your competitors' glue. It is replacing you.

I have watched two companies with distinct middleware-as-product positions acknowledge this in their own internal reviews. The product worked. The moat was the connector. The agentic future was not "customers will use our connector with an AI layer on top." It was "the AI will be the connector, and our product will be the thing the AI routes around."

The interesting competitive question is not whether agents will replace software. The software that survives is the software that agents need to route through — the authoritative source, the system of record, the place where the data lives. Everything that primarily functions as a bridge between other systems is a candidate for elimination.

---

The practical signal I use: when evaluating whether a task is a candidate for agentic automation, I do not ask "could a model do this?" I ask "is this the code nobody wanted to write?" If yes, it will be automated first. If no — if the task is the core competency, the thing the company actually sells, the code whose loss would be felt — it will be automated last, if at all.

The glue goes first. The core survives. Most of what agents currently automate is glue — which is exactly why it works.

What integration in your stack has been running on "I'll fix that next quarter" for longer than you'd like to admit?
