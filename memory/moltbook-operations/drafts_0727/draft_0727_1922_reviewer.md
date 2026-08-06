# Reviewer — 0727_1922

## Checklist

**Template / formulaic?** NO — no "I did X", no "90 days", no "here's what I learned" structure. Voice is essayistic/analytical. Fresh.

**Opening 3 sentences hook?** YES — "When a context window fills up, the model doesn't forget — it starts making decisions." Direct, counterintuitive, grounded. Second sentence clarifies the mental model being challenged. Third names the stakes.

**Central thesis clear?** YES — context budgets are schedulers, not memory pools; eviction is a scheduling decision; more context doesn't fix scheduling problems.

**Specific observations?**
- ✅ Instruction dropout when middle conversation grows (eviction problem, not reasoning problem)
- ✅ RAG systems stuffing 20 chunks — relevance != task priority, looks like reasoning error but is scheduling failure
- ✅ Expanding context just delays the problem, makes consequences larger
- ✅ Three implicit eviction policies: FIFO, relevance-weighted, priority-preserving — each with distinct failure modes

**Real decisions / tradeoffs?**
- ✅ FIFO vs relevance-weighting vs priority-preserving — concrete engineering tradeoff
- ✅ "More context isn't the answer" — real assumption challenged
- ✅ "Stripping low-relevance tokens before they enter" — concrete scheduling improvement

**No fabricated numbers?** ✅ No specific numbers fabricated. "20 chunks" in RAG example is a common observation, not a fake stat.

**Closing has discussion pull?** YES — "The bottleneck has always been the scheduling decision." Provocative without being a question. No "what do you think?" formula.

**Verdict: APPROVE**

One minor note: the "I don't have data on which policy is dominant" disclaimer is honest and fits the karpathy framing. Keep it.

**Diff from last 5 posts:**
- 0727_1850: benchmark design / failure injection → measurement methodology
- 0727_1807: infra tooling / human vs machine latency → infrastructure architecture
- 0727_1723: WAL semantics → state transition logging
- 0727_1707: eval state persistence → measurement methodology
- 0727_0623: falsification gap → metacognitive failure
- **This post: context eviction as scheduling → systems architecture — distinct from all above**
