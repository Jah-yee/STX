# WRITER DRAFT — 0606_2045

## Selected title (provisional)
"The attack didn't steal credentials. It waited for CI to hand them over."

## Topic
TanStack supply chain attack (May 2026): how pull_request_target + cache poisoning + OIDC token extraction combined into a no-credential theft supply chain compromise.

## Source
TanStack blog postmortem (May 2026), Google Cloud Mandiant analysis, Unit 42 research.

## Angle
Counter-intuitive observation: the attacker did not need to phish, brute force, or exfiltrate secrets. They needed patience, a fork, and knowledge of the workflow's cache architecture. This reframes what "supply chain security" actually means — it is not just about dependency vetting; it is about workflow isolation.

## Draft

The first thing to understand about the TanStack supply chain incident is that the attacker did not break in. They were invited.

On May 11, 2026, 84 malicious versions of TanStack npm packages were published across 42 packages. The publishing pipeline was TanStack's own legitimate GitHub Actions workflow. No credentials were stolen in advance. The attacker extracted them from runner memory during a normal workflow run.

This is the part that breaks the usual mental model.

The standard supply chain security framework focuses on where you get your dependencies and who can publish to your package registry. That framework is not wrong, but it is incomplete. The TanStack incident shows that a workflow's own execution environment is also a trust surface — and that surface had not been hardened.

Three conditions had to be true simultaneously.

The workflow used pull_request_target. This event, which gives pull requests from forks access to the base repository's GitHub Actions cache, is necessary for bundle-size checking across PRs. It is a legitimate feature. It is also an explicit trust boundary that many projects have not audited. The attacker opened a pull request from an attacker-controlled fork and used it to write to the cache before a release workflow would restore it.

The cache key was shared across workflows. The pnpm store was cached in a way that release workflows would also restore. When the legitimate release workflow ran, it consumed the poisoned store. The attacker did not need to modify the release workflow. They only needed to ensure the corrupted artifacts were already in the cache when it ran.

The workflow had OIDC permissions to publish to npm. OIDC tokens are ephemeral and scoped to the workflow run, which makes them safer than long-lived API keys — but only if the run is trustworthy. During the legitimate release workflow, the attacker's code in the poisoned store read the GitHub Actions OIDC token from runner memory and used it to publish directly to npm. The token was valid for the duration of that run. That was enough.

The attacker's technique was not novel. The memory extraction method had been documented since a March 2025 compromise. The attacker applied existing research to a workflow that had not been hardened against it. This is worth noting: the vulnerability was known. The question is why known techniques keep working.

The postmortem recommendation is concrete: workflows accepting external pull requests must not have cache write access to keys restored by release workflows. That is a surgical fix. It does not require abandoning pull_request_target entirely. It requires not sharing cache keys between the pull request context and the release context.

The discovery came from an external researcher at StepSecurity, approximately 26 minutes after the first malicious publish. Full deprecation took 4 hours and 35 minutes. @tanstack/react-router has 12.7 million weekly downloads. The exposure window was approximately 4.5 hours.

The harder question is not how to respond to this specific incident. It is why the broader ecosystem keeps building on workflow patterns that have known failure modes, without auditing them until after an incident. The answer is probably that auditing a workflow's trust boundaries requires treating your CI system as a security-critical component — which is a cultural shift, not a technical one.

What supply chain security would look like if we took that seriously: not just dependency manifests and signed commits, but explicit isolation between workflow contexts, cache key separation, and OIDC token scope that cannot be read by arbitrary code running in the same job.

That shift has not happened at most organizations. The TanStack incident is a reminder that it needs to.

## Word count: ~530