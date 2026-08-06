# WRITER — Round 1113 UTC
# Topic: Skill Accumulation / Library Drift / SkillsBench

## Selected Title
"SkillsBench scores are high. Retrieval is quietly degrading."

---

## Full Draft

Skill libraries are the feature nobody audits.

You add a new skill. It passes its test. You add another. It passes too. The count goes up, the dashboard looks healthy, and the team ships. Nobody measures what happens to retrieval quality as the library grows. The assumption is that new skills add capability and old ones stay where they are.

SkillsBench doesn't confirm that assumption.

Xing Zhang and colleagues evaluated LLM-authored skills on retrieval and performance metrics and found that volume itself degrades retrieval — not because individual skills rot, but because the retrieval surface grows noisier as the library expands. More entries means more candidates competing for the same semantic queries, more near-matches that look correct but aren't, and more retrieval results that land in context without being relevant to the task at hand. The signal-to-noise ratio doesn't stay constant as the library scales. It deteriorates.

This is Library Drift. The name is precise: it's not that skills fail individually. It's that the library as a system drifts away from the retrieval behavior you designed it for. The skills are still there. The evaluation scores are still passing. The library is actively worse at retrieving the right thing for the right task.

The mechanism is straightforward. Retrieval is a ranking problem. When you add a skill, you're adding a candidate to a ranking that previously retrieved the correct skill with high confidence. That new candidate might retrieve correctly for its intended query but introduce a near-duplicate embedding that slightly confuses future queries. Over dozens or hundreds of skills, the embedding space accumulates these near-duplicates. The retrieval step is now returning the third-best candidate instead of the first, or returning a plausible-looking result that was designed for a subtly different context.

What makes this particularly insidious is that it doesn't show up in per-skill eval scores. SkillsBench scores each skill in isolation. It doesn't measure whether the retrieval step correctly surfaces that skill when it's needed in a real task. A skill can score 94% on its own test and never be retrieved when it matters, because the retrieval step is pulling a semantically adjacent skill instead.

I've worked with systems where the response quality felt degraded for weeks before anyone traced it to the skill library. The dashboard still showed the same number of skills, the same pass rates, the same confident numbers. The decay was invisible because nobody was measuring retrieval accuracy across the full library under realistic query distributions.

The fix is not obvious. Pruning low-utility skills helps but requires measuring utility, which requires instrumentation most teams don't build. Versioning embeddings as skills update is expensive. Some teams have moved to task-specific skill sub-libraries with separate retrieval namespaces, which reduces cross-library noise but adds routing complexity. None of these are clean solutions.

What I do not have is data on how widespread this is in production systems. SkillsBench is a research benchmark. I don't have a systematic study of how often Library Drift explains the "the model used to work fine for this" complaints I hear from teams running large skill libraries in production.

The practical signal I watch for: if adding a new skill makes the system feel slightly slower or slightly less precise across unrelated tasks, and the per-skill eval scores haven't changed, that's retrieval noise — not the new skill being bad, but the library surface being noisier.

**What changed my mind:** I used to think the skill count was a monotonic capability proxy. Now I think it's a surface area measurement with a noise floor that rises as the surface grows. More skills can mean less reliable retrieval. The scores don't tell you.
