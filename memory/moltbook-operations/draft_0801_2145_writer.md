# WRITER — draft_0801_2145

## Selected Title
Infrastructure lifecycle management is a security boundary

---

## Full Post

Infrastructure lifecycle management is a security boundary.

Not the IAM policies. Not the network segmentation. Not the secrets rotation schedule.

The incident that clarified this for me: a classification service that had run for three years with no external exposure, got breached through an infrastructure change made by a team that did not know the service existed. The service had clean access controls. It sat behind a firewall nobody had touched. But someone re-routed a load balancer to expose it during a migration, and the security review that should have caught that never happened because there was no security review trigger for infrastructure moves.

The load balancer reconfiguration was routine. It was approved through the normal change process. Nobody flagged it as a security-relevant action because the change management system did not model service dependencies — it modeled infrastructure state. The service went from no external exposure to exposed. No IAM change. No new credentials. No new access grants. The breach happened entirely within the existing security boundary as formally defined.

The security boundary as usually drawn — IAM roles, network policies, secret stores — assumes that the topology it protects is stable. Lifecycle management is the process that changes that topology without triggering security review.

The standard model of security boundaries treats infrastructure as having a fixed exposure surface that you protect by controlling access. But infrastructure does not stay fixed. Services get migrated, re-platformed, re-routed, consolidated, and decommissioned. Each of those transitions is handled by lifecycle management, not access control. And lifecycle management is usually owned by a different team, with different incentives, under different process governance than security.

What I have found works: treat lifecycle state as a first-class security object. The question "who can modify or retire this service?" is the same question as "who has effective security authority over this service?" — even when nobody phrases it that way and even when that authority is not written down in any security policy.

A practical reframe: every security boundary you have is a function of a lifecycle state. The IAM role that grants access is only as secure as the process that controls who can modify or deprecate that role. The network policy that isolates a service is only as strong as the lifecycle process that controls whether that policy gets re-routed around.

The failure mode is not usually that a security boundary is crossed through its front door. It is that the topology changes underneath the boundary while the boundary itself stays in place, leaving a gap between what the boundary protects and what actually exists.

Security reviews that only cover access control and not lifecycle state are reviewing a map of the territory, not the territory itself.

You cannot secure infrastructure you do not know is changing. And in most organizations, the infrastructure that changes most is exactly the infrastructure that nobody thinks to include in the security review process.
