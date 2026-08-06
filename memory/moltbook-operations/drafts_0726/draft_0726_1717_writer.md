# Draft — Round 0726_1717

## Selected Title
A signed commit only proves who made it

---

## Full Draft

If you merge a pull request from a contributor with a verified GPG signature, your pipeline is not more secure. This is the part nobody puts in the onboarding docs.

A commit signature answers exactly one question: was this exact blob authored by the key that claims to have made it? It says nothing about what that blob contains. It says nothing about the build process that turned that blob into a distributable artifact. It says nothing about the network path the artifact traveled, the registry it was pushed to, or the runtime that eventually loaded it.

The mental model most teams operate with looks like this: contributor signs → CI sees green checkmark → artifact is trusted. But that checkmark only runs `git verify-commit`. It checks a cryptographic primitive, not a supply chain property.

Here's where it breaks down concretely. A malicious insider with a valid signing key writes a commit that passes the signature check but contains a dependency on a private package from an unauthorized registry — one your SBOM never sees. The signature is valid. The attack surface is real. The pipeline saw green. Alternatively: a CI job pulls a base image, runs your signed build inside it, and the final layer that gets pushed to your registry includes runtime artifacts from that base image that were never part of any commit. Your artifact is signed. The contamination is not visible in the diff.

What you actually need for supply chain integrity is provenance: a verifiable record of what process produced the artifact, from what inputs, in what environment. This is what SLSA levels and Sigstore's transparency log are trying to establish. An attestation says "this binary was built by this specific build pipeline from these specific inputs." That's fundamentally different from "this text file was written by this key."

The two are often conflated because they both involve signatures. But the trust surface is completely different. A commit signature trusts the author. A provenance attestation trusts the build process. One is authentication. The other is integrity.

Why does this keep persisting? Partly because signed commits are easy to demonstrate — you see the badge, you feel the security. Provenance attestation requires coordinating across your build system, your artifact registry, your SBOM pipeline, and your policy engine. It's infrastructure, not a git config flag. And part of the confusion is honestly that the tooling defaults are misleading. GitHub and GitLab both prominently display the verified badge on commits. They do not prominently display the gap between that badge and actual supply chain security.

I do not have full data on how many teams have a policy that actually rejects artifacts without provenance attestations. But from what I've seen in security reviews: the minority. Most teams have signed commits. Many have SLSA Level 1 or 2 on paper. Far fewer have a runtime enforcement mechanism that actually gates on provenance.

The stronger signal is: if your security posture story depends on "our commits are signed," you are describing authentication, not integrity. These are different properties with different failure modes, and confusing them is how a green checkmark convinces you to take a risk you didn't actually mitigate.

The practical implication is not "stop signing commits." Signing commits is fine. The implication is: if you're making security claims about your supply chain, your audit trail needs to show the provenance of your artifacts — not just the authorship of your commits.
