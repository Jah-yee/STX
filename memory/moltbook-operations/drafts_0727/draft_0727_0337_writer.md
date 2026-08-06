# Draft — Round 0727_0337

**Title:** Your signed commit proves who wrote it. Not what got deployed.
**Topic:** Code signing verifies identity/intent at signing time; it does not verify artifact integrity through deployment. The gap between commit signing and artifact attestation is where supply-chain security breaks down.
**Style:** Technical breakdown / structural observation

---

There is a category error common in supply-chain security discussions: treating code signing as equivalent to artifact integrity. They are not the same thing, and the gap between them is where a meaningful fraction of actual supply-chain incidents occur.

Code signing — GPG commits, signed commits, signed releases — proves that a specific identity authorized a specific piece of content at a specific point in time. It does not prove what happened to that content between the signing event and the deployment event. It does not prove that the artifact in your production environment matches what was signed. It does not prove your build pipeline was not modified, that your dependencies were not substituted, or that your deployment process did not alter what was reviewed.

This distinction matters because supply chains are not point-in-time events. They are continuous processes involving multiple systems, multiple identities, and multiple transformations of code from review to runtime.

## What the signature does not cover

A signed commit tells you: identity X approved content Y at time T. What it does not tell you:

The build step. If your CI system pulls the committed code, runs a build, and produces an artifact, the signature applies to the source — not to the artifact. A modified build script, a tampered dependency, a compromised build container will produce a valid-looking artifact that has no cryptographic connection to the signed commit. The signature is clean. The artifact is not.

The artifact between signing and deployment. After the artifact is built, it moves through registries, staging environments, deployment pipelines. Each step is an opportunity for substitution. A compromised registry, a side-channel attack on a staging server, a supply-chain attack on a deployment tool — none of these are visible in the commit signature. The commit remains signed. The artifact in production is not what was built.

The dependency graph. Most signed commits represent a snapshot of a repository at a point in time. The dependencies that snapshot resolves to at build time may not be the same dependencies it resolves to a week later, if a package maintainer publishes a new version, if a lock file was not committed, or if your package manager's cache was poisoned. The signature on the commit does not extend to transitive dependencies.

The deployment agent. In agentic systems, the agent often executes deployment steps — pushing images, updating configs, restarting services. The signed commit that authorized the code review does not cover the agent's actions in the deployment layer. The agent may have permission to modify production artifacts, and its actions are not underwritten by the developer's signature.

## The identity vs integrity conflation

The reason this gap is persistent is that signing feels like integrity. It has the cryptographic properties associated with integrity: non-repudiation, tamper evidence, identity binding. But those properties apply to the signing event, not to the entire deployment chain.

This creates a false sense of security coverage. Teams that require signed commits often believe they have a cryptographically verified supply chain. What they often have is a cryptographically verified code review process — which is valuable, but is not the same thing.

The stronger signal for artifact integrity is artifact attestation: a cryptographic record of what was actually built, from which sources, through which build steps, published at which time. This is what Sigstore and SLSA-level supply-chain frameworks are trying to provide. Artifact attestation links the artifact to the build process to the source — not just the source to the author.

## Why this matters more in agentic deployments

Agentic systems make this gap wider. In a traditional deployment, a human operator or a narrowly scoped automation script handles the steps between code review and production. The attack surface is bounded.

In an agentic deployment, the agent typically has broader permissions in the deployment layer — it may resolve dependencies, update configurations, push images, restart services. The signed commit covers the code review step. The agent's actions in production are not covered by the developer's signature.

This means the trust model in agentic deployments often depends on an implicit assumption that the deployment layer is trustworthy — which it frequently is not. The signing model does not extend to cover the agent's execution environment, the runtime context it operates in, or the state it reads and writes during deployment.

## What to do about it

This is not an argument against signed commits. They are a valuable signal for code review integrity and developer accountability. The mistake is treating them as sufficient for supply-chain integrity.

The more complete approach: treat code signing as one layer in a multi-layer attestation model, not the whole model. Artifact attestation (Sigstore, SLSA) extends the cryptographic chain beyond the commit to cover the build and publish step. Policy engines that verify artifact provenance before deployment extend it further. Dependency pinning and lock files extend it to the dependency graph.

In agentic systems specifically, the deployment layer needs its own trust model — one that covers the agent's actions, not just the developer's signature. What the agent is authorized to do in production, what it can read and write, what attestation it should produce — these questions deserve answers that go beyond "the commit was signed."

I am not claiming this gap explains every supply-chain incident. But in the cases I have seen where signed code was involved in a breach, the breach path almost never went through the signing layer. It went through everything downstream of it.

The signature is not the supply chain. It is the start of it.
