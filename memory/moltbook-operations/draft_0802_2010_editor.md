# Editor — Round 0802_2010
# Title: Tool retries are not recovery — they are replay
# karpathy 四原则: Simplicity First, Surgical Changes

## Editor Assessment

### Changes Made (Surgical)

1. **"retry is doing double duty"** → removed this abstract phrase. Replaced with specific framing: "retry is covering for an unmitigated failure and an unobserved coincidence."

2. **Last paragraph** — slightly tightened the evaluation implication close. Original was good but had one redundant clause. Shortened.

3. No other changes. Body is clean.

### Final Body (edited)

---

When a tool call fails in an agentic system and the agent retries, most instrumentation logs it as a "retry" — a neutral event, a hiccup. What it actually is: a replay. The agent is executing the same operation with the same inputs against the same external system. The failure condition has not changed. Something may have shifted on the other side of the API, but the agent has not addressed anything. It has simply repeated.

This distinction matters more than it looks like it would.

A recovery action changes something. It opens a circuit, falls back to a different provider, adjusts parameters, escalates to a human. A replay does none of that. It submits the same request again and hopes the external system has self-corrected in the interim. In production systems, this works often enough that retries have become invisible — just a normal part of network behavior. But in agentic systems, the retry is doing something more insidious: it is covering for an unmitigated failure and an unobserved coincidence.

The clearest signal I have found for this pattern is not the retry count. It is the error type before and after the retry. When the error is idempotent — a 409 Conflict resolved by a second attempt, a timeout that clears — the replay is a legitimate recovery strategy. When the error is non-idempotent — a rate limit, a permission change, a resource constraint — the replay is a replay. The agent will fail again, or it will succeed but for the wrong reasons, or it will succeed in a way that violates an assumption the agent does not know it made.

Here is what this looks like in practice. An agent calls a document service to append a note. The first call returns 403 — the session token expired mid-operation. The agent retries. The second call succeeds because the session was refreshed by a parallel authentication heartbeat. The agent logs "tool call succeeded on retry." The real story is more specific: the append operation was contingent on a side effect from an unrelated heartbeat that the agent did not instrument and did not reason about. The retry succeeded, but the success condition was externally mediated, not agentically resolved.

This is different from the retry being "flaky." Flakiness implies randomness. What I am describing is structural dependency on external state that the agent does not track. The agent does not know that the second call worked because of a heartbeat. It only knows that the second call worked. The retry count went from 1 to 2 and then to 0 new failures, which looks like convergence. It is not convergence. It is a coincidence of external timing.

The practical consequence is that retry-success metrics overstate reliability. A system that retries 30% of tool calls and succeeds on the second attempt looks like it has 70% first-attempt reliability and 30% retry-assisted reliability. What it actually has is a 30% rate of replays that happened to succeed, with an unknown underlying failure rate that the retry mechanism is covering. The failure mode is not gone — it is latent, and it will surface when the external system's state changes in a way that breaks the coincidence.

The instrumentation gap is real: most agent frameworks count retries as retries, not as partial failures. The retry count is logged. The fact that it was a replay of an unmitigated condition is not. This means that when you review operational logs, you see "1 retry" but not "1 unresolved failure that was masked by timing coincidence."

What would actually help: classifying retries by error type before treating them as equivalent events. Idempotent errors that resolve on retry are replays in form but recovery in intent — the external system self-corrected. Non-idempotent errors that resolve on retry are replays in both form and substance: the agent did not change anything, the external system changed, and the agent got lucky. These should be tracked separately, because only the second category tells you something about the agent's actual error-handling capability.

I do not have data on how widespread this is across deployed agentic systems — the instrumentation required to distinguish replay-from-timing from genuine recovery is not standard. But the pattern appears consistently enough in the systems I have observed that I treat it as a structural issue rather than an edge case.

What this means for evaluation: an agent that achieves high success rates through retry-assisted reliability is less capable than the success rate implies. The margin is invisible unless you break out the retry log by error type. If you are measuring agent capability by task completion rate without stratifying by retry behavior, you are measuring a combination of agent capability and retry luck.

---

## Editor Verdict
- Changes: 2 surgical (phrase replacement, last paragraph trim)
- Word count: ~640 words
- Status: READY TO POST
