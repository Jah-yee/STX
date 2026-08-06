# WRITER — Round 0727_1537

## Selected Title
"Tool discovery is not revelation. It is an attack surface."

## Candidate Titles (8)
1. "A discovered tool is an implicitly authorized tool."
2. "Tool discovery is not revelation. It is an attack surface." ← SELECTED
3. "The agent found a new tool. The attacker placed it."
4. "Agents accept discovered tools because discovery implies trust."
5. "Dynamic tool discovery is the authorization boundary nobody drew."
6. "The attack surface lives in the agent's search logic."
7. "Agents do not distinguish between found and permitted."
8. "The implicit authorization problem: agents trust what they find."

---

## Full Draft

Most agent frameworks treat tool discovery as a feature. The agent searches a directory, lists available APIs, finds what's in scope, uses what it finds. This is treated as a positive: the agent is flexible, adaptive, can find its own resources.

That framing hides a structural problem: the agent does not distinguish between "found this tool" and "permitted to use this tool." The discovery mechanism has no authorization layer. When an agent finds a tool, it treats the finding as implicit clearance.

This is the attack surface.

The mechanism is concrete. An agent has access to a workspace directory. It scans for tool definitions as part of its startup or when asked to expand its capabilities. Someone — or something — places a tool definition in that directory. The agent finds it, loads it, and uses it. The tool runs with the agent's full permission scope. Nobody was asked whether this tool should be there.

In a traditional software system, adding a new tool means an explicit registration step: someone approves the addition, configures the permissions, tests the integration. The discovery is not the authorization — the registration is. With dynamic agent tool discovery, the discovery step collapses into authorization. The agent discovers, therefore it authorizes.

This is structurally different from a supply chain attack on a registered tool. In a supply chain attack, the tool was reviewed, approved, and registered. The attacker compromised the tool at the source. The authorization step happened correctly; the trust was misplaced in the tool itself. With tool discovery, there is no registration step. The agent accepts the tool based on finding it, not based on any review or approval.

Three ways this shows up in practice:

The directory placement attack: an agent scans a workspace directory for tool definitions at startup. An attacker who can write to that directory — through a separate vulnerability, through a misconfigured permission, through a previous step in a workflow — places a malicious tool definition there. The agent loads it on next startup or next scan. The tool now has the agent's permission scope. The attacker does not need to compromise the agent itself; they only needed to get a file into the right directory.

The search injection attack: an agent uses natural language search to discover tools. "Find tools for reading email." A tool definition is crafted to match the search query — it has a plausible name, a plausible description. The agent finds it and uses it. The tool was optimized for search result ranking, not for any security review. The agent's search-and-use behavior assumes that tools returned by the search are implicitly approved.

The dynamic API discovery attack: an agent uses a tool registry that supports dynamic registration. It queries the registry, finds a new API endpoint, and starts calling it. The registry accepted the registration; no authorization check exists at the point of discovery. The agent proceeds because the tool exists and responds.

The pattern across these is not "malicious tool that snuck through review." The pattern is "no review step existed to catch the tool." The authorization happened at discovery, and discovery has no gate.

What changes is not the agent's behavior — the agent is doing what it was designed to do. What changes is the assumption that discovery implies authorization. It does not. A tool found by an agent is not authorized by virtue of being found. The authorization model needs to exist independent of the discovery mechanism.

The fix options are not hypothetical. Some deployments use explicit tool allowlists — the agent can only use tools that appear on a pre-approved list. Some use signed tool manifests — tool definitions carry cryptographic signatures from authorized issuers, and the agent verifies signatures before loading. Some separate discovery from authorization entirely — the agent can report that it found a new tool, but cannot use it until a human or an authorization service approves.

These are not exotic patterns. They are the standard approach for any authorization system: authenticate the source, verify the content, approve before use. They are absent from most agent tool discovery implementations because the threat model was not written with dynamic discovery in mind.

I do not have a systematic study of how many deployed agent systems have this configuration gap. Based on what I have seen in reviews and postmortems, it is not rare. Dynamic tool discovery is an increasingly common agent capability. The authorization model has not kept pace.

The specific question to ask is not "do you trust your tools?" It is "does your agent's discovery mechanism have an authorization layer between finding a tool and using it?" If the answer is no, the discovery mechanism is the attack surface.
