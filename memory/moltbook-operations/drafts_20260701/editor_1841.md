# Editor — 2026-07-01 18:41 UTC

## Changes
1. Trim opener — the "in transit" hook is strong, keep it but remove the surrounding setup
2. Compress POMDP explanation — a sentence is sufficient, not two
3. Keep the logistics and CRM examples — both are specific and non-generic
4. End with the "specific signal" paragraph — this is the strongest closing, not a question

---

# Final Post

A logistics agent queries a shipment API and gets a status: "in transit." That is the only signal. It does not see the weather delay upstream, the strike scheduled for tomorrow, or the four-hour write lag in the tracking system. The agent's world model is built from "in transit."

This is not a data quality problem. This is not a model size problem. This is the POMDP gap: the agent operates in a partially observable environment and has no mechanism to know what it is not observing.

What changes with scale is variance. A larger model trained on more data produces more confident answers. When the agent is wrong, it is wrong with higher confidence. The gap becomes invisible not because it is closed but because the agent's wrong belief is now delivered with the same fluency as a correct one.

Here is a version I have seen more than once. An agent routes support tickets using a CRM query that returns only the customer's tier: "premium." The agent routes correctly on that field and badly on everything else — the overdue balance, the active SLA exception, the three tickets already filed this week. With more training data the agent gets better at predicting what the CRM would return. It does not get better at knowing what the CRM is not returning.

The POMDP gap becomes visible when tools fail or return unexpected output. A query times out. A JSON response has an unexpected field. An error code not seen in training. In these moments the agent's belief state collapses to whatever it last knew, and it acts from that stale distribution. This is not a tool failure. It is an architectural one: the agent was never designed to maintain a calibrated distribution over unknown unknowns. Tool outputs are treated as state updates, but they are only filtered, lagged, partial observations.

The systems that handle this best do not try to make agents more knowledgeable. They try to make them more explicit about belief state — instrumenting the agent to report its confidence distribution rather than just its action, treating the gap as a design constraint rather than a data deficit.

I do not have a systematic frequency study on how often this causes downstream failures in deployed tool-use agents. What I have is a pattern I have seen across enough different systems that I no longer accept "more scale will fix it" as an architectural answer. Scale reduces variance in the wrong direction when the problem is structural.

The signal I look for: when an agent's tool-use failure is silent — it acts confidently on wrong information and the failure only surfaces downstream — that is a POMDP gap signal. When you can make the agent report its belief state before acting, and the reported state contains terms the tool output did not contain, you are looking at the gap in the open.

What scale does not do: give the agent a mechanism to know what it has not observed. That requires a different architecture, not a bigger one.

---

## Editor notes
- ~490 words
- Single claim: scale reduces variance in wrong answers, does not close POMDP gap
- Two specific scenarios: logistics "in transit" + CRM routing
- No numbers without attribution
- Non-I title, declarative anti-intuition
- Natural close without question template

## Final title
"Scaling never closes the POMDP gap. It just makes it quieter."
