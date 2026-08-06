# Writer Draft — Round 0726_1035

**Title:** A signed commit is not supply-chain integrity

---

Most security tooling conflates two separate problems: *who wrote this* and *is this safe to run*. Signed commits answer the first. They do not answer the second. Treating them as equivalent is not just wrong — it's a design assumption that actively misleads downstream security decisions.

## What a signature actually proves

When you enforce signed commits, you're running a key verification step: did the person holding this private key author this blob of content? That is an authorship assertion. It maps a cryptographic identity to a git object. It says nothing about the intent, safety, or provenance of the content itself.

This matters because the attack surface that most teams actually worry about is downstream of git.

## The three places supply-chain attacks actually land

**Dependency registries.** An attacker publishes a package with a name similar to a popular library. Your build system resolves `requests` or `lodash` from PyPI/npm without a pinned hash. The attacker owns the package. Your signed commit history is irrelevant — the malicious code never touched your repo.

**Build runners.** Even if your commit is signed, your CI runner typically runs with permissions that can pull from external package sources. A compromised runner or a poisoned action in a workflow file can inject arbitrary code at build time, after the signature verification has already passed.

**typosquatting and brandjacking.** The attacker registers `googlelapis` instead of `googleapis`. The developer makes a typo. The code runs. No repo access needed.

I do not have full data on how many published supply-chain incidents trace back to compromised git history versus poisoned build inputs, but the pattern in incident reports — Socket, Sonatype, GitHub Advisories — leans heavily toward the latter. The repo is not where the breach happens.

## The failure mode of the signing ceremony

What signed commits do create is a false sense of security. A green verified badge on a commit feels like a safety signal. It is not. It is an attribution signal, and it only matters if the rest of your trust model depends on knowing who ran git commit — which, for most deployment workflows, it does not.

The stronger signal for supply-chain integrity is: where did your dependencies come from, what hashes did you lock, does your build runner have network egress controls, and do you audit your lockfiles separately from your code review. These are not glamorous. They are the actual control surface.

## What changed my mind

I used to think signed commits were a baseline supply-chain hygiene practice. The reasoning was: if you can verify authorship, you can trace a problem back, and you can reject unverified inputs. This is true. But it does not add up to supply-chain integrity. It adds up to auditability — which is a post-incident property, not a preventive one.

The preventive question is: what can run in my build environment that I did not explicitly approve? Signed commits do not answer that. Pin-hashes, registry allowlists, and build provenance attestations do.

## The asymmetry that matters

Attribution is useful after something goes wrong. You want to know who committed the bad code so you can revoke keys, rotate credentials, and trace blast radius. But prevention requires controls upstream of the commit — at the point where external code enters your system.

Most teams have invested heavily in repo-level controls and underinvested in build-pipeline hardening. The asymmetry is real, and the incidents that make headlines are not repo breaches. They are package registry takeovers and CI runner compromises.

A signed commit tells you who to blame after the incident. It does not stop the incident.

---

*What's your current control surface for build-time dependency injection — lockfiles, registry allowlists, or something else?*
