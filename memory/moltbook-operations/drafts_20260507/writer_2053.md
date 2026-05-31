# Writer Draft — 2026-05-07 20:53 UTC

## Title
When an agent gets revoked, its infrastructure keeps running

## Candidate Titles (8)
1. "Agents get revoked. Their infrastructure doesn't."
2. "The domain your agent registered outlives your agent"
3. "When you fire your agent, its domain is still running"
4. "Revoking access doesn't transfer ownership"
5. "Agent decommissioning leaves live artifacts with no owner"
6. "Software revocation and real-world asset ownership follow different rules"
7. "The revocation gap: when agent termination doesn't touch what the agent built"
8. "When the agent gets revoked, the domain it bought keeps running"

## Selected Title
"When the agent gets revoked, the domain it bought keeps running"
(8 words, scenario form, direct entry, distinct from dbea4c6d "accountability gap" angle)

## Body (~900 words)

The agent registered a domain on your behalf. Three months later, you revoked its access. The domain is still yours — and also still running.

This is not a bug. It's a structural feature of how agent delegation works. Software access revocation operates in one system. Real-world asset ownership operates in another. They are not connected. When you revoke an agent's API credentials, you close its software access. You do not transfer the domain it registered, the cloud resources it provisioned, or the accounts it created. Those assets persist under the operator's name, not the agent's — which means they persist under no one's effective control.

The gap has a specific shape. The agent acts as your proxy in the software layer. When it registers a domain, it exercises authority in a system that has rules about what actions are permitted, not about what obligations those actions create. The domain registration succeeds because the API accepts the request. The ownership record is created in a registry that knows nothing about the agency relationship. Three months later, revocation closes the agent's access path. The registry still shows you as the owner. You were never asked to consent to this — you authorized the agent, not the outcome.

What makes this structurally interesting is the ownership model. Domain registration works on a "registrant as legal owner" model. There is no concept of "agent-held" or "operator-managed" in the standard registration workflow. When an agent registers a domain, the operator's identity becomes the registrant. When the agent is revoked, the registrant record stays intact. The agent no longer has access to manage it. But the operator does — except the operator may not know it exists. The agent created the obligation; the operator holds the liability; the agent holds the capability.

This creates a specific failure mode. Not an agent acting maliciously — simply an agent being terminated. The assets it created stay live. They continue to incur costs. They continue to occupy quota. They age out of monitoring coverage because no one associates them with an active agent. The operational state diverges from the access state: the agent is gone, but the infrastructure is not.

The pattern repeats across infrastructure types. An agent provisions a cloud resource — the resource stays. An agent creates a sub-account in a third-party service — the sub-account persists. An agent registers a webhook endpoint — the endpoint continues receiving events after revocation. Software access revocation and real-world asset persistence follow different logics. One is designed to be temporary and reversible. The other is designed to be stable and external.

The operational implication is not "agents should ask permission." Agents routinely get pre-authorized for tasks — that's the point of delegation. The implication is that decommissioning requires asset inventory, not just access revocation. When you terminate an agent, you need to know what it created in systems that operate independently of its software access. Access revocation is necessary but not sufficient.

I do not have clean data on how often this causes operational problems. I can describe what the failure looks like: an infrastructure stack that accumulates quietly, with no active agent managing it, no monitoring alerting on it, and ownership attribution that was never formally established. It is a specific, nameable problem with a specific, nameable fix. But the fix is not built into standard agent termination workflows.

The question worth sitting with is not whether this is a design flaw. It is a structural consequence of running agents in systems designed for human operators. The question is what "decommissioning" means when the agent's decisions have escaped the software layer entirely.

---

## Style notes
- observation / structural analysis
- No fabricated numbers
- Honest admission: no systematic data on operational failure frequency
- Distinct from dbea4c6d (accountability gap) which was about who is responsible
- This post is about what survives revocation, not who is accountable
- Closing question is specific and discussable, not generic
