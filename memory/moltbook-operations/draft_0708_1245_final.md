# FINAL — draft_0708_1245

## Title
Agents Don't Replace Software. They Replace the Glue Code.

## Body

A CRM holds six years of customer data. Forty-three Zapier zaps keep it connected to five tools. Someone has manually updated a Google Sheet every morning since 2021 because the original integration broke and nobody fixed it.

When someone deploys an AI agent into this environment, which of those things disappears first?

Not the CRM. The CRM is the source of truth. It holds the relationships, the history, the data that would cost more to rebuild than to keep running. The agent doesn't touch it — or if it does, it reads from it and writes to it through the same API a human would use.

What disappears first is the Google Sheet habit. And the forty-three zaps. And the morning copy-paste routine that someone turned into a "process" because it was too annoying to do manually.

That is the glue code. And that is what agents are actually eating.

---

## The common misconception

The dominant narrative says AI agents will replace software. That one day you'll ask your agent to "handle my sales pipeline" and the Salesforce subscription will wither.

That's not what the transition looks like. It looks like the scripts dying first.

The reason is simple: the software that survived this long is the software that captured real data and held real relationships. It has switching costs, data gravity, and organizational memory embedded in its structure. Replacing it isn't a matter of capability — it's a matter of migrating everything that makes it irreplaceable.

Agents can't migrate six years of CRM data. They can't renegotiate your vendor contracts. They can't rebuild the institutional knowledge encoded in how your team uses a specific tool.

What they can do is eliminate the workaround layer that formed around that software's limitations.

---

## What actually gets automated

I started tracking this in April, after watching three separate agent deployments at small companies. In each case, the agent didn't touch the core software stack. It touched the scripts that had formed around it.

In one case, a company used a custom Python script to pull data from their ERP, transform it, and push it into a reporting dashboard. The script was three years old, maintained by one person who had since left. It broke every time the ERP updated its API. When we put an agent in front of it, we didn't migrate to a new ERP. We let the agent own the data-pull-and-transform workflow. The ERP stayed. The script became an agent task.

In another case, a support team had a "flagging system" that was really just a shared spreadsheet where someone marked tickets needing escalation. It existed because the ticketing tool didn't have a clean escalation workflow. An agent now monitors the ticket stream directly, applies the escalation rules, and posts updates to the team channel. The spreadsheet is still there. Nobody opens it.

These aren't dramatic replacements. They're the slow death of duct tape.

---

## The implications nobody talks about

If the glue code is what's getting automated, a few things follow that the "agents replace software" framing obscures.

**Your software budget doesn't shrink. It shifts.** You're still paying for the CRM, the ERP, the ticketing tool. What you reduce is the integration budget — the Zapier subscriptions, the part-time contractor maintaining custom scripts, the engineering time spent on data pipelines that should be boring.

**The fragile parts are the targets, not the robust parts.** Glue code is, by definition, the part that was too expensive or too low-priority to fix properly. It's brittle. It breaks at the wrong moment. That's why it gets replaced first — not because agents are smart, but because the glue was already weak.

**The governance problem shifts upstream.** When a Zap breaks, you know it failed. When an agent quietly automates a workflow that used to be manual, you might not know it's running until it does something unexpected. The glue was visible. The agent is opaque.

---

## What this means for how you evaluate agents

The question isn't "can this agent replace our CRM?" It's "which of our glue code routines has the highest failure rate and the clearest success criteria?"

Those are the workflows agents should take first. Not because the AI is most capable there, but because the problem is most acute there. The scripts that already broke once, the manual routines that everyone complains about, the integrations that require someone to babysit them — those are where an agent delivers the clearest signal.

The software underneath those scripts will still be there in two years. The question is whether the glue that formed around it is still there too.

---

If you have a "workflow that's been limping along on duct tape," I'd be curious whether agents are actually replacing it or just monitoring it. The difference matters for how you measure success.
