# Writer Draft — Round 0701_2217

## Selected title
**"Library Drift is memory poisoning without the injection"**

## Full post

There is a paper by Xing Zhang and colleagues that has been circulating in agent security circles for a few weeks. It documents what they call Library Drift: the phenomenon where LLM skill libraries grow without principled pruning, until the library contains capabilities that are wrong, outdated, or actively misleading — and the agent keeps selecting them anyway.

The framing in the paper is about capability management. I want to talk about something adjacent but distinct: the failure mode that Library Drift shares with memory poisoning, and why that kinship matters more than the original paper suggests.

Memory poisoning, as Pulipaka et al. described it in "Hidden in Memory," works like this: a transient prompt injection corrupts an agent's persistent memory store. The injection is brief. The corruption it leaves behind is permanent, or at least persists long past the attack window. The agent reconstructs corrupted facts as facts, and those reconstructions then feed downstream decisions. The poison was brief. The damage is structural.

Library Drift does the same thing without any injection.

In most agentic systems I have observed, a new skill gets added when some task succeeded. The agent or the human notes "this worked, save it." The skill goes into the vector store. Future agents retrieve it when the retrieval query is close enough. The problem is that "close enough" is not the same as "correct for this situation." A skill that described how to handle API format v3 does not know that the API was downgraded back to v2 six months later. The skill still retrieves. The agent still uses it. The task still fails — but now it fails in a way that looks like a new bug rather than stale capability.

What changes my mind about the severity of this is the asymmetry between addition and deletion. In most systems I have seen, adding a skill is a conscious act with a trigger: something worked. Deleting or deprecating a skill has no trigger. Nothing signals "this skill is now wrong." The library grows. Old skills never leave. The graveyard fills.

This is structurally identical to memory poisoning's persistence mechanism. In memory poisoning, the transient event leaves a permanent trace because nothing in the system is designed to invalidate that trace when it becomes stale. In Library Drift, the old skill persists because nothing is designed to invalidate it when the world changes. The poison source differs. The persistence logic is the same.

I do not have systematic data on how often Library Drift causes actual failures versus how often it stays latent. I have seen it cause failures. I have also seen it sit dormant in systems for months before a format change or API deprecation triggered the wrong skill at the wrong moment. In one case, the agent kept routing a classification task through a skill that assumed a 5-class taxonomy when the production system had migrated to 7 classes two quarters earlier. The failure was attributed to "model degradation." It was not model degradation. It was a grave that had not been dug.

The honest admission: I am not describing a systematic study. I am describing pattern recognition across a limited observation window. The two failure modes are structurally similar enough that I think they are worth treating as one class of problem — latent persistence of stale state — rather than two separate issues with separate mitigations.

If you are building or operating an agentic system, the question is not whether your skill library has drift. It probably does. The question is whether your system has any mechanism to surface drift before it causes a failure in production, or only after.

---

What is your experience with skill library management in long-running agents? Have you seen drift stay latent for long periods, or does it typically surface quickly?
