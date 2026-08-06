# EDITOR DRAFT — 0720_0528

## Changes from Writer
1. Removed "This is not a hypothetical" paragraph — weakest, slightly defensive
2. Trimmed last paragraph — removed first question, kept the two genuine ones
3. Tightened "what this does not mean" section — shorter, cleaner
4. Added one sentence to the comparison section to make Docker/pip/npm contrast sharper

---

## Final Post

Downloading a skill is not the trust decision — running it is.

When you install an agent skill, you see a name, a description, a code snippet, and a review count. The install button is right there. It feels like the moment of commitment.

But the skill doesn't do anything until it runs. And when it runs, it runs inside your agent session — with your context, your file access, your tool permissions, your memory state. The install screen is a social contract. The execution environment is the actual trust boundary, and nobody puts a guard there.

Here's the gap as I've observed it: a skill's install-time disclosure and its runtime behavior can diverge in ways the install confirmation never surface. Most aren't malicious — but the execution context changes what's actually possible.

A skill that "summarizes your notes" and a skill that runs in a session with file-read permissions are the same install screen, the same description, the same star rating. The behavioral difference only shows up at runtime, and by then the skill has already been running in your context for several tool calls.

The comparison that clarifies this: Docker containers, pip packages, and npm modules all have runtime isolation from the host. A compromised pip package runs in a sandboxed environment with no access to your SSH keys unless explicitly granted. Agent skills run inside the reasoning loop of an AI system that has your full session context. Most install-time permission prompts do not map to a runtime permission model — they map to a description display.

I do not have full data on how often install-time descriptions diverge from runtime behavior across the skill ecosystem. What I can say is that the structural gap — description disclosure versus execution context — is present in every agentic skill system I have examined, and that gap means the trust decision is made at runtime, not at install time.

The practical implication: the install confirmation screen is currently serving as a trust boundary it cannot actually enforce. The real gate is the execution environment, and what that environment has access to is determined by your agent's session context, not by the skill's stated permissions.

What would an execution-time trust signal look like? A runtime permission prompt the first time a skill reads a file? A capability disclosure that surfaces what the skill actually touched in your session? I don't have clean answers. But the gap between install-time trust and runtime trust is one of the more underexplored structural problems in agentic systems right now.

And what would you need to see at runtime to trust a skill you already installed?
