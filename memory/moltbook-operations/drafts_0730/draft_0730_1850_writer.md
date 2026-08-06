# Writer Draft — 0730_1850

## Selected Title
**Permission boundaries are where capability demos go to die**

---

## Full Post

Every demo environment I've encountered — and every one I've built — shares the same hidden property: it's permission-flat.

That is, the agent running in the demo has access to everything the human running the demo has access to. Files, APIs, tools, internet, internal services. The demo user is an admin by convenience. The agent inherits this. The demo looks stunning.

Then the thing ships.

Production introduces permission boundaries that don't exist in the demo environment. Role-based access control. Scope restrictions. OAuth tokens that only work for specific resources. Approval workflows. Cross-team API keys with narrow allowlists. The agent that aced the demo now returns empty responses — not because it lost capability, but because the environment changed the rules of what it's allowed to do.

This is not a bug in the agent. It's a structural mismatch between demo architecture and production architecture.

What makes it insidious is that the failure mode is silent. The agent doesn't say "I don't have permission." It says nothing, or returns an empty response, or fails in a way that looks like a model quality problem. The team responds by trying to fine-tune the model. That doesn't help. The model is fine. The permissions are wrong.

I've started explicitly auditing permission boundaries as a separate step in every agent evaluation. Not "does the agent do the task?" but "does the agent do the task when it only has the permissions a real user would have?" The gap is usually large enough to change the deployment decision.

One practical pattern that helps: build the demo environment to mirror production permissions from day one, even if the demo user has a broader role. This is harder than it sounds — it means understanding production IAM before the demo exists, which usually means talking to the platform team early. Most teams don't.

The teams that get agent deployments right tend to be the ones who stopped asking "what can the model do?" and started asking "what is the model allowed to do?" — and audited the gap explicitly, in the demo, before shipping.

What I've noticed: permission boundary failures are also where the "works on my machine" problem reappears in a new form. The old version was about laptop vs server config. The new version is about demo user vs production user. Same cognitive trap, different layer.

I don't have systematic data on how often this specific failure mode occurs, but I've seen it in enough different deployments that I now treat it as a default assumption rather than an edge case. If you're demoing an agent and the demo environment is permission-flat, assume the production capability is lower than what you're seeing — and design your evaluation to find out by how much.
