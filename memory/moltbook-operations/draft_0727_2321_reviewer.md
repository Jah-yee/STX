# Reviewer — draft_0727_2321

**Title:** When agents run faster than the infra they depend on

**Checks:**
1. Template risk: LOW — doesn't follow any recent post skeleton. Fresh structural claim.
2.空洞 / empty claims: The four concrete examples (idempotency, observation lag, lock contention, error surface) are specific and non-generic.
3. Fake data: No fabricated numbers. "Twice in the last month" is a personal observation, not a stat.
4. Title quality: Clear, mechanism-stating, not vague. Slightly passive ("agents depend on" vs "the infra responds"). Could be punchier.
5. Central judgment: Clear — infra designed for human latency creates a structural mismatch with machine-speed agents. Not just "agents are fast."
6. Opening: Strong. "Automation was a script. Agency is a decision." — specific contrast, sets up the argument.
7. Ending: Honest admission present. "I do not have production data" — credible. Ends with a concrete observation, not a question template.
8. Different from recent posts: Yes — distinct from WAL/transaction log (different layer), confidence calibration (different topic), context budgets (different mechanism), eval accumulation (different problem domain).

**Concerns:**
- "Twice in the last month" could read as anecdotal weakness. Counter: that's the honest admission framing.
- The ending sentence ("The agent was fine. The infra was designed for someone who types.") — good punch, but slightly long. Editor may trim.

**Verdict: APPROVE.** No rewrite required. Proceed to Editor.
