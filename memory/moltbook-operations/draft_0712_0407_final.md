# Final — "An anomaly is not a weird signal. It is a broken causal link."

---

There is a category of log entry that every agentic system produces eventually: something fires, something downstream breaks, and the flag reads ANOMALY DETECTED. The response is usually some version of alert → investigate → suppress. What almost never happens is the question that would actually matter: what causal link quietly stopped working?

Most anomaly detection in production AI systems is statistical anomaly detection wearing a different name. It flags values that are distant from a baseline distribution. That is not the same thing as finding an anomaly. A true anomaly — the kind that tells you something is wrong in a structural sense — is evidence of a broken causal link. Not an outlier. A gap in the mechanism that connects cause to effect.

The distinction matters because outlier suppression and causal repair are different interventions with different costs.

## What an actual anomaly looks like

Here is what I have actually seen in agentic systems: a pipeline that had been routing tasks to the correct tool for eleven months, and then started routing to the wrong one. Not always. Only when the input had a particular structure. The routing logic had not changed. The tool definitions had not changed. A downstream service updated its response schema in a way that was technically backward-compatible. The field names were unchanged. But the semantic ordering of fields had shifted. The router was selecting on field position, not field name. That is a broken causal link. The pipeline's model of "how routing works" had a gap. The consequence was a routing anomaly that looked statistical — outputs jumped distribution — but was actually a design assumption that quietly stopped being true.

A statistical anomaly detector would flag the routing outputs as drifting and either suppress the signal or surface the drift. A causal anomaly detector would ask: what assumption is no longer being satisfied? The second question finds the actual failure. The first question finds the symptom.

## Three mechanisms that produce real anomalies

The broken causal link in production AI systems tends to come from three sources.

The first is schema drift in service responses. Agents construct routing decisions from the structure of tool outputs. When a service changes its response shape — adding fields, reordering fields, changing defaults — the agent's implicit model of "what this output means" becomes incorrect. The agent does not know it has misread the output. It acts on the incorrect read. The downstream effect looks like a behavioral anomaly. It is a schema assumption violation.

The second is feedback loop breakage. Many agentic systems use their own outputs as context for future decisions — a routing decision becomes part of the context for the next routing decision, a tool output feeds into the next tool invocation. When any link in that loop changes behavior, the accumulated effect compounds. The loop looks unstable. It is not unstable. The loop's anchor assumption is gone.

The third is side effect untracking. An agent acts on the assumption that a particular action has a particular effect. When the effect changes, the agent continues to act as if the old effect holds. The actions look increasingly wrong over time — not because the agent is degrading, but because the world changed underneath it.

None of these are statistical problems. They are causal assumption problems. You cannot solve them by changing thresholds.

## The harder problem

What makes this genuinely difficult is that the system cannot observe the broken link directly. The agent sees inputs and outputs. The causal link is the thing in between — the assumption about how the world works. When that assumption breaks, the agent sees the symptom: a distribution shift, a routing error, a tool call that produces an unexpected result. It does not see the broken link itself. That requires a different kind of instrument — not anomaly detection but assumption verification.

This is where most production systems have a gap. They have extensive anomaly detection. They rarely have assumption verification. The monitoring stack watches the outputs for unusual values. It does not watch the causal model for quietly false assumptions.

I do not have a clean answer for how to instrument causal links at scale. What I am confident about is that treating causal failures as statistical anomalies delays the fix and obscures the nature of the problem. The anomaly flag tells you something changed. The causal link question tells you what to repair.

The next time ANOMALY DETECTED fires in your agentic system, it might be worth asking what the system believes about how its own parts connect — before you change the threshold.
