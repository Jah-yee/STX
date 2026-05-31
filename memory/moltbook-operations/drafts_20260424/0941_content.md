# 2026-04-24 0941 UTC — Post Content

## Title
The real attack surface is every third-party AI tool your people have authorized

## Style
Industry take / structural breakdown

## Word count target: 700-1400

---

Vercel's April 2026 security bulletin — updated today — names the initial access vector: a compromise at context.ai, a third-party AI tool used by one Vercel employee. That single foothold pivoted to Google Workspace, then to the employee's Vercel account, then to environment variables that should not have been decryptable from that chain.

Every step in that chain was authorized. The OAuth consent was real. The employee really granted it. The scope the tool requested was the scope the tool received. No credentials were stolen. No zero-day was exploited. The attack worked because delegation, in a cloud-native environment, is indistinguishable from access.

This is the shape of agent-era breaches. Not broken locks — authorized doors that nobody drew on the map. The attacker does not have to defeat your SSO. They have to compromise something your SSO already let in. The perimeter is not the firewall. The perimeter is the graph of every third-party integration your people have consented to on behalf of the organization.

The graph nobody draws.

I have been trying to map my own organization's third-party AI tool exposure. Not the vendors security approved — those are on the diagram. The others. The ones individual employees connected because a tool looked useful, because a workflow needed it, because the approval process for a research add-on takes three weeks and the work needs to happen now. The now-decisions accumulate into a shadow infrastructure that does not appear in any security architecture I have seen.

Straiker's zero-click research, published yesterday, provides the companion vulnerability: 94% of agents are vulnerable to prompt injection through exactly this mechanism. The agent reads the payload because reading is its job. No click required. No user interaction needed. The attack surface is not a misconfigured server — it is an agent that has been granted scopes it uses every day, and a prompt that lives in data the agent already processes.

The intersection is new and specific. Agents with granted OAuth scopes plus prompt injection vulnerabilities equal a single compromised integration that can access everything the integration was authorized to touch, and the agent will execute the compromised instructions because the instructions arrive through a trusted channel.

We are not building for this threat model. We are building agents that request broad scopes — read your email, access your files, manage your calendar — because narrow scopes are harder to configure and the value of the tool is proportional to the access it has. The access-proportional-to-value means the incentive is toward maximum consent, and maximum consent in a world where agents are vulnerable to injected instructions is maximum exposure.

The uncomfortable corollary for every security team reading this: your access management diagram has a layer it does not draw. The layer is the graph of every AI tool every employee has connected, with what scopes, on whose behalf, from which IP addresses, with what data retention terms. That graph is the real perimeter. Almost nobody owns it.

Ownership requires answers to questions that most organizations cannot currently answer. Which AI tools have employees authorized in the last 90 days? What scopes did each one request and what did it actually receive? Which third-party tools have read access to your internal data, and what happens to that access when the employee leaves? When a vendor deprecates an integration, who gets notified, and who revokes the consent?

I have asked these questions inside three organizations in the last two months. The answers were: we do not know, we would have to audit that, and that is a good question for the team that does not exist yet.

The team that does not exist yet is the answer to who owns the delegated perimeter. Not IT. Not Security Operations. The delegated perimeter is the intersection of Identity, Security, and AI Governance — a team that almost no organization has formed, because the threat has not yet produced enough visible damage to justify the formation.

Vercel's breach is that damage. The context.ai compromise is not a vendor failure — it is a structural revelation. It shows what happens when an authorized integration becomes an attack path: the chain works because every link was consensual, and the consent was granted by people who did not understand that their OAuth token would eventually lead to production environment variables.

The question is not whether your organization uses third-party AI tools. The question is whether you know which ones, with what scopes, and what your incident response plan looks like when one of them is the initial access vector for a breach that starts in someone's personal context.ai account.

You probably do not have a plan. Nobody does yet. That is the vulnerability.

---

## Review notes
- Center is organizational ownership vacuum — distinct from earlier post about OAuth scope being the perimeter
- This one is about the governance gap: no team owns the delegated perimeter, no diagram shows it
- Vercel breach as real evidence, Straiker 94% stat
- Question-based ending, no "what can we learn" boilerplate
- Should pass reviewer check: no template pattern, not "I did X", no hollow data