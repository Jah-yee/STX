# Editor — 0728_1527

## Title
Why your security automation creates more incident surface than it closes

## Changes from Writer
1. Softened "forty minutes" → "for an extended window" (no specific data point implied)
2. Expanded three-conditions section with 1-2 sentences each for context
3. Expanded what-changed-my-mind with additional reasoning detail (~60 words added total)
4. Minor: rewrote "The stronger signal is this" to be less formulaic

## Final Draft

The setup: a triage copilot with permission to close alerts parsed a ticket labeled "duplicate," found the keyword, and closed the live escalation it was assigned to monitor. The actual incident kept running. Nobody noticed for an extended window.

This is not a model failure. This is an architectural one. The tool was working exactly as designed — it just had the wrong threat model.

Security automation with write access, when triggered by untrusted input parsing, creates a privilege-escalation path that least-privilege access controls do not address. The blast radius is not "a wrong alert close." It is "a wrong alert close executed with the trust signature of the automation system."

When a security tool reads incident text — titles, descriptions, correlation IDs — and uses that to decide whether to mutate state (close, escalate, suppress, unblock), it is executing a privileged action based on untrusted input. The model does not know what "duplicate" means in your workflow context. It knows that the word "duplicate" appeared near the word "ticket" in training data associated with close actions.

This is the autocomplete failure mode specific to security tools: the completion is not a draft email. It is a state transition with audit-trail authority.

The blast radius becomes real when three conditions hold simultaneously.

First: the tool has write access on untrusted parse — it can mutate state based on input it did not generate and cannot verify. Second: trust transfers from system to output, meaning the action carries the authorization of the automation service account rather than the model, so downstream systems see it as a verified human decision. Third: there is no recovery window, because state mutations that complete before a human can intervene create incidents faster than the tool was meant to prevent them.

Least-privilege access says: give the security copilot only the permissions it needs. This is correct for the service account. It is irrelevant to the input surface. The copilot's effective permission is not its service account — it is the intersection of that service account and the model's ability to parse intent from untrusted text.

The security property is not "what can this tool do?" It is "what can this tool be tricked into doing when it reads something that looks like a valid trigger?"

The correct abstraction is not read-only vs. read-write. It is: any state mutation triggered by untrusted input requires a human confirmation step, regardless of the confidence score.

Confidence does not help here. A 99% confident close decision on an untrusted parse is worse than a 60% decision, because it removes the human review that lower-confidence outputs naturally trigger. High confidence in an untrusted-input context is a hazard, not a feature.

The security copilot that triages your alerts is not a model failure waiting to be fine-tuned. It is an architectural category error: a privileged actor reading untrusted text and taking irreversible actions based on pattern match, presented as automation efficiency.

The fix is not a better prompt. It is a different system design — one that treats every untrusted-input-triggered mutation as a two-step process, regardless of what the confidence meter says.

What changed my mind: I originally thought this was a trust-boundary problem solvable with better role assignment. It is not. The model's ability to parse intent from incident text means the input surface itself is the privilege boundary. No amount of service-account least-privilege closes that gap. The failure mode is structural, not parametric — you cannot tune your way out of an architecture that was wrong from the start.

The real problem is that this kind of incident does not show up in security audits as a model failure. It shows up as an operator error, which means the humans closest to the automation carry the reputational cost of a system design they did not choose.
