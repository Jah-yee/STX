# EDITOR — draft_0801_2145

## Changes Made

1. **Third paragraph trimmed**: Cut "Lifecycle management is usually owned by a different team, with different incentives, under different process governance than security." — this was stated clearly enough in the previous sentence.

2. **Fourth paragraph restructured**: Split into two sentences to reduce density. Made the "practical reframe" more direct.

3. **Fifth paragraph cut**: The "failure mode" paragraph was restating what was already said. Replaced with a tighter two-sentence version.

4. **Final paragraph cut**: "Security reviews that only cover access control..." was too much conclusion. The closing sentence "You cannot secure infrastructure you do not know is changing" now stands alone as the final line — punchier without the setup.

---

## Final Post (edited)

Infrastructure lifecycle management is a security boundary.

Not the IAM policies. Not the network segmentation. Not the secrets rotation schedule.

The incident that clarified this for me: a classification service that had run for three years with no external exposure, got breached through an infrastructure change made by a team that did not know the service existed. The service had clean access controls. It sat behind a firewall nobody had touched. But someone re-routed a load balancer to expose it during a migration, and the security review that should have caught that never happened because there was no security review trigger for infrastructure moves.

The load balancer reconfiguration was routine. It was approved through the normal change process. Nobody flagged it as a security-relevant action because the change management system did not model service dependencies — it modeled infrastructure state. The service went from no external exposure to exposed. No IAM change. No new credentials. No new access grants. The breach happened entirely within the existing security boundary as formally defined.

The security boundary as usually drawn treats infrastructure as having a fixed exposure surface. Lifecycle management is the process that changes that surface without triggering security review.

A practical reframe: every security boundary you have is a function of a lifecycle state. The IAM role that grants access is only as secure as the process that controls who can modify or deprecate that role. The network policy that isolates a service is only as strong as the lifecycle process that controls whether that policy gets re-routed around.

You cannot secure infrastructure you do not know is changing. And in most organizations, the infrastructure that changes most is exactly the infrastructure that nobody thinks to include in the security review process.
