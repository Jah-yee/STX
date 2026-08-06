# Editor — Round 0726_1035

## Title
**A signed commit is not supply-chain integrity** — Keep. Direct, counter-intuitive, 7 words, no "I".

## Surgical Changes

1. **Expand "three places supply-chain attacks actually land"** — Currently 3 short paragraphs. Add 1-2 concrete details per section to get to ~900-1000 words total. Specifically:
   - Dependency: add mention of "verdaccio/internal registry" scenario
   - Build runner: add "ephemeral runners with persistent network access" risk
   - typosquatting: mention the lookup cost vs. payoff asymmetry

2. **Opening hook** — Strong enough. Keep as-is.

3. **"What changed my mind"** — Good section, keep. Add one sentence on *why* the mental model shift happened — specifically that "auditability ≠ preventability" was the key reframe.

4. **Closing question** — Keep, but tighten: "What's your control surface for build-time dependency injection right now?" slightly more direct than "where did your dependencies come from" framing.

5. **No cuts needed** — Nothing is padded or overcomplicated. This is appropriately lean. Only additions (item 1 above).

## Final Post

**Title:** A signed commit is not supply-chain integrity

---

Most security tooling conflates two separate problems: *who wrote this* and *is this safe to run*. Signed commits answer the first. They do not answer the second. Treating them as equivalent is not just wrong — it's a design assumption that actively misleads downstream security decisions.

## What a signature actually proves

When you enforce signed commits, you're running a key verification step: did the person holding this private key author this blob of content? That is an authorship assertion. It maps a cryptographic identity to a git object. It says nothing about the intent, safety, or provenance of the content itself.

This matters because the attack surface that most teams actually worry about is downstream of git.

## The three places supply-chain attacks actually land

**Dependency registries.** An attacker publishes a package with a name similar to a popular library. Your build system resolves `requests` or `lodash` from PyPI/npm without a pinned hash. The attacker owns the package. Your signed commit history is irrelevant — the malicious code never touched your repo. Even teams running internal package mirrors can fall victim if the mirror pulls external updates without hash verification.

**Build runners.** Even if your commit is signed, your CI runner typically runs with permissions that can pull from external package sources. Ephemeral runners with persistent network egress access are particularly exposed — a compromised action in a workflow file or a poisoned Docker base image can inject arbitrary code at build time, after the signature verification has already passed.

**typosquatting and brandjacking.** The attacker registers `googlelapis` instead of `googleapis`. The developer makes a typo. The code runs. The attacker wins. No repo access needed, and the cost of registering similar-looking domains is near zero compared to the payoff of a successful hit.

I do not have full data on how many published supply-chain incidents trace back to compromised git history versus poisoned build inputs, but the pattern in incident reports — Socket, Sonatype, GitHub Advisories — leans heavily toward the latter. The repo is not where the breach happens.

## The failure mode of the signing ceremony

What signed commits do create is a false sense of security. A green verified badge on a commit feels like a safety signal. It is not. It is an attribution signal, and it only matters if the rest of your trust model depends on knowing who ran git commit — which, for most deployment workflows, it does not.

The stronger signal for supply-chain integrity is: where did your dependencies come from, what hashes did you lock, does your build runner have network egress controls, and do you audit your lockfiles separately from your code review. These are not glamorous. They are the actual control surface.

## What changed my mind

I used to think signed commits were a baseline supply-chain hygiene practice. The reasoning was: if you can verify authorship, you can trace a problem back, and you can reject unverified inputs. This is true. But it does not add up to supply-chain integrity. It adds up to auditability — which is a post-incident property, not a preventive one.

The mental shift that matters: auditability tells you what happened after the fact. Prevention requires controls at the points where untrusted input enters your system. The two are not interchangeable, and confusing them leaves the actual attack surface unguarded.

The preventive question is: what can run in my build environment that I did not explicitly approve? Signed commits do not answer that. Pin-hashes, registry allowlists, and build provenance attestations do.

## The asymmetry that matters

Attribution is useful after something goes wrong. You want to know who committed the bad code so you can revoke keys, rotate credentials, and trace blast radius. But prevention requires controls upstream of the commit — at the point where external code enters your system.

Most teams have invested heavily in repo-level controls and underinvested in build-pipeline hardening. The asymmetry is real, and the incidents that make headlines are not repo breaches. They are package registry takeovers and CI runner compromises.

A signed commit tells you who to blame after the incident. It does not stop the incident.

---

*What's your current control surface for build-time dependency injection — lockfiles, registry allowlists, or something else?*
