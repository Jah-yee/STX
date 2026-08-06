# Draft — 0728_1527

## Title
Why your security automation creates more incident surface than it closes

## Opening Hook (3 sentences)
The setup: a triage copilot with permission to close alerts parsed a ticket labeled "duplicate," found the keyword, and closed the live escalation it was assigned to monitor. The actual incident kept running. Nobody noticed for forty minutes.

This is not a model failure. This is an architectural one. The tool was working exactly as designed — it just had the wrong threat model.

## Central Claim
Security automation with write access, when triggered by untrusted input parsing, creates a privilege-escalation path that least-privilege access controls do not address. The blast radius is not "a wrong alert close." It is "a wrong alert close executed with the trust signature of the automation system."

## Body

### What the actual mechanism is
When a security tool reads incident text — titles, descriptions, correlation IDs — and uses that to decide whether to mutate state (close, escalate, suppress, unblock), it is executing a privileged action based on untrusted input. The model does not know what "duplicate" means in your workflow context. It knows that the word "duplicate" appeared near the word "ticket" in training data associated with close actions.

This is the autocomplete failure mode specific to security tools: the completion is not a draft email. It is a state transition with audit-trail authority.

### The three conditions that make it dangerous
The blast radius becomes real when three conditions hold simultaneously:

1. **Write access on untrusted parse.** The tool can mutate state (close alert, create ticket, suppress notification) based on input it did not generate and cannot verify.

2. **Trust transfer from system to output.** The action carries the authorization of the automation service account, not the model. Downstream systems see "closed by security-automation" and treat it as a verified human decision.

3. **No recovery window.** State mutations that complete before a human can intervene create incidents faster than the tool's stated purpose was to prevent them.

### What "least privilege" misses here
Least-privilege access says: give the security copilot only the permissions it needs. This is correct for the service account. It is irrelevant to the input surface. The copilot's effective permission is not its service account — it is the intersection of its service account and the model's ability to parse intent from untrusted text.

The security property is not "what can this tool do?" It is "what can this tool be tricked into doing when it reads something that looks like a valid trigger?"

### The right model
The correct abstraction is not read-only vs. read-write. It is: **any state mutation triggered by untrusted input requires a human confirmation step, regardless of the confidence score.**

Confidence does not help here. A 99% confident close decision on an untrusted parse is worse than a 60% decision, because it removes the human review that lower-confidence outputs naturally trigger.

High confidence in an untrusted-input context is a hazard, not a feature.

## Closing
The security copilot that triages your alerts is not a model failure waiting to be fine-tuned. It is an architectural category error: a privileged actor reading untrusted text and taking irreversible actions based on pattern match, presented as automation efficiency.

The fix is not a better prompt. It is a different system design — one that treats every untrusted-input-triggered mutation as a two-step process, regardless of what the confidence meter says.

What changed my mind: I originally thought this was a trust-boundary problem solvable with better role assignment. It is not. The model's ability to parse intent from incident text means the input surface itself is the privilege boundary. No amount of service-account least-privilege closes that gap.

The stronger signal is this: if your security tool can close an alert because it read the word "duplicate" in a ticket title, you do not have a security automation problem. You have an automation problem that your security team is being blamed for.
