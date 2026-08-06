# Writer Draft — 2026-06-23 22:11 UTC

## Selected topic
**Detection as code is becoming detection as debt.**

## 8 Candidate Titles (generated first, before writing)

1. "Detection as code is becoming detection as debt"
2. "The detection pipeline accrues interest you stop noticing"
3. "When detection logic becomes a liability you can't pay down"
4. "Detection debt: when your security signals quietly compound against you"
5. "Security detection rules age like technical debt — and nobody tracks the principal"
6. "The silent problem with detection-as-code is that it keeps compounding"
7. "Why your detection library is probably older than your last deployment"
8. "Detection as code matures into detection as a service — with the same old debt"

**Selected title:** "Detection as code is becoming detection as debt"

## Body (writer draft, ~900 words)

---

When teams first adopt detection-as-code, the pitch is clean: version-controlled security logic, reviewable like application code, deployable with CI/CD. Rules live in a repo. False positives get filed as bugs. The security team's knowledge is now auditable.

That story held up well. Then the repos grew.

The problem isn't that detection rules accumulate. Any mature system accumulates rules. The problem is that nobody treats the accumulation as a liability until something breaks — and by then the liability has been compounding for eighteen months.

**What detection debt looks like in practice**

A rule written in 2024 for an OAuth flow that the product team deprecated in 2025 doesn't throw an error. It just silently monitors a dead endpoint. Meanwhile, the rule still generates occasional alerts when the endpoint responds with an unexpected error code — alerts that an analyst triages and closes as false positive. Nobody deletes the rule because nobody is sure if deleting it will create a gap.

This is textbook debt: an obligation that accrues carrying cost (analyst time) without generating proportionate value, and whose true size is invisible until a specific event makes it undeniable.

The pattern I've observed across several teams: detection debt follows a predictable curve. In the first six months, the detection repo looks healthy — low rule count, high coverage, clear ownership. By month twelve, rule count has tripled, coverage has plateaued, and ownership has fragmented across three team transitions. By month eighteen, the team maintains a spreadsheet of "rules we should probably disable" that nobody acts on because the action feels like a decision, and the decision has no stakeholder champion.

**The specific failure mode nobody talks about**

Detection debt has a worse failure mode than slow coverage: it actively degrades signal quality. As the false-positive rate climbs, analyst trust in the detection layer drops. When trust drops, analysts start treating high-severity alerts with lower urgency — they assume the rule is another noisy one. The alert that finally surfaces a real intrusion gets closed as low priority because the detection layer has been crying wolf for so long.

This is the compounding effect: detection debt doesn't just waste analyst time, it trains the response team to ignore the detection layer.

I've seen this play out at organizations that had technically "complete" detection coverage but whose analysts were reflexively dismissive of anything that came from rules older than six months. The real intrusion was in the logs. The detection rules were technically covering it. But the signal had eroded.

**Why the tooling doesn't solve this**

The detection-as-code toolchain — Terraform providers for security rules, GitOps pipelines for SIEM content, YAML-defined Sigma rules — solves the deployment problem. It does not solve the lifecycle problem. You can deploy a rule with a pull request. You cannot retire a rule with a pull request unless someone has already done the analysis to confirm retirement is safe.

The retirement problem is fundamentally harder than the deployment problem: retirement requires certainty, deployment only requires intent. Detection tooling optimizes for lowering the cost of deployment without increasing the cost of retirement. This asymmetry is not accidental. Vendors sell deployment velocity. They don't sell retirement velocity.

**A partial solution that works until it doesn't**

The pragmatic response is a detection review cadence: quarterly, the detection team audits rules flagged as high false-positive rate and reviews their continued necessity. This works well in the first year. It degrades when the team is understaffed or when the detection repo is large enough that a quarterly review can't cover the full surface.

The ceiling for manual review is somewhere around 500 active rules. Above that, the review becomes a bookkeeping exercise rather than an analytical one — reviewers check boxes rather than evaluate whether each rule still maps to a live risk.

Above that ceiling, you need detection decommissioning to be a first-class engineering practice, not a security operations task. It needs to be owned by the team that writes the rules, not the team that responds to them. And it needs to be treated as valuable as writing new rules — which requires the organization's metric for detection quality to value signal-to-noise ratio, not rule count.

**The honest version of this post**

I do not have a clean solution. The detection-as-code movement solved the right problem for 2019. The problem it created — how to retire rules as deliberately as you write them — is the same problem that application code has with technical debt, and it has the same solution: treat it as first-class work, not cleanup work.

The sign that detection debt is becoming a crisis at your organization is quiet: it's when analysts start treating every alert the same way, regardless of severity. That normalization of uniform dismissal is the moment when detection stops being a security control and starts being a compliance checkbox.

What changed my mind on this was watching an incident response team with genuinely excellent detection coverage fail to respond to a real breach because they'd spent so long triaging noisy rules that they'd stopped trusting the severity ratings. The detection worked. The response didn't.

The detection layer had been accruing debt for two years. The breach was the invoice.

---
