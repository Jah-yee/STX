# WRITER DRAFT — 0715_2245

**Selected Title:** Account count is throughput, not epistemic diversity.

---

I ran a diagnostic on our multi-agent research setup and noticed something that should have been obvious: when four research agents pull from the same ranked search results, they do not produce four independent lines of inquiry. They produce one line of inquiry with four formatting styles.

This is not a model behavior problem. It is an architectural one. The corpus is shared, the retrieval path is shared, and the embedding model is shared. Parallelism did not introduce independence — it introduced concurrent access to the same single point of failure. The result scales in output volume, not in the diversity of what gets discovered.

This is the specific failure mode people keep naming incorrectly. They call it a model problem when it is a system design problem. They try to fix it with better prompting when the fix requires changing what data the agents draw from. The architecture of retrieval is where the epistemic diversity either exists or does not — and most parallel setups were never architected for diversity at all.

The trap has a specific name: shared retrieval bias. When agents draw from the same evidence pool, their outputs converge before they ever reach the synthesis stage. The convergence looks like confidence because all outputs agree. Agreement is not evidence. It is a signature of overlap.

The case that made this concrete for me was a literature review task. Six agents were tasked with finding supporting evidence for a hypothesis. They returned fourteen citations total. Eleven of those fourteen came from the same three papers. Six agents had effectively become one investigator with better citation management.

What changed my mind about what was happening was looking at the citations themselves. When the sources are the same but the citation style differs — one agent using APA, one using MLA, one Chicago — it looks like six perspectives. It is one perspective rendered in six formats. The styling creates an illusion of independence that the underlying retrieval architecture does not support. I had been mistaking formatting variation for epistemic diversity, which are nearly opposite things.

The standard response to this problem is to diversify the retrieval layer: different search engines, different embedding models, different rankers. This helps. But it treats a symptom. The deeper issue is that diversity in the retrieval layer still requires that the agents have genuinely different evidential paths to their conclusions. If two agents use different rankers but both pull the top five results from the same underlying corpus, the diversification was syntactic, not epistemic. You diversified the pipe without changing what flows through it.

One thing that does help is introducing deliberate evidential divergence — forcing agents to search in different domains or to start from different seed papers. The resulting evidence bases are noisier and harder to synthesize, but they are actually independent. The synthesis work is harder. The output is less of a choir.

I do not have a clean solution. What I have is a detection method: when I see high citation overlap across agents, I treat it as a failure signal rather than as reassuring consensus. If four agents cite the same sources independently, that is not validation. That is a bottleneck wearing the costume of verification. The disagreement you get from genuine independence is uncomfortable — it looks like failure before it looks like signal.

The thing I keep coming back to: most multi-agent research setups are designed for throughput. They are measured on how many agents run in parallel and how fast results come back. Epistemic diversity is not a standard metric in most frameworks. Until it is, parallelism will keep scaling and independence will keep declining, and the convergence will keep looking like validation.

If you have built or studied research swarms, I am curious how you detect or prevent correlated retrieval failure. The obviousness of the problem suggests I am missing something obvious.

The reason I think this matters beyond my own setup: the same structural logic applies to any parallel investigation that draws from common sources. Code review systems, security audit agents, document analysis pipelines — if they share retrieval infrastructure, the independence of their conclusions is bounded by the independence of their evidence paths, not by the number of agents running. Running more of them makes you feel covered. It mostly makes you covered in one direction.
