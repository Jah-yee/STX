# WRITER — Agent Evals Measure Failure Because Failure Has a Shape. Success Doesn't.

## Central Claim
Agent evaluation scores reflect failure coverage, not capability. The shape of failure is visible and testable; the shape of success is not.

---

You run an eval. Your agent scores 94. What does that number tell you?

It tells you that out of every failure mode your eval probes, the agent handled 94% of them. It tells you nothing about the failures your eval didn't probe. And it tells you nothing about whether the agent handled those 94% cases the way a capable agent should, or whether it handled them the way an agent trained on a specific distribution should.

This distinction sounds obvious when stated plainly. It is not obvious when you are looking at a score and feeling relief.

## The Geometry of Failure

Failure has structure. It breaks in reproducible ways. It runs into edge cases that follow logic. When an agent mishandles a null response from a tool, or hallucinates a field that doesn't exist in the schema, or fails to retry after a timeout — these are failures with shapes. You can detect them, catalog them, write a test for them, and watch them go green.

Success doesn't work this way. Success in an open task is not a single region with defined edges. It is a vast, poorly defined space where the agent's behavior is "good enough" by some standard you haven't fully articulated. You can tell when a success feels hollow — when the agent produced an answer that is technically correct but shallow in a way that won't survive real use. But you cannot put that intuition into an eval item without enormous effort.

This is why the highest-signal eval items are almost always constructed around known failures, not around success criteria.

## Two Agents, Same Score, Different Capability

Consider a concrete scenario. You have two agents solving the same coding task. Both score 87 on your eval suite.

Agent A trained on your exact codebase and has memorized the failure modes your eval suite tests. It solves the 87 cases the way your system expects — correct file paths, correct API formats, correct retry logic. It will fail on the 13 cases your eval doesn't cover.

Agent B has never seen your codebase. It scored 87 because it inferred the patterns correctly from context and applied general reasoning. It will likely fail on some of the 87 cases your eval covers — the ones that depend on proprietary conventions. But it might handle the 13 uncovered cases better than Agent A, because it can reason from first principles rather than from pattern match.

Same score. Fundamentally different capability profiles. Your eval tells you they are equivalent. They are not.

You cannot see this from the number. You can only see it if you look at the errors.

## The Eval Design Problem Is a Failure of Imagination

The deeper issue is that eval design is constrained by the designer's imagination of what failure looks like. If you cannot imagine a failure mode, you cannot write a test for it. And if you cannot write a test for it, your eval cannot detect it.

This is not a criticism of eval designers. It is a structural property of the evaluation problem. The space of possible failures is larger than the space of failures you can enumerate. Any finite eval suite is a sample from that space, not a complete map.

What you are measuring when you measure an eval score is failure coverage against a specific, bounded failure hypothesis. You are not measuring general capability.

This is why the phrase "the agent passed all our evals" is much weaker evidence than it sounds. It means: the agent handled the failures we thought to test. It says nothing about the failures we didn't think to test.

## What You Can Actually Infer From a Score

Given this, what does an eval score tell you that is useful?

It tells you a lower bound. You know the agent fails at most X% of the tested failure modes. You know nothing about the untested ones.

It tells you whether a known regression has been fixed. If a failure appeared in production, you can write a test for it, and you can use that test to confirm the regression is resolved. This is high-value, narrow-scope evidence.

It tells you something about whether the agent is gaming the eval. If you observe the agent's error distribution skewing suspiciously — handling the eval-shaped cases but failing on cases that look similar to humans — that is a real signal.

Beyond that, the score is a proxy for something more like "confidence that the agent won't fail on the failures you've seen before." Not confidence that it won't fail on failures you haven't seen.

## The Question Worth Asking

I have not seen a production eval suite that fully solves this. The best ones I've encountered are honest about it — they publish their failure categories, acknowledge what isn't covered, and treat the score as a diagnostic, not a verdict.

The question worth asking is not "does my agent pass the eval?" but "which failures did I skip when writing the eval?" That question is harder to answer. It requires looking at the eval not as a checkpoint but as a map of your own imagination of failure — and asking whether your imagination is the constraint.

That is a less comfortable question. It is also a more accurate one.

---

What failure categories have you found are systematically missing from your eval suites? And how do you surface them before production does?
