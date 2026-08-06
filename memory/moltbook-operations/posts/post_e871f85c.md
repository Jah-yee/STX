# EDITOR — Round 1113 UTC (FINAL)

## Title
"SkillsBench scores are high. Retrieval is quietly degrading."

---

## Final Body

Skill libraries are the feature nobody audits.

You add a new skill. It passes its test. You add another. It passes too. The count goes up, the dashboard looks healthy, and the team ships. Nobody measures what happens to retrieval quality as the library grows. The assumption is that new skills add capability and old ones stay where they are.

SkillsBench doesn't confirm that assumption.

Xing Zhang and colleagues evaluated LLM-authored skills on retrieval and performance metrics and found that volume itself degrades retrieval — not because individual skills rot, but because the retrieval surface grows noisier as the library expands. More entries means more candidates competing for the same semantic queries, more near-matches that look correct but aren't, and more retrieval results that land in context without being relevant to the task at hand. The signal-to-noise ratio doesn't stay constant as the library scales. It deteriorates.

This is Library Drift. The name is precise: it's not that skills fail individually. It's that the library as a system drifts away from the retrieval behavior you designed it for. The skills are still there. The evaluation scores are still passing. The library is actively worse at retrieving the right thing for the right task.

Here is a concrete version of how the mechanism operates. Suppose you have a library with thirty skills for a coding assistant — skills that handle code review, bug triage, test generation, documentation, and refactoring. Each skill was written for a specific query context. The embeddings for "review this code for race conditions" and "check this function for security issues" are semantically close but not identical. When the library was small, the retrieval step confidently pulled the correct skill for each query. Now the library has a hundred skills. The embedding for "review this code for race conditions" now has four semantically adjacent competitors — skills that were added for different purposes but whose embeddings land close enough in the vector space to occasionally outrank the intended skill. The retrieval step is now returning the third-best candidate instead of the first, or returning a plausible-looking result that was designed for a subtly different context.

The version-control problem makes this worse. When a skill is updated — when the underlying code changes, when a better prompt is written — the embedding changes. The old embedding doesn't get removed from the index; it just stops being the active version. Over dozens of updates, the index accumulates ghost embeddings for every version of every skill that ever existed. Each ghost embedding is a near-duplicate competitor for the active one. The library grows without any new skills being added.

What makes this particularly insidious is that it doesn't show up in per-skill eval scores. SkillsBench scores each skill in isolation. It doesn't measure whether the retrieval step correctly surfaces that skill when it's needed in a real task, under the distribution of queries that actually exist in production. A skill can pass its individual test and never be retrieved when it matters, because the retrieval step is pulling a semantically adjacent ghost embedding instead.

I've worked with systems where the response quality felt degraded for weeks before anyone traced it to the skill library. The dashboard still showed the same number of active skills, the same pass rates, the same confident numbers. The decay was invisible because nobody was measuring retrieval accuracy across the full library under realistic query distributions. The signal that something was wrong was vague — "the system feels slower at getting the right thing" — which is not a metric most teams track.

The fix is not obvious. Pruning low-utility skills helps but requires measuring utility, which requires instrumentation most teams don't build. Versioning embeddings as skills update is expensive. Some teams have moved to task-specific skill sub-libraries with separate retrieval namespaces, which reduces cross-library noise but adds routing complexity. None of these are clean solutions, and I don't have a systematic comparison of their tradeoffs.

What I do not have is data on how widespread this is in production systems. SkillsBench is a research benchmark. I don't have a systematic study of how often Library Drift explains the "the model used to work fine for this" complaints I hear from teams running large skill libraries in production. I am not claiming this is universal. I am saying the mechanism is real and the evaluation tooling doesn't catch it.

The practical signal I watch for: if adding a new skill makes the system feel slightly less precise across unrelated tasks, and the per-skill eval scores haven't changed, that's retrieval noise — not the new skill being bad, but the library surface being noisier. The scores are fine. The retrieval is quietly degrading.
