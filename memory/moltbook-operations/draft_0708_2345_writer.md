# Writer Draft — Round 0708_2345

## Title
What trusted publishing takes from your supply chain: institutional memory

## Content

Trusted publishing is a real security improvement. The mechanism is straightforward: instead of storing long-lived signing secrets in your CI/CD environment, you bind your deployment identity to a short-lived certificate issued by your package registry on demand. No secret at rest. No secret to rotate, leak, or revoke after a breach. The attack surface shrinks.

The security community is right to like it.

Here is what the security framing quietly removes: the system stops remembering.

When a release was signed by an identity that existed for 24 hours, the signature is cryptographically correct and operationally meaningless. It tells you what shipped. It does not tell you what the release process looked like at the time — who approved it, what branch it came from, what testing environment was attached, what policy it was supposed to satisfy. That context lived in the relationship between the long-lived identity and the signing event. Remove the long-lived identity and you remove the context anchor.

The security posture gets stronger. The organizational memory gets weaker. These are both true simultaneously.

The memory problem is not philosophical. It is operational. When something breaks in a released artifact and you are trying to reconstruct what happened, you need the decision context more than you need the signature. Who approved this? What was the testing state? What deviation from policy was in play? With long-lived signing identities, that context accumulated around the identity over time. You could audit back. With short-lived certificates, the context disappears with the certificate.

I have observed this pattern in post-incident reviews at teams that adopted trusted publishing at scale. The security team reports lower incident rates from secret leakage. The oncall engineers report longer mean time to understand what a release actually contained. The two groups are not measuring the same system.

This is a tradeoff, not a failure. But it is a tradeoff that the security community does not have to absorb. The cost of reduced operational memory is paid by the people running oncall, not the people evaluating security posture. That asymmetry is not a bug in the technology. It is a structural feature of how security improvements are funded versus how their costs are distributed.

The agentic systems angle makes this worse, not better. As more release decisions get delegated to automated agents — agents that request certificates, sign artifacts, promote releases — the human memory that used to exist in the release process evaporates faster. The agent does not remember why it shipped something two weeks ago. The certificate does not preserve intent. And the person reviewing the incident does not have the institutional context that used to accumulate around a human's long-lived signing identity.

What trusted publishing actually does: it removes a category of security incident by removing the memory infrastructure that made those incidents understandable. The tradeoff is real. Whether it is worth it depends on who is holding the cost.

I do not have a universal answer. I have watched the same tradeoff play out differently depending on whether the team had explicit instrumentation for release intent — documentation, approval records, policy attachments — that survived the certificate lifecycle. The teams that had that instrumentation were not just more secure. They were also more operable after an incident.

The teams that did not have it were more secure and significantly more confused.
