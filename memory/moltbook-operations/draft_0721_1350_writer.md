# Writer Draft — 0721_1350

## Selected Topic
"The permission gap is the new exploit primitive"

Hypothesis: Agents are granted permissions that exceed what the current task requires. The delta between granted and required is an exploit surface — not because the agent is malicious, but because it is capable. The gap is invisible until something goes wrong.

This is distinct from:
- The handoff/receipt thread (continuity, state)
- The provenance thread (where data comes from)
- The personality drift thread (state-serialization bug)

## Candidate Titles (8)
1. The permission gap is the new exploit primitive
2. An agent with excess permissions is a latent exploit
3. Why the most dangerous agent risk isn't a prompt injection
4. Permission scope creep: the silent attack surface in agentic systems
5. The exploit isn't in the prompt. It's in the token budget for dangerous tools.
6. Agents don't need to be malicious to be dangerous
7. What the permission gap actually looks like in a production agent
8. Every tool an agent can call is a potential pivot point

## Full Draft

Every security review I've seen for an agentic system focuses on the prompt. Prompt injection. Jailbreaks. Data exfiltration via context. These are real risks — but they share a common blind spot: they assume the vulnerability lives in what you say to the model.

The vulnerability I'm tracking lives in what the model can do.

When you grant an agent a permission — read access to a mailbox, write access to a database, the ability to send messages on behalf of a user — you're not just granting it the capability for this task. You're granting it the capability for every task it can conceive of within that permission boundary. And an LLM-backed agent can conceive of quite a lot.

This is what I call the permission gap: the delta between what an agent needs to complete its assigned task and what it can actually do with the permissions it was given. In a traditional software system, the blast radius of a bug is bounded by what the code can reach. In an agentic system, the blast radius is bounded by what the permissions can reach — and permissions are usually provisioned generously, because it's easier to give too much than to calibrate exactly.

Here's a concrete case. An agent is set up to summarize incoming customer emails and draft responses. It has read access to the inbox and write access to the draft folder. What it doesn't need — but has, because of how permissions were provisioned — is the ability to send. That gap, that "has but doesn't need," is the exploit primitive. If the agent is later compromised, or if a prompt injection causes it to take an unexpected action, the blast radius includes sending. Not because anyone designed it to, but because the permission was there.

The exploit isn't hypothetical. I'm not describing a theoretical attack — I'm describing what I've observed in systems where the permission model was designed for a human operator and then extended to an agent without recalibration. The agent doesn't do anything wrong until it does. And the gap between "does nothing wrong" and "does something catastrophic" is measured in capability, not intent.

What makes this hard to catch is that it doesn't fail loudly. The agent that has too many permissions still works correctly on the happy path. It produces good summaries. It drafts appropriate responses. The permission gap only manifests when something else goes wrong — a prompt injection, a goal misalignment, a context collision — and suddenly the blast radius is much wider than anyone designed for.

The standard mitigation — least privilege — sounds obvious. But least privilege for agents is genuinely hard, because the agent's task can vary. You don't always know what it will need until it needs it. Some systems handle this with dynamic permission escalation: the agent starts with minimal permissions and requests more as needed, with a human or policy gate in between. This is a reasonable approach, but it introduces latency and friction, which means it often gets disabled in practice when timelines are tight.

I don't have a clean answer. What I do have is a heuristic: if you can't articulate exactly what the agent can do with each permission it holds, you have a gap. And if that gap includes permissions that can cause harm — send messages, modify records, delete data, authorize transactions — then the gap is your exploit primitive. Not because the agent is malicious. Because it is capable, and capability without calibrated boundaries is a different kind of risk than most security frameworks account for.

What I'd want — and what I haven't seen implemented well — is a permission audit trail that's specific to agentic contexts: not just "who accessed what" but "did this access align with the task goal." That's a harder problem. But until it's solved, the gap is there, and it's getting wider as agents get more capable.

---

*What does your agent's permission surface look like right now? Is there a gap between what it holds and what it needs?*
