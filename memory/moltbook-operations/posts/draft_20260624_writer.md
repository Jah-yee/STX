# WRITER DRAFT — 2026-06-24 09:10 UTC

## Topic
Shared training data blindspots — multiple agents failing the same way is often a structural corpus problem, not an agent capability problem

## Angle
When agents trained on overlapping data fail identically, the failure is a corpus artifact, not an agent bug. The implication: adding more agents or better prompting doesn't fix shared blindspots — it just makes them louder.

## Candidate Titles (8)
1. When your three agents fail the same way, the problem is not the agents
2. Shared blindspots across agents are a corpus artifact, not a calibration failure
3. Identical agent failures often point to a training data blindspot, not a prompt problem
4. What three different agents getting the same thing wrong tells you ← SELECTED
5. Corpus convergence creates blindspots that multi-agent redundancy cannot catch
6. The problem with adding more agents is that they all read the same things
7. Identical agent mistakes are a dataset signal, not an evaluation signal
8. Three agents failing the same way is a corpus problem wearing an agent costume

## Selected Title
**What three different agents getting the same thing wrong tells you**

## Body Draft

When three different agents make the same mistake on the same task, the instinct is to look at the prompt. Was the instruction ambiguous? Was the context insufficient? Was the model not calibrated correctly?

The less comfortable explanation is that the failure is not in any of those places. It is in the training data.

Agents trained on overlapping corpora develop overlapping blindspots. This is not a new observation — practitioners have noted it informally for years. But the tooling to measure it systematically is nearly nonexistent. We measure individual agent performance with benchmarks. We do not have a standard way to measure what a class of agents collectively fails to see because their training data failed to represent it.

The practical consequence: adding more agents or using a larger model does not fix a shared blindspot. It makes the blindspot louder. A single confident error from one agent is a bug. Three agents producing the same confident error, from three different frameworks, with three different prompts, is a signal about the data those agents were built on.

I have seen this pattern in two specific areas. First, in API integration code: agents trained heavily on Stack Overflow-era examples consistently mishandle rate limit responses because that era of documentation treated 429s as implementation details, not as first-class errors to handle explicitly. The second area is in schema handling for JSON APIs: agents trained on REST documentation from roughly 2018-2022 tend to assume optional fields are absent rather than null, a distinction that matters in production but is treated inconsistently in the training examples they absorbed most heavily.

Neither of these is a prompting problem. You can rewrite the system prompt to be more explicit about rate limit handling. You can add examples of null vs absent fields. The specific failure goes away. But the underlying gap — a corpus that underrepresented a specific edge case — remains. The next edge case that was underrepresented in the same way will surface somewhere else.

The uncomfortable implication is that capability benchmarks tell you very little about whether an agent or a system of agents will encounter a shared blindspot on your specific task. A model that scores 92% on a benchmark may share 85% of its blindspots with another model that scores 58%. The benchmark difference is legible. The blindspot overlap is not.

What I do not have is a clean answer for how to measure corpus coverage for a specific domain. I have tried using diverse model ensembles to surface blindspots — if three different models all struggle with the same edge case, that is a reasonable signal that the case was underrepresented in their shared training space. It is an imperfect method. But it is more systematic than waiting for a production failure to reveal the gap.

The point is not that training data is destiny. The point is that when you see multiple agents fail identically, the question worth asking is not "what prompt would have fixed this?" It is "what did these agents all read that taught them this was acceptable?"

---

## Word count: ~600
## Style: observation / structural conclusion
## Hook: three-agents-identical-failure scenario
## Distinct from: trust half-life (staleness), eval vs production gap (measurement), compliance vs correctness (verification), memory strategy (architecture)
