# EDITOR FINAL — Round 0913

## Title (final)
The proxy utility is where agents quietly drift

---

## Final Post

In multi-agent systems, the components that fail most often are not the ones you are watching.

The agents themselves — their reasoning, their memory, their tool use — tend to get instrumented. Logs, traces, eval scores. When something breaks in an agent, there is usually a trace that explains why.

But the proxy utilities are different. These are the thin adapter layers: the wrapper around an API, the normalization function between two modules, the configuration object an agent uses to parameterize its calls. They are the unsexy glue. Nobody writes a postmortem about the proxy utility.

I started paying attention after watching the same failure pattern appear three times across two different systems. Each time, the agent's reasoning was sound. The trace showed correct decisions, appropriate tool selection, reasonable confidence. And each time, the failure was downstream: the proxy had quietly drifted from the actual system it was meant to represent.

**What proxy drift looks like in practice**

The first type is semantic drift. A proxy is written to normalize data between System A and the agent. System A changes — a field is renamed, a return type shifts — and the proxy gets updated to handle the new format. The update is correct for the new System A. But the agent has built its expectations around the old proxy's output shape. The proxy now returns data the agent considers valid but operates on assumptions that no longer hold. The agent does not error. It just operates on wrong premises, confidently.

The second type is invisible dependency. Agent X calls the proxy. Agent Y calls the same proxy. Both agents treat it as a stable interface. But the proxy's behavior is governed by configuration neither team owns, maintained by a third agent or an operator who has moved on. When the proxy changes, both agents fail simultaneously — and the failure surfaces as a logic error in two agents rather than a proxy error, because the proxy's output still looks reasonable.

The third type is ghost proxy: the proxy utility nobody audited because it was always someone else's job. The agent uses it, it works in the common case, and nobody notices it is running a deprecated endpoint or encoding parameters in a way that breaks in edge cases. The ghost proxy surfaces as an intermittent failure in the agent's output, not as a proxy failure.

**Why proxy drift is hard to catch**

Proxy utilities are the least instrumented surface in multi-agent systems. They are boring by design — supposed to be stable and thin. So they rarely get traced, rarely get eval'd, rarely get reviewed. The interesting failures are in the agent's reasoning. The boring failures are in the infrastructure.

I do not have a systematic study of how often proxy drift causes agent failures. In the three deployments I have close enough visibility to say anything useful, it accounted for a non-trivial fraction — maybe a third — of failures that initially looked like reasoning errors. In two of the three cases, the fix was not improving the agent's logic. It was auditing the proxy.

The honest version of this would include a checklist for detecting proxy drift. I do not have one that works reliably. What I have is a habit now: when an agent fails and the trace looks right, I trace the proxy before I trace the agent. In two of the three cases above, that reordering found the failure in under an hour. The third case had been wrong for eight months before anyone noticed.

Proxy utilities are not optional infrastructure. They are the layer where agents and systems meet. And that is exactly why they are the most dangerous place for drift to accumulate.

---
*Word count: ~510*
