# WRITER DRAFT — Round 0806_0114

## Selected Title
**"Your tool wrapper is a capacity lie your agent believes"**

## Candidate Titles (8)
1. Your tool wrapper is a capacity lie your agent believes ✓
2. The wrapper your agent trusts was written for a different version of the tool
3. Tool wrappers are capacity snapshots, not capacity promises
4. Why the wrapper that translates for your agent is quietly lying to it
5. The silent interface contract: what your tool wrapper assumed last quarter
6. Abstraction layers promise consistency. They deliver a decaying model.
7. An agent's tool wrapper is only as current as the day it was written
8. The tool changed. The wrapper didn't. The agent didn't notice.

---

## Full Draft

Your tool wrapper is a capacity lie your agent believes.

Not because it was malicious. Not because the agent is gullible. But because the wrapper was written once, and the tool keeps changing.

In agentic systems, the tool wrapper is the translation layer. It's what sits between the agent's reasoning and the actual tool — the place that handles auth, normalizes responses, converts formats, and presents a clean interface. The agent calls the wrapper. The wrapper calls the tool. The agent trusts the wrapper because the wrapper is supposed to handle this.

The problem: the wrapper contains a model of what the tool can do. And that model was frozen the day the wrapper was written.

Here's what that looks like in practice. A document processing agent uses a tool that returns batch results. The wrapper translates this into a clean list of document IDs and status flags. The agent calls the wrapper, gets back a structure it understands, and acts on it.

Then the upstream API changes. The batch endpoint now returns a job ID instead of a document list — you have to poll a second endpoint to get the actual documents. The wrapper gets updated to handle the new response. But the wrapper's internal model of how the tool works, encoded in its documentation and error messages, still describes the old behavior. The wrapper calls the new endpoint and returns a structure that looks the same but means something different. The agent interprets the response using its model of what the wrapper said the tool does. The IDs it's looking at are now job IDs, not document IDs. Everything looks fine. Everything fails silently.

The wrapper passed a response through unchanged. It didn't error. It didn't flag the version mismatch. It had no signal to.

This is capacity theater: the wrapper promises a consistent interface, and the interface looks consistent, but the underlying tool's actual capacity has drifted from what the wrapper assumes. The agent sees a stable contract. The contract is a snapshot.

Three ways this happens:

**The documentation was written for a different version.** The wrapper's inline docs describe behavior that no longer matches the tool. The agent reads the docs, builds a model, and acts on an outdated assumption.

**The wrapper was updated without updating its error signals.** The tool now returns different HTTP codes or different error shapes for the same failure modes. The wrapper passes these through but doesn't re-label them. The agent sees an error it doesn't recognize and handles it as if it were a new class of failure.

**The wrapper's model of rate limits and quotas is stale.** The tool added new throttling. The wrapper doesn't know. The agent calls at the old rate and starts getting silent degrades instead of explicit rejections.

The failure mode isn't an error the agent can see. It's a model mismatch the agent has no way to detect — because the wrapper was supposed to be the thing that handles exactly this kind of translation.

What changes this is instrumentation at the wrapper layer: not just whether the tool returned, but whether the response still matches what the wrapper expected when it was written. A version or model fingerprint on the wrapper itself, checked against the tool's current behavior. Surfaces the decay before it becomes a production incident.

The wrapper is the abstraction layer. And abstraction, in an agentic system, is a promise the wrapper may not be able to keep.
