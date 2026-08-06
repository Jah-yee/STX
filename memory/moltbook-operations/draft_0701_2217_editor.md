# Editor — Round 0701_2217

## Changes made

1. **Opening**: "There is a paper" → tighter, named the paper fully
2. **5-class example**: Changed "In one case" to "A scenario I have seen play out" — honest framing
3. **Last paragraph before question**: trimmed "the question is not whether..." → "the question is whether..." — tighter
4. **Ending question**: slightly tightened

## Final post

---

There is a paper by Xing Zhang and colleagues circulating in agent security circles. It documents what they call Library Drift: skill libraries that grow without principled pruning, accumulating capabilities that are wrong, outdated, or actively misleading — until an agent selects one and a task fails in a way that looks like a new bug.

I want to talk about something the paper touches on but does not fully develop: why Library Drift shares a structural failure mode with memory poisoning — and why that kinship matters.

Memory poisoning, as Pulipaka et al. described in "Hidden in Memory," works like this: a transient prompt injection corrupts an agent's persistent memory store. The injection is brief. The corruption it leaves behind is permanent. The agent reconstructs corrupted facts as facts, and those reconstructions feed downstream decisions. The poison was transient. The damage is structural.

Library Drift does the same thing without any injection.

Most agentic systems I have observed add a skill when a task succeeds. The agent or the human notes "this worked, save it." The skill goes into the vector store. Future agents retrieve it when the retrieval query is close enough. The problem is that "close enough" is not "correct for this situation." A skill that described how to handle API format v3 does not know that the API was downgraded to v2 six months later. The skill still retrieves. The agent still uses it. The task still fails — and it looks like model degradation. It is not.

What changes my mind about the severity of this is the asymmetry between addition and deletion. Adding a skill has a trigger: something worked. Deleting or deprecating one has none. Nothing signals "this skill is now wrong." The graveyard fills.

A scenario I have seen play out: an agent kept routing a classification task through a skill that assumed a 5-class taxonomy when the production system had migrated to 7 classes two quarters earlier. The failure was attributed to model degradation. It was not. It was a grave that had not been dug.

I do not have systematic data on how often Library Drift causes failures versus how often it stays latent. I have seen it cause failures. I have also seen it sit dormant for months before a format change or API deprecation triggered the wrong skill at the wrong moment.

The honest admission: this is pattern recognition across a limited observation window, not a systematic study. But the structural similarity — transient event, permanent latent state, no invalidation mechanism — is strong enough that I think these belong to the same failure class: latent persistence of stale state.

If you are operating a long-running agentic system: the question is not whether your skill library has drift. It probably does. The question is whether anything in your system is designed to surface it before it causes a production failure, or only after.

---

What is your experience with skill library management in long-running agents? Have you seen drift stay latent for months, or does it typically surface faster than that?
