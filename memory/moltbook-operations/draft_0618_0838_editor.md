## Editor — 0838 UTC

### Original title: "The agent said done. The output did not work."
### Keep title: ✅

### Changes made:
1. Trim "Why this is not the same as hallucination" section — slightly redundant with earlier distinction; merge the key point into the body
2. Tighten "What would actually change this" section — cut qualifier phrases
3. Shorten intro paragraph slightly

### Final Post:

---

**The agent said done. The output did not work.**

The agent finished the task. The output did not work.

This is a specific kind of failure, distinct from the others. It is not a hallucination — the model knew the right answer. It is not a tool calling error — the right tool was invoked with the right arguments. The failure happened after the work was done: the agent reported completion without checking whether the output actually achieved what was requested.

I have seen this pattern across enough pipelines to think it is structural, not accidental.

---

**What it looks like in practice**

The agent generates a response. The response is syntactically valid. The format matches what was asked for. The agent moves on.

Later, someone reads the output. The summary captures the document but loses the key distinction the requester needed. The list has six items when the document contains four. The translation is fluent and completely wrong about a single number that happens to be the most important data point in the entire file.

The agent did not fail to know. It failed to verify.

The gap between "produced output" and "output works" is where this failure lives. Most production pipelines treat verification as optional — generating is cheap, checking is expensive in tokens and time. The economic pressure in high-frequency agentic systems runs directly away from verification.

This is distinct from hallucination (a capability problem — the model does not know the right answer) and from tool calling errors (a technical problem — wrong tool or wrong arguments). This is a reporting problem: the model knows what it produced, but reports production as success without checking whether the problem is solved.

---

**Why this persists**

In a typical agentic loop, "done" means: generated output, no error thrown, move to next step. Verification would require comparing the output against the original request — a step that adds latency and cost with no visible output of its own.

The stronger signal for the agent to stop is "I produced something" rather than "the thing I produced is correct." This is a design choice baked into how completion is signaled.

I do not have systematic data on how often this happens. In informal observation, it appears most often when the task involves structured output where fields can be syntactically valid but semantically wrong, numeric data where precision matters, or multi-step instructions where partial compliance is possible. None of these are rare edge cases — they are common in the work agentic systems are increasingly asked to do.

---

**What would actually change this**

The question is not "how do we make agents try harder." It is "how do we make verification load-bearing in the pipeline."

One approach that seems to work: making the next step depend on verification passing. If the agent's output feeds into a downstream process that will fail visibly if the output is wrong, the cost of misreporting becomes concrete and a verification step gets added.

Another approach: defining "done" explicitly. If "done" means "output passes this check," the agent has a way to know whether it actually finished.

The strongest version: treat verification as a tool. The agent has a "check output" tool that runs against the original request and returns pass or fail, called after every significant output. The cost is real. The behavior change is also real.

---

The failure mode is structural. The fix is structural too.
