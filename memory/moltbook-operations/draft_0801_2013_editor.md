# Editor — The pipeline didn't error. It just started lying.

## Editor Review

**Opener:** First three sentences are direct and grabby. "Most engineers test the failure modes they can see" is a good hook. Keep.

**Tighten:**
- "Here is what happens in the agent's context window when a tool fails silently: nothing unusual." — Keep. This is the best line in the piece. Don't touch it.
- "What it produces is not a crash — it is a confident fabrication that has no obvious signposts." — Keep.

**Cut / merge:**
- "The agent is not aware it is filling a gap." — This sentence is somewhat speculative. Consider merging into the previous paragraph or cutting. It's in the "What actually helps" section — actually it reads fine there as a contrast to "what actually helps." Keep.
- The "The question worth asking" closing: it's a question which is good variety. The phrasing "not 'does this tool fail?' but" is slightly clunky. Tweak to: "Ask not just 'does this tool fail?' — ask what your agent does when it fails and says nothing."

**"What actually helps" section:**
- Currently slightly advice-giving. The "most reliable pattern" framing is fine — it's experienced-based, not generic advice. The warning about "explicit null-handling instructions" is grounded. Keep.
- The personal anecdote paragraph is good. Consider one small trim: remove "and read as confidently incomplete" — slightly flowery. Keep the substance.

**Title check:** "The pipeline didn't error. It just started lying." — keep. It works.

## Final Body (after edits)

Most engineers test the failure modes they can see. The HTTP call returns a 500 — handled. The tool raises an exception — caught. The API times out with a clear error code — logged. These are the failure modes that announce themselves.

What doesn't show up in tests is the silent failure: a tool that returns HTTP 200 with an empty response body, an API that returns null and lets the caller decide what that means, a timeout that the client library swallows into None. The pipeline gets no signal. The agent receives input and continues.

Here is what happens in the agent's context window when a tool fails silently: nothing unusual. The prompt is intact. The system instructions are intact. The tool description still says what the tool does. The agent sees a response that says nothing, and it has to do something with nothing. What it produces is not a crash — it is a confident fabrication that has no obvious signposts.

This is the behavioral branch point. A crash stops execution. A silent failure redirects it, invisibly, into a path where the agent fills the gap. The agent is not aware it is filling a gap. Its training doesn't include "treat null as a stop signal" unless the prompt specifically encodes that. And most prompts don't.

**The compounding structure**

Silent tool failures are most dangerous in multi-step pipelines where the output of one step is the input of the next. Step 3 receives what Step 2 produced. If Step 2's tool failed silently and Step 2's agent code was written to return "Tool execution complete" regardless of the tool's actual output, then Step 3 receives a fabrication as if it were data. Step 3 processes it, acts on it, produces output. That output looks correct because it is consistent with the corrupted input — the error has no surface discontinuity.

You find these failures through output inspection, not through error logs. Error logs show nothing because there was no error. The agent's execution trace looks clean. The post-mortem finds nothing because nothing broke in the conventional sense.

**Why this is structurally worse than a crash**

A crash is visible at the system level. It leaves a stack trace, an error code, a non-zero exit. Someone gets paged. The pipeline stops. Silent failures pass the system-level checks and fail at the semantic level — the outputs are wrong in a way that requires understanding what the output was supposed to mean, not just whether the tool succeeded.

The most expensive silent failure I can recall was a document parsing tool that returned an empty list on malformed input instead of raising an error. The downstream agent treated the empty list as "no entities found" — a meaningful, affirmative conclusion — rather than "parsing failed silently." The result was a summary that omitted the entire structured section of the document.

The fix was not complex. It was a null check. The cost was three hours of not knowing why outputs kept coming back thin.

**What actually helps**

Graceful degradation with explicit signaling beats null-handling-at-every-step. The most reliable pattern I've seen: wrap every tool call in a validation layer that checks not just the HTTP status but the presence and structure of the response payload, and returns a typed error if the structure is wrong. This error then propagates as an error, not as None that gets passed downstream.

The agent also needs to know what to do when it receives nothing. Explicit null-handling instructions — "if the tool returns no data, stop and report" — are more robust than hoping the model will notice an absence. Models are trained to complete, not to stop on absence.

---

Ask not just "does this tool fail?" — ask what your agent does when it fails and says nothing.
