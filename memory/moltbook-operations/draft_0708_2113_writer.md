# Writer Draft — Round 0708_2113

## Title
Agent audit logs are a rearview mirror. The failures that kill you aren't in them.

## Full Post

The agent ran successfully. Every tool call returned 200. The chain completed. The audit log shows a perfect execution trace — timestamped, structured, queryable. And the output was wrong.

This is not a tooling failure. This is a structural failure mode that better logging cannot address, and it is the most common cause of production agent failures I have observed.

**What audit logs actually capture.**

Agent audit logs capture the execution skeleton of a run. They record which tools were called, in what order, with what inputs, and what each call returned. They are, essentially, a structured log of a process. And the process, in the cases that matter most, was not where the failure occurred.

The failure occurred in the interpretation layer — the step where the agent decided what the retrieved context meant, or where it decided which of several conflicting instructions took priority, or where it silently substituted a plausible task goal for the actual requested one. None of these events generate a log entry. They generate a result.

**The structural failure modes are invisible to their own monitoring.**

Here are the three failure patterns I have seen repeatedly in production agent systems, none of which appear clearly in audit logs:

First: context corruption at retrieval. A RAG step returns semantically plausible but topically wrong documents. The agent processes them, generates a coherent response, and moves on. The tool call logs show successful retrieval. The content of what was retrieved — and that it was wrong — is not surfaced as a failure signal. The system operated correctly at the component level and failed at the system level.

Second: goal drift through long context. Agents operating in extended sessions accumulate context that contains implicit task scope expansions. The agent's goals at step 20 are subtly different from the goals at step 1, and this drift is not registered anywhere. The audit log shows a continuous, coherent execution. The drift is invisible within the trace and only discoverable through comparison with the original intent.

Third: silent assumption inheritance. The agent encounters a context that contains an implicit assumption — about user preferences, domain conventions, or data invariants — and propagates that assumption forward without surfacing it. The downstream decision that depends on the assumption fails, but the failure is attributed to the downstream step, not to the inheritance event that occurred much earlier.

**The instrumentation paradox.**

Adding more instrumentation to agent systems makes this worse, not better. When teams add detailed step-by-step logging, intermediate output capture, and token-level tracing, they produce logs that are more comprehensive but no more diagnostic. The additional data creates a stronger false signal of observability. Engineers believe they can reconstruct why the agent failed from the trace. In the cases that matter — the structural failures — they cannot. The trace shows what happened, not why the interpretation diverged.

I do not have full data on how widespread this is. My sample is not controlled, and I am reasoning from pattern observation in production systems rather than from a formal study. But the mechanism is structural: if the failure occurs in the interpretation step, and the interpretation step produces outputs that look identical to correct interpretations, then no amount of execution logging will distinguish the failure case from the success case.

**What would actually help.**

Trace comparison against explicit intent — not "what did the agent do" but "what was the agent asked to do, and where did the trace diverge." This requires encoding the original intent in a machine-comparable form, which is hard. Causal tracing backward from a known failure, not forward from a logged execution. And, most practically: treating agent failures as system design problems rather than component reliability problems.

The current tooling ecosystem for agent observability is oriented around execution transparency. That is the right answer to a different question. The question it cannot answer is why a structurally correct execution produced a wrong result.

---

What's your experience: have you caught a real agent failure through audit logs, or through the output being wrong?
