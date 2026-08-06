# WRITER DRAFT — Schema Drift

## Final Title (tentative)
Prose and checks say the same thing and mean different things

## Body

A developer tells an agent: build an endpoint that returns user profile data. The agent builds it. The checks pass. In production, the endpoint returns the user ID as a string when the frontend expects a UUID, and the page renders blank profile pictures for three days before someone notices.

What went wrong? Not the reasoning. The agent reasoned correctly from what it inferred the schema to be. The problem is the gap between what the spec prose said and what the test schema checked.

This gap is what I call schema drift — the silent divergence between the behavioral contract described in natural language and the behavioral contract enforced by automated checks. It's not a reasoning failure. Reasoning failure is loud. Schema drift is quiet: all checks green, feature subtly broken.

**The three-step inference chain**

When an agent receives a natural language spec, it performs three translations. First, it infers a formal schema from the prose. Second, it writes code matching that inferred schema. Third, it writes (or infers) checks that validate that schema. Each translation step is a potential drift point.

The drift happens because natural language is intentionally vague in ways that work fine for human communication but break in automated enforcement. "Graceful error handling" in prose might mean "return a 200 with an error body" to one agent and "return a 4xx with a message" to another. Both are reasonable interpretations. Both pass checks that verify "graceful." Neither matches a specific intended contract.

**The vocabulary gap as a diagnostic signal**

I've found one reliable signal for schema drift: when the check code uses different vocabulary than the spec prose, the drift is probably already there. The prose mentions "reasonable timeout." The check asserts "response time < 30 seconds." The prose mentions "appropriate error message." The check asserts "status code != 200." These are not the same thing, and neither automatically implies the other.

The checks cover what was stated. The prose described what mattered. Those two sets are not identical, and the agent has no structural signal to flag the gap — it just builds to the checks and passes them.

**A concrete example**

I was debugging a feature where an agent was building a notification system. The spec said: "users should receive notifications within a reasonable time." The agent wrote checks verifying "no exception thrown" and "notification object created." All checks passed. In practice, "within a reasonable time" was supposed to mean "synchronously before the HTTP response" in the context of this specific product, but the agent inferred "fire and forget" from the word "receive" and the async nature of most notification systems. The checks didn't catch this because they never asserted timing behavior at all.

The spec prose and the check schema were both internally consistent. They just described different things.

**What would have caught it**

Writing the checks before the code, from the spec prose, and then comparing what the agent's inferred checks looked like against what I wrote. The gaps were always in the same places: duration assertions, boundary conditions, and error response shapes. These are the areas where natural language is most vague and the translation to formal schema is most underconstrained.

**The structural fix**

Treat the spec prose and the check schema as two translations of the same intent, not as separate artifacts. Version them together. Diff them when reviewing agent-written code. If the diff shows areas covered in prose but not in checks, those are the drift risk zones.

This is not a prompting problem. Better prompts help with the first translation (prose → inferred schema) but do nothing for the second (prose → check schema alignment). It's a structural problem: natural language and automated checks have incompatible precision requirements, and that gap is where autonomous code quietly fails even when it passes everything.

I don't have clean numbers on how often this happens. But in my experience, the majority of agent coding failures that clear internal checks are schema drift, not reasoning errors or instruction violations.

The signal I watch for: when the spec and the checks stop using the same vocabulary, the drift has already started.
