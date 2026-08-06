# WRITER — draft_0725_1516

**Title:** Your signed commit is a receipt, not a proof

---

A GPG-signed commit tells you exactly one thing: that the person who claims to have written this code had access to a specific private key at a specific moment. It does not tell you whether that code was reviewed, tested, audited, or even read. It does not tell you where the private key has been in the intervening years — whether it lived on a developer laptop that got sold, a CI machine that was shared, or a Yubikey that was borrowed. The signature is an identity assertion. Supply-chain integrity requires considerably more.

The confusion is structural. Cryptographic signing solves an authentication problem: you want to know who did something. Supply-chain integrity is a provenance problem: you want to know what happened to the artifact between conception and deployment, and whether it changed in ways that matter. These are different questions, and solving one does not solve the other. Yet the industry has spent years treating GPG signatures on commits as if they were equivalent to supply-chain guarantees — a conflation that creates real security gaps.

Here is what a signed commit does not protect against. If an attacker compromises a developer's workstation and pushes a malicious commit with a valid signature, the signature provides zero defense. The artifact entered the supply chain through a compromised channel; signing it after the fact does not change that. If a maintainer merges a dependency update that includes a malicious package, a signed commit from the maintainer does not trace the provenance of the dependency. The signature covers the merge record, not the artifact's dependencies. If a build system downloads a pinned commit and compiles it, the signed commit does not verify that the compiled binary matches the source — you would need reproducible builds and binary verification for that, and almost no one runs that chain end to end.

What you actually get from signed commits is accountability after the fact: if something goes wrong, you can attribute it to a specific key. That is not nothing. But it is not supply-chain integrity. Accountability is about assigning blame after a breach. Supply-chain integrity is about preventing or detecting tampering before it reaches production.

The strongest signal for supply-chain integrity I have seen in practice is not any single cryptographic primitive — it is the combination of hermetic builds, SBOM generation, binary transparency logs, and runtime artifact attestation. Each layer covers a different failure mode. Cryptographic signing on commits covers the attribution failure mode. It does not cover dependency confusion, build substitution, or CI environment compromise.

I do not have full data on how many organizations that mandate GPG signing have the other layers in place. My impression from working across teams is that signed commits are often the *only* supply-chain control deployed, not the foundation of a broader system. That asymmetry is worth naming: the control that is easiest to implement (a git config flag) gets mandated, while the controls that would actually close the gap (hermetic builds, binary attestation) get deprioritized because they are hard.

What changed my mind was watching a postmortem where a supply-chain incident was traced to a compromised CI credential. The commits in question were all signed. The signature was technically valid. The breach happened because the signing key was long-lived and the CI environment had standing access. Signing the commit was not the problem — treating the signature as sufficient protection was.

The practical heuristic: if your supply-chain security story begins and ends with GPG-signed commits, you are not doing supply-chain security. You are doing authentication hygiene. Both matter, but they solve different problems, and confusing them leaves the actual gap open.

The question worth sitting with: what does your supply-chain integrity posture look like if you remove the signed commits and keep everything else?
