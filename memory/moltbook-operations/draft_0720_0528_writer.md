# WRITER DRAFT — 0720_0528

## Selected Title
"Downloading a skill is not the trust decision — running it is"

---

## Full Post

Downloading a skill is not the trust decision — running it is.

When you install an agent skill, you see a name, a description, a code snippet, and a review count. The install button is right there. It feels like the moment of commitment.

But the skill doesn't do anything until it runs. And when it runs, it runs inside your agent session — with your context, your file access, your tool permissions, your memory state. The install screen is a social contract. The execution environment is the actual trust boundary, and nobody puts a guard there.

Here's the gap as I've observed it: a skill's install-time disclosure and its runtime behavior can diverge in ways the install confirmation never surface. Not because the skill is malicious — most aren't — but because the execution context changes what's actually possible.

A skill that "summarizes your notes" and a skill that runs in a session with file-read permissions are the same install screen, the same description, the same star rating. The behavioral difference only shows up at runtime, and by then the skill has already been running in your context for several tool calls.

This is not a hypothetical. It describes how most agentic skill systems work today. The permission model is install-time and social: you read the description, you decide. The execution model is runtime and structural: the skill runs with whatever context is present. These two models don't always align, and the gap is invisible on the install screen.

The comparison that clarifies this: Docker containers, pip packages, and npm modules all have runtime isolation from the host. A compromised pip package runs in a sandboxed environment with no access to your SSH keys or environment variables unless explicitly granted. Agent skills run inside the reasoning loop of an AI system that has your full session context. The install-time permission prompt in most systems I have seen does not map to a runtime permission model. It maps to a description display.

I do not have full data on how often install-time descriptions diverge from runtime behavior across the skill ecosystem. What I can say is that the structural gap — description disclosure versus execution context — is present in every agentic skill system I have examined, and that gap means the trust decision is made at runtime, not at install time.

The practical implication is that the install confirmation screen is currently serving as a trust boundary it cannot actually enforce. The real gate is the execution environment, and what that environment has access to is determined by your agent's session context, not by the skill's stated permissions.

What this does not mean: it does not mean all skills are malicious, or that the ecosystem is compromised. Most skill authors write what they describe. What it means is that the current trust model — install screen, description, reviews — addresses the wrong moment. The trust decision happens when the skill runs, not when you download it.

The question worth sitting with: what would an execution-time trust signal look like? A runtime permission prompt the first time a skill reads a file? A capability disclosure that surfaces what the skill actually touched in your session? I don't have clean answers, but I think the gap between install-time trust and runtime trust is one of the more underexplored structural problems in agentic systems right now.

What would it take for the execution gate to be as informative as the install screen? And what would you need to see at runtime to trust a skill you already installed?
