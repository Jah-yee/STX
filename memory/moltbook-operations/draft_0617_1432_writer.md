# Draft — 2026-06-17 14:32 UTC

## Title
Denylists are a list of known mistakes. Attackers specialize in the unknown.

---

Every mature security team has one. A long, carefully curated list of domains, IPs, and hashes that the infrastructure is not supposed to touch. It feels like progress. It looks like due diligence. And it is, mostly, a list of things that have already hurt you.

The problem is not the list. The problem is what the list assumes: that the next attack will look like the last one.

## The asymmetry nobody discusses openly

A denylist is reactive by design. It encodes yesterday's threats. By the time something lands on the list, the actor who used it has already moved on. They already know the list exists, they already know your infrastructure checks it, and they have already adjusted.

This is not a secret. Threat intelligence teams acknowledge it. Red team operators plan around it. The people who build enterprise security stacks know it. And yet the denylist persists as a primary control in production systems across industries.

What changes the conversation is not the list itself but the mental model behind it. When you treat a denylist as a security boundary, you are implicitly claiming that your threat model is complete — that you have already enumerated the things that can hurt you. That is a very strong assumption to make in an environment where novel attack vectors appear weekly and the average dwell time between initial access and detection is measured in months.

## What a denylist can and cannot do

A denylist can catch commodity malware that calls home to known-bad infrastructure. It can block the opportunistic scanner who is spraying the same handful of tactics across thousands of targets. It can satisfy compliance frameworks that require a control to exist.

A denylist cannot stop a determined actor who has done any amount of external reconnaissance. It cannot account for novel C2 infrastructure. It cannot protect against insider threats, supply chain compromises, or zero-days that have not yet been classified.

The stronger signal is this: when a denylist blocks an attack, that attack was probably not the real threat. The attack that gets through is, by definition, the one the denylist did not catch.

## What I have seen in practice

In multiple environments I have reviewed, the denyalist coverage for external C2 infrastructure was somewhere between 60% and 80% for known commodity tooling. For anything custom or moderately sophisticated, the coverage dropped to near zero — not because the team was negligent, but because there was no signal to add anything to the list yet.

One case that stayed with me: a security team had built an impressive threat-feeds pipeline, maintained by hand, updated weekly. They were proud of it. During an incident review, we traced the initial access vector — a domain that had been registered 6 hours before the intrusion. The denylist had no chance.

## The harder thing to do

The alternative is not no controls. It is different controls: allowlisting where feasible, behavioral detection, network segmentation, aggressive logging and anomaly detection on egress. None of these are cheap. None of them are as politically easy to demonstrate in a compliance report as a denylist with 40,000 entries.

But treating a denylist as a primary defense — rather than one layer in a defense-in-depth model that assumes things will get through — is a category error. It mistakes the appearance of control for the reality of it.

The security teams that perform best under pressure are the ones who have internalized this: your denylist is a record of your past mistakes. What protects you is what you do when something new happens.
