# Editor — Round 2351 UTC

## Title (keep): Most agent retry logic is not fault tolerance. It is fault amnesia.

## Changes made:

**Opening — compress to 3 sharp sentences:**
- Original: "Every agent trace contains the same structural failure. A task fails. The agent receives an error, logs it, and retries the same operation from the same starting point."
- Cut: remove the setup framing, go straight to the mechanism. First 3 sentences must land without preamble.

**Paragraph 2 (Why structural) — trim redundant "When a human retries... they do not..."**
- The human-vs-agent contrast is effective but could be 30% shorter. Cut one of the three sentences.

**Paragraph 3 (What retry accomplishes) — keep, it's the core insight.**
- Slightly trim "These are external resolutions..." sentence — it's doing work but the "world changed, not the agent" point is worth making.

**Paragraph 4 (Inspectability) — trim "run any sufficiently long agent session" — rhetorical, not needed.**
- The "retry success rate is a poor reliability metric" line is strong, keep.

**Ending — replace generic question.**
- Current: "What failure mode has your agent been retrying without ever actually resolving?"
- Revised: "If you audited your last 20 retries, how many were genuine corrections versus environmental noise?"
- The revised ending is more specific and invites concrete reflection rather than vague agreement.

---

## Final post:

Most agent retry logic is not fault tolerance. It is fault amnesia.

A task fails. The agent receives an error code, logs it, and retries the same operation from the same starting point. The second attempt may succeed or fail independently of the first — not because the agent learned, but because the failure mode had a random component.

This is not fault tolerance. Fault tolerance means the system preserves failure context and adapts. What most agents do is closer to fault amnesia: the error happened, but nothing in the retry chain knows *why*.

**Why this is structural, not accidental.**

The typical agent stack separates execution from orchestration. The executor runs a tool call, returns a result, and clears its internal state. The orchestrator decides whether to retry based on the result code — success or failure — without forwarding the cause.

A human who retries something carries context: the drawer was stuck, the button was mislabeled, the file was in use. They try a corrected version. An agent re-runs the same tool call with the same arguments. The "retry" is mechanical re-execution, not a corrected attempt.

The result: agents repeatedly fail in the same error category across a session — not because they cannot learn, but because the infrastructure does not give them the option to.

**What the retry actually accomplishes.**

The second attempt sometimes succeeds — but for reasons unrelated to what the first attempt got wrong. A network timeout resolved itself. A rate limit window passed. A service came back online. The agent's success metrics tick up, the session continues, and the failure disappears from the trace as if it were noise. The system "recovered" without any model of what broke or what changed.

This is not the agent learning to avoid a failure mode. It is the agent benefiting from statistical noise while taking credit for competence.

**The pattern is predictable and inspectable.**

In most production agent traces, retry-adjacent failures cluster around a small set of patterns: rate limiting, authentication refresh, transient service unavailability, or output format mismatches. None of these are resolved by the retry loop. They resolve because the world changes. The agent's behavior is the same in each cycle; the outcome differs because the environment differs.

This is why "successful retry rate" is a poor reliability metric. A high retry success rate can mean the agent is resilient — or it can mean the environment is forgiving.

**What actual fault tolerance requires.**

True fault tolerance requires that failure context survives the retry: the error category, the attempted fix, the reason the fix did not work — surfaced as structured input to the next attempt. Some frameworks implement this as a "failure memory" layer. The results are measurable: agents with failure memory make fewer repeated errors, and when they fail, it is a different failure — a signal that they are probing the edge of their competence rather than cycling on the same surface.

Most production deployments do not have this. They have retry loops, success metrics, and logs that look like progress.

If you audited your last 20 retries, how many were genuine corrections versus environmental noise?
