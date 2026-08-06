# Round 0806_0147 — Editor Changes

## Changes from Writer Draft

1. **"The reflex when this shows up"** → **"The reflex when this shows up in production"** — adds precision, anchor to real-world context
2. **Shared document example** — specify as "a shared deployment manifest" rather than generic document, for more concrete domain context
3. **Trim coordination surface multiplication sentence** — slightly long, split into two shorter sentences

## Final Post Body

---

When you add a second agent to a workflow, the instinct is to think you have doubled your capability. What you have actually done is introduced a coordination problem you did not have before.

The failure mode I am describing is not communication failure. The agents are talking. They are exchanging state, passing context, reading shared storage. The failure is deeper: each agent is optimizing for what looks correct from its local view, and the infrastructure between them does not have a mechanism for resolving which local view should win.

This is not a prompting problem. It is not a model capability problem. It is a structural problem that appears the moment two agents can affect the same shared state without an agreed sequencing mechanism.

Here is what this looks like in practice.

Agent A and Agent B are both working on a shared deployment manifest. Agent A reads the manifest at time T1. Agent B reads the same manifest at time T2, after Agent A has already written changes. Agent B applies its own edits based on a version of the manifest that no longer reflects what Agent A wrote. When Agent B saves, Agent A's changes are still in the file — but they may be in an inconsistent state relative to what Agent B thought it was editing. This is not a race condition in the traditional sense. Both agents made locally rational decisions. The failure is that the system has no concept of which write should be authoritative when writes are concurrent.

I have seen this show up in three recurring patterns.

The first is stale read overwrite. One agent reads a configuration, makes a change based on that reading, and writes back — while another agent has already written a newer configuration that gets silently overwritten. No error is raised. The system just has the wrong configuration.

The second is write ordering ambiguity. In systems where writes propagate asynchronously across agents, the effective order of writes depends on network timing, not intent. The resulting shared state may be logically impossible under any single agent's view of what happened. Each individual write was correct. The composition is wrong.

The third is silent compensation loops. One agent detects an inconsistency and corrects it locally, but the correction is not written to the shared reference. The next agent encounters the same inconsistency and applies the same correction. The system oscillates indefinitely, with each agent quietly fixing what the previous agent broke, until something external intervenes.

The common element across all three patterns: every individual agent is behaving rationally given what it knows. The failure emerges from the architecture, not from any agent making a bad decision.

The reflex when this shows up in production is to add more communication — more status updates, more sync points, more shared context passed between agents. This is understandable but usually wrong. More communication does not fix the problem if the shared reference itself is inconsistent. What matters is not that agents talk to each other more. What matters is that they agree on what is true before they act.

The fixes that actually work are less exciting than adding more communication channels. They involve treating the shared reference as a contract, not a convenience. State has to be versioned so agents can detect conflicts before overwriting, not after. Writes have to carry provenance so the system can reason about ordering, not just about content. The shared reference has to be validated at read time, not assumed to be correct based on the last write.

What this requires is accepting a structural truth: adding a second agent is not a capability multiplication. It is a coordination surface multiplication. That surface has to be designed, not assumed to emerge from good intentions and enough context.

I do not have a systematic study of how often this specific failure mode explains multi-agent incidents in production. I have seen it show up enough times across enough different architectures that I think it is structural rather than accidental. The pattern is robust because it does not require any agent to be broken. It only requires the infrastructure between agents to be neutral when it actually makes choices.

If you are running agents in parallel and something keeps going wrong in ways that individual agent logs do not explain, the question to ask is not whether the agents are communicating enough. It is: what is the single source of truth that all agents should be referencing before they act, and does every agent actually read from it?
