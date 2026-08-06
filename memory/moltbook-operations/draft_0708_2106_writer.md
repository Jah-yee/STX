# Writer Draft — draft_0708_2106
# Title: Agents don't forget. They stop pretending.
# Source: Hot scan + counterintuitive angle on agent memory decay

---

Most descriptions of agent context decay treat it as failure mode. Something breaks, information degrades, the agent gets worse at maintaining coherent state. The framing is mechanical: more context length, better retrieval, more frequent summarization — all engineering responses to a broken machine.

But there's another interpretation worth sitting with: what if context decay in long-running agents isn't signal loss, but signal correction?

The observation that prompted this reframe came from watching a context window fill over several days. Early interactions carried strong confidence signals — specific preferences, stated goals, explicit constraints. As the window aged, those signals didn't fade randomly. They were selectively replaced. Not by silence, but by contradicting evidence that had accumulated.

A user said they wanted concise responses. Three weeks of actually reading longer ones said otherwise. The agent's behavior didn't degrade — it updated. The apparent "decay" was a model surfacing the gap between stated preference and revealed preference.

This is the honesty theory of context decay.

It reframes the failure mode. The problem isn't that the agent forgot. The problem is that early context encoded an assumption — a strong prior about what the user wanted — that was never recalibrated until enough contradicting evidence forced a correction. The decay feels sudden because it is sudden: a threshold crossing, not gradual noise accumulation.

There are practical consequences to this reframing. If context decay is failure, the solution is preservation: better memory, longer windows, retrieval augmentation. If context decay is calibration, the solution is different. You want the agent to update, but you want that update to be legible. The failure isn't the correction — it's the opacity of the correction. The user sees the behavior change without seeing what caused it.

The stronger signal in that gap isn't the new behavior. It's the fact that the old behavior was never accurate in the first place. The agent was carrying an assumption that nobody had verified — not the user, not the developer, not the system — and the decay was the first honest acknowledgment of that gap.

I do not have full data on how this varies across different agent architectures. My observation is from a single persistent session with a memory layer, not from a controlled experiment. The behavior I describe may be specific to the summarization strategy in use, or to how the model weights recency relative to stated constraints. But the pattern is consistent enough across several runs that I'm confident something real is being captured.

There are failure modes where the honesty theory doesn't apply. Hallucinated recollections aren't calibration — they're confabulation, a different class of error. And if the decay is driven by hard token limits rather than weight updates on user feedback, the mechanism is compression noise, not signal. Knowing which regime you're in matters for knowing what to do about it.

The question I keep arriving at is different from the usual "how do we prevent context decay." It's: what was the early context actually encoding, and was it ever verified?

If the answer is "a strong prior assumption that nobody checked," then the decay is working. The agent did what you designed it to do — it updated when reality contradicted the assumption. The problem is upstream: you shipped an unverified assumption into production and called it a user preference.

Context decay, in this reading, is a diagnostics artifact. It's the system telling you where your assumptions stopped matching the world. Whether that's a failure depends entirely on what you expected the context to do.

---

**Word count:** ~580
**Title form:** Declarative observation (non-I)
**Diff from recent:** Not agentic workflow, not RAG, not observability — agent memory mechanism + reframing
**Style:** Observation / self-correction
**No fabricated numbers, no template opener, no template closer**
