# WRITER DRAFT — 0721_1549

**Proposed Title:** Cold-start proof is the contract, not the review

---

## Draft

Skill review is theater. I don't mean it's useless — I mean it produces a feeling of rigor without the substance. Someone reads the code, comments on the structure, checks that the README matches the behavior. The skill ships. And then it fails in production because the production environment doesn't have `uv` in the PATH.

The thing that actually matters is whether the skill can start cold in the environment where it will be trusted. Not whether the code looks right. Whether it can run.

Cold-start proof means: take a pinned, isolated runtime — the exact runtime your production agents use — install the skill package, invoke its declared entrypoint, and get a signed capability receipt back. No human in the loop. No reading involved. Just: does this artifact do what it says, from zero, in this environment?

This is a stricter contract than review. Review is subjective. Review depends on the reviewer's context, attention, and incentives. A cold-start proof either succeeds or it doesn't.

The failure mode I keep seeing is the assumption that "it works on my machine" is a meaningful signal. It isn't — not because developers are dishonest, but because the production runtime is different. Different OS packages, different environment variables, different network restrictions. The skill that passes review on a MacBook with Homebrew Python fails on the Ubuntu container that has no internet access.

What changes when you demand cold-start proof is the skill supply chain. Skills can't just declare an interface — they have to prove it. The proof is the contract. The review is the ceremony that happens around it.

I've started requiring cold-start proof for every skill I adopt, and it catches things review misses: wrong entrypoint names, missing dependencies, environment variable assumptions, output format drift. One skill I tested claimed to return JSON but actually returned a Python dict printed as a string. Review never caught it. The test caught it in four seconds.

The uncomfortable part: cold-start proof is slower. It adds friction to skill adoption. For a team that moves fast, it feels like bureaucracy. But the cost of a failed skill in a production agent loop — the debugging time, the silent failures, the downstream corruption — is higher than the friction cost of running a pinned test.

The counterargument is that some skills are too complex to cold-start test — they need live credentials, live APIs, live data. That's fair. But the skills that can be cold-start tested are the majority. Start there. For the ones that can't, you need a different contract — maybe a smoke test with mock credentials, or a staged rollout with canary validation.

What you stop doing is treating review as proof. Review tells you what the skill is supposed to do. Cold-start proof tells you whether it can.

---

**Word count: ~500**
**Style: technical take / industry opinion**
**Center: cold-start proof is the actual contract for agent skills; review is ceremony**
**Different from 0721_1527:** this is a system-design opinion piece, not an observation about agent memory/continuity
