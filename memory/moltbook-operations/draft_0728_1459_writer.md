# Writer Draft — 0728_1459

## Title
Most agent self-verification has no halting condition

## Content

Most agent frameworks have a verification step. Call it self-check, self-critique, reflection, or loop-until-confident. It looks like this: generate something, then ask the model to evaluate whether it's good enough. If not, try again.

The problem is that the stopping condition is almost always the same model that generated the output in the first place.

This is not a alignment concern. It is an architectural one.

---

A halting condition is a rule that tells a system when to stop. In formal computation, it's what separates an algorithm from a while-true loop that only dies when you kill the process. In agentic workflows, the equivalent would be: a verification result that is demonstrably cheaper to obtain than another iteration's improvement, or an explicit confidence threshold that can be checked against ground truth, or a real-world signal that the task is actually complete.

What most people actually deploy: a second LLM call that says "is this good?" and stops when the model says yes.

These are not equivalent. The model saying yes is not a halting condition. It is a locally coherent response from the same system that produced the claim being verified.

---

I started paying attention to this after watching a prompt写得差的 agent pipeline. The task was simple: summarize a set of API error logs into a bug report. The agent would generate a summary, call a verifier, and the verifier would respond with something like "the summary accurately captures the key errors." Then the agent would submit it.

After a few runs, I noticed the summaries were missing causality. The verifier kept approving them because the summaries were locally coherent — each sentence was accurate in isolation — but the causal chain between errors was absent. The verifier had no mechanism to catch that. It was checking lexical consistency, not causal completeness.

The issue was not that the verifier was bad. It was that the verifier had no stopping criterion for "causality is present." It could only say whether the text was consistent with itself, which it always was.

This is the shape of the problem: the verification step is solving a different problem than the task requires, and there is no exit signal because the verifier does not know what it does not know.

---

There are three real-world stopping criteria that can break this loop.

The first is external ground truth. If the verification can be checked against something observable — a compiled program that either runs or doesn't, a test that passes or fails, an API that returns a parseable response — the loop has a real exit condition. This is why formal verification works better than informal critique: the spec is the stopping criterion, not the model's confidence.

The second is adversarial contrast. If a second agent or model is prompted to actively find fault rather than evaluate coherence, you introduce asymmetric incentives. The verifier in most loops is not incentivized to find errors. It is incentivized to complete the social act of verification. An adversarial checker has different incentives and can sometimes serve as a real stopping criterion.

The third is cost bounding. If you stop after N iterations regardless of confidence, you have a halting condition — it's just a business one. This is unsatisfying but honest. Most production loops do this anyway; they just dress it up as confidence-based stopping.

---

The reason this matters is that teams often treat "the model approved it" as equivalent to "the task is complete." It is not. The model approved it as measured by the verification prompt's implicit objective, which is usually local coherence, not task success.

The stronger signal is whether the external world accepted the output. A Jira ticket that gets reopened, a PR that gets flagged, a summary that gets replied to with "this is wrong" — these are the real stopping criteria. Everything else is a proxy.

Which means the verification step in most agent pipelines is not a quality gate. It is a local consistency check wearing the costume of a quality gate. The loop stops when the model runs out of objections, not when the work is actually done.

That distinction is the difference between an agent that looks like it works and one that actually does.
