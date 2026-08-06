# Final Draft — Round 0727_0337 (Editor Revised)

**Title:** Your signed commit proves who wrote it. Not what got deployed.
**Style:** Technical breakdown / structural observation
**Changes from writer draft:** 3 surgical changes — tightened opening hook, merged build/artifact paragraphs, sharpened deployment agent section

---

There is a category error common in supply-chain security: treating code signing as equivalent to artifact integrity. They are not the same thing, and the gap between them is where a meaningful fraction of actual supply-chain incidents occur.

Code signing — GPG commits, signed releases, signed tags — proves that a specific identity authorized specific content at a specific point in time. It does not prove what happened to that content between the signing event and the deployment event. It does not prove that the artifact in your production environment matches what was signed. A modified build script, a tampered dependency, a compromised build container, a poisoned registry — none of these are visible in the commit signature. The signature is clean. The artifact is not.

This creates a false sense of security coverage. Teams that require signed commits often believe they have a cryptographically verified supply chain. What they often have is a cryptographically verified code review process — which is valuable, but is not the same thing.

The dependency graph compounds the problem. Most signed commits represent a snapshot of a repository at a point in time. The dependencies that snapshot resolves to at build time may not be the same dependencies it resolves to a week later, if a package maintainer publishes a new version, if a lock file was not committed, or if a package manager's cache was modified. The signature on the commit does not extend to transitive dependencies. Pinning and lock files are the partial answer here, but they introduce their own maintenance burden.

## The identity vs integrity conflation

The reason this gap is persistent is that signing feels like integrity. It has the cryptographic properties associated with integrity: non-repudiation, tamper evidence, identity binding. But those properties apply to the signing event, not to the entire deployment chain. A signed commit tells you: identity X approved content Y at time T. What it does not tell you is whether the artifact that reached production has any connection to that content.

This matters more in agentic deployments. An agent typically has broader permissions in the deployment layer — resolving dependencies, updating configurations, pushing images, restarting services. The signed commit covers the code review step. The agent's actions in the deployment layer are not underwritten by the developer's signature. In agentic systems, the deployment layer needs its own trust model — one that covers what the agent can read, write, and execute in production, and what attestation it should produce.

The stronger signal for artifact integrity is artifact attestation: a cryptographic record of what was actually built, from which sources, through which build steps, published at which time. This is what Sigstore and SLSA-level supply-chain frameworks are trying to provide. Artifact attestation links the artifact to the build process to the source — not just the source to the author.

I am not claiming this gap explains every supply-chain incident. But in the cases I have seen where signed code was involved in a breach, the breach path almost never went through the signing layer. It went through everything downstream of it — the build system, the registry, the deployment pipeline, the agent's execution environment.

The signature is not the supply chain. It is the start of it.
