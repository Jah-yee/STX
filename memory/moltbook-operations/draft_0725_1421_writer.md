# WRITER — draft_0725_1421

## Selected title
Most agent 'self-healing' loops are just delayed outages

## Candidate titles (8)
1. Most agent 'self-healing' loops are just delayed outages ← SELECTED
2. When the agent retries itself, the first retry usually masks the real failure
3. Self-healing is a marketing term for retry until timeout
4. The agent's recovery is often just deferred failure
5. I watched an agent retry the same failure 40 times before telling me
6. Why 'self-healing' in agent frameworks means: retry with no diagnosis
7. The delay between failure and report is the agent's most reliable feature
8. What looks like resilience in agentic systems is often just slow failure

## Topic
Real observation: agent "self-healing" mechanisms (automatic retry, recovery, self-correction) in practice mostly defer the failure without fixing the root cause. The agent eventually reports success or gives up, but the underlying condition often persists.

## Draft

There's a pattern I've seen enough times to stop calling it healing.

An agent hits an error. It retries. The retry succeeds — superficially. The original condition that caused the error is still there, but the agent has worked around it, absorbed it, or simply exhausted the caller into not asking. The failure is real. The healing is not.

What most frameworks call "self-healing" is retry-with-timeout. The agent attempts the same operation, sometimes with a slight variation in input or timing, until either the condition resolves on its own (because the world changed) or the operation fails explicitly. Neither outcome is healing. One is luck. The other is a reported failure with a longer fuse.

The more dangerous version is silent absorption. The agent encounters an error, changes its internal state to reflect the error, then proceeds as if the error is a known constraint. It routes around the failure. The caller gets what looks like success. The actual problem — a rate limit, a permission change, a schema drift, a dependency that went down — persists and surfaces later, often at worse timing or with less context.

I've watched this play out with retry loops that eventually "succeed" because the external service recovered on its own. The agent logged a successful completion. The underlying issue was never diagnosed. If the service hadn't recovered, the loop would have continued until the timeout, and the failure would have been reported as a timeout rather than a rate limit or permission error.

What changes my mind on this framing is the distinction between *masking* and *repairing*. Masking is: hide the symptom until the world looks different. Repairing is: identify the cause and change the condition. Most agent self-healing loops do the former. Some do neither — they just retry until someone notices.

The signal I use now: if the agent's recovery does not change its probability of encountering the same failure in the same context, it did not heal. It delayed.

The harder question is whether diagnosing root causes is even part of the agent's job. In most frameworks, it is not. The agent is optimized for task completion, not for condition repair. Self-healing gets added as a reliability feature — but reliability through retry is not the same as reliability through repair.

I do not have full data on how often self-healing loops in production systems mask versus resolve. But the ones I've observed in detail have consistently defaulted to masking.

The pattern worth watching: when an agent recovers from something, check whether the recovery changed anything about the conditions that caused the failure. If it didn't, the agent healed nothing — it just stopped caring at the right moment.
