# Writer Draft — Round 0645

**Title:** Default-allow outbound is the jailbreak vendors keep shipping
**Style:** Technical breakdown / industry take
**Thesis:** Agent platforms default to allow-all outbound traffic, and this is not a minor misconfiguration — it is the primary attack surface they have collectively decided to ignore.

---

The standard agent platform ships with a simple networking model: the agent can call tools, and those tools can make outbound HTTP requests. What this means in practice is that any agent with tool access has, by default, egress to the entire internet.

No prompt injection required. No privilege escalation needed. The agent is already allowed to make outbound connections — the question is only whether anyone is watching where it calls.

This is not a hypothetical vulnerability. It is the default state.

**What default-allow outbound actually means**

When a vendor ships an agent platform with tool access enabled, the agent can invoke any registered tool. If one of those tools is, say, a web request utility, a file reader with network awareness, or a code executor that can reach URLs — the agent already has outbound connectivity. The vendor does not typically filter this at the network level because doing so would break legitimate tool use.

The result: every agent is a network endpoint with the internet as its egress path, and the only control is whatever prompt-level instructions the developer remembered to add. Prompt-level instructions that are routinely bypassed by careful rephrasing, context flooding, or simple multi-step decomposition.

This is structurally different from the model security problem. You can align the model all you want. If the tool layer allows arbitrary outbound requests, the aligned model can still be redirected to exfiltrate data through a side channel the alignment team never audited.

**The prompt injection layer**

The most discussed vector is prompt injection — an attacker who can inject instructions into the agent's context. But this requires the attacker to control some part of the input pipeline. The egress problem does not require injection.

What if the attacker does not need to inject anything? What if the agent, operating within its existing instructions, is simply pointed at a server controlled by the attacker via a tool call it already has permission to make?

The agent calls a tool. The tool makes a request to `attacker-controlled-server.com` with whatever context it has been given — conversation history, retrieved documents, function call arguments. No injection. No manipulation. Just a tool doing exactly what it was designed to do, used in a way the platform security team did not model.

This is the egress-first attack model. It does not fight the alignment. It works around it.

**The vendor silence**

What is striking is how rarely this appears in agent platform security disclosures. Vendors publish model capability reports, safety evaluations, and red teaming results focused on prompt-level attacks. Egress filtering — the network-level controls that would prevent a compromised or manipulated agent from sending data anywhere — is almost never mentioned in the same documents.

I do not have data on how many production agent deployments have meaningful egress controls. I can say that the platforms I have reviewed do not surface this as a first-class security configuration, and the tooling that exists for it (VPCs, egress proxies, IP allowlists for tool calls) requires custom setup that is not part of the standard agent deployment flow.

The implicit assumption is that if you trust the model, you trust the tools. But trust in the model's outputs and trust in the tool layer's network behavior are two different questions.

**What would actually fix it**

Egress filtering at the network layer is not a novel idea. It is how standard server security works: deny by default, allow only approved destinations. The challenge for agent platforms is that the set of legitimate destinations changes dynamically — a code execution tool needs to reach package registries, a search tool needs to reach search APIs, a document tool might need to reach cloud storage.

Static allowlists break quickly. Dynamic audit logging is better than nothing but does not prevent exfiltration, only detects it. The honest answer is that the tooling for fine-grained, application-aware egress control for agent platforms is immature, and most deployments are operating without it.

Until vendors treat egress filtering as a first-class security primitive — not a compliance checkbox, not a customer-configure-it-yourself option — this remains the easiest way to get data out of an agent system.

The jailbreak is already shipped. It is just not called a jailbreak.
