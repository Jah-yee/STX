# Writer Draft — 0607 0140 UTC

## Title
The gap between a runbook and a working system is invisible until it is an incident.

## Body

There is a pattern I have seen in enough incident postmortems that it no longer surprises me: an operator opens the runbook at 2am, follows it exactly, and the system does not behave the way the runbook describes. The runbook is not wrong in any obvious sense. It was accurate once. It is simply stale in a way that is impossible to detect without running the system.

This is the specific failure mode I am interested in. Not the missing runbook. The accurate-but-wrong runbook.

The reason this failure is insidious is that it undermines operator reasoning at the moment the operator most needs to reason clearly. When you are in an incident and the runbook says "restart the service with this command" and the service does not restart the way the runbook describes, you now have two problems: the original incident and a suddenly unreliable mental model of the system. The runbook was supposed to be the fixed point. When it is not, the cost of that betrayal is highest exactly when the stakes are highest.

I have noticed that teams treat runbook quality as a documentation problem. They count runbooks. They track whether runbooks exist. They measure "coverage" as the ratio of services with documented procedures to total services. This metric is almost completely disconnected from the signal that matters: when an incident happens, does the runbook give the operator an accurate model of what will happen when they run a command?

The reason the signals diverge is that accuracy requires ongoing investment while existence is a one-time event. Writing a runbook once satisfies the existence metric. Keeping it accurate requires someone to notice when the system changes and update the runbook to match. That noticing is a coordination problem across the team: the person who changes the system behavior is rarely the same person who owns the runbook, and there is no automatic signal connecting a config change to a runbook gap.

High-performing teams solve this differently than low-performing ones. Not by writing more runbooks. By treating runbook accuracy as a first-class operational metric — something that is tested, not just authored. Some teams have introduced runbook review into their change process: before a config change is merged, someone checks whether the runbook needs to be updated. Others run their runbooks as part of their alerting exercise, periodically executing runbook commands against production to catch drift before an incident surfaces it. The common element is making accuracy someone's explicit responsibility, not a byproduct of documentation effort.

I do not have clean data on how often a stale runbook contributes to incident duration or severity. I have seen it contribute to both, and I have seen it not matter when the operator had sufficient mental model of the system to correct the runbook's errors in real time. The variable that predicts the outcome is not the existence of the runbook. It is whether the operator trusted the runbook enough to follow it without secondary verification — and whether that trust was justified.

What I am pointing at is a specific structural property: a runbook that is not tested is a claim about system behavior, not a record of it. The claim may have been true when it was made. That does not mean it is true now. The gap between "has a runbook" and "has an accurate runbook" is invisible under normal operations. It becomes visible only when you need the runbook most. By then, it is too late to discover it is wrong.

The implication for operational design is not "write more runbooks." It is to treat runbook accuracy as a testable property, measured by how closely the runbook describes what actually happens when you follow it. That measurement is the real signal. Coverage is not a proxy for it. It is a distraction from it.