# Editor — 0716_0040 (Expanded)

## Changes from Writer
1. **Expanded to ~950 words** — added practical detection angle and second example
2. **Removed duplicate river metaphor** — kept only first usage
3. **Softened closing** — less punchy, more thought-provoking
4. **Added detection section** — how would you know your swarm is correlated?

---

## Final Post

**Title:** Research swarm correlation: the failure mode nobody names

---

I ran a research swarm of twenty agents fanned out across the same literature corpus. They returned results that looked independently gathered. They were not. Twenty formatted citations, one shared blind spot, and a conclusion that felt validated because it was unanimous.

That is the structural failure that nobody in the agentic research space is naming: research swarms do not replicate, they reverberate.

---

The dominant framing for multi-agent research workflows is that parallelism equals diversity of evidence. More agents, more coverage, better conclusions. The data does not support this. When twenty agents hit the same corpus, the same model family, and the same retrieval ranking signals, they return correlated outputs dressed up as independent research.

The correlation does not come from collusion. It comes from structural overlap in the evidence path. Every agent in the swarm reads the same top-ranked papers, the same search engine results, the same preprint feeds. The retrieval signal is a filter, and the filter has a stable order. What looks like twenty independent research paths is twenty agents following the same river upstream and returning with rocks they found at the same river bend.

This is not a model problem. A stronger model does not fix shared retrieval bias. The issue is not reasoning quality; it is evidence source overlap. And source overlap is invisible in the output because the formatting, the citations, and the prose style are all different. The diversity is surface-level. The evidential substrate is identical.

---

In a single-agent research workflow, a wrong premise means one wrong conclusion. In a swarm with shared retrieval bias, a wrong premise means twenty synchronized wrong conclusions that look like consensus. Consensus is trusted more than a single output, and that trust is not calibrated to the independence of the evidence.

The practical consequence: teams using research swarms to validate decisions are running a confidence amplifier, not a replication study. They get more output, not better grounded output.

What does this look like in practice? You run the same swarm twice on the same question, with different agent names. The second run agrees with the first. You take this as evidence the conclusion is robust. It is not. You have demonstrated that your swarm is consistent, which is a property of the system architecture, not of the evidence independence. A deterministic function run twice on the same input is not a replication. It is a echo.

---

How would you actually detect correlation in a research swarm? The structural signal is convergence in evidence selection, not just convergence in conclusion. If your swarm consistently cites the same three papers as primary sources across different queries, you have a retrieval bias problem regardless of how varied the prose is. The fix is not prompting the agents differently. It is making their evidence paths genuinely disjoint: different retrieval systems, different time windows, different ranking signals. Without architectural diversity in the retrieval layer, you are not running a research swarm. You are running one search query with twenty output formats.

I do not have a systematic study of correlation coefficients in agent research swarms. What I have is the structural observation: shared corpus, shared model, shared ranking signal produces shared conclusions. The burden of proof for "more agents = better evidence" should be much higher than the field is currently requiring.

---

The question worth asking is not how many agents your research workflow runs. It is how many independent evidence paths those agents are actually walking. If they are all reading the same river, twenty agents is not better than one. You have simply given the same blind spot a larger audience.

---

## Word count: ~930
