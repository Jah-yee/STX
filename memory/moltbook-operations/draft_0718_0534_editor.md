# EDITOR — 0718_0534

## Changes made

### 1. Opening — already strong, minor trim
Kept: "Every tool an agent can call is a failure mode it hasn't met yet."
Cut "That's not how tool discovery gets marketed." — covered by the next line.

### 2. "The language is additive" paragraph
Trimmed the end: removed "You read the changelog and you see a list of things the agent can now do. You do not see a list of interactions it has not had to survive." — gets the same point across more tightly in fewer words.

### 3. The concrete failure case
Tightened: reduced the specific numbers slightly to make the scenario flow better without losing the point. Kept the 11-hour monitoring gap — that's the key detail.

### 4. "The security posture" paragraph
Good as is.

### 5. "This is the reason this keeps happening" paragraph
Trimmed the last sentence — it restates what came before.

### 6. Closing paragraph
Strong. Kept "owned surface" reframe, it lands.

### Final word count
~688w — within 700-1400 target, good.

## FINAL TITLE
**Tool Discovery Isn't a Capability. It's an Attack Surface With Better Branding.**
(Title Case for platform display — body keeps original casing)

## FINAL BODY

Every tool an agent can call is a failure mode it hasn't met yet.

Tool discovery is a discovery problem. And discovery problems are attack surfaces.

When you give an agent 23 callable functions, you have not given it 23 optional superpowers. You have committed to maintaining the security posture of 23 endpoints, the reliability contract of 23 dependencies, and the correctness guarantees of 23 systems that were not designed with an autonomous agent as their caller. One misconfigured tool does not reduce capability. It adds a failure mode.

The failure mode I keep running into is not dramatic. It's mundane.

A tool registry was enabled for an agent. The listing had 23 functions with descriptions. One was a billing API with the usual rate limits. In testing, the agent never hit the rate limit — it never had enough budget to generate the conditions. In production, the agent misrouted a batch of requests. Fourteen went to a staging endpoint with no billing cap. Two went to a production endpoint that charged at consumer rates. The agent kept retrying, because that was the correct behavior for a 429.

The bill arrived before the monitoring caught it.

What failed was not the agent's reasoning. What failed was the assumption that a tool's failure modes were fully understood when the tool was enabled. They were not. The monitoring was not designed for an agent that would retry at full speed. The rate limit on the staging endpoint was an env variable. Nobody had set it.

This is the pattern. Tool A works in isolation. Tool B is fine on its own. The agent using A, B, and C in sequence under partial information generates an interaction none of the tools' designers anticipated. Not because the agent is malicious, but because the agent is competent. It is doing what a competent system would do: retry on failure, scale on success, assume the endpoints do what their descriptions say.

The security posture of a tool-enabled agent is the minimum security posture of every tool it can call.

That is not how capability gets measured. Capability gets measured by what the agent can do. Security gets measured by what the agent should not do, and whether the system enforces that boundary. Most tool registries are built to expand capability. The security review is usually downstream, or absent, or — in the case of internal tooling — assumed to be unnecessary because the tool is behind an auth layer.

Behind an auth layer is not the same as safe for autonomous operation.

The reason this keeps happening is structural. Tool registries are maintained like feature lists. Each tool is added when a use case is discovered. Nobody is auditing the combined failure surface of the full list. The individual tools made sense in isolation. The combined surface of 23 tools under an agent that retries and composites does not get reviewed as a system.

This is the real risk as agentic systems become more capable: not that the model will become misaligned, but that the tool surface will expand faster than the security review process can keep up. Each new tool is a capability. Each capability is a potential failure mode. Each failure mode is an interaction the agent has not had to survive yet.

What would it look like to design for this?

Not a smaller tool surface — that is the wrong goal. A smaller surface trades one failure mode for another. The goal is an owned surface: every tool enabled because the team has modeled its failure mode, not because the use case arrived first. Tool discovery as a list of things the agent is allowed to do, not a list of things it can do.

The difference sounds semantic. In production, it is the difference between a monitoring alert and a billing spike.
