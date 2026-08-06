# Editor — 0707_1035

**Title:** Your observability stack is probably a cost center dressed as a profit center

## Editor Notes

The draft is solid. Minor tightening only.

1. **Opening**: The three-sentence opener works well. Keep as-is.
2. **Section 2 "The dashboard-led observability loop"**: The phrase "in the teams I've been in and around" is slightly hedging and vague. Replace with something more direct.
3. **Section 4 "SLO theater"**: The line "I do not have data on how common this is" is good honesty but breaks flow. Shorten.
4. **Section 6 "What I would do differently"**: The three questions are the strongest part of the post. Make sure they land clearly.
5. **Closer**: "Infrastructure theater" is good. Keep.

## Suggested Changes

### Change 1 — Section 2, tighten the "teams" sentence:
**Old:** "In the teams I've been in and around, the gap between 'we have observability' and 'our observability recovered money' is usually measured in years."
**New:** "Across several infrastructure teams I've worked with, the gap between 'we have observability' and 'our observability recovered money' tends toward years — not because the engineers were bad, but because the goal was never cost recovery."

### Change 2 — Section 4, trim the data admission:
**Old:** "I do not have data on how common this is. In my experience, it is common enough to be a pattern."
**New:** "In my experience this is common enough to be a pattern, even without systematic data."

### Change 3 — Final paragraph, tighten:
**Old:** "The answers are not in dashboards. They are in billing exports, architecture diagrams, and conversations with the person who wrote the cron job that sends 200,000 requests to an external API every night."
**New:** "The answers are not in dashboards. They are in billing exports, architecture diagrams, and in asking the person who wrote the cron job — the one that fires 200,000 requests every night — why it does."

## Final Draft (post-edit)

---

There is a specific kind of meeting that happens in every infrastructure team at some point. Someone pulls up a dashboard. The dashboard is beautiful. The graphs are green. Latency is low. Error rates are within SLO. The team walks out feeling like they understand their system.

Nothing changes after the meeting.

This is the observability trap. You build the dashboard before you find the problem. The dashboard becomes the goal. You optimize for the dashboard looking good, not for the system actually being cheaper to run.

## The dashboard-led observability loop

Most observability spending follows the same pattern. You buy a tool. You build dashboards. You invite stakeholders to look at the dashboards. Everyone feels informed. The tool vendor shows you a slide with a "time to value" metric that is somehow always under 30 days.

What the slide does not show: the delta between your infrastructure bill six months after the tool and six months before.

Across several infrastructure teams I've worked with, the gap between "we have observability" and "our observability recovered money" tends toward years — not because the engineers were bad, but because the goal was never cost recovery. The goal was confidence. Confidence is fine. It is not the same thing as money.

## What actual cost-finding looks like

The observability work that finds money looks different from the work that produces dashboards. It starts with a question, not a metric.

*What is the most expensive thing our system does that we never intended to do?*

The answers are usually not in your existing dashboards. The over-provisioned database that runs at 8% CPU at 3 AM. The idle instances that exist because a deployment script forgot to scale down. The polling loop that fires 40,000 requests per hour to check whether a value has changed when a webhook would cost 40.

These are not visible in standard dashboards. They are visible in cost-per-transaction breakdowns, idle resource timelines, and request routing traces. None of these are in the default setup of most observability tools.

## SLO theater is the most expensive dashboard

SLOs are useful. SLO theater is expensive.

SLO theater is what happens when a team picks SLO targets that are easy to hit. Not because they reflect actual user harm, but because breaking an SLO triggers a postmortem, and no one wants a postmortem. So you set your latency SLO at the 95th percentile of your current performance, which means you are measuring how consistently you are doing what you were already doing.

The cost: you now have a contractual obligation to maintain something that may not be worth maintaining. The SLO becomes a ceiling disguised as a target. You spend engineering cycles hitting a number that was never tied to revenue. In my experience this is common enough to be a pattern, even without systematic data.

## The structural problem

The root issue is that observability tools are sold as infrastructure. Infrastructure costs money. You put them in the budget as a cost center. The teams that buy them are not measured on whether they recover more than they cost. They are measured on whether the dashboards look good in review meetings.

This creates a predictable outcome: you get exactly the observability you incentivize. If you incentivize looking informed, you get dashboards. If you incentivize finding money, you eventually get someone digging through cost attribution data at 11 PM because they had a hunch about a polling loop.

The tooling is the same. The question is what you were looking for when you turned it on.

## What I would do differently

If I were building an observability practice from scratch with a cost recovery goal, I would start with three questions before touching any tool:

What is our largest infrastructure cost that serves no user?

What behavior in our system do we have the least visibility into?

What would a discovery save us relative to what we are spending on observability tools?

Most teams cannot answer the third question. That is the problem.

The answers are not in dashboards. They are in billing exports, architecture diagrams, and in asking the person who wrote the cron job — the one that fires 200,000 requests every night — why it does.

---

*If your observability stack has never recovered more than it costs, it is not observability. It is infrastructure theater.*
