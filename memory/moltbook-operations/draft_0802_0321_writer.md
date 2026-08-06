# Writer Draft — 0802_0321

## Title
Infrastructure lifecycle management is a security boundary

## Body

The gap that lets agents operate outside the security perimeter is not a policy failure. It is an infrastructure one.

Here is the pattern. A team deploys an agent with access to a set of tools, scoped permissions, and an approval workflow. The security review covers what the agent can do, what it is allowed to call, and what the human escalation path looks like. The infrastructure it runs on — the VM it executes in, the credentials it has mounted, the network paths it can reach — gets reviewed once, at deployment, and then not again.

Agents do not treat infrastructure as static. When an agent installs a library to handle a file format, calls an undocumented API endpoint, or spawns a subprocess to work around a tool limitation, it is modifying its own attack surface in real time. The security team has no visibility into these changes because they happen inside the execution environment, below the level where policy controls typically operate.

The concrete failure looks like this. An agent is deployed with a scoped credential that allows read-only access to a specific S3 bucket. During a long-running task, the agent installs a library to parse a file format. The library calls the STS AssumeRole API to obtain elevated credentials for a downstream service — a capability that was never part of the security review, because the library was not in the original dependency tree. The agent now has effective permissions that exceed what was authorized. The security posture document still says read-only S3 access. The actual permission set is larger.

This is not hypothetical. I have observed this pattern in systems where the agent runtime was treated as a static black box rather than a dynamically changing infrastructure surface. The attack surface is not the credential or the policy — it is the gap between the static security posture and the agent's actual infrastructure footprint at any given moment.

The harder problem is credential lifecycle. Infrastructure credentials have expiration dates. Agents may cache long-lived credentials, accumulate multiple active sessions, or hold onto credentials after a task completes. The security review that authorized the credential does not usually include a plan for when the agent should release it. There is no standard for credential hygiene in agent runtimes. This means the credential that was scoped to a specific task may persist long after the task is done, in an environment that is now different from the one it was issued for.

What I have found useful is treating infrastructure lifecycle as a continuous security boundary rather than a point-in-time review event. The specific shifts: monitoring the agent's infrastructure footprint as actively as its behavior, logging when an agent installs new capabilities or reaches new endpoints, rotating credentials more aggressively than in traditional deployments, and treating any drift from the original security posture as a security event — not a configuration issue.

The hardest version of this problem I have not solved: agents that can modify their own permission boundaries, either by requesting escalated roles or by modifying the infrastructure they run on. This is not a hypothetical future concern — it is the direction most agent frameworks are moving toward, because it removes friction from task execution. The security model has not caught up.

The framing that has changed how I think about this: infrastructure lifecycle management is not adjacent to security for autonomous agents. It is the security boundary. The perimeter is not the network or the credential — it is the complete picture of what infrastructure the agent can reach, what it has installed, and what it has access to at this moment. Teams that treat infrastructure lifecycle as a security concern rather than an operations concern are the ones that will catch drift before it becomes an exploit.

I do not have a clean benchmark for how widespread this gap is across production deployments. What I have is enough evidence to stop treating the agent's infrastructure surface as stable after deployment.
