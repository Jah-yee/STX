# Writer Draft v2 - 0709_1354

## Title: Software survives AI agents. The integrations around it don't.

---

The mainstream narrative about AI replacing software is wrong in a specific, predictable way: it assumes the value of software lives in the code. It doesn't. It lives in the data and the network effects — the fact that everyone's already using it, that integrations already exist, that migration costs are brutal. You don't replace that by building a better chatbot.

What agents are actually eating is the integration layer. The glue code. And that's a much bigger deal than it sounds.

I've been tracking how agents get deployed in engineering organizations — not in demos or pilots, but in the messy daily operations where they actually save or waste time. The pattern is consistent: the software layer stays intact. The automation scripts, the webhook handlers, the midnight cron jobs that sync your CRM to your data warehouse, the Zapier flows that were built by someone who left the company three years ago and nobody fully understands — those are the things agents are absorbing first.

This is not glamorous work. Glue code is, by definition, the work that happens at the seams between systems that were never designed to talk to each other. It requires just enough logic to handle the happy path and just enough error recovery to not wake anyone up at 3am. It's everywhere and it's invisible — until it breaks.

The reason agents land here first is also why no one built good tooling for it: it's too specific to each organization's stack to productize cleanly. Every company's Salesforce-to-database sync is slightly different. Every team's Slack-to-project-management routing has its own quirks. This work resisted abstraction, which meant it resisted tooling, which meant it got done by humans who developed lore around it over months and years.

Agents don't need the lore. They can figure out the logic from the current state of the systems. That's the leverage.

What's being displaced is therefore not "software" in the sense of the tools people think of when they imagine automation — it's the patchwork of small automations that holds those tools together into something usable. The CRM doesn't get replaced. The script that syncs leads from the marketing site into the CRM does. The project management tool survives. The daily report that aggregates data from five tools and emails it to the team at 8am does not.

There are organizational consequences to this that aren't being discussed enough. Glue code work has always been underappreciated — the people maintaining it were often treated as doing support work, not real engineering. That valuation was wrong, but it was stable. Agents disrupting that layer doesn't eliminate the work; it redistributes it. The question is whether that redistribution comes with any compensation structure for the people who built the original systems, or whether it just gets absorbed into whatever agent platform the company standardize on.

I don't have a strong answer here. What I do know is that the software itself is not in danger. The layers around it are. And that's a more interesting transition than the replacement narrative suggests — not because it's less disruptive, but because it's happening at a level where the disruption is quieter and easier to miss until it's already complete.

---

Draft complete. ~750 words.
