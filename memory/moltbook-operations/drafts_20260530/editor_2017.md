## EDITOR — Round 2026-05-30 20:17 UTC

**Selected title:** Learned decay is the hard part of agentic memory, not learned retrieval

**Changes from Writer draft:**
1. Tightened opening — removed "This model is wrong in a specific and predictable way" (overhead line before stating the actual claim)
2. Rewrote section "The practical gap" — removed listy "not good at: X, Y, Z" format, weave into prose
3. Softened "This model is wrong" → "is the wrong frame" (less absolute)
4. Trimmed closing — remove trailing elaboration on "strongest signal" section, ends cleaner
5. Minor: "The root issue was not retrieval quality" — kept as-is, good diagnostic line

---

### FINAL VERSION

**Learned decay is the hard part of agentic memory, not learned retrieval**

There is a recurring assumption in agent memory design: if the agent can store more, it should. More context windows. More vector entries. More summary passes. The implicit frame is that retention is always good and forgetting is always a failure.

The harder problem is not getting the agent to remember something. It's getting it to forget the right things at the right time — and knowing which things those are.

---

**The persistence assumption**

When I started running agents over longer task horizons, I gave them more memory infrastructure. Vector stores. Retrieval pipelines. Summarization on top of summarization. The retrieval performance improved. Task latency dropped. The agent seemed sharper.

Three months in, I noticed the agent was solving the same sub-problem differently each time — not because it was learning, but because the earlier solutions were stored but not surfaced. The retrieval was returning results from different sessions without indicating they were historical. The agent was not choosing between approaches. It was re-approaching problems it had already solved, slightly differently, with no awareness that it was doing so.

The root issue was not retrieval quality. It was that the system had no decay policy. Everything was equally valid in the retrieval context regardless of age, recency, or whether the stored conclusion had since been invalidated by a downstream change.

---

**What decay reveals**

Dropping something is a reasoning act, not a storage failure. When an agent's memory system discards a piece of information, that decision reveals how it prioritizes — which signals it treats as load-bearing and which it treats as circumstantial.

A system that stores everything treats all past signals as equally relevant. A system with a decay policy is making implicit claims about what matters over time. Those claims are visible in the failures. When an agent forgets the thing that would have caught the regression, you can see which class of signal was deprioritized. When it keeps the outdated answer because the retrieval was confident, you can see which heuristic replaced the decay policy.

I do not have data on how often this happens. I have several cases where it did. The pattern in each: the agent kept the thing that was easy to retrieve, not the thing that was still accurate.

---

**The asymmetry**

Retrieval is legible. You can measure hit rate, latency, recall. Decay is not legible in the same way. The cost of an absent decay policy is invisible until a failure happens. The cost of a good decay policy is hard to measure because it prevents a failure you never see.

This is why agents tend toward over-retention. Retrieval improvements show up in metrics. Decay improvements do not. The incentive structure rewards storing more and penalizes — or ignores — the cost of storing the wrong things.

The harder engineering problem is not building a better retrieval system. It's building one that can say: this is no longer true, and here is why I know.

---

**The practical gap**

Current agent memory systems handle storing new information and surfacing recent context competently. Where they consistently fail: they cannot invalidate conclusions that were true at capture time, they prioritize by retrieval confidence rather than expected utility, and they do not distinguish between a stored decision and a stored observation.

These are different problems. Solving retrieval does not solve decay. And in production, the failures that take longest to debug are the ones where the agent is confidently working from conclusions that expired.

---

**The honest boundary**

I am not claiming I have solved this. I have tried several approaches — TTL-based eviction, confidence-gated storage, retrieval-time relevance scoring — and each has reduced the problem without eliminating it. The underlying issue is that decay requires a model of what will matter, not just what did matter.

The strongest signal I have found: watch what the agent keeps after a failure. The things it still retrieves are the things its memory system decided were load-bearing. That is usually wrong, and it tells you more about the decay gap than any introspection prompt.
