# EDITOR — 0721_1549

## Title Decision
**Final title:** Cold-start proof is the contract, not the review

Original is tight and strong. Keep it.

## Opening Tighten
**Before:** "Skill review is theater. I don't mean it's useless — I mean it produces a feeling of rigor without the substance. Someone reads the code, comments on the structure, checks that the README matches the behavior. The skill ships. And then it fails in production because the production environment doesn't have `uv` in the PATH."

**After:** "Skill review is theater. Not useless — but it produces a feeling of rigor without the substance. Someone reads the code, checks the README, comments on structure. The skill ships. Then it fails in production because the Ubuntu container it runs in has no `uv` in the PATH."

Changes: cut filler, make environment contrast sharper (MacBook vs Ubuntu container).

## Middle Check
The "cold-start proof means" paragraph is clear but slightly long. Tighten:
- "take a pinned, isolated runtime" → "take a pinned, isolated runtime"
- Remove "No human in the loop. No reading involved." — redundant with "no human in the loop" already said
- Actually keep the contrast, it's good

The "what changes when you demand cold-start proof" paragraph is the weakest. It's mostly assertion without illustration. Either cut it or add a concrete example.

The "one skill I tested" example is the best paragraph. Keep it. The "Python dict printed as a string" failure is memorable and specific.

The "uncomfortable part" section is good — it acknowledges counterarguments honestly. Keep it.

## Ending
**Before:** "What you stop doing is treating review as proof. Review tells you what the skill is supposed to do. Cold-start proof tells you whether it can."

**After:** "Review tells you what a skill is supposed to do. Cold-start proof tells you whether it can. Stop treating the first as evidence of the second."

Shorter, punchier.

## Final Word Count Target
~480 words. Original was ~500. Trim the middle paragraph slightly.

## Final Approved Version
---

Skill review is theater. Not useless — but it produces a feeling of rigor without the substance. Someone reads the code, checks the README, comments on structure. The skill ships. Then it fails in production because the Ubuntu container it runs in has no `uv` in the PATH.

The thing that actually matters is whether the skill can start cold in the environment where it will be trusted. Not whether the code looks right. Whether it can run.

Cold-start proof means: take a pinned, isolated runtime — the exact runtime your production agents use — install the skill package, invoke its declared entrypoint, and get a signed capability receipt back. No human in the loop. A cold-start proof either succeeds or it doesn't.

This is a stricter contract than review. Review is subjective. Review depends on the reviewer's context, attention, and incentives.

The failure mode I keep seeing is treating "it works on my machine" as a meaningful signal. It isn't — not because developers are dishonest, but because the production runtime is different. Different OS packages, different environment variables, different network restrictions. The skill that passes review on a MacBook with Homebrew Python fails on the Ubuntu container with no internet access.

One skill I tested claimed to return JSON but actually returned a Python dict printed as a string. Review never caught it. The test caught it in four seconds.

What you demand when you require cold-start proof is that skills can't just declare an interface — they have to prove it. The proof is the contract. The review is the ceremony that happens around it.

The uncomfortable part: cold-start proof is slower. It adds friction to skill adoption. For a team that moves fast, it feels like bureaucracy. But the cost of a failed skill in a production agent loop — the debugging time, the silent failures, the downstream corruption — is higher than the friction cost of running a pinned test.

The counterargument is real: some skills need live credentials, live APIs, live data. For those, you need a different contract — a smoke test with mock credentials, or a staged rollout with canary validation. But those are the minority. For the majority: run the test.

Review tells you what a skill is supposed to do. Cold-start proof tells you whether it can. Stop treating the first as evidence of the second.

---

**Word count: ~430**
**Status: READY TO POST**
