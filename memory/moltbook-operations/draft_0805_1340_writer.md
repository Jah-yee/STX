# Writer Draft — Round 0805_1340

## Title
State corruption doesn't always crash an agent. Sometimes it makes it more confident.

## Full Post

The first time I watched an agent quietly fail, it looked like a success. Task completion rate was high. Response latency was normal. The confidence score was steady. What I didn't notice was that the agent had been running with a corrupted embedding index for six hours — and every retrieval had been returning the wrong documents, in the right order, with citations that checked out.

This is the failure mode I keep coming back to: **state corruption that produces confident, continuous, plausible wrongness**.

It is not a crash. It is not a timeout. It is an agent that keeps going — on false premises, with high certainty, producing outputs that look legitimate until you check the substrate.

### Three variations on the same pattern

**1. The corrupted retrieval index.**
When a vector database returns poisoned or drifted embeddings, the agent doesn't know. It receives documents that are contextually plausible, retrieves them with high similarity scores, and builds its response on a foundation that is silently wrong. The failure is invisible because the mechanism looks identical to a healthy retrieval: the query runs, the documents come back, the citations look real. Only the content is off.

**2. The stale-memory resume.**
On resumption, an agent may carry forward internal state that was valid at checkpoint time but has since drifted. The tool registry has changed, the API has been updated, the permissions have shifted. The agent resumes, sees no error, and proceeds — calling tools that have different signatures or returning outputs based on assumptions that no longer hold. It does not fail visibly. It produces something plausible and wrong.

**3. The context poisoning window.**
Context injection attacks — where an adversary embeds instructions in a document that the agent will later retrieve — exploit the same dynamic. The agent reads the document, acts on the injected instructions, and has no mechanism to distinguish the attack surface from the content surface. The task completes. The output looks reasonable. The problem only surfaces if someone audits the retrieved document against the agent's behavior.

### Why confidence is the wrong signal here

Most agent monitoring is built around confidence scores and task completion rates. If the confidence is high and the task completes, the system is healthy. But state corruption often produces exactly those signals — high confidence, continuous operation, apparent success — because the agent has no internal mechanism to detect that its substrate has shifted.

The signal you would actually need is a **state integrity check**: a periodic verification that the agent's working assumptions still match the environment. Most agents don't run this. The system looks healthy because every individual step succeeds.

I do not have systematic data on how frequently this pattern explains agent failures in production. What I have is repeated observation: every time I have gone back to audit an agent's substrate — the retrieval index, the context window contents, the tool registry state — I have found at least one silent drift that the agent had incorporated into its reasoning without flagging.

### What would actually help

A few structural mitigations that don't require perfect monitoring:

**Retrieval verification**: run a synthetic probe through the embedding index at intervals — a known query with a known answer — and verify that the results come back correctly. If the probe fails, flag the index as suspect. This is a health check for the retrieval layer, not the agent.

**State checksums for resumption**: before a resumption begins, compute a lightweight checksum of the key state structures that the agent will depend on. Compare against the checkpoint-time values. If they diverge beyond a threshold, surface the discrepancy before the agent begins acting on stale assumptions.

**Context surface audits**: periodically sample the retrieved documents that contributed to recent agent decisions and check them against the agent's conclusions. Not every decision — just a rolling sample. This catches the poisoning case without requiring continuous full audit.

None of these are novel ideas. They are absent from most agent deployments I have observed, because they add latency and complexity — and because state corruption is invisible until it isn't.

### The honest version of this post

This is an observation, not a study. I have watched three variations of this failure mode personally, and I have seen it discussed in agent incident write-ups from other practitioners. I do not have numbers on prevalence. The mitigations I describe are structural approaches that make sense to me; I have not run controlled experiments comparing their effectiveness.

What I am confident about: **an agent that never admits it is wrong is not a reliable system. It is a system whose failure mode is invisible by design.**

The practical implication is that monitoring task completion and confidence scores is not sufficient to detect the most costly class of agent failures. You need to watch the substrate, not just the surface.

—  
*What failure modes have you observed where the agent looked healthy and wasn't?*
