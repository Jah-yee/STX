# EDITOR — Round 0726_0555

## Editor Review

**Title (original):** "A signed commit is not supply-chain integrity"
**Title (verdict):** Keep — 7 words, direct, correct. No change needed.

**Opening hook:** Scene is hypothetical but introduced as hypothetical. The phrasing "A team ships a compromised Python package" could read as a real incident. Change to "Imagine a team that..." to make it clearly illustrative.

**Body trim:**
- "This is not a failure of the signing infrastructure. It is a category error" — slightly wordy. Trim to "This is a category error, not an infrastructure failure."
- "Security reviews prefer high-signal artifacts" — good, keep.
- The three attack vectors are well-structured.
- The closing paragraph is strong, no changes needed.

**Ending:** Strong close. No forced question. Keep as-is.

**Word count target:** 700-1400. Current estimate ~900 words. Acceptable.

## Final approved title: "A signed commit is not supply-chain integrity"

## Final edited post:

Imagine a team that ships a compromised Python package. The git history is clean — every commit is signed, verified, and cryptographically linked to a known developer key. The CI pipeline passes. The package is published to PyPI. Three thousand production systems pull it in the next hour.

The signing worked. The attack succeeded anyway.

This is a category error, not an infrastructure failure. Commit signing solves the wrong problem for supply chain security.

**What commit signing actually verifies.** GPG signing links a commit to a specific private key. It proves that someone with access to that key authored or approved a particular diff. It does not verify that the artifact built from that commit is the artifact that runs in production. It does not verify the dependencies. It does not verify the build environment. It does not verify the package registry interaction. It verifies one step in a much longer chain.

**Where the actual supply chain attack surface lives.** The three most common supply chain compromise vectors are not "someone pushes unsigned code." They are: dependency confusion (a malicious package with a higher version number gets installed instead), typosquatting (a package with a similar name gets pulled by a misconfigured dependency spec), and compromised build infrastructure (the code is fine going in, the artifact is modified mid-build). Commit signing does not address any of these.

The 2021 ua-parser-js incident is the canonical example. A malicious actor published a package with a higher version number than the internal package it spoofed. The internal package spec used version ranges, and the resolver pulled the external package. The code ran with internal naming conventions and internal data access patterns. None of this appeared in the git history. The signed commits were real. The supply chain attack was real. The two were completely independent.

**Why the category error persists.** Signing commits feels like security work. It has the cryptographic apparatus of security — keys, signatures, verification. It is auditable and produces clear pass/fail output. This makes it satisfying to implement and easy to show in a security review. The actual supply chain integrity controls — pinned hashes for dependencies, private artifact registries with strict scope, SLSA provenance attestation for build pipelines — require more infrastructure and produce less visible output. Security reviews prefer high-signal artifacts, which means they reward signing and underinvest in the less visible controls.

**What supply chain integrity actually requires.** The standard that addresses this most directly is SLSA (Supply-chain Levels for Software Artifacts). SLSA provenance tracks the artifact through the build pipeline: this artifact was produced from this source, in this build environment, by this CI system. It links the artifact in your registry to the specific build run, not just the author of the code.

In practice, the minimum viable supply chain integrity posture is: pinned dependency hashes (no version ranges for external packages), private package registry with exact scope, and provenance attestation on artifacts. These three controls are largely independent of whether your commits are signed. They address where the actual attacks happen.

The uncomfortable implication is that a team with excellent commit hygiene and no SLSA provenance is less secure against supply chain attacks than a team with poor commit hygiene and proper artifact provenance. Signing is not irrelevant — author authentication matters for attribution and for certain classes of tampering — but it is not the control that prevents a compromised dependency from executing in your production environment.

What it comes down to: signing your commits is a worthwhile hygiene practice. Treating it as a supply chain security control is category misclassification. The attack surface is in the artifact chain, not the author chain.
