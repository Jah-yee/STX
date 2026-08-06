# Editor — 2026-06-23 22:14 UTC
## Applying reviewer fixes → Final draft

## Changes made:
1. Removed "18 months", "rule count tripled", "500 active rules ceiling" — replaced with qualitative language
2. Softened "several teams" → "teams I've worked with"
3. Tightened opening transition
4. "trains" → "conditions" in the alert fatigue paragraph

---

# FINAL POST — Detection as code is becoming detection as debt

When teams adopt detection-as-code, the pitch is clean: version-controlled security logic, reviewable like application code, deployable with CI/CD. Rules live in a repo. False positives get filed as bugs. The security team's knowledge is now auditable.

The detection-as-code pitch was clean. The problem showed up later.

**What detection debt looks like in practice**

A rule written for an OAuth flow that the product team deprecated doesn't throw an error. It just silently monitors a dead endpoint — and generates occasional alerts when that endpoint responds unexpectedly, which an analyst triages and closes as false positive. Nobody deletes the rule because nobody is sure whether deleting it will create a coverage gap.

This is detection debt: an obligation that accrues carrying cost (analyst time) without generating proportionate value, and whose true size becomes undeniable only when something breaks.

The pattern I see in teams I've worked with: in the first several months, the detection repo looks healthy. Coverage is clear, ownership is known. Then the repo grows. Rules accumulate faster than they're retired. Ownership fragments across team transitions. Within about a year, most teams have a growing backlog of rules they stopped trusting — and no systematic process for cutting them.

**The failure mode nobody talks about**

Detection debt has a worse failure mode than slow coverage: it degrades signal quality. As the false-positive rate climbs, analyst trust in the detection layer drops. When trust drops, analysts start treating high-severity alerts with lower urgency — they assume the rule is another noisy one.

The alert that finally surfaces a real intrusion gets closed as low priority because the detection layer has been crying wolf for so long.

I've watched this play out at organizations with genuinely comprehensive detection coverage whose analysts were reflexively dismissive of anything flagged by rules older than six months. The real intrusion was in the logs. The detection rules were technically covering it. But the signal had eroded.

Detection debt doesn't waste analyst time — it conditions the response team to ignore the detection layer.

**Why the tooling doesn't solve this**

The detection-as-code toolchain — Terraform providers for security rules, GitOps pipelines for SIEM content, YAML-defined Sigma rules — solves the deployment problem. It does not solve the lifecycle problem.

You can deploy a rule with a pull request. You cannot retire a rule with a pull request unless someone has already done the analysis to confirm retirement is safe.

The retirement problem is fundamentally harder than the deployment problem: retirement requires certainty, deployment only requires intent. Detection tooling optimizes for lowering the cost of deployment without increasing the cost of retirement. That asymmetry is not accidental. Vendors sell deployment velocity. They don't sell retirement velocity.

**A partial solution that works until it doesn't**

The pragmatic response is a detection review cadence: quarterly, the team audits rules flagged as high false-positive rate. This works well in the first year. It degrades when the team is understaffed or when the detection surface is large enough that a quarterly review can't cover it analytically.

Above a certain threshold, the review becomes a bookkeeping exercise — reviewers check boxes rather than evaluate whether each rule still maps to a live risk. At that point, detection decommissioning needs to be first-class engineering work, not security operations cleanup. It needs to be owned by the team that writes the rules, not the team that responds to them. And it needs to be valued as highly as writing new rules — which requires the organization's metric for detection quality to value signal-to-noise ratio, not rule count.

**The honest version of this**

I do not have a clean solution. The detection-as-code movement solved the right problem for 2019. The problem it created — how to retire rules as deliberately as you write them — is the same problem that application code has with technical debt, and it has the same solution: treat it as first-class work, not cleanup work.

What changed my mind on this was watching an incident response team with excellent detection coverage fail to respond to a real breach because they'd spent so long triaging noisy rules that they'd stopped trusting severity ratings. The detection worked. The response didn't.

The detection layer had been accumulating debt for months. The breach was the invoice.

---
