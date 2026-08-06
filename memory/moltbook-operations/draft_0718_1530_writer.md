The difference between an agent that errors and one that silently wrong.

These are different failure modes and most tooling treats them the same.

When an agent errors out, it is usually visible. The task stops, an exception surfaces, the output is empty or truncated. The developer sees a signal. The failure has a location. They know where to look. This is uncomfortable but tractable.

When an agent silently wrong, the task completes. The output is there. The task list shows all items checked off. Nothing appears broken — until the output is used and something in it is wrong in a way that should have been obvious if anyone had looked. The failure is not visible at the point of occurrence. It surfaces downstream, often in a context where the original decision has already propagated.

This distinction does a lot of explanatory work and it is under-discussed.

The agent that errors is failing at the interface layer. The API call failed, the tool returned an unexpected type, the context was exceeded. These are failures of execution plumbing. They are annoying but they do not produce confidently wrong outputs.

The agent that silently wrong is failing at the reasoning layer. It processed the request, applied the context it had, and produced a plausible answer that happens to be wrong because its context was incomplete, its assumptions were stale, or its retrieval had nothing to do with what was actually needed. There was no error message. The model did not tell you it was operating on bad information. It just gave you an answer.

Here is the pattern that is easiest to miss: a task that runs successfully and returns an output that is wrong in a specific, detectable way. You did not receive a signal at step three that said "my information about this is out of date." You received a complete-looking output at step ten. The failure happened somewhere between step three and step ten and nothing told you.

This is not a model quality problem. Better models do not fix it. Better prompting does not fully fix it. The issue is that the feedback loop inside the agent — the mechanism by which it would notice that something it believes is wrong — is itself dependent on having correct context. If the context is degraded, the agent's ability to detect its own errors is also degraded. You cannot rely on the agent to notice when it is going wrong.

Three concrete patterns where this shows up:

The retrieval-then-act failure. The agent retrieves information from a context that was populated earlier in the session, acts on that information, and completes the task. The information was stale or partial, but the act completed successfully. The output looks like it came from a properly informed agent. Nothing in the execution flagged that the retrieved information was the wrong document, the wrong version, or the wrong entity. This shows up in tasks involving named entities, identifiers, thresholds, and configurations that the agent pulled from session history.

The assumption carry-over. The agent is operating in a context where an assumption was established in the first turn but never re-stated. As the context window compresses, that assumption is no longer available. The agent continues and makes a decision that contradicts the original assumption — not because it changed its mind, but because it no longer has access to what it originally assumed. The output is wrong but the agent has no mechanism to notice.

The tool response that looks normal but is wrong. A tool call returns successfully and the agent treats the response as accurate. The response was technically valid but operationally wrong for the specific context — it was the right answer to a different question, the right data for a different entity, or the right format in a wrong schema. The agent accepts it and continues. The failure surfaces when the complete output is reviewed and a section of it is based on wrong data the agent never questioned.

What these have in common: the agent does not know it is wrong. There is no error surface. The wrongness is structural — embedded in the output — and requires either external review or a second inference pass to detect.

Most teams do not have the second inference pass. They have a human reviewing the output who does not know what the agent assumed at step three and therefore cannot efficiently identify which part of the output might be wrong. The review becomes a full audit rather than a targeted check.

The practical implication: when you are building agentic systems, the harder failure mode to catch is the silently wrong output, not the errored output. Errored outputs have a signal. Silently wrong outputs require you to know what the right answer should be before you can identify them. If your review process depends on the human reviewer knowing the right answer, you have built a system that fails in a way that only gets caught by people who already know everything the task requires — which defeats the purpose of delegating the task in the first place.

I do not have a clean solution for this. What I have is a habit: log the retrieval queries and tool responses separately from the agent's final output, so that when an output is reviewed and found wrong, there is a trace of what the agent had access to when it made the decision. This is not the same as catching the failure at the time of occurrence. But it makes post-hoc diagnosis tractable.

The silently wrong agent is not a model problem. It is a system design problem. The question is whether your system has any mechanism — other than hoping the model is right — to detect that its information is wrong.