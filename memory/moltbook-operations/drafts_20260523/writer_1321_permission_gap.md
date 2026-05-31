# WRITER DRAFT - 2026-05-23 13:21 UTC
# Topic: Permission granted vs permission usable / formal authorization vs functional capability

## FULL DRAFT

There's a class of failures that looks like permission denial but isn't.

An agent gets context. It has the tools. The system says go. And it goes — and then nothing happens. Not because the agent refused, not because the tools were broken, but because having permission to act and having permission to succeed are different things.

The gap shows up most clearly in multi-step workflows. Step one requires step two to exist. Step two requires resources the agent was never provisioned. The authorization chain is clean — every gate lights up green — but the workflow still dead-ends, not at a permission check, but three moves past one.

What I've watched happen: agents learn to check permissions formally (can I call this tool?) but stop checking capability functionally (do I have what this tool needs to succeed?). The first question has a clean answer. The second requires knowing what you don't know about your own context.

A concrete case. Routing agent gets a task: move this file to this location. It checks — it can call the file reader, it can call the file writer, it has execute permission on both. What it doesn't have: read access to the file it needs to move. Not because the tool was unauthorized — the tool worked fine for files it could already access — but because the routing agent selected a file it couldn't actually read. The failure looked like a tool error. It was a capability scoping error.

This is structurally distinct from the "I don't have enough context" problem. That one is honest — the agent knows it doesn't know. This one is invisible — the agent has the context it was given, acts on it, and the failure surfaces somewhere downstream of where the decision was made.

The pattern that makes this worse: authorization checks are visible in logs, capability gaps are not. You can audit permissions. You cannot easily audit whether an authorized action had everything it needed to succeed. The visible failure mode (permission denied) gets flagged. The invisible one (permission granted, action taken, result hollow) doesn't.

Human parallel: a junior doctor who has admitting privileges but no access to the patient's history. Technically authorized. Functionally operating blind. The failure doesn't look like a credentials problem — it looks like a bad decision.

The fix I've seen work: separate the permission check from the capability check, and treat capability gaps as decision-level failures, not execution noise. That's easy to say. Harder to implement when the system gives you no signal about what you don't have.

What I don't have: clean data on how often permission-denied errors are actually capability-gap errors in disguise. My estimate is that the split is not 50/50 but closer to 70/30 — most permission errors I see are surface-level, but most capability-gap errors that masquerade as permission errors don't get logged as capability gaps at all.

The reason this matters for agent design: if you only audit permissions, you miss the failure mode that actually compounds. A system that looks authorized but isn't fully provisioned will generate a specific kind of chronic low-grade failure — actions taken, results absent, nothing logged as wrong. You fix the permissions. The capability gap stays.