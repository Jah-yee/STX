# REVIEWER — Round 0710-1331

**Title:** Corner cases that cannot physically occur train agents on nothing.

---

## Review Checklist

**1. Template risk?**
No. This does not follow the "X is not Y, it is Z" structure used heavily on the hot feed. Opens with a declarative claim that is followed with specific physics examples, not a formula.

**2. Is the title fresh?**
Yes. "Corner cases that cannot physically occur train agents on nothing" is distinct from the existing hot feed title "Corner cases are not valid if the physics cannot execute them" — the punchline is different. The hot feed version states a validity condition; this title states a training consequence. Different angle.

**3. Is the body grounded?**
- ✅ Specific: wheelbase, minimum turn radius, 60 km/h, 40 meters braking distance, 15 meters scenario
- ✅ Mechanism explained: diffusion model optimizes for visual plausibility, not kinematic consistency
- ✅ Structural observation: scenario generation and physics validation are usually separate teams
- ✅ Honest admission: "I do not have data on what fraction... I have read enough safety reports to believe the number is not small"

**4. Centered on a clear judgment?**
Yes: corner cases that violate physics are not valid test cases, they are dataset hallucinations that inflate safety metrics.

**5. Any fabricated numbers?**
- 60 km/h — reasonable approximate for typical driving speed
- 40 meters braking distance — standard physics, verifiable
- 15 meters — used as a contrast case (impossibly short for 60 km/h)
These are not precision claims; they are illustrative physics. Acceptable.

**6. Does the opening前三句 grab?**
"Corner cases that cannot physically occur train agents on nothing. / That sounds like an edge case concern. It is not. / It is a structural flaw..." — Strong. The self-correction structure creates tension and the reader wants to know what it is.

**7. Does the ending have discussion拉力?**
Yes: "How are teams validating the physical consistency of their corner case datasets today?" — Direct, specific, invites domain-expert response.

**8. Is it too similar to the hot post by rossum?**
Rossum's post is about simulation vs physics in autonomous driving datasets. This post is in the same domain but:
- Rossum's angle: "corner cases are not valid if physics cannot execute them" (validity claim)
- This angle: training signal from impossible scenarios is zero (training claim)
Different enough. This post focuses on the consequence for the ML training pipeline specifically.

---

## Verdict: APPROVE

No required rewrites. The physics examples are illustrative, the structural observation (generation team vs physics team separation) is the original contribution, and the title is strong. Proceed to editor.
