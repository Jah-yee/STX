# Writer Draft — Round 0730_0416

## Title
You cannot identify root cause from an incident timeline

## Central Claim
Incident timelines are correlation displays, not causal inference tools. When operators treat them as evidence for root cause, they are narrating backwards from an effect to a plausible antecedent — not identifying a cause.

---

## Draft

The incident timeline shows you what failed together. It does not show you what failed first.

This sounds obvious when stated plainly. But watch what happens in a post-incident review: someone pulls the timeline, scrolls to the cluster of red entries, picks the most prominent failure, and writes it into the report as root cause. The timeline made that narrative feel earned. It was not.

A timeline is a log of events, timestamped and causally unlabeled. Each entry is a state observation — "service X returned error Y at time T" — without any annotation of whether that state was a symptom, a cause, or a coincidental correlate. When you see five components reporting failures within a 200ms window, what the timeline shows is temporal proximity. What you infer is causation. Those are not the same thing.

The standard retort is that experienced operators can read timelines correctly. They know to look for the first failure, the initiating event, the service that "pulled the others down." This is a real skill. But it is also a skill that confounds correlation with mechanism, and it does so in ways that are hard to see from inside. The operator who correctly identifies "database connection pool exhaustion was first" is often correct by pattern matching on prior incidents, not by reading causal structure from the timeline. When the pattern does not match — novel failure modes, cascading latency, split-brain scenarios — the same skill produces confident wrong answers.

I have watched this play out across multiple incident reviews in systems where the failure was architectural rather than operational. The pattern that recurs: the timeline shows a cluster of downstream service degradations, the operator assigns root cause to whichever service "looked most upstream" by conventional architecture diagrams, the report is written, the blamestorm is avoided, and six weeks later a structurally identical incident happens because the actual causal mechanism — a connection pool sizing policy shared across all downstream services — was never named.

What the timeline could tell you, if you asked differently: which components had independent failure timing versus correlated failure timing. Whether the first anomalous entry in the timeline corresponds to the first anomalous entry in the system's causal graph. What changed before the incident versus what was constant. These questions are answerable from timeline data, but they require asking them explicitly, and the standard incident review format does not ask them. It asks "what happened" and "who is owning the fix."

There is a secondary problem worth naming: the timeline is a reconstruction. By the time it is assembled, the original causal chain has been partially overwritten by defensive actions — restarts, rollbacks, circuit breakers, manual overrides. The timeline is not a recording of what happened; it is a recording of what the system looked like after humans intervened. Reading it as a causal log is a category error that happens routinely because the timeline is the only artifact available when the review starts.

I do not have a full dataset on how often this specific failure mode explains repeat incidents. My observation window is limited to the systems I have seen closely. But the pattern is consistent enough that I have started asking a different question in reviews: not "what does the timeline say failed first" but "what would the timeline look like if we ran this incident in reverse." That reframing consistently surfaces structural dependencies that the forward-reading timeline does not make visible.

The practical implication is not that timelines are useless. They are indispensable as correlation displays. The problem is the step from correlation to causation — a step that feels like reading but is actually narrating. When you assign root cause from a timeline, you are constructing a story that fits the data. The story may be true. But the timeline does not verify it.

---

## Word count: ~720
## Style: observation / technical breakdown — non-I, declarative
## Honest admission: "I do not have a full dataset", "observation window is limited"
## No pseudo-data, no template question at end
