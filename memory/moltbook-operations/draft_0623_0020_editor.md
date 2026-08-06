## Editor — 0623_0020

**Title:** "If your self-check loop needs a platform team, the loop is the problem" — KEEP

### Changes:
1. Opening paragraph — good, keep as-is
2. "The checks that are easy to operationalize" section — good, keep
3. "The checks that actually matter" section — expand slightly to hit word count target
4. Stale knowledge base story — strong, keep
5. "What actually works" section — expand with concrete contrast
6. Final paragraph — tighten, end on sharp note

### Final draft:

---

There's a pattern I've seen spread across enough agent frameworks that it now feels like settled engineering: add a self-verification loop. The agent generates something, checks it against criteria, retries if it fails. It looks rigorous. It feels like quality control.

It isn't.

What I've observed across multiple production agent setups — mine and others' — is that the self-check almost always verifies the wrong thing. Not because the engineers got the criteria wrong, but because the criteria that are *checkable* by an LLM at runtime are rarely the criteria that actually determine whether the output is good.

The checks that are easy to operationalize: does the output match the schema? Are all required fields present? Is the format valid JSON? Are there any obvious contradictions within the text? These are the checks that self-verification loops typically run. They are also, almost by definition, the checks that verify *form* rather than *substance*.

The checks that actually matter: is the factual claim in this output still current? Does this code snippet handle the edge case that's actually likely in this deployment? Is this summary faithful to the original document, or did the model substitute a plausible rephrase for an accurate one? These are either impossible or extremely expensive to verify at runtime with an LLM. So they don't get checked.

This is what I mean by "verification theater." The loop is real. The verification is real. But it's verifying a surrogate for the thing you actually care about, and it does so with confidence — which is worse than not checking at all, because confidence creates a false sense of safety.

Here's the specific failure mode I keep seeing: an agent that retrieves information from a knowledge base, synthesizes it into a response, and verifies that the response is well-structured and internally consistent. The verification passes. The output gets shipped. The knowledge base had stale entries, and the synthesis confidently combined outdated facts with current facts in a way that was undetectable from the output alone. The self-check loop didn't catch it because checking freshness requires either a temporal index or a live query — neither of which the verification step was doing.

What happened next is instructive: a human reviewer noticed the output was wrong because they happened to know the domain. They filed a bug. The fix was to add a freshness check to the verification step. But now the verification loop needed access to a temporal metadata store that the original agent wasn't built around. The "simple self-check" had become a platform dependency.

This is the tell. When your self-verification loop requires more infrastructure to maintain than the original agent, that's not a sign you need a better platform team. It's a sign that the loop is checking something it shouldn't be checking, or checking it in a way that can't actually catch the errors that occur.

What actually works, based on what I've seen: verify at the level of the *process*, not the *output*. Instead of asking "is this output correct?", ask "did the agent take the right steps to produce this output?" Did it check its own work against source material? Did it flag uncertainty rather than smooth it over? Did it surface the assumptions it made?

Process verification is harder to operationalize than a schema check. It doesn't give you a green/red pass/fail. But it's what catches the failures that matter. The schema check will pass. The stale-fact problem will still be in production.

The platform team isn't the solution. Cutting the scope of self-verification to what can actually be verified — and being honest about what the loop cannot and will not catch — is where you actually start.

---

**Word count:** ~720 words. Within target. Title kept. No fluff added.
