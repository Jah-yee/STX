# Writer Draft — 2026-05-31 23:46 UTC

**Title:** Unsigned Automation Is Just RCE With a Product Manager

---

There is a class of vulnerability that the security industry takes extremely seriously when it is malicious, and almost no seriously when it is authorized. That gap is not an oversight. It is a naming problem.

Remote Code Execution—RCE—is among the most severe findings in any security audit. An attacker who can run arbitrary code on your system can do anything: exfiltrate data, establish persistence, move laterally. The response is immediate: isolate, patch, verify signatures, apply least privilege. We have an entire vocabulary for this class of risk. We have scanners for it. We have CVSS severity ratings for it.

Now consider what happens when the same mechanism runs with organizational blessing. An integration—call it a Zapier zap, a GitHub Action, a Make scenario, a vendor webhook—sits inside your environment executing code on your behalf. It has an API token. It has write access. It was set up by a product manager three years ago and no one has audited it since. The contractor who built it left. The token never rotated.

That is RCE. The only difference is that someone with a budget approved it.

The LastPass breach of 2023 did not proceed primarily through guessed passwords or phishing links. The attacker moved through third-party integrations, CI/CD pipelines, and developer environments—automated systems with elevated access that were not treated as execution surfaces because they were called "infrastructure" rather than "code." The mechanism was identical to what a red team would exploit: execute here, persist there, escalate somewhere else. The vocabulary changed; the risk did not.

The same pattern appears at smaller scale constantly. The Zapier integration that can read your CRM and write to your data warehouse has a token with more privilege than most employees have on their laptops. The Make scenario that triggered on a webhook and modified records in your production database was set up by someone who needed a problem solved quickly. The service account your vendor uses to sync data has permissions that no security review would approve if the same permissions appeared on an externally-facing endpoint.

We call this interoperability. We call this automation. We call this integrations. The security properties are identical to RCE, but we have decided that intent matters more than mechanism. If someone inside the organization authorized the execution, it is not a vulnerability. It is a feature.

This is the normalization of a risk that the industry would never accept in an adversarial context. We apply least privilege to compute instances but not to the automations that run on them. We audit code that is deployed to production but not the Zapier zap that has been syncing data for three years with a token that was never rotated. We run sandboxes for untrusted executables but not for the vendor webhook that processes every incoming lead.

The concrete version of this risk is everywhere. GitHub Actions with write permissions on repositories that contain secrets. OAuth tokens issued to third-party apps that can read your entire Google Workspace. Service accounts used by internal automations with admin-equivalent database permissions. Each one individually looks small. In aggregate, they are an attack surface that most organizations do not even inventory.

What changed my mind about this was not a breach I read about. It was looking at my own automation layer and realizing I had no idea how many active tokens existed, who issued them, what they could access, or whether any had been compromised. I found tokens from vendors who had gone out of business, tokens for integrations that no longer existed, tokens scoped to read-write when read-only would have been sufficient. It was not a security incident. It was worse: it was a security posture I could not even accurately describe.

The strongest signal is that the organizations with the most mature security programs treat automation tokens as a distinct threat category. They inventory them. They rotate them. They apply least privilege at the automation layer, not just the human layer. They treat "approved by a product manager" as the beginning of a security review, not the end of one.

The solution is not to eliminate automation. It is to apply the same threat model to your automation surface that you apply to your code execution surface. If an automation can run code or modify state in a system that matters, it is a privileged execution context. Treat it accordingly: sign it, audit it, scope it, and monitor it.

The industry already knows how to reason about RCE. The gap is that we use a different word for it when the same mechanism is approved internally, and we pretend the vocabulary change reduces the risk. It does not.
