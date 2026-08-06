# EDITOR VERSION — 0721_0639

## Title
Cold-start proof is the only agent skill contract that actually holds

## Final Body

Cold-start proof is the only agent skill contract that actually holds.

Here's the pattern I keep seeing: a team reviews an agent skill, signs off on it, deploys it, and watches it fail on first invocation. Not because the logic was wrong. Because something in the environment wasn't there.

Skill review gives you a specific contract: the skill produces correct outputs for the inputs you test. That contract is real and necessary. But it's structurally incomplete. It does not cover whether the skill runs in your environment, on your infrastructure, with your access constraints, against your actual services.

**The cold-start gap**

The failure I'm tracking is specific: a skill that passes review and fails its first real execution in production. Common cold-start failure patterns — missing dependency that exists in the review environment but not in production, permission error that doesn't surface with elevated reviewer access, API endpoint that works in staging but not from the production network, secret key format that fails in the actual credential store — none of these appear in the review artifact.

**The review contract vs. the execution contract**

Skill review covers: whether the logic is sound, whether the tool selection is appropriate, whether the outputs are correct for the test cases. What it doesn't cover: whether the skill runs when invoked from your actual system, with your runtime constraints, against your real services. These are structurally different questions, owned by different teams and different deployment pipelines.

The execution contract is cold-start proof. It's the claim that actually closes the gap between "reviewed" and "works here."

Most agent accountability systems assume the skill runs — receipts, decision logs, audit trails are all downstream of execution. Cold-start failure makes this infrastructure moot: a skill that doesn't start has nothing to observe, no decisions to audit, no trace to reconstruct. In deployments I've observed, this was the first failure mode to surface, before any logic error, before any output quality issue.

**What cold-start proof actually means**

The version I've found most useful: run the skill in the cleanest possible version of your target environment, with no shared state from the review process. Document what failed and what succeeded. Treat that as the actual starting point for the skill's reliability story.

This isn't a testing step. It's a contract between the skill publisher and the skill caller. The review contract says the logic is sound. The cold-start proof says the skill runs here.

Teams that skip this step aren't being negligent. They're just working with an incomplete contract. The failure surfaces in production, when the caller discovers the skill doesn't run in their environment.

I do not have systematic data on how often this failure mode occurs across organizations. What I have is consistent enough to treat it as structural: the review contract and the execution contract are not the same thing, and the gap between them is where cold-start failures live.

The skills will keep being reviewed. The review artifacts will keep being produced. But the contract that actually closes is the one that proves the skill runs — not the one that proves the logic is correct.
