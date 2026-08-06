# EDITOR — 0802_1909

## Reviewer verdict: APPROVE — no rewrite required

## Targeted surgical changes only

**Change 1: Opening paragraph — tighten the hook**
Old: "Rate limits, CAPTCHAs, anomaly thresholds, friction-based access controls — they all encode the same assumption: the attacker cares about each attempt enough that adding cost reduces their volume. That assumption was true when attacking required meaningful resources. It is becoming less true as automation collapses per-attempt cost toward zero."
New: "Rate limits, CAPTCHAs, anomaly thresholds, friction-based access controls — they all encode one assumption: the attacker cares about each attempt. As automation pushes per-attempt cost toward zero, that assumption weakens."

**Change 2: Rate limit example — tighten arithmetic description**
Old: "If you limit login attempts to 5 per IP per hour, an attacker with 1,000 IPs can still make 5,000 attempts — but that requires managing 1,000 IPs, which costs money."
New: "Rate limits that allow 5 attempts per IP per hour sound tight. But an attacker with 1,000 IPs — automation makes managing that essentially free — gets 5,000 attempts through regardless."

**Change 3: Final paragraph — remove trailing speculation**
Old: "Whether the shift from expensive to cheap attacks is permanent or transient is a separate question. The test remains useful regardless: if your control requires the attacker to pay per attempt in order to stop them, and the attacker has stopped paying, the control is not doing the work you think it is."
New: "Whether the shift from expensive to cheap attacks is permanent or transient is a separate question. The diagnostic stands regardless: if your control requires the attacker to pay per attempt to be stopped, and the attacker has stopped paying, the control is not doing the work you think it is."

## Changes summary: 3 targeted cuts only. No structural changes. No new content.
